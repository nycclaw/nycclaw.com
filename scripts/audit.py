#!/usr/bin/env python3
"""Audit site structure: sitemap coverage, orphan pages, interlinking."""
import os, glob, re

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Get all HTML files
html_files = []
for pattern in ['*.html', 'for/*.html', 'integrations/*.html']:
    html_files.extend(glob.glob(os.path.join(SITE, pattern)))
html_files = sorted(html_files)

# Get sitemap URLs
with open(os.path.join(SITE, 'sitemap.xml')) as f:
    sitemap = f.read()
sitemap_urls = set(re.findall(r'<loc>(.*?)</loc>', sitemap))

# Map files to expected URLs
def file_to_url(fp):
    rel = os.path.relpath(fp, SITE).replace('.html', '').replace('index', '')
    if rel == 'index':
        return 'https://nycclaw.com/'
    return f'https://nycclaw.com/{rel}'.rstrip('/')

# Check sitemap coverage
print("=" * 60)
print("SITEMAP COVERAGE")
print("=" * 60)
missing_from_sitemap = []
for f in html_files:
    url = file_to_url(f)
    if url not in sitemap_urls:
        missing_from_sitemap.append((f, url))

if missing_from_sitemap:
    print(f"❌ {len(missing_from_sitemap)} pages NOT in sitemap:")
    for f, url in missing_from_sitemap:
        print(f"   {url}")
else:
    print(f"✅ All {len(html_files)} pages in sitemap")

# Check for orphan pages (no inbound links from other pages)
print("\n" + "=" * 60)
print("ORPHAN CHECK (pages with 0 inbound links)")
print("=" * 60)

# Build link map
link_map = {}  # url -> set of pages linking to it
for f in html_files:
    with open(f) as fh:
        content = fh.read()
    # Find all internal links
    links = re.findall(r'href="(/[^"]*)"', content)
    for link in links:
        clean = link.split('?')[0].split('#')[0].rstrip('/')
        if clean not in link_map:
            link_map[clean] = set()
        link_map[clean].add(os.path.relpath(f, SITE))

orphans = []
for f in html_files:
    rel = os.path.relpath(f, SITE).replace('.html', '').replace('index', '').rstrip('/')
    path = f'/{rel}' if rel else '/'
    if path == '/':
        continue  # homepage doesn't need inbound
    if path == '/book' or path == '/privacy' or path == '/terms':
        continue
    inbound = link_map.get(path, set())
    # Remove self-links
    self_file = os.path.relpath(f, SITE)
    inbound = inbound - {self_file}
    if len(inbound) == 0:
        orphans.append(path)

if orphans:
    print(f"⚠️  {len(orphans)} orphan pages:")
    for p in sorted(orphans):
        print(f"   {p}")
else:
    print("✅ No orphan pages — everything has at least 1 inbound link")

# Check nav consistency
print("\n" + "=" * 60)
print("NAV CONSISTENCY")
print("=" * 60)

nav_counts = {}
for f in html_files:
    with open(f) as fh:
        content = fh.read()
    nav_match = re.search(r'<nav.*?</nav>', content, re.DOTALL)
    if nav_match:
        nav = nav_match.group()
        vertical_links = len(re.findall(r'href="/for/', nav))
        integrations_link = 1 if '/integrations"' in nav or '/integrations/' in nav else 0
        key = f"verticals:{vertical_links} integrations_nav:{integrations_link}"
        if key not in nav_counts:
            nav_counts[key] = []
        nav_counts[key].append(os.path.relpath(f, SITE))

if len(nav_counts) == 1:
    key = list(nav_counts.keys())[0]
    print(f"✅ All pages have consistent nav: {key}")
else:
    print(f"⚠️  {len(nav_counts)} different nav configurations:")
    for key, files in nav_counts.items():
        print(f"   {key} ({len(files)} pages)")
        if len(files) <= 5:
            for f in files:
                print(f"      - {f}")

# Industries hub check
print("\n" + "=" * 60)
print("INDUSTRIES HUB")
print("=" * 60)
with open(os.path.join(SITE, 'industries.html')) as f:
    hub = f.read()
hub_verticals = set(re.findall(r'href="/for/([^"]+)"', hub))
all_verticals = set()
for f in glob.glob(os.path.join(SITE, 'for', '*.html')):
    slug = os.path.basename(f).replace('.html', '')
    all_verticals.add(slug)

missing = all_verticals - hub_verticals
if missing:
    print(f"❌ {len(missing)} verticals NOT in industries hub: {missing}")
else:
    print(f"✅ All {len(all_verticals)} verticals linked from industries hub")

print("\n" + "=" * 60)
print(f"TOTAL: {len(html_files)} pages | {len(sitemap_urls)} sitemap URLs")
print("=" * 60)
