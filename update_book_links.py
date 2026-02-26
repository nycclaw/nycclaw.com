#!/usr/bin/env python3
"""Replace /book links with UTM-tagged Cal.com links."""
import os, re, glob

CAL_BASE = "https://cal.com/giovanninyc/15min"

def get_page_info(filepath):
    fname = os.path.basename(filepath).replace('.html', '')
    dirname = os.path.basename(os.path.dirname(filepath))
    if dirname == 'integrations':
        return 'integrations', fname
    elif dirname == 'for':
        return 'industries', fname
    elif fname == 'index':
        return 'homepage', 'home'
    elif fname == 'industries':
        return 'industries', 'hub'
    else:
        return 'other', fname

def process_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    
    if '/book' not in content:
        return False
    
    original = content
    campaign, page = get_page_info(filepath)
    cal_url = f"{CAL_BASE}?utm_source=nycclaw&utm_medium=website&utm_campaign={campaign}&utm_content={page}--discovery"
    
    # Replace all /book links with the UTM-tagged cal link
    # Match href="/book" patterns
    content = content.replace('href="/book"', f'href="{cal_url}" target="_blank"')
    
    if content != original:
        with open(filepath, 'w') as f:
            f.write(content)
        return True
    return False

files = []
files.append('/tmp/nycclaw-git/index.html')
files.append('/tmp/nycclaw-git/industries.html')
files.extend(glob.glob('/tmp/nycclaw-git/for/*.html'))
files.extend(glob.glob('/tmp/nycclaw-git/integrations/*.html'))

changed = 0
for f in sorted(files):
    if process_file(f):
        changed += 1
        print(f"✅ Updated /book links: {f.replace('/tmp/nycclaw-git/', '')}")

print(f"\n{changed} files updated")
