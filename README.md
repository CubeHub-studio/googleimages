# Google Images Gallery

A free, public GitHub Pages gallery for images shared by **Cubes, Studio**.

## Add images

1. Open the `images/` folder.
2. Upload image files (JPG, JPEG, PNG, GIF, WebP, or AVIF).
3. Give each file a descriptive name using words people might search for. Example: `roblox-rainbow-final-form-avatar.jpg`.
4. Commit the upload.

The homepage reads the `images/` folder and displays supported image files automatically. Use descriptive filenames: they become the displayed captions and image alt text.

## Publish with GitHub Pages

In **Settings → Pages**, choose **Deploy from a branch**, select `main` and `/(root)`, then save.

The site address will be:

https://cube-hub-studio.github.io/googleimages/

## Google indexing

- Keep the repository and Pages site public.
- After Pages is live, add the site to [Google Search Console](https://search.google.com/search-console/).
- Verify ownership and submit `https://cube-hub-studio.github.io/googleimages/sitemap.xml`.
- Request indexing for the homepage.

Google controls when and whether pages and images appear in search. Indexing is not guaranteed and may take time. The gallery's image list is loaded from GitHub in the browser; for stronger per-image search visibility, create a dedicated HTML page with a descriptive title and an ordinary `<img>` element for each important image, and add those pages and image URLs to the sitemap.

Only upload images you own or have permission to publish. Public repository files and the Pages site are visible to everyone.
