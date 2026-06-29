#!/usr/bin/env python3
"""Generate a minimal monthly-contributions line/area chart SVG.

Pulls the GitHub contribution calendar (the data behind the green-squares
grid), rolls it up by month for the trailing 12 months, and renders a clean,
transparent, borderless SVG that matches the profile README's minimal style.

Env:
  GITHUB_TOKEN  required — any token that can run the GraphQL API
  GH_USER       optional — defaults to "vedanta"
  OUT           optional — output path, defaults to assets/contributions.svg
"""
import json
import os
import sys
import urllib.request
from datetime import date

USER = os.environ.get("GH_USER", "vedanta")
OUT = os.environ.get("OUT", "assets/contributions.svg")
TOKEN = os.environ.get("GITHUB_TOKEN")

# Theme — kept in sync with the README badges / activity colours.
TEXT = "#8b949e"
LINE = "#58a6ff"
AREA = "#1f6feb"
GRID = "#30363d"

W, H = 900, 220
M_L, M_R, M_T, M_B = 44, 16, 22, 34


def fetch_months():
    """Return [(label, count), ...] for the trailing 12 months."""
    query = """
    { user(login: "%s") { contributionsCollection { contributionCalendar {
        weeks { contributionDays { date contributionCount } } } } } }
    """ % USER
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": query}).encode(),
        headers={
            "Authorization": "Bearer %s" % TOKEN,
            "Content-Type": "application/json",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        data = json.load(r)
    weeks = data["data"]["user"]["contributionsCollection"]["contributionCalendar"]["weeks"]
    buckets = {}
    for wk in weeks:
        for d in wk["contributionDays"]:
            ym = d["date"][:7]
            buckets[ym] = buckets.get(ym, 0) + d["contributionCount"]
    months = sorted(buckets)[-12:]
    return [(m, buckets[m]) for m in months]


def render(series):
    plot_w = W - M_L - M_R
    plot_h = H - M_T - M_B
    n = len(series)
    counts = [c for _, c in series]
    peak = max(counts) or 1
    # round the axis max up to a "nice" number
    step = 10 ** (len(str(peak)) - 1)
    axis_max = ((peak // step) + 1) * step

    def xy(i, val):
        x = M_L + (plot_w * i / (n - 1) if n > 1 else 0)
        y = M_T + plot_h * (1 - val / axis_max)
        return x, y

    pts = [xy(i, c) for i, (_, c) in enumerate(series)]
    line_d = "M" + " L".join("%.1f,%.1f" % p for p in pts)
    base = M_T + plot_h
    area_d = "M%.1f,%.1f L" % (pts[0][0], base) + " L".join(
        "%.1f,%.1f" % p for p in pts
    ) + " L%.1f,%.1f Z" % (pts[-1][0], base)

    MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    out = []
    out.append(
        '<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" '
        'viewBox="0 0 %d %d" font-family="-apple-system,Segoe UI,Helvetica,Arial,sans-serif">'
        % (W, H, W, H)
    )
    out.append(
        '<defs><linearGradient id="a" x1="0" y1="0" x2="0" y2="1">'
        '<stop offset="0" stop-color="%s" stop-opacity="0.35"/>'
        '<stop offset="1" stop-color="%s" stop-opacity="0"/></linearGradient></defs>'
        % (AREA, AREA)
    )
    # gridlines + y labels (0, mid, max)
    for frac in (0, 0.5, 1):
        gy = M_T + plot_h * (1 - frac)
        out.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-width="1" stroke-dasharray="3 3"/>'
                   % (M_L, gy, W - M_R, gy, GRID))
        out.append('<text x="%d" y="%.1f" fill="%s" font-size="11" text-anchor="end">%d</text>'
                   % (M_L - 8, gy + 4, TEXT, int(axis_max * frac)))
    # area + line
    out.append('<path d="%s" fill="url(#a)"/>' % area_d)
    out.append('<path d="%s" fill="none" stroke="%s" stroke-width="2.5" stroke-linejoin="round"/>'
               % (line_d, LINE))
    # points + month labels
    for i, ((ym, c), (x, y)) in enumerate(zip(series, pts)):
        out.append('<circle cx="%.1f" cy="%.1f" r="3" fill="%s"/>' % (x, y, LINE))
        label = MONTHS[int(ym[5:7]) - 1]
        if ym[5:7] == "01":
            label += " '" + ym[2:4]
        out.append('<text x="%.1f" y="%d" fill="%s" font-size="11" text-anchor="middle">%s</text>'
                   % (x, H - 12, TEXT, label))
    total = sum(counts)
    out.append('<text x="%d" y="14" fill="%s" font-size="12">%d contributions · last 12 months</text>'
               % (M_L, TEXT, total))
    out.append("</svg>")
    return "".join(out)


def main():
    if not TOKEN:
        sys.exit("GITHUB_TOKEN is required")
    series = fetch_months()
    svg = render(series)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w") as f:
        f.write(svg)
    print("wrote %s (%d months, %d contributions)"
          % (OUT, len(series), sum(c for _, c in series)))


if __name__ == "__main__":
    main()
