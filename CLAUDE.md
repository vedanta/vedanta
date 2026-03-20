# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This is a **GitHub profile repository** (`vedanta/vedanta`). The README.md is rendered as the GitHub profile page. There is no application code — the repo contains a styled profile README and GitHub Actions workflows that generate visual assets.

## Architecture

- **README.md** — The profile page. Uses HTML/Markdown with badge shields, skill icons, featured project links, and embedded SVG visualizations.
- **profile-3d-contrib/** — Auto-generated 3D contribution calendar SVGs (committed by CI, do not edit manually).
- **.github/workflows/** — Three automated workflows:
  - `3d-contrib.yml` — Generates 3D contribution calendar SVGs daily and on push to main (uses `yoshi389111/github-profile-3d-contrib@0.7.1`). Output committed directly to `main`.
  - `snake.yml` — Generates snake animation SVGs daily and on push to main (uses `Platane/snk/svg-only@v3`). Output pushed to the `output` branch.
  - `blog-posts.yml` — Pulls latest Medium posts from `@barooah` feed daily (uses `gautamkrishnar/blog-post-workflow@v1`). Expects a `<!-- BLOG-POST-LIST -->` marker in README.md.

## README Layout Rules

The profile page sections appear in this order:
1. Header banner + social badge links
2. Featured Projects (with "🦍 The Gorilla Stack" tagline in `<kbd>` style)
3. Snake animation
4. Tech Stack
5. Contributions (3D calendar)
6. Footer

### Featured Projects

- Projects are displayed in a single `<table>` row with equal-width columns (currently 4 at 25%).
- All `<td>` cells use `align="center" valign="top"` to keep images top-aligned.
- Hero images come from `https://raw.githubusercontent.com/vedanta/hero-images/main/<projectname>.png`.
- If a project has a GitHub Pages site, link to that instead of the repo. Use `gh api repos/vedanta/<repo>/pages` to check.
- When adding a new project, adjust column `width` percentages so all columns are equal (e.g., 5 projects = 20% each).
- After any README change, always `git pull --rebase` before pushing since CI frequently commits to main.

## Key Details

- The `output` branch holds snake animation SVGs and is managed entirely by CI — do not commit to it manually.
- SVG files in `profile-3d-contrib/` are large (170KB–400KB) and regenerated daily — avoid including them in diffs.
- Most recent commits are automated bot commits ("Update 3D contribution calendar").
