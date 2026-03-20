# Claude Cowork Page Build Instructions

_Master prompt for sub-agents building pages in /claude-cowork/_

---

## Template

Use `side-projects/nycclaw/for/real-estate.html` as your HTML/CSS template. Match:
- Nav bar (including Industries dropdown, Book a Call button)
- Font loading (Inter from Google Fonts)
- `style.css` link (use `/style.css`)
- Footer structure
- FAQ accordion pattern
- Schema markup pattern (FAQPage + Service)
- Mobile responsiveness classes

**But adapt the content structure** for Cowork pages as specified below.

---

## Page Types & Content Structure

### Pillar Page (`index.html`)
1. Hero — "Claude Cowork: The Complete Guide" + subheading
2. What is Cowork — brief explainer (how it differs from Chat and Claude Code)
3. Key capabilities overview (file management, web research, scheduled tasks, mobile assignment)
4. Plugins & skills section — what they are, link to `/claude-cowork/plugins` and `/claude-cowork/skills`
5. Connectors overview — 38+ integrations, link to `/claude-cowork/connectors`
6. Industry section — grid linking to all industry spoke pages
7. Pricing overview — plans table, link to `/claude-cowork/pricing-guide`
8. CTA — "Book a Free 15-Minute Call"
9. FAQ — 6-8 questions with schema markup

### Industry Spoke Pages
1. Hero — "Claude Cowork for [Industry]" + one-line hook
2. The Problem — 3-4 specific pain points for this industry (be concrete, not generic)
3. How Cowork Solves It — 3-5 specific workflows with real detail
4. What We Build For You — Custom skills, plugins, connectors, scheduled tasks for this vertical
5. Training — "We train your team. Remote or in-person."
6. CTA — "Book a Free 15-Minute Call"
7. FAQ — 4-5 industry-specific questions with schema markup

### Feature/Use Case Pages
1. Hero — "Claude Cowork [Feature]" + value prop
2. What it is — Technical explanation made accessible
3. How it works — Step-by-step with examples
4. Use cases — 4-6 real examples (pull from CLAUDE-COWORK-REFERENCE.md research section)
5. How we help — Setup, customization, training
6. CTA — "Book a Free 15-Minute Call"
7. FAQ — 4-5 questions with schema markup

### Comparison Pages
1. Hero — "Claude Cowork vs [Competitor]"
2. Quick comparison table — features side by side
3. Where Cowork wins — specific advantages
4. Where [Competitor] wins — be honest, builds trust
5. Who should use which — decision framework
6. How we help — "We'll set up Cowork for your specific needs"
7. CTA — "Book a Free 15-Minute Call"
8. FAQ — 3-4 questions

### Training/Service Pages
1. Hero — clear service offering
2. What's included — specific deliverables
3. Who it's for — target audience
4. Process — how an engagement works
5. CTA — "Book a Free 15-Minute Call"

---

## Writing Rules (MANDATORY)

### Things to NEVER do:
- **Zero em dashes (—)** — use periods, commas, or colons instead
- **No AI buzzwords:** leverage, seamless, revolutionize, game-changer, unlock, empower, harness, supercharge, elevate, cutting-edge, holistic, synergy, paradigm, transformative, groundbreaking, nestled, tapestry, pivotal, testament, landscape, showcasing, streamline, delve, moreover, furthermore, additionally, it's important to note, in today's rapidly evolving
- **No sycophantic openers:** "Great question!", "Absolutely!", "That's a great point!"
- **No filler phrases:** "In order to" (use "to"), "Due to the fact that" (use "because"), "It's worth noting that" (just state the thing)
- **No generic conclusions:** "The future looks bright", "Exciting times ahead"
- **No significance inflation:** "marking a pivotal moment in the evolution of..."
- **No em dash clauses** — rewrite as separate sentences
- **No excessive hedging:** "could potentially possibly" → "may"
- **No rule of three lists** where items are vague: "innovation, inspiration, and insights"
- **No synonym cycling:** Pick one term and stick with it
- **No emoji in body content**
- **Max 1 exclamation mark per page**
- **No promotional fluff:** "nestled within the breathtaking..." → state facts

### Things to ALWAYS do:
- **Use contractions** — "you'll" not "you will", "it's" not "it is"
- **Vary sentence length** — mix short punchy sentences with longer ones
- **Be specific** — name actual tools, actual workflows, actual numbers
- **Use "you" and "your"** — speak directly to the reader
- **Repeat the clearest term** — don't cycle synonyms for variety
- **Start sections with the point** — don't build up to it
- **Use plain verbs:** "is" not "serves as", "has" not "boasts", "helps" not "empowers"

### Humanizer Check
After writing all content, run `/humanizer` on the full text. Fix any remaining AI-isms it catches. This is not optional.

---

## SEO Requirements

### Every page must have:
- `<title>` — primary keyword near the front, "| NYC Claw" at end
- `<meta name="description">` — compelling, includes primary keyword, under 160 chars
- `<link rel="canonical">` — `https://nycclaw.com/claude-cowork/[slug]`
- OG tags (title, description, image, type, url)
- Twitter card meta
- FAQPage schema (JSON-LD) with 4+ questions
- Service schema (JSON-LD)
- H1 — one per page, includes primary keyword
- H2s — section headings, include secondary keywords naturally
- Internal links — see linking rules below

### URL structure:
- All pages in `/claude-cowork/` directory
- File: `claude-cowork/[slug].html`
- Canonical: `https://nycclaw.com/claude-cowork/[slug]`

---

## CTA Links

ALL call-to-action buttons use Cal.com with UTM params:

```
https://cal.com/giovanninyc/15min?utm_source=nycclaw&utm_medium=website&utm_campaign=claude-cowork&utm_content=[slug]--discovery
```

Replace `[slug]` with the page slug (e.g., `real-estate`, `legal`, `plugins`).

**Button text:** "Book a Free 15-Minute Call" (primary) or "Book a Call" (nav/secondary)

**NO pricing on any page.** No dollar amounts. No tier cards. Just the free call CTA.

---

## Internal Linking Rules

### Every industry spoke MUST link to:
- Pillar page `/claude-cowork/` (in breadcrumb + body text)
- `/claude-cowork/plugins/` (mention relevant plugins)
- `/claude-cowork/skills/` (mention custom skills)
- `/claude-cowork/training/` (CTA section)
- Matching `/for/[industry]` page (if it exists)
- 2-3 related spoke pages (e.g., real-estate links to property-management and mortgage-brokers)
- 1-2 relevant connector/feature pages

### Every feature/comparison page MUST link to:
- Pillar page `/claude-cowork/`
- 2-3 relevant industry spokes
- `/claude-cowork/training/` or `/claude-cowork/consulting/`

### Breadcrumb format:
```html
<nav class="text-sm text-gray-500 mb-4">
  <a href="/" class="hover:text-gray-700">Home</a> →
  <a href="/claude-cowork/" class="hover:text-gray-700">Claude Cowork</a> →
  <span class="text-gray-900">Page Title</span>
</nav>
```

---

## Reference Material

The sub-agent MUST read this file before writing any content:
- `side-projects/nycclaw/CLAUDE-COWORK-REFERENCE.md` — comprehensive reference on Cowork features, plugins, skills, connectors, real-world workflows, and use cases

This is the source of truth for technical accuracy. Do NOT make up features or capabilities not documented in this file.

---

## Nav Update

Every page should include the standard NYC Claw nav with an ADDED "Cowork" link:
```html
<a href="/claude-cowork/" class="text-sm font-medium text-gray-600 hover:text-gray-900 transition-colors">Claude Cowork</a>
```
Place this between "Industries" and "Book a Call" in the nav.

---

## Quality Checklist (Agent must verify before saving)

- [ ] HTML validates (no unclosed tags)
- [ ] All internal links use relative paths starting with /
- [ ] All CTA links go to cal.com with correct UTMs
- [ ] No em dashes anywhere in the file
- [ ] No banned buzzwords
- [ ] Canonical URL is correct
- [ ] Schema markup is valid JSON-LD
- [ ] Page has breadcrumb navigation
- [ ] Humanizer check completed
- [ ] At least 4 internal cross-links
- [ ] FAQ has 4+ questions
- [ ] Content is specific to this industry/topic (not generic AI fluff)
