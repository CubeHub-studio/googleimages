#!/usr/bin/env python3
"""Generate crawlable HTML pages and an image sitemap from images/."""
from html import escape
from pathlib import Path
from urllib.parse import quote
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
SITE = "https://cubehub-studio.github.io/googleimages"
IMAGE_DIR = ROOT / "images"
PAGE_DIR = ROOT / "image-pages"
EXTENSIONS = {".avif", ".gif", ".jpeg", ".jpg", ".png", ".webp"}

def humanize(filename):
    return Path(filename).stem.replace("-", " ").replace("_", " ").strip() or filename

def main():
    ET.register_namespace("image", "http://www.google.com/schemas/sitemap-image/1.1")
    PAGE_DIR.mkdir(exist_ok=True)
    images = sorted(
        (p for p in IMAGE_DIR.iterdir() if p.is_file() and p.suffix.lower() in EXTENSIONS),
        key=lambda p: p.name.lower()
    )
    expected = set()
    gallery_items = []
    urlset = ET.Element("urlset", {
        "xmlns": "http://www.sitemaps.org/schemas/sitemap/0.9",
    })
    homepage = ET.SubElement(urlset, "url")
    ET.SubElement(homepage, "loc").text = SITE + "/"

    for image in images:
        filename = image.name
        slug = quote(filename, safe="")
        image_url = f"{SITE}/images/{slug}"
        # Include the original extension to prevent collisions such as photo.jpg and photo.png.
        page_name = image.name + ".html"
        expected.add(page_name)
        page_url = f"{SITE}/image-pages/{quote(page_name, safe='')}"
        title = humanize(filename)
        title_html = escape(title)
        file_html = escape(filename)
        image_html = escape(image_url, quote=True)
        page = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title_html} | Cubes, Studio</title>
  <meta name="description" content="View {file_html}, shared in the Cubes, Studio public image gallery.">
  <meta name="robots" content="index,follow,max-image-preview:large">
  <link rel="canonical" href="{page_url}">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{title_html} | Cubes, Studio">
  <meta property="og:description" content="View {file_html}, shared in the Cubes, Studio public image gallery.">
  <meta property="og:image" content="{image_html}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:image" content="{image_html}">
  <style>
    body{{margin:0;padding:2rem 1rem;background:#11111b;color:#f4f1ff;font:16px system-ui,sans-serif}}
    main{{max-width:900px;margin:auto}}img{{display:block;max-width:100%;max-height:75vh;height:auto;margin:1.5rem auto;object-fit:contain}}
    a{{color:#c8b5ff}}.name{{overflow-wrap:anywhere;color:#c8c0e8}}
  </style>
</head>
<body>
  <main>
    <p><a href="../">← Back to the image gallery</a></p>
    <h1>{title_html}</h1>
    <a href="{image_html}"><img src="{image_html}" alt="{title_html}" loading="eager" decoding="async"></a>
    <p class="name">{file_html}</p>
  </main>
</body>
</html>
"""
        (PAGE_DIR / page_name).write_text(page, encoding="utf-8")
        page_href = escape("image-pages/" + quote(page_name, safe=""), quote=True)
        image_src = escape("images/" + slug, quote=True)
        gallery_items.append(
            f'<figure><a href="{page_href}"><img src="{image_src}" alt="{title_html}" loading="lazy" decoding="async"></a>'
            f'<figcaption>{title_html}</figcaption></figure>'
        )
        entry = ET.SubElement(urlset, "url")
        ET.SubElement(entry, "loc").text = page_url
        image_entry = ET.SubElement(entry, "{http://www.google.com/schemas/sitemap-image/1.1}image")
        ET.SubElement(image_entry, "{http://www.google.com/schemas/sitemap-image/1.1}loc").text = image_url

    # Remove generated pages for images that have since been deleted or renamed.
    for old_page in PAGE_DIR.glob("*.html"):
        if old_page.name not in expected:
            old_page.unlink()

    # Render image cards into the homepage as real HTML, not client-side API results.
    homepage_path = ROOT / "index.html"
    homepage_html = homepage_path.read_text(encoding="utf-8")
    start_marker = "<!-- GENERATED_GALLERY_START -->"
    end_marker = "<!-- GENERATED_GALLERY_END -->"
    if homepage_html.count(start_marker) != 1 or homepage_html.count(end_marker) != 1:
        raise RuntimeError("index.html must contain exactly one generated gallery marker pair")
    start = homepage_html.index(start_marker) + len(start_marker)
    end = homepage_html.index(end_marker)
    if end < start:
        raise RuntimeError("Generated gallery markers are out of order")
    gallery_html = "\\n" + "\\n".join(gallery_items) + "\\n" if gallery_items else "\\n<p>No images have been published yet.</p>\\n"
    homepage_path.write_text(homepage_html[:start] + gallery_html + homepage_html[end:], encoding="utf-8")

    ET.indent(urlset, space="  ")
    ET.ElementTree(urlset).write(ROOT / "sitemap.xml", encoding="utf-8", xml_declaration=True)
    print(f"Generated {len(images)} image page(s) and sitemap.xml")

if __name__ == "__main__":
    main()
