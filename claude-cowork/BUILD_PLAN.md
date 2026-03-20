# Claude Cowork Pages — Build Plan

_30 pages targeting the Claude Cowork keyword cluster for nycclaw.com_

---

## Build Order

### Batch 1: Pillar + Core (5 pages)
| # | File | Primary Keywords | Vol | Status |
|---|------|-----------------|-----|--------|
| 1 | `claude-cowork/index.html` | claude cowork, cowork claude | 40,900 | ✅ |
| 2 | `claude-cowork/plugins.html` | claude cowork plugins, best plugins | 650 | ✅ |
| 3 | `claude-cowork/skills.html` | claude cowork skills, custom skills | 90 | ✅ |
| 4 | `claude-cowork/setup-guide.html` | claude cowork setup, tutorial, getting started | 80 | ✅ |
| 5 | `claude-cowork/pricing-guide.html` | claude cowork pricing, how much does it cost | 340 | ✅ |

### Batch 2: Top Industry Spokes (5 pages)
| # | File | Primary Keywords | Status |
|---|------|-----------------|--------|
| 6 | `claude-cowork/legal.html` | claude cowork legal | ✅ |
| 7 | `claude-cowork/real-estate.html` | claude cowork real estate | ✅ |
| 8 | `claude-cowork/marketing.html` | claude cowork marketing | ✅ |
| 9 | `claude-cowork/finance.html` | claude cowork finance | ✅ |
| 10 | `claude-cowork/healthcare.html` | claude cowork healthcare | ✅ |

### Batch 3: More Industry Spokes (5 pages)
| # | File | Primary Keywords | Status |
|---|------|-----------------|--------|
| 11 | `claude-cowork/ecommerce.html` | claude cowork ecommerce | ✅ |
| 12 | `claude-cowork/property-management.html` | claude cowork property management | ✅ |
| 13 | `claude-cowork/insurance.html` | claude cowork insurance | ✅ |
| 14 | `claude-cowork/construction.html` | claude cowork construction | ✅ |
| 15 | `claude-cowork/startups.html` | claude cowork startups | ✅ |

### Batch 4: Remaining Industry Spokes (5 pages)
| # | File | Primary Keywords | Status |
|---|------|-----------------|--------|
| 16 | `claude-cowork/accounting.html` | claude cowork accounting | ✅ |
| 17 | `claude-cowork/recruiting.html` | claude cowork recruiting | ✅ |
| 18 | `claude-cowork/mortgage-brokers.html` | claude cowork mortgage brokers | ✅ |
| 19 | `claude-cowork/real-estate-investors.html` | claude cowork real estate investors | ✅ |
| 20 | `claude-cowork/coaches-consultants.html` | claude cowork consultants | ✅ |

### Batch 5: Feature + Use Case Pages (4 pages)
| # | File | Primary Keywords | Vol | Status |
|---|------|-----------------|-----|--------|
| 21 | `claude-cowork/use-cases.html` | claude cowork use cases, examples | 190 | ✅ |
| 22 | `claude-cowork/scheduled-tasks.html` | claude cowork scheduled tasks | 10+ | ✅ |
| 23 | `claude-cowork/chrome-extension.html` | claude cowork chrome extension | 60 | ✅ |
| 24 | `claude-cowork/enterprise.html` | claude cowork enterprise, for teams | 40 | ✅ |

### Batch 6: Comparison + Connector Pages (4 pages)
| # | File | Primary Keywords | Status |
|---|------|-----------------|--------|
| 25 | `claude-cowork/vs-chatgpt.html` | claude cowork vs chatgpt | ✅ |
| 26 | `claude-cowork/vs-copilot.html` | claude cowork vs microsoft copilot | ✅ |
| 27 | `claude-cowork/connectors.html` | claude cowork connectors | ✅ |
| 28 | `claude-cowork/custom-plugins.html` | claude cowork custom plugins | ✅ |

### Batch 7: Training + Service Pages (2 pages)
| # | File | Primary Keywords | Status |
|---|------|-----------------|--------|
| 29 | `claude-cowork/training.html` | claude cowork training | ✅ |
| 30 | `claude-cowork/consulting.html` | claude cowork consulting | ✅ |

---

## Pipeline Per Batch

1. **Research** — Agent reads CLAUDE-COWORK-REFERENCE.md + studies template
2. **Generate** — Agent creates each HTML page following COWORK_PROMPT.md rules
3. **Humanize** — Agent runs `/humanizer` on all content before saving
4. **Link Check** — Agent verifies all internal links, CTAs, cross-links
5. **Review** — Bruce audits output (structure, links, writing, SEO, nav)
6. **Fix** — Address any issues
7. **Update tracker** — Mark pages as done in BUILD_PLAN.md

---

## Post-Build (after all 30 pages)

- [ ] Update `sitemap.xml` with all 30 new URLs
- [ ] Update `industries.html` hub to include Cowork section
- [ ] Update nav dropdown on ALL existing pages to include `/claude-cowork/` link
- [ ] Cross-link existing `/for/` pages to matching `/claude-cowork/` spokes
- [ ] Cross-link `/claude-cowork/` spokes to matching `/for/` pages
- [ ] Verify all internal links work (no 404s)
- [ ] Git commit + push
- [ ] Deploy: `wrangler pages deploy . --project-name nycclaw`
- [ ] Submit updated sitemap to Google Search Console
