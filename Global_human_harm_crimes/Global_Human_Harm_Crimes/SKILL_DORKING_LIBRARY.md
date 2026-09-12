# DuckDuckGo / Google Dorking Command Library

**OSINT Research Agent A â€” Core Capability Reference**

50+ dorking commands organized across 10 categories for investigating money trails, government records, corporate structures, and suppression evidence.

---

## Operator Reference

| Operator | Function | Example |
|----------|----------|---------|
| `site:` | Restrict to domain | `site:sec.gov` |
| `filetype:` | Restrict to file type | `filetype:pdf` |
| `intitle:` | Match in title | `intitle:"annual report"` |
| `inurl:` | Match in URL | `inurl:edgar/filing` |
| `intext:` | Match in body text | `intext:"secret settlement"` |
| `""` | Exact phrase | `"mixture of experts"` |
| `*` | Wildcard | `"*LLC"` |
| `-` | Exclude term | `-site:wikipedia.org` |
| `OR` | Either term | `"contract" OR "grant"` |
| `before:` / `after:` | Date range | `after:2024-01-01` |
| `cache:` | View cached version | `cache:example.com` |
| `related:` | Find related sites | `related:sec.gov` |

---

## 1. GOVERNMENT SITES

### 1.1 Federal Spending and Contracts

```
site:usaspending.gov "recipient name" "total obligations"
```
**Finds:** Federal contract and grant award summaries for a named entity.

```
site:usaspending.gov "prime award" "sub-award" filetype:json
```
**Finds:** Structured award data with sub-award breakdowns (machine-readable).

```
site:usaspending.gov "recipient" "city" "state" "amount" -site:reddit.com
```
**Finds:** Location-filtered spending records, excluding Reddit discussions.

```
site:gsa.gov "schedule" "contract" "awardee" filetype:pdf
```
**Finds:** GSA Schedule contract awards in PDF format.

```
site:gov "sole source" "justification" "contract" filetype:pdf
```
**Finds:** Sole-source contract justification documents (red flags for no-bid awards).

### 1.2 Open Payments (Pharma / Medical Device)

```
site:openpaymentsdata.cms.gov "physician" "general" "payment"
```
**Finds:** Physician payment records from pharmaceutical/device companies.

```
site:openpaymentsdata.cms.gov "nature_of_payment" "consulting_fee"
```
**Finds:** Consulting fee payments (potential conflicts of interest).

```
site:openpaymentsdata.cms.gov "recipient" "entity_name" "total_amount"
```
**Finds:** Aggregated payment totals by recipient entity.

### 1.3 Grants and Research Funding

```
site:reporter.nih.gov "project_num" "contact_pi" "award_amount"
```
**Finds:** NIH grant details with principal investigator names and award amounts.

```
site:nsf.gov "award" "principal_investigator" "funding" filetype:pdf
```
**Finds:** NSF award abstracts with PI information.

```
site:energy.gov "funding opportunity" "award" "recipient" filetype:pdf
```
**Finds:** DOE grant and contract award documents.

**Tips:**
- Combine `site:usaspending.gov` with `before:` / `after:` to narrow by fiscal year.
- Use `-site:reddit.com -site:quora.com` to strip noise from government dorks.
- Cross-reference NIH PIs against Open Payments for conflicts of interest.

---

## 2. COURT RECORDS

```
site:courtlistener.com "docket" "filed" "motion"
```
**Finds:** Federal and state court docket entries with filing dates.

```
site:courtlistener.com "opinion" "text" "reversed" "circuit"
```
**Finds:** Appellate court opinions with reversal outcomes.

```
site:pacermonitor.com "case" "party" "filed" "status"
```
**Finds:** PACER case summaries with party names and case status.

```
site:unicourt.com "complaint" "defendant" "jurisdiction"
```
**Finds:** UniCourt civil complaints with jurisdiction details.

```
site:courtlistener.com "sealed" "document" "motion to unseal"
```
**Finds:** Attempts to unseal sealed court documents (suppression evidence).

```
site:gov "court" "settlement" "agreement" filetype:pdf
```
**Finds:** Government settlement agreements in PDF format.

```
site:courtlistener.com "amicus" "brief" "filed"
```
**Finds:** Amicus briefs (identifies organizations intervening in cases).

```
site:gov "consent decree" "enforcement" filetype:pdf
```
**Finds:** Consent decree agreements between regulators and entities.

**Tips:**
- Combine `site:courtlistener.com` with `"defendant" "entity name"` for targeted case searches.
- Use `filetype:pdf` on court sites to find full opinion/receipt documents.
- Cross-reference court dates with lobbying disclosures for temporal correlation.
- `"sealed" "filed"` on courtlistener often surfaces suppression attempts.

---

## 3. FINANCIAL DISCLOSURES

### 3.1 SEC Filings

```
site:sec.gov/edgar "10-K" "annual report" "entity-name"
```
**Finds:** Annual corporate filings on EDGAR.

```
site:sec.gov "form 4" "insider" "transaction" "sale"
```
**Finds:** Insider trading filings (Form 4 sales are potential red flags).

```
site:sec.gov "DEF 14A" "executive" "compensation" "proxy"
```
**Finds:** Proxy statements with executive compensation details.

```
site:sec.gov "form 13F" "holdings" "institutional"
```
**Finds:** Institutional investment holdings (13F filings).

```
site:sec.gov "S-1" "registration" "IPO" "underwriter"
```
**Finds:** IPO registration statements with underwriter information.

```
site:sec.gov "8-K" "material" "event" "acquisition"
```
**Finds:** Current reports on material corporate events.

```
site:sec.gov " Schedule 13D" "beneficial owner" "percent"
```
**Finds:** Large shareholder ownership disclosures.

### 3.2 Political Finance

```
site:opensecrets.org "top contributors" "PAC" "industry"
```
**Finds:** Campaign contribution data by contributor and industry.

```
site:opensecrets.org "revolving door" "lobbyist" "former"
```
**Finds:** Revolving door records between government and industry.

```
site:fec.gov "committee" "disbursements" "operating expenditures"
```
**Finds:** FEC committee expenditure records.

```
site:opensecrets.org "outside spending" "election" "independent"
```
**Finds:** Independent expenditure data (dark money, super PACs).

**Tips:**
- EDGAR full-text search: `site:sec.gov/edgar "exact phrase"` searches all filing text.
- Use `inurl:edgar/filing` to find specific filing index pages.
- Cross-reference 13F holdings with lobbying disclosures to identify pay-to-play patterns.
- `form 4` dorks + date filters reveal insider sell-off timing.

---

## 4. ACADEMIC PUBLICATIONS

```
site:arxiv.org "mixture of experts" "calibration" "gating"
```
**Finds:** arXiv papers on MoE architecture and calibration.

```
site:scholar.google.com "patterned" OR "golden ratio" "neural network"
```
**Finds:** Google Scholar papers on patterned approaches in neural networks.

```
site:jstor.org "consciousness" "quantum" "field theory"
```
**Finds:** JSTOR academic articles on consciousness-quantum intersections.

```
site:arxiv.org "adaptive response" "error correction" "quantum"
```
**Finds:** arXiv papers on adaptive response error correction (novel territory).

```
site:scholar.google.com "holographic compression" "neural" "lossless"
```
**Finds:** Scholar results on holographic compression in neural systems.

```
site:arxiv.org "distribution shift" "robustness" "calibration" after:2024-01-01
```
**Finds:** Recent arXiv papers on distribution shift robustness.

```
site:pubmed.ncbi.nlm.nih.gov "consciousness" "field" "measurement"
```
**Finds:** PubMed papers on systemic behavior measurement.

```
site:acm.org "mixture of experts" "transformer" "scaling"
```
**Finds:** ACM publications on MoE transformer scaling.

**Tips:**
- Use `filetype:pdf` on arXiv to get direct PDF links.
- Combine `site:scholar.google.com` with `intitle:` for title-specific searches.
- Use `after:` date filters on arXiv for cutting-edge research.
- Cross-reference arXiv authors with funding sources from NIH/NSF dorks.

---

## 5. FOIA DOCUMENTS

```
site:muckrock.com "FOIA" "request" "agency" "released"
```
**Finds:** FOIA requests and released documents via MuckRock.

```
site:muckrock.com "exempt" "withheld" "b(7)" "investigation"
```
**Finds:** Documents with law enforcement exemptions (suppression evidence).

```
site:foia.state.gov "memorandum" "classified" "declassified"
```
**Finds:** State Department FOIA releases including declassified memos.

```
site:efoia.fbi.gov "request" " responsive" "page"
```
**Finds:** FBI electronic FOIA reading room documents.

```
site:foia.state.gov "cable" "embassy" "dissent" "channel"
```
**Finds:** State Department cables including dissent channel communications.

```
site:cia.gov/reading-room "document" "declassified" "FOIA"
```
**Finds:** CIA FOIA reading room declassified documents.

```
site:nsarchive.gwu.edu "national security" "memorandum" "declassified"
```
**Finds:** National Security Archive FOIA releases (GWU).

```
site:muckrock.com "appeal" "denied" "GLBM" OR "Exemption"
```
**Finds:** FOIA appeal denials (identifies suppression patterns).

**Tips:**
- MuckRock tracks request status - use `"status" "completed"` vs `"status" "pending"` to find released vs pending docs.
- `filetype:pdf` on FOIA sites surfaces actual released documents.
- Cross-reference FOIA releases with court filings for evidence chains.
- `"withheld" "in full"` on FOIA sites identifies maximum suppression.

---

## 6. CORPORATE FILINGS

```
site:sec.gov/edgar "full-text-search" "entity-name" "filing"
```
**Finds:** EDGAR full-text search results for a specific entity.

```
site:opencorporates.com "officers" "jurisdiction" "status"
```
**Finds:** Global corporate officer and director records.

```
site:opencorporates.com "agent" "registered agent" "address"
```
**Finds:** Registered agent information (shell company indicator).

```
site:opencorporates.com "dissolved" "inactive" "entity"
```
**Finds:** Dissolved/inactive entities (potential paper trail cleanup).

```
site:opencorporates.com "annual_filing" "delinquent" "jurisdiction"
```
**Finds:** Corporations with delinquent filings (compliance red flags).

```
site:sec.gov "S-4" "merger" "acquisition" "consideration"
```
**Finds:** Merger/acquisition proxy filings with deal terms.

```
site:sec.gov "DEFM14A" "merger" "tender" "offer"
```
**Finds:** Merger proxy statements with tender offer details.

```
site:sec.gov "SC 13G" OR "SC 13D" "passive" OR "active" "ownership"
```
**Finds:** Beneficial ownership filings distinguishing passive vs active investors.

**Tips:**
- OpenCorporates `opencorporates.com/companies/{jurisdiction}/{company_number}` gives structured data.
- Cross-reference SEC filing dates with lobbying disclosure dates for temporal patterns.
- Use `site:opencorporates.com "officer_name"` to find all companies a person is associated with.
- Dissolved entities often reappear in new jurisdictions - track officer names across states.

---

## 7. INTERNATIONAL RECORDS

```
site:un.org "sanctions" "committee" "entity" "list"
```
**Finds:** UN Security Council sanctions committee entity listings.

```
site:icc-cpi.int "case" "suspect" "warrant" "situation"
```
**Finds:** ICC case information with suspect names and arrest warrants.

```
site:coe.int "convention" "monitoring" "compliance" "report"
```
**Finds:** Council of Europe monitoring and compliance reports.

```
site:europarl.europa.eu "resolution" "inquiry" "committee" "report"
```
**Finds:** European Parliament resolutions and inquiry committee reports.

```
site:fsb.gov.ru "sanctions" OR "ÑÐ¿Ð¸ÑÐ¾Ðº" "entity" filetype:pdf
```
**Finds:** Russian Federal Sanctions Bureau entity listings.

```
site:gov.uk "sanctions" "consolidated" "list" "entity" filetype:csv
```
**Finds:** UK consolidated sanctions list in CSV format.

```
site:oecd.org "bribery" "foreign" "corruption" "case" "enforcement"
```
**Finds:** OECD anti-bribery convention enforcement cases.

```
site:fatf-gafi.org "mutual evaluation" "jurisdiction" "compliant"
```
**Finds:** FATF mutual evaluation reports on financial system compliance.

**Tips:**
- UN sanctions: `un.org/securitycouncil/sanctions/un-sc-consolidated-list` is the canonical source.
- Cross-reference OFAC SDN with UN sanctions for multi-jurisdictional coverage.
- ICC cases often cross-reference with national court proceedings via `site:icc-cpi.int` dorks.
- FATF grey/black list indicates high-risk jurisdictions - useful for offshore investigation context.

---

## 8. SCIENCE FUNDING

```
site:reporter.nih.gov "award_amount" "contact_pi" "project_title"
```
**Finds:** NIH RePORTER grant details with PI names and funding amounts.

```
site:reporter.nih.gov "nih" "ro1" "investigator" "abstract"
```
**Finds:** NIH R01 grant abstracts with investigator details.

```
site:nsf.gov/award "principal_investigator" "award_number" "abstract"
```
**Finds:** NSF award abstracts with PI and award details.

```
site:nih.gov "grant" "recipient" "institution" "total" filetype:csv
```
**Finds:** NIH grant award data in CSV format.

```
site:energy.gov "grant" "award" "recipient" "research" filetype:pdf
```
**Finds:** DOE grant award documents.

```
site:nsf.gov "program" "officer" "panel" "review" "merit"
```
**Finds:** NSF program-level review and merit information.

```
site:nih.gov "coi" OR "conflict of interest" "investigator" "disclosure"
```
**Finds:** NIH conflict of interest disclosures for funded investigators.

```
site:reporter.nih.gov "administering_ic" "activity" "study_section"
```
**Finds:** NIH administrative and study section information for grants.

**Tips:**
- Cross-reference NIH PIs with Open Payments (Category 1.2) for pharma industry conflicts.
- Use `site:reporter.nih.gov "pi_name"` to find all grants for a specific investigator.
- NIH FOIA data includes conflict of interest disclosures - combine with FOIA dorks.
- NSF and NIH award databases are searchable via their APIs - dorks for discovery, APIs for bulk.

---

## 9. MEDIA AND PUBLICATIONS

```
site:reuters.com "investigation" "company" "alleged" "billion"
```
**Finds:** Reuters investigative journalism on corporate misconduct.

```
site:apnews.com "exclusive" "investigation" "corruption" "billion"
```
**Finds:** AP exclusive investigations on corruption and financial misconduct.

```
site:nytimes.com "investigation" "hidden" "shell company" "offshore"
```
**Finds:** NYT investigative pieces on offshore shell companies.

```
site:theguardian.com "offshore" "leak" "paradise papers" OR "panama papers"
```
**Finds:** Guardian coverage of offshore financial leaks.

```
site:bloomberg.com "investigation" "hedge fund" "insider" "trading"
```
**Finds:** Bloomberg investigations on hedge fund insider trading.

```
site:wsj.com "investigation" "lobbyist" "government" "contract"
```
**Finds:** WSJ investigations on government contracting and lobbying.

```
site:propublica.org "investigation" "dark money" "nonprofit" "shell"
```
**Finds:** ProPublica investigations on dark money and nonprofit shells.

```
site:icij.org "investigation" "offshore" "leak" "network"
```
**Finds:** ICIJ cross-border investigative journalism.

**Tips:**
- `site:reuters.com OR site:apnews.com "entity name"` broadens wire service coverage.
- Use `before:` / `after:` on news dorks to narrow temporal coverage.
- ICIJ investigations link directly to the offshore leaks database.
- ProPublica's search index is excellent for cross-referencing with court/SEC dorks.

---

## 10. DEEP SEARCH PATTERNS

### 10.1 Combination Dorks (Multi-Source Cross-Reference)

```
"entity name" site:sec.gov OR site:usaspending.gov OR site:opensecrets.org
```
**Finds:** SEC filings, federal spending, and political contributions for a single entity in one query.

```
"executive name" site:sec.gov "form 4" OR site:opencorporates.com "officer"
```
**Finds:** Insider trading filings and corporate officer records for a person.

```
"physician name" site:openpaymentsdata.cms.gov OR site:reporter.nih.gov
```
**Finds:** Pharma payments and NIH grant funding for a physician (conflict of interest detection).

```
"entity name" site:courtlistener.com OR site:unicourt.com OR site:gov "settlement"
```
**Finds:** Court cases, civil complaints, and government settlements for a single entity.

```
"lobbyist name" site:opensecrets.org OR site:fec.gov OR site:senate.gov "disclosure"
```
**Finds:** Campaign contributions, lobbying disclosures, and revolving door records.

### 10.2 Wildcard Dorks

```
"LLC" site:opencorporates.com "officer" "dissolved"
```
**Finds:** All dissolved LLCs with officer records (shell company hunting).

```
"attn:" OR "c/o" site:sec.gov/edgar "address"
```
**Finds:** SEC filings with care-of addresses (common in nominee/shell structures).

```
"beneficial owner" site:sec.gov "Schedule 13D" OR "Schedule 13G"
```
**Finds:** All beneficial ownership disclosures across both active and passive investor types.

```
"filed under seal" OR "under seal" site:courtlistener.com
```
**Finds:** All court documents filed under seal (suppression surface area).

```
"in the matter of" site:sec.gov OR site:justice.gov
```
**Finds:** SEC and DOJ enforcement actions (formal investigation proceedings).

### 10.3 Exclusion Dorks (Noise Reduction)

```
"entity name" site:sec.gov -site:sec.gov/cgi-bin -site:sec.gov/search
```
**Finds:** SEC results excluding search pages and navigation (content only).

```
"contract award" site:gov -site:usaspending.gov -site:beta.usaspending.gov
```
**Finds:** Government contract awards from agency-specific sources, not the aggregator.

```
"NIH grant" site:nih.gov -site:reporter.nih.gov -site:grants.nih.gov
```
**Finds:** NIH grant references outside the main databases (news, testimony, reports).

```
"FOIA" site:muckrock.com -site:muckrock.com/agency -site:muckrock.com/request
```
**Finds:** MuckRock FOIA content excluding index/listing pages.

```
"annual report" site:sec.gov -site:sec.gov/edgar -site:sec.gov/cgi-bin
```
**Finds:** SEC annual report references outside EDGAR (speeches, press releases).

### 10.4 Temporal Dorks (Time-Based Investigation)

```
"sole source" "justification" site:gov after:2024-01-01 before:2024-12-31
```
**Finds:** Sole-source contract justifications filed in a specific year.

```
"form 4" "sale" site:sec.gov "entity name" after:2024-06-01
```
**Finds:** Recent insider sales (potential advance knowledge of bad news).

```
"settlement" "agreement" site:gov after:2023-01-01 before:2023-12-31
```
**Finds:** Government settlements from a specific year.

```
"lobbying" "disclosure" site:senate.gov after:2024-01-01
```
**Finds:** Recent Senate lobbying disclosures.

### 10.5 File Type Deep Dives

```
filetype:xls OR filetype:xlsx site:usaspending.gov "recipient"
```
**Finds:** Downloadable spending data spreadsheets.

```
filetype:csv site:fec.gov "committee" "disbursements"
```
**Finds:** FEC expenditure data in machine-readable CSV.

```
filetype:pdf "executive summary" site:sec.gov "investigation"
```
**Finds:** SEC investigation executive summaries.

```
filetype:json site:usaspending.gov "award" "sub-award"
```
**Finds:** Structured API data for federal awards.

```
filetype:xml site:sec.gov/edgar "filing"
```
**Finds:** EDGAR XBRL structured financial data.

### 10.6 Entity Name Variation Dorks

```
"EX CORP" OR "EX CORP LLC" OR "EX CORP INC" OR "EX CORP GROUP" site:sec.gov
```
**Finds:** SEC filings for all name variations of an entity.

```
inurl:"ex-corp" OR inurl:"excorp" site:opencorporates.com
```
**Finds:** OpenCorporates records using URL slug variations.

```
"EX*LLC" OR "EX*INC" site:opencorporates.com "officer"
```
**Finds:** Wildcard entity name matches across corporate registries.

**Tips:**
- Always search name variations: LLC, Inc, Corp, Group, Holdings, Partners, LP, LLP.
- Use `inurl:` to match URL-friendly name formats (hyphens, no spaces).
- Cross-reference the same entity across categories 1-8 to build complete profiles.

---

## STRATEGIC FRAMEWORKS

### A. Fibonacci Search Strategy

Search at phi-spaced intervals (1, 1, 2, 3, 5, 8, 13, 21, 34...) for coverage efficiency. This mimics the golden ratio's natural sampling optimality.

**Protocol:**

1. **Iteration 1-2 (Narrow):** Search the most specific source first (e.g., `site:sec.gov/edgar "entity name"`)
2. **Iteration 3 (Expand x2):** Add one adjacent source (e.g., `site:usaspending.gov`)
3. **Iteration 5 (Expand x3):** Add two more sources (e.g., `site:courtlistener.com` + `site:opencorporates.com`)
4. **Iteration 8 (Expand x5):** Broader web search with exclusions (`"entity name" -site:wikipedia.org`)
5. **Iteration 13+ (Flood):** Full multi-source cross-reference

**Why it works:**
- Early iterations find the highest-signal sources first.
- Later iterations catch what narrower searches miss.
- The phi spacing prevents redundant queries (each new search covers exponentially more ground).
- Stops before diminishing returns set in (typically 8-13 iterations for most investigations).

**Example - Investigating "Acme Defense Corp":**

| Iteration | Query | Sources Covered |
|-----------|-------|-----------------|
| 1 | `site:sec.gov/edgar "Acme Defense Corp"` | SEC EDGAR |
| 1 | `site:usaspending.gov "Acme Defense Corp"` | Federal Spending |
| 2 | `site:courtlistener.com "Acme Defense Corp"` | Court Records |
| 3 | `site:opencorporates.com "Acme Defense"` | Corporate Registry |
| 5 | `"Acme Defense Corp" -site:wikipedia.org` | Broad Web |
| 8 | `"Acme Defense" site:reuters.com OR site:apnews.com` | Media |
| 13 | `"Acme Defense" site:muckrock.com OR site:foia.state.gov` | FOIA |

### B. Verification Loop

A four-stage iterative process: **Search â†’ Extract â†’ Verify â†’ Re-Search**

```
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”    â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”    â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”    â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚  SEARCH  â”‚â”€â”€â”€â–¶â”‚ EXTRACT  â”‚â”€â”€â”€â–¶â”‚ VERIFY   â”‚â”€â”€â”€â–¶â”‚RE-SEARCH â”‚
â”‚  (Dork)  â”‚    â”‚ (Content)â”‚    â”‚ (Cross-  â”‚    â”‚ (Refined â”‚
â”‚          â”‚    â”‚          â”‚    â”‚  Check)  â”‚    â”‚  Query)  â”‚
â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜    â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜    â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜    â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
     â–²                                              â”‚
     â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
```

**Stage 1: SEARCH**
- Apply a dork from the library targeting one source category.
- Record: query, source, date, result count.

**Stage 2: EXTRACT**
- Open top 3-5 results.
- Extract: entity names, dates, amounts, relationships, document IDs.
- Flag: any claims not directly supported by the extracted data.

**Stage 3: VERIFY**
- For each extracted fact, apply a dork from a DIFFERENT category to confirm.
- Example: SEC filing mentions a contract â†’ search `site:usaspending.gov "contract number"`.
- Example: Court filing names a company â†’ search `site:opencorporates.com "company name" "officers"`.
- Confidence levels:
  - **Confirmed:** Found in 2+ independent sources.
  - **Probable:** Found in 1 source, consistent with other data.
  - **Unverified:** Found in 1 source, no corroboration.
  - **Contradicted:** Conflicting information across sources.

**Stage 4: RE-SEARCH**
- Based on verification results, generate refined queries:
  - Confirmed facts â†’ search for related entities and deeper connections.
  - Probable facts â†’ search for additional corroboration.
  - Unverified facts â†’ search for alternative sources.
  - Contradicted facts â†’ search for resolution (amended filings, corrections).
- Return to Stage 1 with refined queries.

**Termination criteria:**
- 3 consecutive searches with zero new findings.
- All key claims at "Confirmed" confidence level.
- Diminishing returns: <1 new finding per 5 queries.

### C. Token-Efficient Search Tips

Minimize queries while maximizing findings. Each search costs tokens in an agent context.

**1. Batch by Source, Not by Question**
- BAD: Search SEC for entity A, then SEC for entity B, then SEC for entity C.
- GOOD: `site:sec.gov "entity A" OR "entity B" OR "entity C"` (one query, three entities).

**2. Use OR Instead of Separate Queries**
- BAD: 4 separate queries for LLC, Inc, Corp, Group variations.
- GOOD: `"entity" site:opencorporates.com "LLC" OR "Inc" OR "Corp" OR "Group"`

**3. Combine Exclusions to One Query**
- BAD: 3 separate queries excluding Wikipedia, Reddit, Quora.
- GOOD: `"query" -site:wikipedia.org -site:reddit.com -site:quora.com`

**4. Prioritize High-Signal Sources First**
- Source ranking by information density:
  1. `site:sec.gov` (structured financial data)
  2. `site:usaspending.gov` (federal money trails)
  3. `site:opencorporates.com` (corporate structure)
  4. `site:courtlistener.com` (legal proceedings)
  5. `site:opensecrets.org` (political finance)
  6. `site:openpaymentsdata.cms.gov` (pharma payments)
  7. `site:reporter.nih.gov` (research funding)
  8. `site:muckrock.com` (FOIA documents)
  9. `site:reuters.com` OR `site:apnews.com` (media coverage)
  10. General web (broadest, least filtered)

**5. Use `filetype:` to Skip HTML Pages**
- `filetype:pdf` gets you documents, not landing pages.
- `filetype:csv` or `filetype:json` gets machine-readable data directly.

**6. Date Filters Reduce Noise**
- `after:2024-01-01` on government sites cuts stale results.
- `before:` on SEC filings avoids current-period noise.

**7. Chain Queries, Don't Scatter**
- Each query should inform the next. Extract a name from result â†’ search that name in the next query.
- This creates a focused evidence chain rather than scattered data points.

**8. Count Your Queries**
- Track queries per investigation. Target: <20 queries for a complete entity profile.
- If >20 queries with no new findings, pivot strategy or accept current coverage.

**9. Cache Awareness**
- `cache:example.com` shows Google's cached version (useful for deleted content).
- DuckDuckGo has no cache operator - use `web.archive.org` instead.

**10. Stop at Saturation**
- When 3 consecutive queries return only previously-seen results, stop.
- Better to have 15 focused findings than 50 scattered data points.

---

## QUICK REFERENCE: investigation Templates

### Template A: Corporate Due Diligence (8 queries)

```
1. site:sec.gov/edgar "entity name"
2. site:opencorporates.com "entity name" "officers"
3. site:usaspending.gov "entity name"
4. site:courtlistener.com "entity name"
5. site:opensecrets.org "entity name" OR "parent company"
6. site:sec.gov "form 4" "executive name"
7. site:muckrock.com "entity name" OR "parent company"
8. "entity name" -site:wikipedia.org -site:reddit.com
```

### Template B: Individual Background (10 queries)

```
1. site:sec.gov "person name" "form 4" OR "DEF 14A"
2. site:opencorporates.com "person name" "officer"
3. site:courtlistener.com "person name" "defendant" OR "plaintiff"
4. site:opensecrets.org "person name" "contributor" OR "lobbyist"
5. site:openpaymentsdata.cms.gov "person name"
6. site:reporter.nih.gov "person name" "investigator"
7. site:scholar.google.com "person name"
8. site:senate.gov "person name" "disclosure"
9. site:foia.state.gov "person name"
10. "person name" -site:wikipedia.org
```

### Template C: Follow the Money (12 queries)

```
1. site:usaspending.gov "contractor name" "award"
2. site:sec.gov/edgar "contractor name" "10-K" OR "8-K"
3. site:opensecrets.org "contractor name" "contributors"
4. site:senate.gov "contractor name" "lobbying disclosure"
5. site:courtlistener.com "contractor name" "settlement"
6. site:opencorporates.com "contractor name" "subsidiary"
7. site:usaspending.gov "subcontractor name"
8. site:sec.gov "form 4" "executive name" "sale"
9. site:openpaymentsdata.cms.gov "physician name"
10. site:foia.state.gov "contractor name"
11. "contractor name" "investigation" site:reuters.com OR site:apnews.com
12. "contractor name" -site:wikipedia.org -site:reddit.com
```

### Template D: Suppression Evidence Hunt (8 queries)

```
1. site:courtlistener.com "sealed" "filed" "entity name"
2. site:muckrock.com "exempt" "withheld" "entity name"
3. site:foia.state.gov "withheld in full" "entity name"
4. site:efoia.fbi.gov "entity name"
5. site:courtlistener.com "motion to seal" OR "motion to unseal"
6. site:muckrock.com "appeal" "denied" "entity name"
7. "sealed settlement" "entity name" filetype:pdf
8. site:cia.gov/reading-room "entity name" "declassified"
```

---

## APPENDIX: Source API Alternatives

When dorks return insufficient results, use these direct APIs (often more reliable for bulk data):

| Source | API Endpoint | Notes |
|--------|-------------|-------|
| USAspending | `api.usaspending.gov/api/v2/` | REST API, no key needed |
| SEC EDGAR | `efts.sec.gov/LATEST/search-index` | Full-text search API |
| FEC | `api.open.fec.gov/v1/` | Demo key available |
| NIH RePORTER | `api.reporter.nih.gov/v2/projects/search` | POST API, no key |
| OpenCorporates | `api.opencorporates.com/v0.4/` | Free token raises limits |
| CourtListener | `www.courtlistener.com/api/rest/v3/` | Token recommended |
| ICIJ Offshore | `offshoreleaks.icij.org/api/` | Limited public API |
| GDELT | `api.gdeltproject.org/api/v2/` | No key needed |

---

*Library version 1.0 â€” OSINT Research Agent A*
*Last updated: 2026-08-21*

