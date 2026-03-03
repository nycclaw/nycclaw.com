#!/usr/bin/env python3
"""Fix sitemap, industries hub, nav dropdowns, and generate integrations index."""

import os
import re
import glob

SITE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# All verticals (16 total)
VERTICALS = [
    ("real-estate", "Real Estate"),
    ("real-estate-investors", "Real Estate Investors"),
    ("property-management", "Property Management"),
    ("mortgage-brokers", "Mortgage Brokers"),
    ("law-firms", "Law Firms"),
    ("accounting-firms", "Accounting Firms"),
    ("insurance-agencies", "Insurance Agencies"),
    ("financial-advisors", "Financial Advisors"),
    ("healthcare", "Healthcare"),
    ("dental-practices", "Dental Practices"),
    ("recruiting-agencies", "Recruiting Agencies"),
    ("startup-founders", "Startup Founders"),
    ("creative-agencies", "Creative Agencies"),
    ("ecommerce", "E-commerce"),
    ("architecture-firms", "Architecture Firms"),
    ("coaches-consultants", "Coaches & Consultants"),
]

# All integrations grouped by category
INTEGRATIONS = {
    "CRM & Sales": [
        ("hubspot", "HubSpot"),
        ("salesforce", "Salesforce"),
        ("zoho", "Zoho CRM"),
        ("pipedrive", "Pipedrive"),
        ("freshsales", "Freshsales"),
        ("close", "Close"),
        ("attio", "Attio"),
        ("followupboss", "Follow Up Boss"),
        ("kvcore", "kvCORE"),
        ("liondesk", "LionDesk"),
        ("lofty", "Lofty"),
        ("clay", "Clay"),
        ("apollo", "Apollo.io"),
        ("instantly", "Instantly"),
    ],
    "Real Estate & Property": [
        ("buildium", "Buildium"),
        ("appfolio", "AppFolio"),
        ("dealmachine", "DealMachine"),
        ("guesty", "Guesty"),
    ],
    "Legal": [
        ("clio", "Clio"),
        ("practicepanther", "PracticePanther"),
        ("mycase", "MyCase"),
        ("smokeball", "Smokeball"),
        ("filevine", "Filevine"),
        ("rocketmatter", "Rocket Matter"),
        ("litify", "Litify"),
        ("cosmolex", "CosmoLex"),
    ],
    "Healthcare": [
        ("athenahealth", "athenahealth"),
        ("drchrono", "DrChrono"),
        ("kareo", "Kareo"),
    ],
    "Accounting & Finance": [
        ("quickbooks", "QuickBooks"),
        ("xero", "Xero"),
        ("freshbooks", "FreshBooks"),
        ("wave", "Wave"),
        ("bench", "Bench"),
    ],
    "Insurance": [
        ("applied-epic", "Applied Epic"),
        ("hawksoft", "HawkSoft"),
    ],
    "Home Services": [
        ("servicetitan", "ServiceTitan"),
        ("jobber", "Jobber"),
        ("housecallpro", "Housecall Pro"),
    ],
    "Recruiting": [
        ("greenhouse", "Greenhouse"),
    ],
    "Support": [
        ("zendesk", "Zendesk"),
    ],
    "Marketing & Email": [
        ("gohighlevel", "GoHighLevel"),
        ("mailchimp", "Mailchimp"),
        ("calendly", "Calendly"),
    ],
    "Productivity & Collaboration": [
        ("slack", "Slack"),
        ("notion", "Notion"),
        ("monday", "Monday.com"),
    ],
    "Automation": [
        ("zapier", "Zapier"),
        ("make", "Make"),
        ("n8n", "n8n"),
    ],
    "AI Platforms": [
        ("lindy", "Lindy"),
    ],
}

ALL_INTEGRATIONS = []
for cat, items in INTEGRATIONS.items():
    ALL_INTEGRATIONS.extend(items)


def build_nav_html(page_utm_content="general"):
    """Build standardized nav with all 16 verticals + integrations link."""
    vertical_links = ""
    for slug, name in VERTICALS:
        vertical_links += f'                  <a href="/for/{slug}">{name}</a>\n'
    
    return f'''<nav class="fixed top-0 left-0 right-0 bg-white/95 backdrop-blur-sm border-b border-gray-200 z-50">
    <div class="max-w-6xl mx-auto px-6 h-16 flex items-center justify-between">
      <div class="flex items-center gap-10">
        <a href="/" class="text-lg font-bold text-gray-900">NYC Claw</a>
        <div class="hidden md:flex items-center gap-8">
          <div class="industries-dropdown">
            <button class="text-sm text-gray-500 hover:text-gray-900 transition-colors inline-flex items-center gap-1">
              Industries
              <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
            </button>
            <div class="industries-dropdown-panel">
              <div class="industries-dropdown-inner">
                <div class="industries-dropdown-grid">
{vertical_links}                </div>
                <div style="border-top: 1px solid #e5e7eb; margin-top: 0.75rem; padding-top: 0.75rem;">
                  <a href="/industries" style="display: block; text-align: center; font-size: 0.875rem; font-weight: 500; color: #111827;">View All Industries &rarr;</a>
                </div>
              </div>
            </div>
          </div>
          <a href="/integrations" class="text-sm text-gray-500 hover:text-gray-900 transition-colors">Integrations</a>
          <a href="/#pricing" class="text-sm text-gray-500 hover:text-gray-900 transition-colors">Pricing</a>
          <a href="/#community" class="text-sm text-gray-500 hover:text-gray-900 transition-colors">Community</a>
        </div>
      </div>
      <a href="https://cal.com/giovanninyc/15min?utm_source=nycclaw&utm_medium=website&utm_campaign=nav&utm_content={page_utm_content}--discovery" target="_blank" class="inline-flex items-center px-4 py-2 text-sm font-medium text-white rounded-lg bg-gray-900 hover:bg-gray-800 transition-all shadow-sm">Book a Call</a>
    </div>
  </nav>'''


def update_nav_in_file(filepath):
    """Replace the nav block in an HTML file with the standardized nav."""
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Extract page slug for UTM
    basename = os.path.basename(filepath).replace('.html', '')
    if '/for/' in filepath:
        utm = basename
    elif '/integrations/' in filepath:
        utm = basename
    else:
        utm = 'home'
    
    nav_pattern = r'<nav class="fixed[^>]*>.*?</nav>'
    new_nav = build_nav_html(utm)
    
    new_content = re.sub(nav_pattern, new_nav, content, count=1, flags=re.DOTALL)
    
    if new_content != content:
        with open(filepath, 'w') as f:
            f.write(new_content)
        return True
    return False


def build_sitemap():
    """Generate sitemap.xml with all pages."""
    urls = []
    
    # Core pages
    urls.append(('https://nycclaw.com/', '2026-03-02', '1.0'))
    urls.append(('https://nycclaw.com/book', '2026-03-02', '0.9'))
    urls.append(('https://nycclaw.com/industries', '2026-03-02', '0.8'))
    urls.append(('https://nycclaw.com/integrations', '2026-03-02', '0.8'))
    
    # Verticals
    for slug, _ in VERTICALS:
        urls.append((f'https://nycclaw.com/for/{slug}', '2026-03-02', '0.8'))
    
    # Integrations
    for slug, _ in ALL_INTEGRATIONS:
        urls.append((f'https://nycclaw.com/integrations/{slug}', '2026-03-02', '0.7'))
    
    # Legal
    urls.append(('https://nycclaw.com/privacy', '2026-02-20', '0.3'))
    urls.append(('https://nycclaw.com/terms', '2026-02-20', '0.3'))
    
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for loc, lastmod, priority in urls:
        xml += f'  <url>\n    <loc>{loc}</loc>\n    <lastmod>{lastmod}</lastmod>\n    <priority>{priority}</priority>\n  </url>\n'
    xml += '</urlset>'
    
    with open(os.path.join(SITE_DIR, 'sitemap.xml'), 'w') as f:
        f.write(xml)
    
    return len(urls)


def main():
    # 1. Update sitemap
    num_urls = build_sitemap()
    print(f"✅ Sitemap updated: {num_urls} URLs")
    
    # 2. Update nav in all HTML files
    html_files = glob.glob(os.path.join(SITE_DIR, '*.html'))
    html_files += glob.glob(os.path.join(SITE_DIR, 'for', '*.html'))
    html_files += glob.glob(os.path.join(SITE_DIR, 'integrations', '*.html'))
    
    updated = 0
    for f in html_files:
        if os.path.basename(f) in ('BUILD_TRACKER.md', 'MASTER_PROMPT.md'):
            continue
        if update_nav_in_file(f):
            updated += 1
    
    print(f"✅ Nav updated in {updated}/{len(html_files)} files")
    
    # 3. Count total
    all_pages = glob.glob(os.path.join(SITE_DIR, '**', '*.html'), recursive=True)
    all_pages = [p for p in all_pages if '.git' not in p]
    print(f"📊 Total HTML pages: {len(all_pages)}")


if __name__ == '__main__':
    main()
