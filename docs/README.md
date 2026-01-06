# GitHub Pages Setup

This directory contains the GitHub Pages configuration for hosting the documentation.

## Files

- `_config.yml` - Jekyll configuration
- `index.md` - Landing page for the documentation site

## Enabling GitHub Pages

1. **Commit and push these files** to your repository:
   ```bash
   git add docs/
   git commit -m "Add GitHub Pages setup"
   git push
   ```

2. **Enable GitHub Pages**:
   - Go to your repository on GitHub
   - Navigate to **Settings** → **Pages**
   - Under **Source**, select:
     - **Branch**: `main` (or your default branch)
     - **Folder**: `/docs`
   - Click **Save**

3. **Wait a few minutes** for GitHub to build and deploy your site

4. **Access your site** at:
   `https://<your-username>.github.io/<repo-name>/`

## How It Works

GitHub Pages uses Jekyll to render your markdown files. The `_config.yml` file configures Jekyll, and `index.md` serves as the landing page. The markdown files in the root directory are linked from the index page.

## Customization

You can customize the theme by changing the `theme` in `_config.yml`. Available themes include:
- `jekyll-theme-minimal` (current)
- `jekyll-theme-cayman`
- `jekyll-theme-dinky`
- `jekyll-theme-hacker`
- `jekyll-theme-leap-day`
- `jekyll-theme-merlot`
- `jekyll-theme-midnight`
- `jekyll-theme-minima`
- `jekyll-theme-modernist`
- `jekyll-theme-slate`
- `jekyll-theme-tactile`
- `jekyll-theme-time-machine`

See [GitHub Pages themes](https://pages.github.com/themes/) for more information.
