# NYC Claw — SEO & Analytics Status

_Last updated: March 21, 2026_

## Current State

- **109 pages live** (57 integration + 16 vertical + 8 claude-cowork + 4 core + rest)
- **DR: 0** (Ahrefs — still too new for domain rating)
- **~200 organic clicks/month**, ~7,000+ impressions (28-day window)
- **Google Indexing API:** Working — pages crawled within 24 hours of submission
- **OG image:** Updated Mar 21, added site-wide to all integration pages

## What We Did (March 21, 2026)

### New Integration Pages (6)
- **Dental:** Dentrix, Eaglesoft, Open Dental → support `/for/dental-practices`
- **Financial Advisor:** Redtail CRM, Wealthbox, Riskalyze → support `/for/financial-advisors`

### Content Rewrites (4)
- **GoHighLevel** — orchestration-layer framing (not vs GHL AI), Workflows v2, sub-accounts, SaaS Mode
- **Lofty** — deep RE content, Smart Plans, IDX, "Lofty AI vs OpenClaw" positioning
- **kvCORE** — speed-to-lead angle, lead triage, behavioral triggers
- **Buildium** — PM workflow automation, maintenance triage, lease renewal, owner reporting

### Site-Wide Improvements
- **OG image updated** — removed "In person." from social card
- **og:image + twitter:image** added to all 57 integration pages (was missing)
- **Integrations index** updated with 6 new tools
- **Sitemap** updated (109 URLs)
- All 10 URLs submitted to Google Indexing API

### Strategy Docs Created
- `research/integration-expansion-q2-2026.md` — full Q2 expansion plan
- `integrations/BUILD_TRACKER.md` — updated with all planned builds

## What We Did (March 20, 2026)

### Google Search Console Setup
- OAuth'd with webmasters + indexing + cloud-platform scopes
- Created service account for Indexing API, added as Owner in GSC
- **42 missing pages submitted** for indexing (0 failures)
- Skills created: `google-search-console`, `google-analytics`

### GA4 Event Tracking
- `book_call_click` event on every Cal.com button
- Measurement Protocol for server-side `booking_confirmed` events
- Conversion value: $1,200 for bookings from `/integrations/` pages

### Cowork Branding Fix
- Renamed all "Co-Work" → "Cowork" across 33 pages

## Top Performing Pages (GSC, Feb 21 – Mar 20)

### Vertical Pages
| Page | Clicks | Impressions | Position |
|------|--------|-------------|----------|
| / | 33 | 491 | 5.1 |
| /for/insurance-agencies | 23 | 456 | 5.4 |
| /for/financial-advisors | 19 | 442 | 6.5 |
| /for/accounting-firms | 16 | 641 | 7.3 |
| /for/law-firms | 14 | 324 | 7.3 |
| /for/ecommerce | 12 | 352 | 7.5 |
| /for/healthcare | 10 | 570 | 7.0 |
| /for/real-estate | 10 | 578 | 6.7 |

### Integration Pages
| Page | Clicks | Impressions | Position |
|------|--------|-------------|----------|
| /integrations/xero | 7 | 77 | 5.4 |
| /integrations/clay | 5 | 49 | 4.3 |
| /integrations/clio | 3 | 50 | 3.8 |
| /integrations/followupboss | 3 | 191 | 4.2 |
| /integrations/gohighlevel | 3 | 588 | 8.0 |
| /integrations/jobber | 2 | 23 | 2.7 |

### Traffic Sources (Last 24h — Mar 21)
- Direct: 20 sessions
- Organic Search (Google): 17 sessions
- Unassigned: 13 sessions
- Referral: 2 (Perplexity + ChatGPT — AI search engines citing us)

## Expansion Pipeline (Q2 2026)

### ⏸️ ON HOLD: CTR Fixes
10 existing pages ranking page 1 with 0 clicks. Parked — not convinced it's the right priority yet.

### Next Builds (Tier 1B — Trades + Messaging + Core)
- **Trades:** FieldEdge, ServiceM8, Vonigo, JobNimbus + new `/for/contractors` vertical
- **Messaging:** Telegram (350/mo), WhatsApp (200/mo), Microsoft Teams
- **Core:** Stripe, Shopify, Google Workspace, Airtable

### Content/Hub Pages (Tier 1C)
- `/claude-for-business` (250/mo keyword)
- `/integrations/mcp` (60/mo)
- `/guides/ai-scheduling` (1,700/mo!)
- `/guides/ai-small-business` (90/mo, KD 14)

### Tier 2: New Verticals
- Vet (eVetPractice, Shepherd, Cornerstone)
- PT/Chiro (Jane App, ChiroTouch, WebPT, Mindbody)
- Additional CRMs (Keap, Copper, ActiveCampaign)

### Tier 3: Untapped Verticals (Researched Mar 21)
| Vertical | Volume | KD | CPC | Notes |
|----------|--------|-----|-----|-------|
| Nonprofits | 800 | 42 | $4.00 | Huge volume. Donor mgmt, grants, volunteer coord. |
| Restaurants | 350 | 57 | $4.50 | High CPC. Reservations, inventory, staff. Harder to rank. |
| Logistics | 300 | 53 | $3.50 | Fleet, dispatch, route optimization. Enterprise. |
| Architects | 250 | 55 | $1.60 | Already have vertical page! Validate it's ranking. |
| Interior Designers | 200 | 47 | — | Project mgmt + client comms. |
| Photographers | 200 | 33 | $1.20 | Low KD. Booking, editing, client delivery. |
| Car Dealerships | 150 | 22 | $10.00 | Low KD + highest CPC. Lead follow-up, inventory. |
| Staffing Agencies | 150 | 4 | — | KD 4! Free to rank. Candidate matching, timesheets. |
| Churches | 100 | 30 | $2.00 | Volunteer coord, member comms. Low competition. |
| Electricians | 80 | — | — | Extends trades cluster. |
| Bookkeepers | 80 | — | — | Extends accounting cluster. |
| Event Planners | 60 | — | — | Venue, vendor, timeline automation. |
| Gyms/Fitness | 50 | — | $1.00 | Pairs with Mindbody integration. |

## Conversion Pipeline

### Status: Untested
- [ ] Test full pipeline: visit page → click CTA → `book_call_click` in GA4 → complete booking → `booking_confirmed` in GA4
- [ ] Verify Cal.com passes `metadata[]` URL params into booking payload
- [ ] If metadata doesn't pass, consider embed with JS metadata injection

## Key Metrics Targets

| Metric | Current (Mar 2026) | Target (Jun 2026) |
|--------|-------------------|-------------------|
| Total pages | 109 | 137+ |
| Monthly organic clicks | ~200 | 500+ |
| Monthly impressions | ~7,000 | 20,000+ |
| Integration pages with clicks | 12 of 57 (21%) | 40 of 75 (53%) |
| Pages ranking top 5 | ~15 | 35+ |
| Cal.com bookings from organic | 0 confirmed | 3+/month |

## Pending Actions
- [ ] Check if `/for/architecture-firms` is ranking (250/mo keyword validated)
- [ ] Test conversion pipeline end-to-end
- [ ] Build Tier 1B pages (trades, messaging, core tools)
- [ ] Create staffing agencies + car dealerships verticals (easy wins)
- [ ] Write first case study (Corey/SERHANT)
- [ ] Build backlinks
- [ ] Blog content targeting non-branded keywords
