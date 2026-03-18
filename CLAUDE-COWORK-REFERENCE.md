# Claude Co-Work — Complete Reference for nycclaw.com Content

_Last updated: 2026-03-17. Source: Official Anthropic docs, support articles, plugin repos, and product pages._

---

## What Is Co-Work?

Co-Work brings Claude Code's agentic architecture to Claude Desktop for **non-coding knowledge work**. Instead of responding to prompts one at a time, Claude takes on complex, multi-step tasks and executes them autonomously.

- **Launched:** January 12, 2026 (research preview)
- **Status:** Research preview — still evolving, some enterprise features missing
- **Tagline:** "Claude Code power for knowledge work"
- **How it differs from Chat:** In Chat, Claude responds but can't access files. In Co-Work, Claude can read, edit, and create files in folders you specify — it completes tasks, not just describes them.
- **How it differs from Claude Code:** Claude Code is a CLI for developers. Co-Work is the same agentic architecture in the desktop app, no terminal required.

## Availability & Pricing

| Plan | Price | Co-Work Access | Notes |
|------|-------|---------------|-------|
| Pro | $17/mo (annual) or $20/mo | Included | Quick tasks. Consumes limits faster than Chat. |
| Max 5x | $100/mo | Included | Great for everyday use on longer tasks |
| Max 20x | $200/mo | Included | Power users who hand off work throughout the day |
| Team | $20/seat/mo | Included (standard + premium seats) | Teams of 5-75. Includes Slack connector + self-serve management |
| Enterprise | Custom | Included | Admin controls. Cowork toggle is org-wide. |

**Usage note:** Co-Work consumes significantly more usage allocation than regular Chat because multi-step tasks are compute-intensive and require more tokens.

## Platforms

- macOS (Claude Desktop)
- Windows (latest Claude for Windows required; arm64 NOT supported)
- Mobile (iOS/Android) — can assign tasks remotely that execute on your desktop
- **NOT available:** Web-only (claude.ai), Linux

## How It Works — Technical Architecture

1. **Runs in a VM** — Co-Work runs in an isolated virtual machine on your local computer
2. **Local execution** — Code runs safely in an isolated space, but Claude can make real changes to your files
3. **Conversation history stored locally** — NOT on Anthropic's servers
4. **Process:** You describe outcome → Claude breaks into steps → executes each → shows plan before significant actions → delivers finished work
5. **Persistent thread** — One continuous conversation that syncs across desktop and mobile. Context retained across tasks.

## Core Capabilities

### File & Document Management
- Read, edit, create, and organize local files
- Sort/rename files with sensible conventions
- Extract data from receipts/invoices/screenshots into spreadsheets
- Create formatted documents following brand templates

### Research & Analysis
- Web research via Claude in Chrome extension or web search tool
- Synthesize information from multiple sources
- Market sizing with deliverables (PowerPoint, Excel)
- Competitive analysis

### Scheduled/Recurring Tasks
- Set up via `/schedule` command or "Scheduled" sidebar
- Runs automatically at chosen cadence (daily, weekly, monthly)
- Only runs while computer is awake and Claude Desktop is open
- Each scheduled task runs as its own Co-Work session
- Has access to same connectors, plugins, and file access as regular tasks

### Mobile Task Assignment
- Message Claude from phone, work executes on desktop
- Same conversation context across both surfaces
- Can hand off tasks that use desktop files, connectors, plugins
- Essentially a remote control for desktop resources

## Connectors (38+ Integrations)

Connectors use the **Model Context Protocol (MCP)** — an open standard by Anthropic for connecting AI to external tools. All connectors are free. OAuth-based authentication, respects underlying account permissions.

### Communication
- **Slack** (works with 8 plugins — most connected)
- **Gmail**
- **Microsoft 365** (Outlook, OneDrive, SharePoint, Teams)

### Project Management
- **Jira** (works with 6 plugins)
- **Asana**
- **Linear**
- **Monday.com**
- **ClickUp**

### Content & Knowledge
- **Notion** (works with 6 plugins)
- **Google Drive** (Docs, Sheets, Slides — works with 5 plugins)
- **WordPress.com**
- **Guru**

### CRM & Sales
- **HubSpot** (contacts, deals, campaigns, tickets — works with 3 plugins)
- **Salesforce**
- **Close**
- **Clay**
- **ZoomInfo**
- **LinkedIn**

### Design
- **Canva**
- **Figma**

### Data & Engineering
- **GitHub**
- **Snowflake**
- **Databricks**
- **BigQuery**
- **Hex**
- **Amplitude**
- **Pendo**

### Other
- **Google Calendar**
- **Intercom**
- **Fireflies** (meeting transcripts)
- **Box**
- **Egnyte**
- **DocuSign**
- **Klaviyo**
- **Ahrefs**
- **SimilarWeb**
- **BioRender, PubMed, ClinicalTrials.gov** (bio-research)

### Connector Setup
1. Open Cowork session
2. Plugin prompts you to connect when needed (or set up proactively in settings)
3. OAuth authorization flow in browser
4. One-time auth — stays active across sessions
5. No limit on number of connected tools

## Plugins System

Plugins customize how Claude works for specific roles, teams, and companies. Each bundles **skills, connectors, slash commands, and sub-agents** into a single package.

### Plugin Architecture
```
plugin-name/
├── .claude-plugin/plugin.json   # Manifest (metadata)
├── .mcp.json                    # Tool connections (MCP servers)
├── commands/                    # Slash commands (explicit user actions)
├── skills/                      # Domain knowledge (auto-invoked when relevant)
├── agents/                      # Specialized sub-agents
└── hooks/                       # Event handlers
```

**Everything is file-based** — markdown and JSON, no code, no infrastructure, no build steps.

### Components Explained

**Skills** — Domain expertise, best practices, and workflows. Claude draws on these automatically when relevant. Located in `skills/` directory with `SKILL.md` files.

**Commands** — Explicit actions triggered by user (e.g., `/sales:call-prep`, `/finance:reconciliation`). Located in `commands/` directory as markdown files.

**Connectors** — MCP server configurations in `.mcp.json`. Wire Claude to external tools.

**Agents** — Specialized sub-agents for specific tasks. Claude invokes automatically based on context. Located in `agents/` directory.

**Hooks** — Event handlers that respond to Claude Code events (PreToolUse, PostToolUse, SessionStart, etc.). JSON configuration with matchers and actions.

### 11 Official Anthropic Plugins

| Plugin | Purpose | Key Connectors |
|--------|---------|---------------|
| **Productivity** | Tasks, calendars, daily workflows, personal context | Slack, Notion, Asana, Linear, Jira, Monday, ClickUp, Microsoft 365 |
| **Sales** | Prospect research, call prep, pipeline review, outreach, battlecards | Slack, HubSpot, Close, Clay, ZoomInfo, Notion, Jira, Fireflies, Microsoft 365 |
| **Customer Support** | Triage tickets, draft responses, escalations, KB articles | Slack, Intercom, HubSpot, Guru, Jira, Notion, Microsoft 365 |
| **Product Management** | Specs, roadmaps, user research synthesis, stakeholder updates | Slack, Linear, Asana, Monday, ClickUp, Jira, Notion, Figma, Amplitude, Pendo, Intercom, Fireflies |
| **Marketing** | Content drafting, campaigns, brand voice, competitive briefs | Slack, Canva, Figma, HubSpot, Amplitude, Notion, Ahrefs, SimilarWeb, Klaviyo |
| **Legal** | Contract review, NDA triage, compliance, risk assessment | Slack, Box, Egnyte, Jira, Microsoft 365 |
| **Finance** | Journal entries, reconciliation, financial statements, variance analysis | Snowflake, Databricks, BigQuery, Slack, Microsoft 365 |
| **Data** | SQL queries, statistical analysis, dashboards, data validation | Snowflake, Databricks, BigQuery, Hex, Amplitude, Jira |
| **Enterprise Search** | Cross-platform search (email, chat, docs, wikis) | Slack, Notion, Guru, Jira, Asana, Microsoft 365 |
| **Bio Research** | Literature search, genomics analysis, target prioritization | PubMed, BioRender, bioRxiv, ClinicalTrials.gov, ChEMBL, Benchling |
| **Plugin Create** | Build and customize new plugins from scratch | — |

### Custom Plugin Development
- Use the **Plugin Create** plugin to build from scratch
- Or fork/modify any official plugin from GitHub: `github.com/anthropics/knowledge-work-plugins`
- Customize by: swapping connectors, adding company context, adjusting workflows
- Install scopes: user (global), project (shared via git), local (gitignored), managed (org-wide)

### Organization Plugin Marketplaces (Team/Enterprise)
- Owners can create curated plugin marketplaces
- Per-plugin installation preferences: auto-install, available, or hidden
- Distribute via Organization settings > Plugins

## Instructions & Customization

### Global Instructions
- Standing instructions that apply to every Co-Work session
- Set via Settings > "Cowork instructions" (or pencil icon in Cowork)
- Use for: preferred tone, output format, role context, background info

### Folder Instructions
- Project-specific context when a local folder is selected
- Claude can also update these on its own during sessions

### Plugin Customization
- Swap connectors in `.mcp.json`
- Add company terminology/processes to skill files
- Modify workflow instructions
- Build entirely new plugins for uncovered roles

## Security & Safety

### Protections
- Runs in an isolated VM on local computer
- Claude shows plan before significant actions
- You control which folders and connectors Claude can access
- Cannot access anything without explicit permission
- Conversation history stored locally, not on Anthropic servers

### Risks & Best Practices
- **Prompt injection** — Web content is a primary attack vector. Limit browser access to trusted sites.
- **File access** — Be cautious granting access to sensitive files (financial, credentials). Use a dedicated working folder.
- **Scheduled tasks** — Run without active monitoring. Extra care on setup.
- **MCPs/plugins** — Each extends Claude's scope. Stick to verified extensions. Review permissions.
- **Cross-app data** — With Excel/PowerPoint add-ins, data may flow between apps without explicit direction.
- **Mobile access** — Phone becomes remote control for desktop. Consider what access is appropriate.

### Enterprise Limitations (Current)
- **No audit logging** — Not captured in audit logs, compliance API, or data exports
- **Local storage only** — Not subject to Anthropic's standard data retention policies
- **Org-wide toggle** — All members or none (no per-user granularity without contacting Anthropic)
- **OpenTelemetry** — Available for usage/cost/tool tracking (Team/Enterprise)

## Example Use Cases by Role

### Real Estate
- Automated comp analysis from MLS data + local files
- Listing description generation following brand guidelines
- Client follow-up scheduling and draft emails
- Market report generation (weekly/monthly automated)
- Lead qualification and CRM updates via HubSpot/Salesforce connector
- Contract/lease review with legal plugin

### Law Firms
- Contract review and redlining
- NDA triage and compliance workflows
- Case research synthesis from multiple document sources
- Client billing and time tracking summaries
- Discovery document organization (chronological exhibit sets)
- Regulatory compliance monitoring

### Finance / Accounting
- Journal entries and reconciliation
- Financial statement generation
- Variance analysis
- Audit support and documentation
- Budget vs. actual reporting
- Close workflow management

### Healthcare
- Patient intake form processing
- Insurance pre-authorization workflows
- Clinical note synthesis
- Appointment scheduling and follow-up
- Compliance documentation (HIPAA-aware workflows)
- Research literature review

### E-Commerce
- Customer review aggregation and sentiment analysis
- Product listing optimization
- Competitive pricing analysis
- Ad creative brief generation
- Inventory and fulfillment reporting
- Customer support ticket triage

### Marketing
- Campaign planning and execution
- Brand voice enforcement across content
- SEO keyword research and content optimization (via Ahrefs connector)
- Social media content calendars
- Performance reporting across channels
- Competitive intelligence briefings

### Insurance
- Policy document review and comparison
- Claims processing workflow
- Underwriting data synthesis
- Client renewal preparation
- Compliance reporting
- Risk assessment documentation

### Property Management
- Lease analysis and renewal tracking
- Maintenance request triage and scheduling
- Tenant communication drafts
- Financial reporting per property
- Vendor management and invoice processing
- Occupancy and market rate analysis

### Recruiting
- Candidate resume screening and scoring
- Job description generation
- Interview question prep
- Candidate outreach drafts
- Pipeline reporting
- Offer letter and onboarding document creation

## Training & Service Offering Context

### What NYC Claw Offers (for page CTAs)
NYC Claw provides white-glove Claude Co-Work setup and training:

**Setup Services:**
- Custom plugin development for your specific industry and workflow
- Connector configuration (CRM, project management, document storage)
- Global and folder instruction tuning
- Scheduled task configuration
- Security best practices and permission setup

**Training Services (Remote or In-Person):**
- How to use Co-Work effectively (prompting, task delegation, monitoring)
- Plugin customization for your team
- Building scheduled automated workflows
- Connector setup and management
- Best practices for file organization and instructions
- Team rollout (for Team/Enterprise plans)

**Ongoing Support:**
- Plugin updates as Anthropic evolves the platform
- New connector setup as tools are added
- Workflow optimization based on usage patterns

### Key Selling Points for Pages
1. **It runs on YOUR computer** — No data leaves your machine (unlike cloud-only AI tools)
2. **Connects to tools you already use** — 38+ integrations, not a walled garden
3. **Automates recurring work** — Scheduled tasks for daily/weekly/monthly deliverables
4. **Customizable via plugins** — Not one-size-fits-all; tailored to your role and industry
5. **Mobile assignment** — Hand off work from your phone, come back to finished deliverables
6. **No coding required** — Same power as Claude Code, accessible to everyone

### Differentiator: Why Hire a Consultant for This?
- Plugin development requires understanding MCP, skill files, and connector configs
- Getting good outputs requires well-crafted global/folder instructions
- Security setup needs expertise (which folders, which connectors, what permissions)
- Industry-specific workflows need domain knowledge + AI knowledge
- Most businesses don't have time to learn the plugin system from scratch
- One-time setup → ongoing value without ongoing consulting fees

## Skills — Deep Dive

Skills are the core extensibility mechanism. They teach Claude new capabilities via markdown files — no code required.

### What Is a Skill?

A `SKILL.md` file with YAML frontmatter + markdown instructions. Claude reads the skill and adds it to its toolkit. Skills fire automatically when relevant, or users invoke them directly with `/skill-name`.

Skills follow the **Agent Skills open standard** (agentskills.io) — works across multiple AI tools, not just Claude.

### Skill Types

**Reference Skills** — Domain knowledge that Claude applies to current work (conventions, patterns, style guides). Runs inline alongside conversation context.

**Task Skills** — Step-by-step instructions for specific actions (deployments, reports, code generation). Often invoked explicitly with `/skill-name`.

### Skill File Structure
```
my-skill/
├── SKILL.md           # Main instructions (required)
├── template.md        # Template for Claude to fill in
├── examples/
│   └── sample.md      # Example output showing expected format
└── scripts/
    └── validate.sh    # Script Claude can execute
```

### SKILL.md Anatomy
```yaml
---
name: weekly-report              # Becomes /weekly-report command
description: Generates weekly performance reports. Use when asked for weekly summaries.
argument-hint: [date-range]      # Shown in autocomplete
disable-model-invocation: false  # true = manual only, false = Claude auto-invokes
user-invocable: true             # false = hidden from / menu (background knowledge)
allowed-tools: Read, Grep        # Tools Claude can use without asking permission
context: fork                    # fork = runs in subagent, inline = runs in main context
---

When generating a weekly report:
1. Pull data from connected sources
2. Organize by department
3. Highlight anomalies
4. Format as PDF using company template
```

### Key Frontmatter Fields

| Field | Purpose |
|-------|---------|
| `name` | Display name and /command trigger. Lowercase, hyphens, max 64 chars. |
| `description` | What the skill does. Claude uses this to decide when to auto-invoke. |
| `argument-hint` | Shows in autocomplete (e.g., `[client-name]`). |
| `disable-model-invocation` | `true` = only fires when user types /name. Good for destructive actions. |
| `user-invocable` | `false` = hidden from menu. For background knowledge Claude draws on silently. |
| `allowed-tools` | Tools available without permission prompts when skill is active. |
| `context` | `fork` = runs in isolated subagent. `inline` = runs in main conversation. |
| `model` | Override the model for this skill (e.g., use Haiku for fast tasks). |

### Where Skills Live (Scope)

| Location | Scope | Priority |
|----------|-------|----------|
| Enterprise managed settings | All org users | Highest |
| `~/.claude/skills/` | Personal (all projects) | High |
| `.claude/skills/` | Project-specific | Medium |
| `<plugin>/skills/` | Where plugin is enabled | Low (namespaced as `plugin:skill`) |

Higher-priority locations win when names conflict.

### Dynamic Features

**$ARGUMENTS** — Captures user input after the command. E.g., `/weekly-report Q1 2026` makes `$ARGUMENTS = "Q1 2026"`.

**Supporting files** — Reference templates, examples, scripts from within SKILL.md. Claude reads them when needed.

**Progressive disclosure** — Start with a brief SKILL.md, reference detailed docs in separate files Claude loads only when needed. Keeps token usage efficient.

**Subagent execution** — Set `context: fork` to run skill in an isolated subagent with its own context window. Good for long tasks that shouldn't pollute the main conversation.

### Bundled Skills (Ship with Claude Code/Co-Work)

| Skill | Purpose |
|-------|---------|
| `/batch <instruction>` | Orchestrate large-scale changes in parallel — spawns one agent per unit of work |
| `/claude-api` | Load Claude API reference for your language |
| `/debug [description]` | Troubleshoot session issues by reading debug logs |
| `/loop [interval] <prompt>` | Run a prompt repeatedly on schedule |
| `/simplify [focus]` | Review recent changes for quality, spawns 3 parallel review agents |

### Creating Custom Skills for Clients (NYC Claw Service Angle)

This is the core of what we sell:

1. **Identify repetitive workflows** — What does the client do weekly? Monthly? What takes hours?
2. **Map to skill structure** — Each workflow becomes a SKILL.md with step-by-step instructions
3. **Add supporting files** — Templates the client already uses, example outputs, validation scripts
4. **Configure connectors** — Hook up the CRM, project tracker, email via MCP
5. **Set scheduling** — Recurring tasks via `/schedule` for automated deliverables
6. **Test and tune** — Iterate on prompts until output quality matches client expectations

**Example: Real Estate Agent Skill**
```yaml
---
name: weekly-market-report
description: Generates a weekly market analysis report for client distribution
disable-model-invocation: true
---

Generate a weekly market report:
1. Pull new listings from MLS connector (last 7 days)
2. Calculate median price changes by neighborhood
3. Identify notable sales (above/below ask)
4. Check mortgage rate trends
5. Format using the template in ./templates/market-report.md
6. Save to ~/Reports/weekly/ with date in filename
7. Draft email summary for client newsletter
```

**Example: Law Firm Skill**
```yaml
---
name: contract-review
description: Reviews contracts for standard issues and red flags
---

When reviewing a contract:
1. Identify contract type (NDA, MSA, employment, lease, etc.)
2. Check for missing standard clauses per ./reference/required-clauses.md
3. Flag unusual liability provisions
4. Note indemnification scope
5. Check termination conditions
6. Compare fee structure against market rates in ./reference/market-rates.md
7. Generate a summary memo with: risk level (low/medium/high), key terms, recommended changes
```

## Sub-Agents — Technical Detail

Sub-agents are specialized AI assistants that run in their own context window with custom prompts, tool access, and permissions.

### Built-in Sub-Agents
- **Explore** — Fast, read-only (Haiku model). Searches/analyzes without making changes.
- **Plan** — Research agent for plan mode. Read-only, gathers context before presenting plans.
- **General-purpose** — Full tool access for complex multi-step tasks.

### Custom Sub-Agent Configuration
```yaml
---
name: security-reviewer
description: Reviews code changes for security vulnerabilities
model: sonnet
tools: [Read, Grep, Glob, Bash]
disallowedTools: [Write, Edit]
permissionMode: default
maxTurns: 10
---

You are a security reviewer. Focus on:
- Input validation and sanitization
- Authentication and authorization
- Data exposure risks
- Dependency vulnerabilities
```

### Sub-Agent Scopes
| Location | Scope |
|----------|-------|
| `--agents` CLI flag | Current session only |
| `.claude/agents/` | Current project |
| `~/.claude/agents/` | All projects (personal) |
| `<plugin>/agents/` | Where plugin is enabled |

## Plugin Marketplace & Distribution

### Official Marketplace
- `claude-plugins-official` — auto-available in Claude Code
- Browse via `/plugin` → Discover tab
- Install: `/plugin install plugin-name@claude-plugins-official`
- Submit custom plugins: claude.ai/settings/plugins/submit

### External Integration Plugins Available
- **Source control:** GitHub, GitLab
- **Project management:** Atlassian (Jira/Confluence), Asana, Linear, Notion
- **Design:** Figma
- **Infrastructure:** Vercel, Firebase, Supabase
- **Communication:** Slack
- **Monitoring:** Sentry

### Creating Your Own Marketplace
- Any GitHub repo, Git URL, or local directory can be a marketplace
- Add via: `/plugin marketplace add owner/repo`
- Organization-managed marketplaces for Team/Enterprise (plugin installation preferences: auto-install, available, hidden)

### Plugin Installation Scopes
| Scope | Settings File | Use Case |
|-------|--------------|----------|
| User | `~/.claude/settings.json` | Personal, all projects |
| Project | `.claude/settings.json` | Team, shared via git |
| Local | `.claude/settings.local.json` | Project-specific, gitignored |
| Managed | Enterprise settings | Org-wide, read-only |

## Hooks System

Event-driven automation that fires on Claude actions:

### Available Events
- `PreToolUse` — Before Claude uses any tool
- `PostToolUse` — After successful tool use
- `PostToolUseFailure` — After tool execution fails
- `PermissionRequest` — When permission dialog shows
- `UserPromptSubmit` — When user submits a prompt
- `Notification` — When Claude sends notifications
- `Stop` — When Claude attempts to stop
- `SubagentStart/Stop` — Sub-agent lifecycle
- `SessionStart/End` — Session lifecycle
- `TaskCompleted` — When task is marked done
- `PreCompact` — Before conversation compaction

### Hook Types
- **command** — Execute shell scripts
- **prompt** — Evaluate a prompt with LLM
- **agent** — Run an agentic verifier with tools

### Example Hook (auto-format after writes)
```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "./scripts/format-code.sh"
          }
        ]
      }
    ]
  }
}
```

## MCP (Model Context Protocol) — How Integrations Work

MCP is the open standard Anthropic developed for connecting AI to external tools. It's the protocol layer that powers all connectors and custom integrations.

### How MCP Works
- Each connector is an MCP server that authenticates via OAuth or API keys
- Respects underlying account permissions (Claude only sees what you can see)
- Configured via `.mcp.json` files in plugins or project directories
- Can be local (stdio) or remote (HTTP) servers

### MCP Server Configuration Example
```json
{
  "mcpServers": {
    "hubspot-crm": {
      "command": "npx",
      "args": ["@hubspot/mcp-server", "--api-key", "${HUBSPOT_API_KEY}"],
      "env": {
        "HUBSPOT_API_KEY": "${HUBSPOT_API_KEY}"
      }
    },
    "company-database": {
      "command": "${CLAUDE_PLUGIN_ROOT}/servers/db-server",
      "args": ["--config", "${CLAUDE_PLUGIN_ROOT}/config.json"]
    }
  }
}
```

### Custom MCP Servers
- Anyone can build an MCP server for any tool/API
- Open specification at modelcontextprotocol.io
- Growing ecosystem of community servers
- This is how NYC Claw can build **custom integrations** beyond the 38+ built-in connectors

### Key MCP Concepts for Sales Pages
1. **It's an open standard** — Not locked into Anthropic. Works across tools.
2. **Secure by design** — OAuth flows, scoped permissions, no stored credentials on Anthropic servers.
3. **Extensible** — If a connector doesn't exist for your tool, one can be built.
4. **Free** — All connectors are free. You just need the underlying tool subscription.

## Real-World Workflows & Use Cases (From Reddit, X, Blogs)

_Sourced from actual users sharing what they've built. Gold for content authenticity._

### Marketing & SEO (Reddit power user u/rebelytics)
- **Banner uploads to affiliate network** — Cowork analyzes image content, generates metadata, creates import CSV. Hours → minutes. Built a self-improving skill for repeatability.
- **Prompt tracking strategies** — Built tracking strategies in AI monitoring tools using GSC data + crawl exports. When public API hit limitations, Cowork reverse-engineered the UI's internal API via Chrome extension.
- **Trending topics research (scheduled weekly)** — Classifies by content potential and business impact. Each run accesses previous results so it doesn't repeat. Series builds logically.
- **Product feed optimization** — Loaded 25 feeds with ~100K products each. Analyzed quality issues, missing columns, inconsistencies between feeds.
- **Dev tickets for schema implementation** — Chrome extension analyzes website, identifies page types, extracts structured data, generates developer tickets. Self-improving skill.
- **Image alt texts at scale** — Generates for thousands of images combining crawl data with Chrome extension verification of actual images and context.
- **Website crawl analysis** — Frequent analysis of crawl exports, combined with Chrome extension to verify findings.
- **Meta-skill for self-improving workflows** — Open-sourced at github.com/rebelytics/one-skill-to-rule-them-all. Watches other skills perform, logs corrections, improves skills over time.

### Contact & Networking
- **Twitter → LinkedIn migration** — Scraped mutuals via Chrome extension, set up daily scheduled task surfacing 20 LinkedIn profiles to connect with. Manual connection requests to avoid LinkedIn detection.

### Time Management
- **Weekly review (scheduled)** — Accesses time tracking, strategic goals, planned tasks (iOS Reminders), and calendar. Reviews progress, surfaces content ideas from weekly work topics.

### Bookkeeping & Finance
- **GnuCash MCP for small business books** — User found a gnucash MCP project, now does books for "a few small businesses in minutes"
- **Invoice processing** — Extract key fields (vendor, date, amount, line items), compile into master billing spreadsheet. Handles varying invoice formats, flags missing fields.
- **Stripe reporting (scheduled)** — Automated recurring revenue reports
- **Sales tracking discrepancy analysis** — Compared transaction data exports from shop system vs analytics platform, found patterns across payment providers, countries, order status in tens of thousands of rows

### File Management & Organization
- **Document inbox sorting (scheduled daily)** — Morning task sorts dropped files into categorized folders (clients, finances, projects, personal), generates daily summary report
- **Screenshot organization** — Categorizes and organizes recent screenshots
- **Context management kit** — Near-line tiering system: manifest file → canonical docs → lazy-load other files. Prevents Claude from reading all 462 files.
- **File cleanup (scheduled)** — Recurring file organization and deduplication

### Real Estate Specific (from theaicareerlab.com)
- **Listing descriptions** — Property details → formatted MLS listing in seconds (30-45 min → 5 min)
- **Client follow-up emails** — Personalized recaps of showings with specific property pros/cons
- **Market analysis summaries** — Raw data → client-ready narrative with pricing strategy recommendations
- **Lead generation content** — Instagram captions, blog outlines, email newsletters positioning agent as local expert
- **Transaction management** — Inspection response letters, extension requests, repair request letters
- **CMA templates** — Upload your template, Claude fills in data and formats consistently

### Legal (from Artificial Lawyer viral post — 7M views)
- **Zack Shapiro's "Claude-Native Law Firm"** — Custom skills encoding his analytical frameworks, preferred formats, voice, and judgment for contract review
- **Contract markup at XML level** — Claude opens .docx at XML level, writes exact tracked changes markup attributed to lawyer's name
- **Citation reformatting** — Writes code to parse and reformat every Bluebook citation in seconds
- **NDA triage** — Batch processing: `/triage-nda all-ndas-in-folder` → organized reports, redlined docs, risk matrices
- **Compliance workflows** — Regulatory monitoring and documentation

### Design & UX
- **UX workflows** — Prototyping, wireframing, user journeys, case studies
- **Figma integration** — MCP connection + skills for implementing designs
- **Presentation generation** — Connected to Notion + Jira, generated PowerPoint slides for short-notice presentation

### Founder/Business Workflows (from X)
- **"Reply guy" assistant** — Automated engagement responses
- **BD and partnership outreach** — Research + draft outreach
- **Content pipeline** — X & LinkedIn content generation
- **Flight price tracking (scheduled)** — Monitors prices and alerts on drops

### Advanced Patterns
- **Self-improving skills** — Meta-skill watches sessions, logs observations when corrections are made, applies learnings to improve skills over time
- **Dual-layer activation** — Don't rely on skill descriptions alone; add CLAUDE.md instruction to load critical skills at session start. Skill triggers serve as backup.
- **Handoff docs for context transfer** — When switching between Chat and Cowork, ask Claude to create a downloadable handoff doc
- **Autonomous execution** — Write plan → have Claude rewrite specifically for autonomous execution → one-shot complex projects in Cowork with MCP/connectors
- **Chrome extension as primary data source** — More reliable than web fetch tool (which gets blocked by Cloudflare/bot protection). Chrome extension navigates as normal user.

### Scheduled Task Ideas (from aiblewmymind Substack)
1. Morning email briefing
2. File cleanup and organization
3. Stripe revenue reporting
4. Invoice organizing
5. Apple Notes tidying
6. Flight price tracking
7. Weekly team presentation prep
8. Spreadsheet updates
9. Social media content scheduling
10. Competitive monitoring

### Competitor Content Already Ranking
- **theaicareerlab.com** — "Claude CoWork for Real Estate Agents" (comprehensive guide)
- **claudecowork.im** — Legal plugin tutorial, marketing plugin guide
- **medium.com** — Multiple "Claude Cowork for [industry]" articles (thin content, beatable)
- **successknocks.com** — "Claude Cowork Plugins for Legal Teams"
- **pluginsforcowork.com** — Connector and plugin directory
- **max-productive.ai** — Connector guide
- **the-ai-corner.com** — Cowork setup guide

### Key Insight: Where NYC Claw Wins
Every piece of content out there is a **guide** — "here's how to set it up yourself." Nobody is saying **"we'll build this for you."** That's the gap. Our pages don't just explain what's possible — they offer the service. Every spoke page ends with "Book a free call and we'll set this up for your business."

## Technical Reference Links

- Product page: https://claude.com/product/cowork
- Getting started: https://support.claude.com/en/articles/13345190-get-started-with-cowork
- Safety guide: https://support.claude.com/en/articles/13364135-use-cowork-safely
- Plugins guide: https://support.claude.com/en/articles/13837440-use-plugins-in-cowork
- Scheduled tasks: https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-cowork
- Mobile assignment: https://support.claude.com/en/articles/13947068-assign-tasks-to-claude-from-anywhere-in-cowork
- Team/Enterprise: https://support.claude.com/en/articles/13455879-use-cowork-on-team-and-enterprise-plans
- Plugin blog post: https://claude.com/blog/cowork-plugins
- Plugin marketplace: https://claude.com/plugins-for/cowork
- Plugin GitHub (open source): https://github.com/anthropics/knowledge-work-plugins
- Plugin technical reference: https://code.claude.com/docs/en/plugins-reference
- MCP specification: https://modelcontextprotocol.io/
