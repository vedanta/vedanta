# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This is a **GitHub profile repository** (`vedanta/vedanta`). The README.md is rendered as the GitHub profile page. There is no application code — the repo contains a styled profile README and GitHub Actions workflows that generate visual assets.

## Architecture

- **README.md** — The profile page. Minimal, typographic layout: plain Markdown headers with `---` section rules, monochrome social badge shields, a text-only project list, and grouped text tech-stack categories. No contribution visualization is embedded — GitHub already renders the contribution calendar natively below the profile README, so any embedded chart/snake/3D calendar would be redundant.
- **.github/workflows/** — One automated workflow:
  - `blog-posts.yml` — Pulls latest Medium posts from `@barooah` feed daily (uses `gautamkrishnar/blog-post-workflow@v1`). Expects a `<!-- BLOG-POST-LIST -->` marker in README.md.

  The old contribution-visualization workflows (`3d-contrib.yml` / snake, plus the `profile-3d-contrib/` dir and `output` branch) were removed — GitHub's native contribution calendar makes embedded charts redundant.

## README Layout Rules

The design is deliberately **minimal and typographic** — plain text and whitespace over decoration. No waving banners, no skill-icon walls, no embedded 3D calendar. Sections appear in this order, separated by `---` rules:
1. Header — centered `# Vedanta Barooah`, a `·`-separated tagline, and four monochrome social badges (all `181717`)
2. Featured Projects (one-line text list)
3. More Projects (one-line text list grouped under bold sub-headings: "Dev tools & CLI utilities", "AI / ML / RAG", "Learning & reference")
4. Tech Stack (grouped text categories)
5. Closing handoff — a small centered `<sub>` line that bridges into GitHub's native profile content (pinned repos, contribution graph, recent activity) rendered below the README, with a `↓` pointer.

There is no footer banner and no embedded contributions chart (GitHub renders the contribution calendar natively below the README; the closing line points to it).

### Featured Projects

- Projects are rendered as **borderless-style Markdown tables** (3 columns, left-aligned) — no hero images.
- Each table uses an empty header row (`|  |  |  |` over `|:--|:--|:--|`); the section/category label above the table provides the heading.
- Columns are: **name** (bold) | one-line description | links.
- Keep descriptions to a single scannable line (~6–10 words).
- The same table format is used for both **Featured Projects** (one table) and **More Projects** (one table per category, each under a bold sub-heading).
- If a project has a GitHub Pages site (`gh api repos/vedanta/<repo>/pages` to check), the links cell is `[page](pages-url) · [repo](repo-url)`.
- If a project has no GitHub Pages site, the links cell is just `[repo](repo-url)`.
- When adding a project, just append another table row — no column-width math needed.
- After any README change, always `git pull --rebase` before pushing since CI frequently commits to main.

## Key Details

- After any README change, always `git pull --rebase` before pushing — the `blog-posts.yml` workflow occasionally commits to `main`.
