#!/usr/bin/env python3
"""Replace all Stripe links and plain Cal.com links with UTM-tagged Cal.com links."""
import os, re, glob

CAL_BASE = "https://cal.com/giovanninyc/15min"

# Map filenames to page identifiers for utm_campaign + utm_content(page)
def get_page_info(filepath):
    fname = os.path.basename(filepath).replace('.html', '')
    dirname = os.path.basename(os.path.dirname(filepath))
    
    if dirname == 'integrations':
        return 'integrations', fname  # campaign=integrations, page=hubspot etc
    elif dirname == 'for':
        return 'industries', fname  # campaign=industries, page=real-estate etc
    elif fname == 'index':
        return 'homepage', 'home'
    elif fname == 'industries':
        return 'industries', 'hub'
    else:
        return 'other', fname

def make_cal_url(campaign, page, tier):
    return f"{CAL_BASE}?utm_source=nycclaw&utm_medium=website&utm_campaign={campaign}&utm_content={page}--{tier}"

# All known Stripe link patterns
stripe_patterns = [
    r'https://buy\.stripe\.com/5kA3e9gAVbAY2w84gi',
    r'https://buy\.stripe\.com/7sI5ml8ej7kI5Ik6oq',
    r'https://buy\.stripe\.com/aFaeVe6NTeo7g175SRf3a02',
    r'https://buy\.stripe\.com/7sYaEYb49cfZaGNchff3a03',
    r'https://buy\.stripe\.com/[A-Za-z0-9]+',  # catch any others
]

# Plain cal.com links (no UTM)
cal_plain = r'https://cal\.com/giovanninyc/15min(?![\?&])'

def process_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    
    original = content
    campaign, page = get_page_info(filepath)
    
    # Step 1: Replace Stripe links based on context (which pricing tier)
    # The remote/$1,200 tier buttons - detect by nearby text
    # We need to figure out which stripe link is remote vs in-person
    
    # Strategy: find all <a> tags with stripe links, look at surrounding context
    # For simplicity, replace ALL stripe links with cal links, using context clues
    
    # Remote stripe links (the ones in "Most Popular" / remote sections)
    # In-person stripe links (the ones in in-person sections)
    
    # Since the HTML structure is consistent, remote is always the middle card (border-2)
    # and in-person is always the third card
    
    # Simpler approach: replace stripe links line by line with context
    lines = content.split('\n')
    new_lines = []
    context = 'unknown'
    
    for i, line in enumerate(lines):
        # Track which pricing tier we're in by looking at nearby headings
        if 'Discovery Call' in line or 'discovery' in line.lower():
            if 'h3' in line or 'font-bold' in line:
                context = 'discovery'
        if 'Remote Setup' in line or 'Remote' in line:
            if 'h3' in line or 'font-bold' in line:
                context = 'remote'
        if 'In-Person' in line or 'In-person' in line or 'White Glove' in line:
            if 'h3' in line or 'font-bold' in line:
                context = 'inperson'
        
        # Replace stripe links based on context
        for pattern in stripe_patterns:
            if re.search(pattern, line):
                if context == 'inperson':
                    tier = 'inperson'
                else:
                    tier = 'remote'  # default for stripe links
                cal_url = make_cal_url(campaign, page, tier)
                line = re.sub(pattern, cal_url, line)
                # Also change "Get Started" to "Book a Call" on these buttons
                line = line.replace('>Get Started<', '>Book a Call<')
                break
        
        new_lines.append(line)
    
    content = '\n'.join(new_lines)
    
    # Step 2: Replace plain Cal.com links (no UTM) with UTM-tagged versions
    # These are typically in hero CTAs, free discovery tier, and final CTAs
    # We need context for these too
    
    lines = content.split('\n')
    new_lines = []
    context = 'discovery'  # default for cal links is discovery
    
    for i, line in enumerate(lines):
        if 'Remote Setup' in line and ('h3' in line or 'font-bold' in line):
            context = 'remote'
        if 'In-Person' in line and ('h3' in line or 'font-bold' in line):
            context = 'inperson'
        if '<!-- HERO -->' in line or '<!-- FINAL CTA -->' in line:
            context = 'discovery'
        if 'Discovery Call' in line and ('h3' in line or 'font-bold' in line):
            context = 'discovery'
        
        # Replace plain cal links
        if re.search(cal_plain, line):
            cal_url = make_cal_url(campaign, page, context)
            line = re.sub(cal_plain, cal_url, line)
        
        new_lines.append(line)
    
    content = '\n'.join(new_lines)
    
    # Step 3: Also handle cal links that already have a ? but no utm
    # (shouldn't exist but just in case)
    
    if content != original:
        with open(filepath, 'w') as f:
            f.write(content)
        return True
    return False

# Process all HTML files
files = []
files.append('/tmp/nycclaw-git/index.html')
files.append('/tmp/nycclaw-git/industries.html')
files.extend(glob.glob('/tmp/nycclaw-git/for/*.html'))
files.extend(glob.glob('/tmp/nycclaw-git/integrations/*.html'))

changed = 0
for f in sorted(files):
    if process_file(f):
        changed += 1
        print(f"✅ Updated: {f.replace('/tmp/nycclaw-git/', '')}")
    else:
        print(f"⏭️  No changes: {f.replace('/tmp/nycclaw-git/', '')}")

print(f"\n{changed} files updated")
