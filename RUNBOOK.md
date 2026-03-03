# NYC Claw — Page Build Runbook

_Formalized process for building integration + vertical pages at scale via sub-agents._

---

## Overview

**Two page types:**
1. **Integration pages** (`/integrations/[slug].html`) — software-specific, uses MASTER_PROMPT.md + GHL as template
2. **Vertical pages** (`/for/[slug].html`) — industry-specific, uses existing `/for/real-estate.html` as template

**Pipeline:** Sub-agent builds → Bruce reviews → Fix issues → Update tracker → Batch deploy

---

## Phase 1: Prep

Before spawning any agents:

1. **Update BUILD_TRACKER.md** with all target pages, type, and status columns
2. **Verify templates are current** — GHL for integrations, real-estate for verticals
3. **Verify MASTER_PROMPT.md is current** — especially CTA links (Cal.com, NOT Stripe)
4. **Create VERTICAL_PROMPT.md** if building vertical pages (mirrors MASTER_PROMPT for /for/ pages)

---

## Phase 2: Spawn Sub-Agents

### Integration Pages

Each sub-agent gets this task:

```
Read the build instructions at side-projects/nycclaw/integrations/MASTER_PROMPT.md

Use side-projects/nycclaw/integrations/gohighlevel.html as your design template — match the exact HTML structure, CSS classes, and section order.

Build an integration page for: **[PLATFORM NAME]**

Key rules:
- Output file: side-projects/nycclaw/integrations/[slug].html
- All CTA links go to Cal.com with UTM params:
  https://cal.com/giovanninyc/15min?utm_source=nycclaw&utm_medium=website&utm_campaign=integrations&utm_content=[slug]--discovery
- Follow ALL writing rules in MASTER_PROMPT.md (zero em dashes, no buzzwords, etc.)
- Research the platform's actual API/webhook capabilities — be specific, not generic
- Cross-link to relevant /for/ vertical pages in the "Related Industries" section

When done, output ONLY the file path of the created page.
```

### Vertical Pages

Each sub-agent gets this task:

```
Read side-projects/nycclaw/for/real-estate.html as your design template — match the exact HTML structure, CSS classes, section order, nav, and footer.

Build an industry vertical page for: **[INDUSTRY NAME]**

Key rules:
- Output file: side-projects/nycclaw/for/[slug].html
- Title format: "OpenClaw Setup for [Industry] — AI Transformation | NYC Claw"
- All CTA links go to Cal.com with UTM params:
  https://cal.com/giovanninyc/15min?utm_source=nycclaw&utm_medium=website&utm_campaign=verticals&utm_content=[slug]--discovery
- Follow these writing rules: zero em dashes, no AI buzzwords (leverage, seamless, revolutionize, game-changer, unlock, empower, harness, supercharge, elevate), use contractions, vary sentence length, max 1 exclamation mark on entire page, be specific not generic
- Research the industry's actual pain points, tools, and workflows
- Include "What is OpenClaw?" section (same as other pages)
- Pricing: 3 tiers — Free 15-min discovery / $1,200 remote / $2,400 in-person
- Cross-link to relevant /integrations/ pages if they exist
- Schema markup: Service + FAQPage

When done, output ONLY the file path of the created page.
```

### Concurrency

- Spawn up to **6 sub-agents at a time**
- Wait for batch to complete before spawning next batch
- Update BUILD_TRACKER.md after each batch

---

## Phase 3: Review (Claude Code)

After each batch completes, run a Claude Code review session:

```bash
claude -p "Review all new HTML files in side-projects/nycclaw/integrations/ and side-projects/nycclaw/for/ that were just created. For each file, check:

1. STRUCTURE: Does it match the GHL template (integrations) or real-estate template (verticals) section-by-section?
2. LINKS: All CTAs point to cal.com/giovanninyc/15min with correct UTM params? No Stripe links?
3. WRITING: Zero em dashes (—)? No banned buzzwords? Contractions used? Specific examples (not generic)?
4. SEO: Title tag, meta description, canonical URL, OG tags, schema markup all present and correct?
5. NAV: Industries dropdown present and matches other pages?
6. CROSS-LINKS: Related industries section links to correct /for/ pages?

Output a table: | File | Structure | Links | Writing | SEO | Nav | Cross-Links | Issues |
Mark each ✅ or ❌. List specific issues for any ❌.
" --dangerously-skip-permissions
```

### Fix issues

- If issues are minor (wrong link, missing meta tag): fix directly with edit tool
- If issues are structural (wrong template, missing sections): re-spawn sub-agent for that page

---

## Phase 4: Post-Build

After all pages pass review:

1. **Update sitemap.xml** — add all new URLs with today's date
2. **Update industries.html** — add new verticals to the hub page + nav dropdown
3. **Cross-link existing pages** — update related verticals to link to new integration pages
4. **Update BUILD_TRACKER.md** — mark all as deployed
5. **Git commit + push** — one commit per batch or one big commit
6. **Deploy:** `cd side-projects/nycclaw && wrangler pages deploy . --project-name nycclaw`
7. **Update PROJECT-LOG.md** — log what was built + date

---

## Common Issues & Fixes

| Issue | Fix |
|-------|-----|
| Em dashes (—) in output | Find/replace with periods or commas |
| Stripe links instead of Cal.com | Sub-agent used MASTER_PROMPT which has old Stripe links — update MASTER_PROMPT |
| Generic content ("streamline your workflow") | Re-spawn with explicit instruction to research the platform's actual API |
| Wrong nav dropdown | Copy nav from a recently deployed page |
| Missing schema markup | Copy FAQ + Service schema from GHL template, update |

---

_Last updated: 2026-03-02_
