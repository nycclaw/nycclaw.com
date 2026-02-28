# NYC Claw — Project Log & Roadmap

_Running tracker of what's done, what's in progress, and what's next._
_Rule: Update this file every time work is done on nycclaw.com._

---

## 📊 Current Status

| Metric | Count |
|---|---|
| Total pages live | 40 |
| Industry vertical pages | 11 |
| Integration pages | 24 |
| Core pages | 4 (home, book, privacy, terms) |
| Hub page | 1 (industries) |
| Google-indexed pages | ? (need Search Console) |
| Discovery calls booked | ? (check Cal.com) |

---

## ✅ Completed

### 2026-02-26 — Integration Pages Batch + Legal Deep Dive
- [x] Built 15 Phase 1 integration pages: GHL, HubSpot, Salesforce, Slack, Notion, QuickBooks, Zoho, Pipedrive, Follow Up Boss, Mailchimp, Calendly, Monday, Zapier, Jobber, ServiceTitan, kvCORE
- [x] Built 7 legal software integration pages: PracticePanther, MyCase, Smokeball, Filevine, RocketMatter, Litify, CosmoLex
- [x] Built Clio integration page + cross-linked from law-firms pillar
- [x] Updated law-firms pillar page with legal software cross-links
- [x] Replaced ALL Stripe checkout links with Cal.com UTM booking links across entire site
- [x] Changed discovery call duration: 30 min → 15 min across all pages
- [x] Updated sitemap.xml with all integration pages
- [x] Internal cross-linking: GHL in homepage footer, industries hub, RE/insurance/recruiting pages
- [x] Added _routes.json to bypass Functions for static pages
- [x] Fixed sitemap XML parsing error

### 2026-02-25 — Integration Content Strategy
- [x] Researched GoHighLevel integration opportunity
- [x] 3 sub-agents for exhaustive research: CRMs (37), industry tools (36), SaaS/SEO
- [x] Master strategy: integration-strategy-final.md — 60 concepts in 3 phases
- [x] Supporting research: research-crms.md, research-industry-tools.md, research-saas-seo.md
- [x] Shareable PDF of strategy

### 2026-02-22 — Website Vertical Buildout
- [x] Competitor analysis: Tidal Software (6 verticals mapped)
- [x] Built all 11 industry vertical pages (/for/[industry])
- [x] Created /industries hub page
- [x] Added Industries dropdown to nav on all pages
- [x] SEO pass: "OpenClaw for X" targeting — titles, meta, schema, What is OpenClaw sections
- [x] Sub-agent concurrency bumped to 8

### 2026-02-21 — SEO Deep Dive + Foundation
- [x] Comprehensive SEO keyword research (seo-deep-dive.md, strategy.md, content-ideas.md)
- [x] NYC directory research — 40+ directories (nyc-directories.md)
- [x] NAP: 30 E 20th St, New York, NY 10003 / (929) 673-0062
- [x] Directory submissions — all blocked by CAPTCHA

### Earlier
- [x] Initial site build + Cloudflare Pages deploy
- [x] Cal.com booking (giovanninyc/15min)
- [x] Discord link, Privacy, Terms, llms.txt

---

## 📋 Next Up

### Phase 2 Integration Pages
- [ ] Greenhouse, Guesty, Hostaway, Mindbody, Zendesk, Freshworks
- [ ] Copper, Insightly, Buildium, AppFolio, AthenaHealth, Dentrix
- [ ] 15+ more from integration-strategy-final.md

### More Industry Verticals
- [ ] Property Management, Mortgage Brokers, Commercial RE
- [ ] Dental, Veterinary, Consultants/Coaches

### SEO & Marketing
- [ ] Google Search Console + sitemap submission
- [ ] Connect GitHub → Cloudflare auto-deploy
- [ ] Blog hub + long-form guides
- [ ] Directory submissions (need CAPTCHA solution or manual)
- [ ] Monitor rankings weekly

### Business
- [ ] Client onboarding checklist
- [ ] Case study template
- [ ] Testimonials
- [ ] Ad creative + cold outreach templates

---

## 💡 Ideas / Parking Lot

- Mega menu once 15+ verticals
- City-level programmatic pages (/for/real-estate/nyc)
- Monthly retainer offering
- YouTube video walkthroughs per vertical
- Official OpenClaw referral partnership
- Blog: "GHL AI Employee vs OpenClaw", "Automate GHL Lead Follow-Up"

---

## 🔧 Technical Notes

- **Repo:** github.com/nycclaw/nycclaw.com (private)
- **Hosting:** Cloudflare Pages (direct upload, NOT auto-deploy yet)
- **Deploy:** wrangler pages deploy . --project-name nycclaw
- **Stack:** Static HTML + Tailwind CSS (pre-compiled)
- **Booking:** Cal.com embed at /book (giovanninyc/15min)
- **All CTAs:** Link to /book?utm_source=nycclaw&utm_medium=...
- **Pipeline:** research sub-agent → Claude Code page build → Bruce review → deploy

_Last updated: 2026-02-28_
