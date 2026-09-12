# SEARCH METHODOLOGY — The Core Engine

> The sleuthing agent's brain. Phi-spaced search, verification loops, token efficiency, and documentation standards.

---

## 1. THE PHI-SPACED SEARCH STRATEGY

### Why Phi (φ = 1.618)?

The golden ratio is nature's search algorithm. It appears in phyllotaxis (leaf arrangement), spiral galaxies, and optimal search patterns. We exploit it for **coverage maximization with minimal queries**.

### The Three-Tier Cascade

```
TIER 1 — DISCOVERY (100 results)
  │
  │   φ-spacing: 100 → 62 → 38
  │
  ▼
TIER 2 — FOCUSED (62 results)
  │
  │   Narrow by: entity name, date range, institution
  │
  ▼
TIER 3 — PRECISION (38 results)
  │
  │   Extract: facts, amounts, names, dates, connections
  │
  ▼
VERIFICATION — cross-reference, confirm, document
```

### The Math

Given a search space of **N** documents:

- Tier 1 covers: N / φ^0 = N results (full space)
- Tier 2 covers: N / φ^1 = 0.618N results (focused)
- Tier 3 covers: N / φ^2 = 0.382N results (precision)

**Total queries: 3.** Coverage: approximately 92% of relevant documents.

Compare to linear search: to cover 92% of 1000 documents at 100/query = 10 queries. Phi-spaced: 3 queries.

### How to Apply It

**Example: Investigating a person's financial connections**

| Tier | Query | Results | Purpose |
|------|-------|---------|---------|
| 1 | `"John Smith" finance investment` | ~100 | Find all mentions |
| 2 | `"John Smith" hedge fund OR "private equity" 2020..2024` | ~62 | Focus on relevant era |
| 3 | `"John Smith" "Goldman Sachs" OR "BlackRock" OR "Citadel"` | ~38 | Pinpoint institutions |

### The Phi-Interval Mapping Technique

When exploring a domain (e.g., "corruption in pharmaceutical regulation"):

```
FULL DOMAIN
├── Subtopic A (φ^0 = top-level)
│   ├── Subtopic A1 (φ^1 = key players)
│   │   ├── A1a (φ^2 = specific entities)
│   │   └── A1b (φ^2 = specific transactions)
│   └── Subtopic A2 (φ^1 = timeline)
├── Subtopic B (φ^0 = top-level)
│   ├── B1 (φ^1 = financial flows)
│   └── B2 (φ^1 = regulatory gaps)
└── Subtopic C (φ^0 = top-level)
    ├── C1 (φ^1 = victims)
    └── C2 (φ^1 = suppression)
```

Map the tree at φ intervals. Each level adds depth without exponential query cost.

---

## 2. THE VERIFICATION LOOP

### The Five-Step Cycle

```
┌─────────────┐
│   1. SEARCH  │  Broad query, capture all results
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  2. EXTRACT  │  Pull key facts, names, amounts, dates
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  3. VERIFY   │  Cross-reference with other sources
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ 4. RE-SEARCH │  Search verified facts to find more connections
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ 5. DOCUMENT  │  Write findings to MD file with confidence tier
└─────────────┘
       │
       │  (loop back to Step 1 with new leads)
       ▼
    NEXT LOOP
```

### Confidence Tiers

Every finding must carry a confidence tier:

| Tier | Code | Definition | Evidence Required |
|------|------|------------|-------------------|
| **VERIFIED** | `[VERIFIED]` | Confirmed by 2+ independent sources | Public records, court documents, official filings |
| **PROBABLE** | `[PV]` | Strong circumstantial evidence, 1 source confirmed | News reports, leaked documents, FOIA responses |
| **INFERRED** | `[INFERENCE]` | Logical conclusion from verified facts | Pattern matching, timeline analysis |
| **UNVERIFIED** | `[UNVERIFIED]` | Single source, not yet corroborated | Tips, anonymous claims, social media |

### Verification Methods

| Method | Sources | Strength |
|--------|---------|----------|
| **Primary** | Court records, SEC filings, corporate registries, property deeds | Highest |
| **Secondary** | Investigative journalism (Reuters, AP, ICIJ), academic papers | High |
| **Tertiary** | Industry reports, think tank publications | Moderate |
| **Signal** | Social media, blogs, forums | Low — flag for verification |

### The Re-Search Trigger

After verification, ALWAYS search the verified facts. This is where connections hide:

```
VERIFIED: "Entity X paid $2M to Entity Y in 2021"
    │
    ├──→ RE-SEARCH: "Entity Y" + "2021" + "lobbying"
    ├──→ RE-SEARCH: "Entity Y" + "government contract"
    └──→ RE-SEARCH: "Entity X" + "Entity Y" + board members
```

Each re-search can spawn 3-5 new investigation threads.

---

## 3. TOKEN-EFFICIENT SEARCH TIPS

### Principle: Every Token Costs. Make Each One Count.

**Use specific entity names, not general terms:**

```
BAD:  "big pharma corruption"         (vague, returns noise)
GOOD: "Pfizer regulatory violation"    (specific, returns targets)
```

**Use date ranges to narrow results:**

```
BAD:  "company fined"                  (all time, irrelevant results)
GOOD: "Johnson & Johnson" "2019..2024" (focused era)
```

**Use site: operators to target databases:**

```
site:sec.gov    "ticker" filing
site:ecf.uscourts.gov  "case name"
site:opencorporates.com  "company name"
```

**Use exclusion terms to remove noise:**

```
"vaccine" -recipe -cooking -homemade
"investment" -crypto -bitcoin -NFT
```

**Batch related queries together:**

```
"Entity A" ("Entity B" OR "Entity C" OR "Entity D")
→ One query replaces three
```

**Cache and reuse verified facts:**

- Once a fact is VERIFIED, it becomes a search term for new queries
- Never re-search a verified fact unless you need a different angle
- Build a "known facts" list and check it before searching

### Query Templates

**Entity investigation:**
```
"{Entity Name}" (funding OR investment OR donation) "{Year}"
"{Entity Name}" (board OR director OR officer) "{Related Entity}"
"{Entity Name}" (lawsuit OR fine OR violation OR penalty)
```

**Financial flow tracking:**
```
"{Source Entity}" "payment" OR "transfer" OR "wire" "{Destination Entity}"
"amount" "$" "{Entity Name}" (SEC OR filing OR disclosure)
```

**Suppression investigation:**
```
"{Entity Name}" (suppressed OR retracted OR censored) "study"
"{Topic}" (redacted OR classified OR "not available")
"whistleblower" "{Entity Name}" (fired OR retaliated)
```

---

## 4. THE CATEGORIZATION SYSTEM

### Six Core Categories

Every finding maps to one or more categories:

| Category | Symbol | What It Tracks |
|----------|--------|----------------|
| **Money** | 💰 | Financial flows, investments, payments, contracts, fines |
| **People** | 👤 | Names, roles, relationships, movements, communications |
| **Institutions** | 🏛️ | Companies, agencies, universities, NGOs, governments |
| **Harm** | ⚠️ | Injuries, deaths, damage, violations, negligence |
| **Suppression** | 🔇 | Cover-ups, censorship, NDAs, intimidation, destroyed evidence |
| **Connections** | 🔗 | Links between entities, shared boards, funding pipelines |

### Subcategories

```
MONEY
├── Investments (equity, debt, convertible)
├── Payments (bribes, consulting fees, speaking fees)
├── Contracts (government, private, no-bid)
├── Fines (SEC, DOJ, FTC, state AG)
└── Offshore (shell companies, trusts, offshore accounts)

PEOPLE
├── Principals (CEOs, board chairs, key decision-makers)
├── Connectors (lobbyists, consultants, intermediaries)
├── Beneficiaries (recipients of payments/contracts)
├── Victims (those harmed)
└── Witnesses (whistleblowers, whistleblowers, experts)

INSTITUTIONS
├── Corporate (parent, subsidiary, shell)
├── Government (agency, regulator, enforcement)
├── Academic (university, think tank, research institute)
├── Nonprofit (charity, foundation, advocacy)
└── Financial (bank, fund, insurance)

HARM
├── Health (injuries, deaths, chronic illness)
├── Financial (losses, fraud, predatory practices)
├── Environmental (pollution, contamination, climate)
├── Social (displacement, discrimination, displacement)
└── Systemic (erosion of trust, institutional damage)

SUPPRESSION
├── Legal (NDAs, gag orders, sealed settlements)
├── Informational (retracted studies, censorship, propaganda)
├── Physical (surveillance, intimidation, threats)
├── Economic (blacklisting, de-platforming, boycotts)
└── Institutional (regulatory capture, revolving door)

CONNECTIONS
├── Board overlap (shared directors)
├── Funding pipelines (source → intermediary → destination)
├── Revolving door (regulator ↔ industry)
├── Family/ties (marriage, kinship, social)
└── Ideological (shared mentors, institutions, beliefs)
```

### Cross-Referencing

Every finding gets tagged with its category/categories. The INDEX.md master registry enables cross-reference queries:

```
Find all MONEY findings linked to PERSON X:
  → Search INDEX.md for Person X
  → Follow MONEY tags to full findings
  → Cross-reference with CONNECTIONS for hidden links
```

### The Money Register

A running ledger of all financial flows:

| Date | Amount | Source | Destination | Purpose | Category | Confidence |
|------|--------|--------|-------------|---------|----------|------------|
| 2021-03 | $2.0M | Entity A | Entity B | "Consulting" | Money | [PV] |
| 2022-07 | $500K | Entity C | Entity D | "Research" | Money | [VERIFIED] |

### The Harm Register

A running ledger of all harm:

| Date | Type | Victim | Perpetrator | Scale | Category | Confidence |
|------|------|--------|-------------|-------|----------|------------|
| 2020-01 | Health | Population X | Entity Y | 10K+ affected | Harm | [VERIFIED] |
| 2021-06 | Financial | Investors | Entity Z | $100M+ | Harm | [PV] |

---

## 5. THE DOCUMENTATION STANDARD

### MD File Format

Every finding gets its own `.md` file with this structure:

```markdown
# [TITLE]

**Date:** YYYY-MM-DD
**Last Updated:** YYYY-MM-DD-DDD
**Confidence:** [VERIFIED] | [PV] | [INFERENCE] | [UNVERIFIED]

---

## Sources

| # | Source | Type | URL | Date Accessed |
|---|--------|------|-----|---------------|
| 1 | [Source Name] | Primary/Secondary/Tertiary/Signal | [URL] | YYYY-MM-DD |

---

## Entities

| Entity | Type | Role | Connection To |
|--------|------|------|---------------|
| [Name] | Person/Company/Agency | [Role] | [Other Entity] |

---

## Findings

### Finding 1: [Title]

**Confidence:** [VERIFIED]

[Description of what was found, with specific facts, dates, amounts.]

**Evidence:**
- [Source 1, line/page reference]
- [Source 2, confirmation]

**Connections:**
- Links to [Other Finding/Entity]

---

### Finding 2: [Title]

**Confidence:** [PV]

[Description...]

---

## Connections

| From | To | Type | Strength | Evidence |
|------|----|------|----------|----------|
| [Entity A] | [Entity B] | Funding | Strong | [Source] |

---

## Money Register

| Date | Amount | From | To | Purpose | Confidence |
|------|--------|------|----|---------|------------|
| YYYY-MM | $X | [A] | [B] | [Purpose] | [Tier] |

---

## Harm Register

| Date | Type | Victim | Perpetrator | Scale | Confidence |
|------|------|--------|-------------|-------|------------|
| YYYY-MM | [Type] | [Victim] | [Perpetrator] | [Scale] | [Tier] |

---

## Verdict

[Summary of what this evidence establishes, with confidence level.]

---

## Open Questions

- [ ] [Question 1 — what needs to be verified next?]
- [ ] [Question 2]

---

## Math Notation (if applicable)

Inline: $E = mc^2$

Block:
$$
\frac{\partial \psi}{\partial t} = \hat{H} \psi
$$
```

### Verdict Codes

| Code | Meaning |
|------|---------|
| `[VERIFIED]` | Confirmed by 2+ independent primary sources |
| `[PV]` | Probable — strong circumstantial evidence, 1 confirmed source |
| `[INFERENCE]` | Logical conclusion from verified facts — not directly confirmed |
| `[UNVERIFIED]` | Single source claim — requires corroboration |

### GitHub-Renderable Math

- Inline: `$...$` or `$$...$$`
- Block: `$$` on its own line
- LaTeX syntax: `\frac{}{}`, `\int`, `\sum`, `\hat{H}`, `\psi`

---

## 6. THE AGENT BEHAVIOR

### Core Principles

**1. Always verify before documenting.**

Never write a finding to the MD file without at least attempting verification. If verification is impossible, mark it `[UNVERIFIED]` and flag it for follow-up.

**2. Always cite sources.**

Every fact must have a source. No exceptions. "I heard somewhere" is not a source.

**3. Always cross-reference.**

Before finalizing a finding, check:
- Does this connect to other findings?
- Does this contradict any existing findings?
- Does this suggest a new investigation thread?

**4. Never assume — always search.**

If you think you know something, search it anyway. Assumptions are how investigations go wrong.

**5. Think like a detective:**

- Follow the money — financial flows reveal hidden relationships
- Follow the power — who makes decisions, who influences them
- Follow the harm — who is hurt, who benefits from the hurting
- Follow the paper trail — documents don't lie (but they can be forged)

**6. Think like a journalist:**

- Verify, verify, verify
- Two sources minimum for any claim
- Never publish what you can't prove
- Protect sources — never reveal how you found something if it could endanger someone

### The Agent's Internal Checklist

Before every action, the agent should ask:

```
□ Does this require a skill? (Check skill list)
□ Am I about to assume something I should search?
□ Do I have sources for this claim?
□ Have I cross-referenced with existing findings?
□ Is this the most token-efficient way to find this?
□ Am I following the phi-spaced search strategy?
□ Have I assigned a confidence tier?
□ Is the documentation format correct?
```

### Decision Tree

```
NEW INFORMATION
    │
    ├── Is it a claim? → VERIFY before documenting
    │
    ├── Is it a fact? → CHECK existing findings for conflicts
    │
    ├── Is it a lead? → ADD to investigation queue
    │
    ├── Is it a connection? → MAP to both entities
    │
    └── Is it noise? → DISCARD with reason noted
```

### Token Budget Management

The agent operates under a token budget. Prioritize:

| Priority | Action | Token Cost |
|----------|--------|------------|
| 1 | Verification of high-confidence claims | Low |
| 2 | New searches for unexplored leads | Medium |
| 3 | Cross-referencing existing findings | Low |
| 4 | Documentation updates | Low |
| 5 | Deep dives on low-confidence claims | High |

**Rule:** Never spend tokens on low-priority work when high-priority work is incomplete.

---

## APPENDIX: QUICK REFERENCE CARD

```
PHI-SPACED SEARCH:  100 → 62 → 38 (3 queries, ~92% coverage)

VERIFICATION LOOP:  Search → Extract → Verify → Re-Search → Document

CONFIDENCE TIERS:   [VERIFIED] > [PV] > [INFERENCE] > [UNVERIFIED]

CATEGORIES:         Money | People | Institutions | Harm | Suppression | Connections

DOCUMENT FORMAT:    Title → Sources → Entities → Findings → Connections → Money Register → Harm Register → Verdict

AGENT RULES:        Verify first. Cite sources. Cross-reference. Never assume. Follow the money. Follow the power. Follow the harm.
```

---

*This document is the brain of the research agent. Follow it. Improve it. Iterate on it. The phi-spaced search strategy, verification loops, and documentation standards here are the foundation for all investigation work.*
