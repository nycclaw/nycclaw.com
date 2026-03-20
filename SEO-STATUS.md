# NYC Claw — SEO & Analytics Status

_Last updated: March 20, 2026_

## What We Did (March 20, 2026)

### Google Search Console Setup
- OAuth'd with webmasters + indexing + cloud-platform scopes
- Created service account `gsc-indexing@ai-agent-auth-488416.iam.gserviceaccount.com` for Indexing API
- Added as Owner in GSC for nycclaw.com
- **42 missing pages submitted** for indexing via Google Indexing API (0 failures)
- Skills created: `google-search-console`, `google-analytics`

### Google Analytics Event Tracking
- **`book_call_click` event** — fires on every Cal.com button click
  - Tracks: `page_source`, `cta_type`, `campaign`, `link_url`
- **GA client ID + source page** passed to Cal.com via `metadata[]` URL params
  - `metadata[ga_client_id]`, `metadata[source_page]`, `metadata[source_content]`
- Injected into all 103 HTML pages

### GA4 Measurement Protocol (Server-Side Conversions)
- **Measurement Protocol API secret:** stored as `GA4_MP_API_SECRET` env var on `calcom-webhook` CF Worker
- **Measurement ID:** `G-DBW292SFKX`
- **Flow:** Cal.com BOOKING_CREATED webhook → CF Worker extracts metadata → fires `booking_confirmed` event to GA4 with original client ID
- **Worker:** `calcom-webhook.giovannimail-aa.workers.dev` (updated in `side-projects/calcom-webhook-worker/`)
- **Conversion value:** $1,200 for bookings from `/integrations/` pages

### Cowork Branding Fix
- Renamed all "Co-Work" → "Cowork" across 33 HTML pages (1,250 instances) to match Anthropic's official branding

## TODO — Needs Testing

- [ ] **Test the full conversion pipeline end-to-end:**
  1. Visit an integration page on nycclaw.com
  2. Click "Book a Call" — verify `book_call_click` shows in GA4 Realtime
  3. Complete a test booking — verify `booking_confirmed` shows in GA4
  4. Check that `metadata.ga_client_id` and `metadata.source_page` come through in the Cal.com booking
- [ ] Verify Cal.com actually passes `metadata[]` URL params into the booking payload (untested — previous bookings all had `metadata: {}`)
- [ ] If metadata doesn't pass through, consider alternative: Cal.com embed with JS metadata injection

## SEO Deep Dive Findings

### Current State (as of March 20)
- **DR: 0** (Ahrefs has no data — too new)
- **67 pages** getting impressions out of 103
- **~200 clicks, ~7,000+ impressions** over 28 days
- Almost all traffic is **branded** ("openclaw + industry")
- **100% bounce rate** in GA4 (only 2 days of data)

### Top Performing Pages (GSC, 28 days)
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
| /integrations/xero | 7 | 77 | 5.4 |
| /integrations/clay | 5 | 48 | 4.3 |

### High Impression / Zero Click Pages (title/meta issue)
| Page | Impressions | Position |
|------|-------------|----------|
| /for/dental-practices | 111 | 5.3 |
| /integrations/gohighlevel | 542 | 7.9 |
| /integrations/athenahealth | 66 | 6.9 |
| /integrations/buildium | 64 | 20.9 |
| /for/mortgage-brokers | 61 | 9.8 |
| /integrations/wave | 35 | 3.5 |
| /integrations/guesty | 33 | 5.0 |

### Recommended Next Steps

**Quick wins:**
- [ ] Rewrite titles/metas on `/for/` and `/integrations/` pages — lead with value, not "OpenClaw"
  - ❌ "OpenClaw Setup for Dental Practices — AI Transformation"
  - ✅ "AI for Dental Practices: Automate Scheduling, Insurance & Recalls | NYC Claw"

**Blog / Content Strategy (non-branded keyword targets):**
| Keyword | Volume | Difficulty | Priority |
|---------|--------|-----------|----------|
| ai agent for small business | 80 | 0 | 🔴 Write first |
| ai automation consulting | 300 | 7 | 🔴 Easy win |
| ai for property management | 350 | 30 | 🟡 |
| how to use ai in real estate | 200 | 36 | 🟡 |
| ai integration consultant | 60 | 28 | 🟡 |
| claude for business | 250 | — | 🟡 |
| openclaw alternatives | 250 | — | 🟡 Defensive |
| ai automation agency | 1,800 | 33 | 🟢 Harder but huge |
| ai tools for insurance agents | 150 | — | 🟢 |
| ai consulting for small business | 100 | — | 🟢 |

**Other:**
- [ ] Expand GoHighLevel page into comprehensive guide (542 impressions)
- [ ] Write at least one case study
- [ ] Build backlinks
