# 48: Offshore Account Search Enhancement

**Date:** 2026-08-22
**Agent:** Investigation Agent 66
**Purpose:** Document search limitations, workarounds, and enhanced techniques for offshore account investigation

---

## Walls Encountered

### Wall 1: SEC EDGAR Blocked Direct Access (403)

**What:** Automated or bulk access to SEC EDGAR returns 403 Forbidden.

**Why:** SEC rate-limits and blocks non-browser user agents. EDGAR's Full-Text Search System (EFTS) allows programmatic queries, but the main filing viewer blocks scraping. IP-based throttling kicks in after ~10 requests/second.

**Workarounds (Legal):**

| Method | How | Notes |
|--------|-----|-------|
| **EFTS API** | `efts.sec.gov/LATEST/search-index?q="entity+name"&dateRange=custom&startdt=2020-01-01&enddt=2024-12-31` | Official API, no key needed, returns JSON |
| **XBRL Bulk** | `sec.gov/Archives/edgar/data/` directory browsing | Raw filing data, slower but complete |
| **EDGAR Company Search** | `sec.gov/cgi-bin/browse-edgar?action=getcompany&company=entity+name&type=10-K` | Browser-based, rate-limited but functional |
| **SEC Viewer** | `sec.gov/Archives/edgar/data/{cik}/{accession}/` | Direct filing access by CIK + accession number |
| **EDGAR Full-Text** | `efts.sec.gov/LATEST/search-index?q=%22entity+name%22&forms=10-K,8-K,DEF+14A` | Searches all filing text, not just headers |

**Dork Patterns:**

```
site:sec.gov/edgar "entity name" "10-K" filetype:htm
site:sec.gov "Schedule 13D" "beneficial owner" "entity name"
site:sec.gov "DEF 14A" "executive compensation" "entity name"
```

**Key insight:** EDGAR's EFTS API (`efts.sec.gov/LATEST/search-index`) is the primary legal bulk access method. It returns structured JSON with filing metadata, full text, and XBRL data. No authentication required.

---

### Wall 2: OCCRP Aleph Requires Authenticated Access

**What:** OCCRP's Aleph platform (global corrupt money database) requires login for most searches and all document access.

**Why:** Aleph is a research tool for journalists and investigators. It contains sensitive data on politically exposed persons (PEPs), sanctions, and leaked datasets. Unauthenticated access is limited to basic entity search.

**Workarounds (Legal):**

| Method | How | Notes |
|--------|-----|-------|
| **Free Aleph Account** | Register at `aleph.occrp.org` | Free for journalists, researchers, NGOs |
| **OCCRP API** | `api.occrp.org/` | API key required, apply via OCCRP |
| **Cached Results** | Search `site:aleph.occrp.org "entity name"` | Some entity profiles are indexed by Google |
| **OCCRP Publications** | `occrp.org/en/investigations/` | Public investigation reports reference Aleph data |
| **Partner Databases** | OCCRP shares data with ICIJ,ICIJ Offshore Leaks, Finance Uncovered | Some datasets available through partners |

**Dork Patterns:**

```
site:occrp.org "entity name" "offshore" "shell company"
site:aleph.occrp.org "entity name" "person" OR "company"
site:occrp.org "investigation" "offshore" "money laundering"
```

**Key insight:** OCCRP's public investigation reports (`occrp.org/en/investigations/`) often contain entity names, amounts, and jurisdiction details extracted from Aleph — these are freely searchable.

---

### Wall 3: ICIJ Database is JavaScript-Rendered

**What:** ICIJ's Offshore Leaks Database (`offshoreleaks.icij.org`) uses JavaScript rendering, making direct scraping or API queries difficult.

**Why:** The database is built as a single-page application (SPA) with client-side rendering. Content loads dynamically via JavaScript, so traditional `webfetch` or `curl` returns an empty shell.

**Workarounds (Legal):**

| Method | How | Notes |
|--------|-----|-------|
| **ICIJ API** | `offshoreleaks.icij.org/api/` | Limited public endpoints for entity search |
| **Google Index** | `site:offshoreleaks.icij.org "entity name"` | ICIJ pages are indexed, Google returns rendered snippets |
| **ICIJ Publications** | `icij.org/investigations/` | Public investigation reports with entity details |
| **Panama Papers Search** | `panamapapers.icij.org/search/` | Dedicated search for Panama Papers dataset |
| **Paradise Papers Search** | `paradisepapers.icij.org/search/` | Dedicated search for Paradise Papers dataset |
| **Pandora Papers Search** | `pandorapapers.icij.org/search/` | Dedicated search for Pandora Papers dataset |

**Dork Patterns:**

```
site:offshoreleaks.icij.org "entity name"
site:panamapapers.icij.org "entity name"
site:paradisepapers.icij.org "entity name"
site:pandorapapers.icij.org "entity name"
site:icij.org "investigation" "offshore" "entity name"
```

**Key insight:** ICIJ's investigation pages (`icij.org/investigations/`) are static HTML and fully scrapable. They contain entity names, jurisdictions, and relationships extracted from the leaked databases.

---

### Wall 4: Companies Don't Disclose Subsidiaries

**What:** Many parent companies do not fully disclose subsidiary structures in public filings, especially offshore entities.

**Why:** Legal opacity — subsidiaries in secrecy jurisdictions (BVI, Cayman, Panama) are not required to disclose beneficial ownership in many cases. Even 10-K filings may only list "material" subsidiaries.

**Workarounds (Legal):**

| Method | How | Notes |
|--------|-----|-------|
| **OpenCorporates** | `opencorporates.com` — search officer/director names across jurisdictions | Finds shell companies by matching officer names |
| **SEC Exhibit 21** | 10-K Exhibit 21 lists subsidiaries | Not all companies file this; check `site:sec.gov "exhibit 21" "entity name"` |
| **Beneficial Ownership (BOI)** | FinCEN BOI database (post-2024) | Corporate Transparency Act requires disclosure — limited public access currently |
| **State AG Filings** | Secretary of State filings | Delaware, Nevada, Wyoming are common incorporation states |
| **Annual Reports** | Some jurisdictions require annual returns with officer lists | UK Companies House, BVI FSC, etc. |
| **Leaked Databases** | Panama/Pandora/Paradise Papers | Historical snapshots of beneficial ownership |

**Dork Patterns:**

```
site:opencorporates.com "officer name" "director" "offshore"
site:sec.gov "exhibit 21" "subsidiary" "entity name"
site:opencorporates.com "registered agent" "entity name" "BVI" OR "Cayman" OR "Panama"
"beneficial owner" site:sec.gov "Schedule 13D" OR "Schedule 13G"
```

**Key insight:** Officer name matching across jurisdictions is the most reliable method. If "John Smith" is director of Entity A (US) and Entity B (BVI), the connection exists regardless of subsidiary disclosure.

---

### Wall 5: Offshore Registries Not Publicly Searchable

**What:** Many offshore jurisdictions (BVI, Cayman Islands, Bahamas, Seychelles) do not maintain searchable public registries of companies or beneficial owners.

**Why:** Secrecy is the business model — these jurisdictions attract incorporation precisely because they offer privacy. Some have signed up for limited information exchange (CRS, FATCA) but public search is not available.

**Workarounds (Legal):**

| Method | How | Notes |
|--------|-----|-------|
| **UK Companies House** | `beta.companieshouse.gov.uk` | BVI/Cayman companies sometimes have UK-registered branches |
| **FATF Reports** | `fatf-gafi.org` mutual evaluations | Identify which jurisdictions are non-compliant |
| **EU Blacklist** | EU list of non-cooperative jurisdictions | Identifies high-risk secrecy jurisdictions |
| **OFAC Sanctions** | `sanctionssearch.ofac.treas.gov` | Sanctioned entities often reveal offshore structures |
| **UN Sanctions** | `un.org/securitycouncil/sanctions/un-sc-consolidated-list` | Multi-jurisdictional sanctions data |
| **Leaked Registries** | ICIJ leaked datasets contain registry snapshots | Historical but invaluable |
| **Court Records** | `courtlistener.com` "BVI" OR "Cayman" "entity name" | Offshore entities appear in US litigation |
| **FinCEN SARs** | Suspicious Activity Reports (limited public access) | Some SARs are disclosed in enforcement actions |

**Dork Patterns:**

```
site:beta.companieshouse.gov.uk "entity name" "BVI" OR "Cayman"
site:fatf-gafi.org "mutual evaluation" "BVI" OR "Cayman" OR "Bahamas"
site:sanctionssearch.ofac.treas.gov "entity name"
site:courtlistener.com "BVI" "entity name" "defendant"
"shell company" "BVI" "entity name" site:reuters.com OR site:apnews.com
```

**Key insight:** When direct registry access is blocked, trace the entity through jurisdictions that DO have public registries (US, UK, EU). BVI companies often have US bank accounts, UK registered agents, or appear in US litigation.

---

## Enhanced Search Techniques

### Technique 1: Officer Name Cross-Jurisdiction Search

The most powerful offshore investigation technique: find an officer/director name in a public jurisdiction, then search that name across all secrecy jurisdictions.

**Protocol:**

1. Identify officer/director names from SEC filings (DEF 14A, Schedule 13D)
2. Search those names on OpenCorporates across ALL jurisdictions
3. Cross-reference with ICIJ leaked databases
4. Map the resulting corporate network

**Dork Pattern:**

```
"officer name" site:opencorporates.com "director" OR "officer" OR "shareholder"
"officer name" site:offshoreleaks.icij.org
"officer name" site:sec.gov "form 4" OR "DEF 14A" OR "Schedule 13D"
```

### Technique 2: Registered Agent Tracking

Shell companies use registered agents. The same registered agent services (e.g., Intertrust, Trident, Appleby) appear across thousands of offshore entities.

**Protocol:**

1. Identify a registered agent name from corporate filings
2. Search that agent across all jurisdictions
3. Map all entities using that agent — they may share beneficial owners

**Dork Pattern:**

```
"registered agent" "agent name" site:opencorporates.com
"registered agent" "agent name" site:sec.gov
"c/o" OR "attn:" "agent name" site:sec.gov/edgar
```

### Technique 3: Jurisdiction-Hopping Pattern Recognition

Offshore structures follow predictable patterns:

```
US Corp → BVI HoldCo → Cayman Fund → Panama SPV → Bank Account (Switzerland)
```

**Search for each link in the chain:**

| Link | Search Source | Dork |
|------|--------------|------|
| US Corp | SEC EDGAR, OpenCorporates | `site:sec.gov "entity name"` |
| BVI HoldCo | UK Companies House, ICIJ | `site:beta.companieshouse.gov.uk "entity name"` |
| Cayman Fund | Cayman FSC, ICIJ | `site:gov.ky "entity name"` |
| Panama SPV | Panama Public Registry, ICIJ | `site:rocpanama.gob.pa "entity name"` |
| Swiss Bank | FINMA, leaked data | `site:finma.ch "entity name"` |

### Technique 4: Financial Flow Reconstruction

When direct payment records are unavailable, reconstruct flows from public data:

1. **SEC filings** → parent company payments to subsidiaries
2. **Tax returns** → 990-PF foundation grants to offshore entities
3. **Court records** → litigation revealing financial relationships
4. **FOIA** → government contracts flowing to offshore structures
5. **News investigations** → leaked or revealed payment details

### Technique 5: Sanctions Screening as Discovery

OFAC, UN, and EU sanctions lists reveal offshore structures that are otherwise invisible:

```
site:sanctionssearch.ofac.treas.gov "entity name"
site:un.org/securitycouncil/sanctions "entity name"
site:gov.uk "sanctions" "consolidated list" "entity name"
```

Sanctioned entities often have their full corporate structure documented in the Federal Register notice.

---

## New Databases and Tools

### Free/Public Databases

| Database | URL | What It Contains |
|----------|-----|------------------|
| **OpenCorporates** | opencorporates.com | 200M+ companies across 100+ jurisdictions |
| **ICIJ Offshore Leaks** | offshoreleaks.icij.org | Panama, Paradise, Pandora Papers entities |
| **OFAC Sanctions** | sanctionssearch.ofac.treas.gov | US sanctioned entities |
| **UN Sanctions** | un.org/securitycouncil/sanctions | Global sanctions lists |
| **UK Companies House** | beta.companieshouse.gov.uk | UK companies + overseas entities |
| **SEC EDGAR** | sec.gov/edgar | US public company filings |
| **FinCEN BOI** | fincen.gov/boi | Corporate Transparency Act beneficial ownership (limited access) |
| **EU Sanctions** | data.europa.eu/data/datasets | EU restrictive measures |
| **FATF Reports** | fatf-gafi.org | Mutual evaluations of jurisdictions |
| **USASpending** | usaspending.gov | Federal contract awards |
| **ProPublica Nonprofit** | projects.propublica.org/nonprofits | 990-PF foundation filings |

### API Access Methods

| Database | API Endpoint | Auth | Notes |
|----------|-------------|------|-------|
| **SEC EDGAR EFTS** | `efts.sec.gov/LATEST/search-index` | None | Full-text search across all filings |
| **USASpending** | `api.usaspending.gov/api/v2/` | None | Federal spending data |
| **OpenCorporates** | `api.opencorporates.com/v0.4/` | Free token | Raises rate limits |
| **FEC** | `api.open.fec.gov/v1/` | Demo key | Political finance data |
| **NIH RePORTER** | `api.reporter.nih.gov/v2/projects/search` | None | Research grant data |
| **CourtListener** | `www.courtlistener.com/api/rest/v3/` | Token recommended | Federal court records |
| **GDELT** | `api.gdeltproject.org/api/v2/` | None | Global news monitoring |
| **ICIJ Offshore** | `offshoreleaks.icij.org/api/` | Limited | Entity search (not full access) |

### Paid/Restricted Tools (Reference Only)

| Tool | Access | What It Does |
|------|--------|-------------|
| **LexisNexis** | Subscription | Corporate records, court filings, news |
| **Dun & Bradstreet** | Subscription | Corporate hierarchies, financial data |
| **World-Check** | Institutional | PEP and sanctions screening |
| **Sayari Graph** | Commercial | Supply chain and beneficial ownership |
| **Kharon** | Commercial | Sanctions and risk intelligence |

---

## FOIA Requests That Could Fill Gaps

### High-Value FOIA Targets

| Agency | What to Request | Why |
|--------|----------------|-----|
| **FinCEN** | Suspicious Activity Reports (SARs) mentioning target entities | SARs reveal offshore money laundering patterns |
| **SEC** | Enforcement action files targeting offshore structures | Reveals full corporate network in investigation files |
| **DOJ** | Deferred Prosecution Agreements (DPAs) | Offshore structure details in plea agreements |
| **Treasury (OFAC)** | SDN List supporting documentation | Detailed entity background for sanctioned entities |
| **IRS** | 990-PF audit reports for target foundations | Foundation grantmaking to offshore entities |
| **State Department** | Diplomatic cables mentioning target entities | International intelligence on offshore flows |
| **DOD** | Contract audits mentioning offshore subcontractors | Defense contracting through offshore shells |
| **FBI** | Financial crime case files (post-investigation) | Detailed financial forensics |

### FOIA Request Templates

**Template A: FinCEN SAR Request**

```
FOIA Request to: Financial Crimes Enforcement Network (FinCEN)
Subject: Suspicious Activity Reports mentioning [Entity Name]

Request: All Suspicious Activity Reports (SARs) filed between [Date] and [Date] 
that mention [Entity Name], [Officer Name], or [Related Entity].

Exemption considerations: SARs are generally exempt under 31 CFR 1010.320, 
but enforcement actions and court filings often reference SAR content.
```

**Template B: SEC Enforcement Request**

```
FOIA Request to: Securities and Exchange Commission
Subject: Enforcement action files for [Entity Name]

Request: All documents related to SEC investigation or enforcement action 
against [Entity Name], including correspondence, testimony, and exhibits.

Note: SEC enforcement actions become public when filed in federal court.
```

**Template C: IRS Foundation Audit Request**

```
FOIA Request to: Internal Revenue Service
Subject: 990-PF audit reports for [Foundation Name]

Request: All audit reports, examination reports, and related correspondence 
for [Foundation Name] for tax years [Year]-[Year], particularly regarding 
grants to foreign entities or offshore accounts.
```

---

## Offshore Investigation Dork Library

### Category A: Beneficial Ownership

```
"beneficial owner" site:sec.gov "Schedule 13D" OR "Schedule 13G"
"beneficial ownership" site:sec.gov "form 10-K" "subsidiary"
"beneficial owner" site:opencorporates.com "BVI" OR "Cayman" OR "Panama"
"UBO" OR "ultimate beneficial owner" site:sec.gov
"beneficial interest" site:sec.gov "form 4" "transaction"
```

### Category B: Shell Company Patterns

```
"LLC" site:opencorporates.com "dissolved" "BVI" OR "Delaware" OR "Wyoming"
"shell company" site:sec.gov "exhibit 21" "subsidiary"
"attn:" OR "c/o" site:sec.gov/edgar "address" "offshore"
"in the matter of" site:sec.gov "shell" OR "nominee"
"registered agent" site:opencorporates.com "Intertrust" OR "Trident" OR "Appleby"
```

### Category C: Offshore Jurisdictions

```
"BVI" OR "British Virgin Islands" site:sec.gov "entity name"
"Cayman Islands" site:sec.gov "fund" OR "holding" OR "entity name"
"Panama" site:sec.gov "corporation" OR "foundation"
"Bahamas" site:sec.gov "bank" OR "trust"
"Jersey" OR "Guernsey" site:sec.gov "fund" OR "entity name"
"Singapore" site:sec.gov "holding" OR "subsidiary"
"Hong Kong" site:sec.gov "entity name" "subsidiary"
```

### Category D: Money Flow Indicators

```
"consulting fee" site:sec.gov "offshore" OR "foreign"
"management fee" site:sec.gov "subsidiary" OR "affiliate"
"royalty" site:sec.gov "offshore" OR "foreign" "license"
"interest payment" site:sec.gov "note" OR "debt" "offshore"
"dividend" site:sec.gov "foreign subsidiary"
"transfer price" OR "transfer pricing" site:sec.gov "intercompany"
```

### Category E: Suppression/Opacity Indicators

```
"filed under seal" site:courtlistener.com "offshore" OR "shell"
"sealed settlement" site:courtlistener.com "entity name"
"protective order" site:courtlistener.com "financial records"
"trade secret" site:courtlistener.com "entity name" "offshore"
"withheld in full" site:muckrock.com "FinCEN" OR "SAR" OR "offshore"
```

---

## Search Protocol for Offshore Accounts

### Step 1: Identify the Target

1. Start with the entity or person of interest
2. Search SEC EDGAR for all filings mentioning them
3. Extract: subsidiaries, officers, directors, beneficial owners
4. Note any offshore jurisdictions mentioned

### Step 2: Map the Corporate Network

1. Search OpenCorporates for each officer/director name across ALL jurisdictions
2. Search ICIJ Offshore Leaks for each entity and person
3. Search UK Companies House for any UK-connected entities
4. Map the full network graph

### Step 3: Trace Financial Flows

1. Search USASpending for federal contracts to the entity or subsidiaries
2. Search SEC filings for intercompany payments, royalties, management fees
3. Search court records for financial disclosures in litigation
4. Search OFAC/UN sanctions for any sanctioned connected entities

### Step 4: Identify Opacity Points

1. Which jurisdictions have no public registry? (BVI, Cayman, etc.)
2. Which subsidiaries are not disclosed in 10-K Exhibit 21?
3. Which officer names appear in leaked databases but not in SEC filings?
4. Which financial flows cannot be explained by public records?

### Step 5: Fill Gaps with FOIA

1. File FOIA requests for FinCEN SARs mentioning the entity
2. File FOIA requests for SEC enforcement files
3. File FOIA requests for IRS audit reports on related foundations
4. Cross-reference FOIA responses with existing findings

### Step 6: Document and Verify

1. Apply verification loop: Search → Extract → Verify → Re-Search
2. Document all findings with 3+ independent sources
3. Tag confidence levels: [VERIFIED] / [PV] / [INFERENCE] / [UNVERIFIED]
4. Update Money Register and corporate network map

---

## Key Insight

The offshore investigation problem is not a lack of data — it's a **fragmentation** problem. Data exists across:
- 100+ corporate registries
- 50+ sanctions lists
- Leaked databases (Panama, Paradise, Pandora Papers)
- Court records in dozens of jurisdictions
- SEC/FinCEN/IRS filings

The enhancement is not finding new data — it's **systematically cross-referencing existing data** across these fragmented sources using the officer-name-matching and jurisdiction-hopping techniques documented above.

---

## Status

**Verification level:** [PV] — Patterns documented based on known limitations and publicly available workaround documentation
**Confidence:** HIGH
**Last updated:** 2026-08-22
