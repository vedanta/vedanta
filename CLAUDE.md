# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This is a **GitHub profile repository** (`vedanta/vedanta`). The README.md is rendered as the GitHub profile page. There is no application code — the repo contains a styled profile README and GitHub Actions workflows that generate visual assets.

## Architecture

- **README.md** — The profile page. Minimal, typographic layout: plain Markdown headers with `---` section rules, monochrome social badge shields, a text-only project list, grouped text tech-stack categories, and a single embedded SVG (the snake animation).
- **profile-3d-contrib/** — Auto-generated 3D contribution calendar SVGs (committed by CI, do not edit manually). The workflow still runs, but these SVGs are **no longer embedded in README.md** — they remain in the repo only as generated artifacts.
- **.github/workflows/** — Three automated workflows:
  - `3d-contrib.yml` — Generates 3D contribution calendar SVGs daily and on push to main (uses `yoshi389111/github-profile-3d-contrib@0.7.1`). Output committed directly to `main`. (Not referenced by the README.)
  - `snake.yml` — Generates snake animation SVGs daily and on push to main (uses `Platane/snk/svg-only@v3`). Output pushed to the `output` branch.
  - `blog-posts.yml` — Pulls latest Medium posts from `@barooah` feed daily (uses `gautamkrishnar/blog-post-workflow@v1`). Expects a `<!-- BLOG-POST-LIST -->` marker in README.md.

## README Layout Rules

The design is deliberately **minimal and typographic** — plain text and whitespace over decoration. No waving banners, no skill-icon walls, no embedded 3D calendar. Sections appear in this order, separated by `---` rules:
1. Header — centered `# Vedanta Barooah`, a `·`-separated tagline, and four monochrome social badges (all `181717`)
2. Featured Projects (one-line text list)
3. More Projects (one-line text list grouped under bold sub-headings: "Dev tools & CLI utilities", "AI / ML / RAG", "Learning & reference")
4. Tech Stack (grouped text categories)
5. Contributions (snake animation only)

There is no footer banner.

### Featured Projects

- Projects are a plain text list, one line per project — **no `<table>`, no hero images, no bullets**.
- Each line: `**name** <sub>(links)</sub> — one-line description` with two trailing spaces to force the line break.
- Keep descriptions to a single scannable line (~6–10 words).
- The same one-line format is used for both the **Featured Projects** and **More Projects** sections.
- If a project has a GitHub Pages site (`gh api repos/vedanta/<repo>/pages` to check), the links are `([page](pages-url) | [repo](repo-url))`.
- If a project has no GitHub Pages site, the links are just `([repo](repo-url))`.
- When adding a project, just append another line — no column-width math needed.
- After any README change, always `git pull --rebase` before pushing since CI frequently commits to main.

## Key Details

- The `output` branch holds snake animation SVGs and is managed entirely by CI — do not commit to it manually.
- SVG files in `profile-3d-contrib/` are large (170KB–400KB) and regenerated daily — avoid including them in diffs.
- Most recent commits are automated bot commits ("Update 3D contribution calendar").
