# Internal Linking Fix Plan — March 24, 2026

## Overview
12 new pages were added (11 integrations + 1 vertical) but they're not wired into the site's internal linking structure. This plan fixes all missing links.

---

## 1. Update Nav Dropdown (ALL pages site-wide)

The industries dropdown in the nav appears on every page. It currently has 16 verticals. Add Contractors.

**In every `.html` file across the entire site**, find the `industries-dropdown-grid` div and add:
```html
<a href="/for/contractors">Contractors</a>
```
Place it alphabetically (after Coaches & Consultants, before Creative Agencies).

**Files affected:** Every `.html` file that has the nav (all integration pages, all vertical pages, all claude-cowork pages, core pages). Approximately 120+ files.

---

## 2. Update `/integrations/index.html` (Hub Page)

Add all 11 new integration pages to the integrations index/hub page. Each should have:
- Platform name
- Short description (1 line)
- Link to `/integrations/[slug]`

**New entries to add:**
| Platform | Slug | Category |
|----------|------|----------|
| Airtable | airtable | Database & PM |
| FieldEdge | fieldedge | Home Services |
| Google Workspace | google-workspace | Productivity |
| JobNimbus | jobnimbus | Contractors |
| Microsoft Teams | microsoft-teams | Communication |
| ServiceM8 | servicem8 | Home Services |
| Shopify | shopify | E-commerce |
| Stripe | stripe | Payments |
| Telegram | telegram | Messaging |
| Vonigo | vonigo | Home Services |
| WhatsApp | whatsapp | Messaging |

Match the existing card/list format in index.html.

---

## 3. Update `/industries.html` (Industries Hub Page)

Add the Contractors vertical to the industries hub page. Match existing format.

```
Contractors — /for/contractors
```

---

## 4. Fix Vonigo Cross-Links

`integrations/vonigo.html` has zero links to other integration pages in its "Related Integrations" section. Add links to:
- `/integrations/fieldedge` (FieldEdge — similar home services)
- `/integrations/servicem8` (ServiceM8 — similar field service)
- `/integrations/jobnimbus` (JobNimbus — similar contractor tools)

---

## 5. Fix Contractors Vertical Cross-Links

`for/contractors.html` should link to relevant integration pages. Add a "Popular Integrations for Contractors" or similar section (match how other vertical pages link to integrations) linking to:
- `/integrations/fieldedge`
- `/integrations/servicem8`
- `/integrations/jobnimbus`
- `/integrations/vonigo`
- `/integrations/quickbooks` (already exists)
- `/integrations/stripe`

---

## 6. Add Reciprocal Links from Old Pages → New Pages

### 6a. Existing vertical pages should link to new relevant integrations:

| Vertical Page | Add Links To |
|---------------|-------------|
| `/for/ecommerce` | Shopify, Stripe, Airtable |
| `/for/startup-founders` | Stripe, Shopify, Airtable, Google Workspace |
| `/for/creative-agencies` | Airtable, Google Workspace, Shopify |
| `/for/coaches-consultants` | Stripe, Google Workspace, Telegram, WhatsApp |
| `/for/accounting-firms` | Stripe, Google Workspace |
| `/for/real-estate` | Google Workspace, WhatsApp, Airtable |
| `/for/healthcare` | Microsoft Teams, Google Workspace |
| `/for/law-firms` | Microsoft Teams, Google Workspace |
| `/for/insurance-agencies` | Microsoft Teams, Google Workspace |

Add these in the "Integrations" or "Related Integrations" section of each vertical page (match existing format — look at how they currently link to existing integrations like HubSpot, Salesforce, etc.).

### 6b. Existing integration pages that should link to new pages:

| Existing Page | Add Links To |
|--------------|-------------|
| `/integrations/hubspot` | Stripe, Shopify |
| `/integrations/salesforce` | Stripe, Microsoft Teams, Google Workspace |
| `/integrations/zapier` | Stripe, Shopify, Airtable, Google Workspace |
| `/integrations/make` | Stripe, Shopify, Airtable, Google Workspace |
| `/integrations/n8n` | Stripe, Shopify, Airtable |
| `/integrations/slack` | Microsoft Teams, Telegram, WhatsApp |
| `/integrations/quickbooks` | Stripe, FieldEdge |
| `/integrations/housecallpro` | FieldEdge, ServiceM8, JobNimbus |
| `/integrations/servicetitan` | FieldEdge, ServiceM8, JobNimbus, Vonigo |
| `/integrations/jobber` | FieldEdge, ServiceM8, JobNimbus, Vonigo |
| `/integrations/calendly` | Google Workspace |
| `/integrations/notion` | Airtable, Google Workspace |
| `/integrations/monday` | Airtable |

Add these in the "Related Integrations" section at the bottom of each page.

---

## 7. Verify After Changes

After all edits:
1. Run `grep -rL "contractors" for/*.html integrations/*.html` to confirm nav is updated everywhere
2. Run `grep -c "fieldedge\|servicem8\|jobnimbus\|vonigo\|stripe\|shopify\|telegram\|whatsapp\|microsoft-teams\|google-workspace\|airtable" integrations/index.html` to confirm index updated
3. Check no broken links: all href targets should match existing files
4. Zero em dashes in any modified content

---

## Priority Order
1. Nav dropdown (highest impact — affects every page's crawlability)
2. Hub pages (index.html, industries.html)
3. Vonigo + Contractors fixes
4. Reciprocal links from old → new pages
