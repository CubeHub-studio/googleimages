# Google Images Gallery

A free, public GitHub Pages gallery for images shared by **Cubes, Studio**.

## Add images

1. Open the `images/` folder.
2. Upload image files (JPG, JPEG, PNG, GIF, WebP, or AVIF).
3. Give each file a descriptive filename that accurately describes the image. Use hyphens between words, for example: `roblox-rainbow-avatar.png`.
4. Commit the upload.

A GitHub Actions workflow generates real HTML image cards on the homepage, a dedicated crawlable HTML page for each image, and an image sitemap. This avoids relying on a browser-side GitHub API request for the gallery content. Generated cards, pages, and the sitemap are updated automatically; do not edit generated gallery cards or pages manually.

The generated alt text and page title are based on each filename. Use clear, accurate filenames; for best accessibility and search relevance, filenames should describe what is actually shown without keyword stuffing.

## Publish with GitHub Pages

In **Settings → Pages**, choose **Deploy from a branch**, select `main` and `/(root)`, then save. Keep this setting if it is already configured.

The site address is:

https://cubehub-studio.github.io/googleimages/

## Google indexing

1. Add the site to [Google Search Console](https://search.google.com/search-console/) and verify ownership. The repository includes the Google HTML verification file at the exact filename Google expects; if Search Console gives you a different verification file, replace it with the exact file Google provides.
2. Submit `https://cubehub-studio.github.io/googleimages/sitemap.xml` in Search Console. This is a GitHub Pages project site under a subdirectory; a `robots.txt` stored inside this repository is not the hostname-root robots file. Submit the sitemap directly in Search Console rather than relying on a subdirectory `robots.txt` directive.
3. After uploading images, allow the **Generate image SEO pages** GitHub Actions workflow to finish. It updates the individual pages and sitemap automatically.
4. You can request indexing for the homepage or an individual image page in Search Console.

Google decides when and whether pages and images appear in search. Indexing is not guaranteed and can take time. Search Console and GitHub Pages are free.

## Privacy and permissions

Only upload images you own or have permission to publish. Public repository files and the Pages site are visible to everyone. Avoid uploading private or identifying information.
