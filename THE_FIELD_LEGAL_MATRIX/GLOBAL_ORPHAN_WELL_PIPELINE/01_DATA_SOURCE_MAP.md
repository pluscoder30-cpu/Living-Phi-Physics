# GLOBAL ORPHAN WELL DATA SOURCE MAP

**Agent 1 — Data Source Mapping & Legal Framework Registry**
**Pipeline Phase: Foundation | Status: ACTIVE**
**Date: 2026-08-31**

---

## EXECUTIVE SUMMARY

This document maps every known orphaned/abandoned oil and gas well database, registry, and data source across 127+ countries. It identifies the colonial/Crown legal frameworks applicable in each jurisdiction. The global inventory stands at **4.5 million abandoned oil and gas wells** across 127 countries (CEADs-AOGI, 2025), with only **420,000 wells (9%)** having detailed well-level records. An estimated **2.5 million orphan wells** lack responsible operators or proper documentation entirely.

**Key Global Statistics:**
- Total abandoned wells: ~4.5 million documented + millions undocumented
- Total orphan wells: ~2.5 million worldwide
- Total wells globally (IEA estimate): ~8 million abandoned onshore
- Documented orphan wells (US alone): 117,672 documented + millions undocumented
- Documented orphan wells (Canada): 19,000+ (Alberta) + thousands in other provinces
- North Sea offshore wells: 20,507 documented (UK: 11,672; Norway: 6,254; Netherlands: 2,108; Denmark: 269; Germany: 204)
- 10 countries account for 98% of global abandoned well methane emissions
- United States alone contributes ~70% of global abandoned well methane emissions

---

## TIER 1: GLOBAL / MULTI-COUNTRY DATABASES

### 1.1 CEADs-AOGI (Global Abandoned Oil and Gas Wells Methane Emissions Inventory)
| Field | Detail |
|-------|--------|
| **Source** | Tsinghua University / University College London |
| **Coverage** | 127 countries, 4.5 million abandoned wells |
| **Well-level detail** | 420,000 wells (9% of total) with location, type, end date |
| **Data fields** | Well location, type, end date, methane emissions estimates, geological characteristics |
| **URL** | https://ceads.net/data/ (login required) |
| **Citation** | Lei et al., "A global inventory of methane emissions from abandoned oil and gas wells," National Science Review, 2025. DOI: 10.1093/nsr/nwaf184 |
| **Key finding** | 10 countries = 98% of emissions; US = 70%; Shell = 28% of Indonesia's + 22% of Nigeria's; Chevron = 42% of Thailand's |

### 1.2 IEA Global Methane Tracker
| Field | Detail |
|-------|--------|
| **Source** | International Energy Agency |
| **Coverage** | Global — 8 million abandoned onshore wells estimated |
| **Data fields** | Methane emissions by country, abatement costs, policy status |
| **URL** | https://www.iea.org/reports/global-methane-tracker-2025 |
| **Key finding** | Abandoned coal mines = ~5 Mt methane; abandoned O&G wells = ~3 Mt methane (2024); combined = world's 4th-largest fossil fuel methane emitter |

### 1.3 OGIM (Oil and Gas Infrastructure Mapping Database)
| Field | Detail |
|-------|--------|
| **Source** | Stanford / Environmental Defense Fund |
| **Coverage** | Global — 6.7 million features including 4.5 million well points |
| **Data fields** | Well location, type (active/inactive/plugged), compressor stations, processing facilities, platforms, pipelines (1.2M km) |
| **URL** | https://gee-community-catalog.org/projects/ogim/ |
| **Key finding** | Includes active, inactive, and plugged & abandoned wells; production data integrated (v2.7, Feb 2025) |

### 1.4 EMODnet Human Activities — Oil and Gas Wells
| Field | Detail |
|-------|--------|
| **Source** | European Marine Observation and Data Network (Cogea) |
| **Coverage** | European offshore — 17 countries: Croatia, Cyprus, Denmark, Faroe Islands, France, Germany, Greece, Ireland, Italy, Latvia, Malta, Montenegro, Netherlands, Norway, Poland, Portugal, Spain, UK |
| **Data fields** | Well location, drilling date, drilling depth, well intent |
| **URL** | https://ows.emodnet-humanactivities.eu/geonetwork/srv/api/records/d16bc9d4-84eb-4713-87ff-d1d978616f0f |
| **Format** | Shapefile, Geodatabase, WMS/WFS |

### 1.5 FracTracker Wells Portal
| Field | Detail |
|-------|--------|
| **Source** | FracTracker Alliance |
| **Coverage** | United States — all 50 states |
| **Data fields** | Well location, type, status, operator, spud date, plug date, FracTracker category |
| **URL** | https://wells.fractracker.org/ |
| **Note** | Normalized from individual state regulatory agency databases |

### 1.6 ACR Carbon Registry — Orphan Well Plugging Methodology
| Field | Detail |
|-------|--------|
| **Source** | American Carbon Registry (Winrock International) |
| **Coverage** | US and Canada |
| **Data fields** | Well location, methane emissions, plugging methodology, carbon credits |
| **URL** | https://acrcarbon.org/methodology/plugging-orphaned-oil-and-gas-wells-2/ |
| **Note** | Carbon credit methodology for orphan well plugging |

---

## TIER 2: COUNTRY-SPECIFIC DATABASES

### 2.1 UNITED STATES 🇺🇸

**Estimated total abandoned wells: 3.4–4+ million**
**Documented orphan wells: 117,672 (USGS DOW dataset, 27 states)**
**Undocumented orphan wells: Unknown, possibly hundreds of thousands**

#### Federal Databases

| Database | Agency | URL | Well Count | Data Fields |
|----------|--------|-----|------------|-------------|
| USGS Documented Orphaned Well (DOW) Dataset | USGS | https://energy.usgs.gov/usdowdb/ | 117,672 wells (27 states) | Location, API number, well type, well status |
| BLM Orphan Well List | Bureau of Land Management | https://www.blm.gov/sites/default/files/docs/2024-06/BLM-OilandGas-Orphanwells-Factsheet-June2024.pdf | 296 (federal lands only) | Well ID, location, status |
| CATALOG (Consortium Advancing Technology) | DOE/NETL | https://catalog.energy.gov/ | National composite database | Multi-source integration |
| NETL Undocumented Orphaned Wells Program | DOE/NETL | https://www.netl.doe.gov/oil-gas/ngi/orphaned-wells | Active research | Well locations, methane measurements |
| EPA Greenhouse Gas Inventory | EPA | https://www.epa.gov/system/files/documents/2024-04/us-ghg-inventory-2024-main-text_04-18-2024.pdf | ~3.9M abandoned (including 2.2M unplugged) | National-level estimates |
| BOEM Offshore Wells | BOEM/BSEE | https://marinecadastre.gov/nationalviewer/ | 55,315 offshore (53,724 in Gulf of Mexico) | Well location, status, operator |
| DOI Well Dataset | Dept. of Interior | https://www.doi.gov/maps-data | Well ID, coordinates, API number, type, status | Complete national dataset |

#### State-Level Databases (Select — All 50 states have some form)

| State | Database/Agency | URL | Well Count | Notes |
|-------|----------------|-----|------------|-------|
| Texas | Railroad Commission of Texas (RRC) | https://www.rrc.texas.gov/ | 1,000,588+ abandoned | Largest single-state inventory |
| Pennsylvania | PA DEP | https://www.dep.pa.gov/ | Significant (pre-1860s wells) | Oldest oil-producing state |
| Ohio | OH DNR — RBDMS | https://gisdata-occokc.opendata.arcgis.com/datasets/OCCOKC::rbdms-orphan-funds-wells/about | Orphan fund wells | Digital records available |
| Oklahoma | OCC (Oklahoma Corp Commission) | https://www.oklahoma.gov/occ.html | Significant | Major producing state |
| Kentucky | KY DEP | https://eec.ky.gov/ | Hundreds of documented | Appalachian region |
| Louisiana | LA DEQ | https://www.deq.la.gov/ | Thousands | Gulf of Mexico proximity |
| California | CalGEM | https://calgem.energy.ca.gov/ | Significant | Kern County concentration |
| New Mexico | NMOGRD | https://www.emnrd.nm.gov/odmm/ | Significant | Permian Basin portion |
| Wyoming | WDEQ | https://deq.wyoming.gov/ | Hundreds | Federal land overlap |
| Colorado | COGCC | https://cogcc.state.co.us/ | Thousands | Regulatory reform state |
| Montana | MDEQ | https://deq.mt.gov/ | Kevin-Sunburst Dome wells measured | Research site |
| West Virginia | WV DEP | https://dep.wv.gov/ | Hundreds | Appalachian |
| Illinois | ISGS | Research program | Active undocumented well finding | CATALOG integration |
| Indiana | IDNR | https://www.in.gov/dnr/ | Hundreds | Appalachian |
| Michigan | EGLE | https://www.michigan.gov/egle | Thousands | Mature basin |
| New York | NYSDEC | https://www.dec.ny.gov/ | Hundreds | Marcellus region |
| Arkansas | AR OGC | https://www.argiscomm.com/arkoilgas/ | Hundreds | Fayetteville Shale |
| Kansas | KCC | https://kcc.ks.gov/ | Thousands | Mature basin |
| North Dakota | NDIC | https://www.dmr.nd.gov/ | Hundreds | Bakken |
| South Dakota | SDDANR | https://danr.sd.gov/ | Limited | Niobrara |
| Utah | DOGM | https://ogm.utah.gov/ | Hundreds | Federal land overlap |
| Alabama | AOGC | https://www.state.al.us/aogc/ | Hundreds | Gulf region |
| Mississippi | MDEQ | https://deq.ms.gov/ | Hundreds | Mature basin |
| Florida | FDEP | https://floridadep.gov/ | Limited | Panhandle |
| Georgia | GA DNR | https://gadnr.org/ | Minimal | Limited production |
| Virginia | VA DEQ | https://www.deq.virginia.gov/ | Limited | Appalachian |
| North Carolina | NC DEQ | https://deq.nc.gov/ | Minimal | Limited |
| Tennessee | TN DEQ | https://www.tn.gov/environment.html | Minimal | Limited |
| Indiana | IDNR | https://www.in.gov/dnr/ | Moderate | Mature basin |
| Iowa | INR | https://iowadnr.gov/ | Minimal | Limited |
| Missouri | MDNR | https://dnr.mo.gov/ | Minimal | Limited |
| Nebraska | NDEQ | https://deq.nebraska.gov/ | Minimal | Limited |
| South Carolina | SC DHEC | https://scdhec.gov/ | Minimal | Limited |
| Connecticut | CT DEEP | https://portal.ct.gov/DEEP | Minimal | Limited |
| Rhode Island | RI DEM | https://dem.ri.gov/ | Minimal | Limited |
| Vermont | VT ANR | https://anr.vermont.gov/ | Minimal | Limited |
| Maine | ME DEP | https://www.maine.gov/dep/ | Minimal | Limited |
| New Hampshire | NH DES | https://www.des.nh.gov/ | Minimal | Limited |
| Massachusetts | MA DEP | https://www.mass.gov/orgs/massdep | Minimal | Limited |
| New Jersey | NJ DEP | https://www.nj.gov/dep/ | Minimal | Limited |
| Maryland | MDE | https://mde.maryland.gov/ | Minimal | Limited |
| Delaware | DNREC | https://dnrec.delaware.gov/ | Minimal | Limited |
| Hawaii | Hawaii DOGGR | https://dlnr.hawaii.gov/ | Minimal | Limited |
| Alaska | AOGCC | https://wwwdog.dnr.alaska.gov/ | Moderate | Prudhoe Bay region |
| Nevada | NV DOGM | https://www.nvrocr.com/ | Minimal | Limited |
| Arizona | ADWR | https://azgeo-open-data-agic.hub.arcgis.com/datasets/azwater::well-registry-2024/explore | 240,674 wells (all types) | Well registry includes abandoned |

### 2.2 CANADA 🇨🇦

**Estimated total abandoned wells: 370,000+**
**Documented orphan wells: 19,000+ (Alberta) + thousands in other provinces**

| Province | Database/Agency | URL | Well Count | Data Fields |
|----------|----------------|-----|------------|-------------|
| **Alberta** | Orphan Well Association (OWA) | https://www.orphanwell.ca/inventory | 19,000+ orphan sites | Well ID, location, status, operator, reclamation status |
| **Alberta** | Alberta Energy Regulator (AER) | https://www.aer.ca/regulations-and-compliance-enforcement/liability-management-programs/insolvency/orphan-energy-sites | Full lifecycle data | Licensing, enforcement, lifecycle |
| **Alberta** | Abandoned Well Database (TownshipCan) | https://townshipcanada.com/learn/data-sources/orphan-abandoned-wells | 240,000+ abandoned + 19,000+ orphan | Normalized data |
| **Saskatchewan** | SK Orphan Fund Procurement Program | https://www.saskatchewan.ca/business/agriculture-natural-resources-and-industry/oil-and-gas/liability-management/orphan-fund-procurement-program/orphan-inventory | ~847+ orphan wells | Orphan Well and Facility List (downloadable) |
| **Saskatchewan** | Saskatchewan GeoAtlas | Provincial geodatabase | Comprehensive | Well location, status, operator |
| **British Columbia** | BC Energy Regulator (BCER) | https://www.bcogc.ca/public-zone/orphan-site-management | 346+ orphan wells (growing) | Orphan site data, reclamation status |
| **Manitoba** | Manitoba Geoscience | Not yet covered by normalized databases | Unknown | Limited data |
| **Ontario** | Ontario Petris | https://www.ontario.ca/ | Limited | Mature Appalachian |
| **Quebec** | MERN | https://www.mern.gouv.qc.ca/ | Minimal | Limited production |
| **New Brunswick** | DNR | Provincial | Minimal | Limited |
| **Nova Scotia** | NSDMM | Provincial | Minimal | Limited |
| **Newfoundland** | C-NLOPB | https://www.cnlopb.ca/ | Offshore focus | Canada-NL Offshore Petroleum Board |
| **Federal** | Natural Resources Canada | https://open.canada.ca/data/en/dataset/330ec960-cc52-47d9-840b-d93470347ab4 | National Inventory of Orphaned/Abandoned Mines (includes O&G) | Name, location, jurisdiction, commodity |

### 2.3 UNITED KINGDOM 🇬🇧

**Total North Sea wellbores: 12,500+ (UK waters)**
**Plugged and abandoned: ~5,500 wells**
**Expected decommissioning spend: £44 billion (~US$58.1B)**

| Database/Agency | URL | Well Count | Data Fields |
|----------------|-----|------------|-------------|
| NSTA (North Sea Transition Authority) — Well Data | https://www.nstauthority.co.uk/data-and-insights/data/themes/wells/ | 12,500+ wellbores | Well location, type, status, operator, spud date, completion date |
| NSTA Public Wellbore Search | https://itportal.nstauthority.co.uk/edufox5live/fox/edu/WONS_WELLBORE_SEARCH_PUBLIC | All UKCS wells | Interactive search portal |
| NSTA TWIST Database | https://www.nstauthority.co.uk/news-publications/right-tool-right-place-database-aims-to-make-decommissioning-cheaper-and-easier/ | 423+ subsea wells (pilot) | Wellhead type, christmas tree, tooling, ownership |
| NSTA Decommissioning Arrears Table | https://www.nstauthority.co.uk/news-publications/new-decom-table-highlights-named-operators-performance/ | 13 named operators behind on obligations | Operator, well count, compliance status |
| BGS Borehole Records | https://www.bgs.ac.uk/information-hub/borehole-records/ | Onshore borehole records | Scanned records, shaft/well data |
| Westwood Atlas Decom | https://www.westwoodenergy.com/atlas-decom-oil-gas-decommissioning-activity | Commercial database | Field-level decommissioning forecasts |

### 2.4 NORWAY 🇳🇴

**Total North Sea wellbores (Norwegian sector): 6,254**
**Abandoned fields: 12+ (as of 2013)**
**48% of decommissioning spend forecast 2035-2044**

| Database/Agency | URL | Well Count | Data Fields |
|----------------|-----|------------|-------------|
| Norwegian Offshore Directorate (NOD) — FactPages | https://factpages.npd.no/en/wellbore | 6,254+ wells | Wellbore location, status, completion reports, plugging data |
| NOD CO2 Atlas — Abandoned Fields | https://www.sodir.no/en/whats-new/publications/co2-atlases/ | 12+ abandoned fields | Field data, CO2 storage potential |
| EMODnet (Norway share) | https://emodnet.ec.europa.eu/en/human-activities | Part of 20,507 North Sea wells | Cross-border data |

### 2.5 AUSTRALIA 🇦🇺

**Crown owns all minerals by default**
**Colonial mining laws from 1851 onward**

| Database/Agency | URL | Well Count | Data Fields |
|----------------|-----|------------|-------------|
| NOPIMS (National Offshore Petroleum Information Management System) | https://www.ga.gov.au/nopims | Comprehensive offshore data | Well location, surveys, physical assets |
| NOPTA (National Offshore Petroleum Titles Administrator) | https://www.nopta.gov.au/ | Title management | Permit data, well data |
| NOPSEMA (National Offshore Petroleum Safety and Environmental Management Authority) | https://www.nopsema.gov.au/ | Safety/environmental | Well integrity, abandonment |
| State geological surveys (each state) | Various | Onshore well data | Varies by state |

**Crown Minerals Legislation (Australia):**
- Each state has its own Mining Act (e.g., NSW Mining Act 1992, Qld Mineral Resources Act 1989, WA Mining Act 1978, SA Mining Act 1971, Vic Mineral Resources Development Act 1990, Tas Mineral Resources Development Act 1995)
- Crown owns all minerals (except pre-1855 freehold grants in some states)
- Victoria and South Australia: legislative expropriation of ALL minerals to Crown
- Tasmania: gold, silver, oil, hydrogen, helium, atomic substances reserved to Crown

### 2.6 NEW ZEALAND 🇳🇿

| Database/Agency | URL | Legislation |
|----------------|-----|-------------|
| NZ Petroleum & Minerals | https://www.nzpam.govt.nz/ | Crown Minerals Act 1991 (amended 2025) |
| Crown Minerals Act regime | https://www.mbie.govt.nz/building-and-energy/energy-and-natural-resources/energy-generation-and-markets/liquid-fuel-market/crown-minerals-act-regime | Primary legislation |

**Crown Minerals Act 1991 (NZ):**
- Section 12: "Every alienation of land from the Crown... shall be deemed to be made subject to a reservation in favour of the Crown of every mineral existing in its natural condition"
- Crown retains all petroleum, gold, silver, uranium
- 2025 Amendment: reversed ban on new petroleum exploration; changed purpose from "manage" to "promote"; new decommissioning rules

### 2.7 SOUTH AFRICA 🇿🇦

| Database/Agency | URL | Legislation |
|----------------|-----|-------------|
| Petroleum Agency SA (PASA) | https://petroleumagencysa.com/ | Mineral and Petroleum Resources Development Act (MPRDA) 2002 |
| DMRE (Dept. of Mineral Resources and Energy) | https://www.dmr.gov.za/ | National Mining Charter |
| Crown Lands Act 1929 (SA) | https://faolex.fao.org/docs/pdf/sa44128.pdf | Historic Crown land framework |

**South African Crown Lands Framework:**
- Crown Lands Act 1929 — original colonial legislation
- MPRDA 2002 — current framework; state custodianship of all mineral rights
- Abandoned mine/energy site rehabilitation requirements exist

### 2.8 GERMANY 🇩🇪

| Database/Agency | URL | Data Fields |
|----------------|-----|-------------|
| TRANSGEO Project (GFZ Potsdam) | EU-funded — abandoned well database for Austria, Croatia, Germany, Hungary, Slovenia | Well location, geology, geothermal potential |
| State Office for Mining, Geology (Brandenburg) | https://www.lgb.brandenburg.de/ | Onshore well data |
| LBGR (Landesamt für Bergbau, Geologie und Rohstoffe Brandenburg) | State geological survey | Well records |
| BGR (Federal Institute for Geosciences) | https://www.bgr.bund.de/ | National geological data |

### 2.9 NETHERLANDS 🇳🇱

| Database/Agency | URL | Data Fields |
|----------------|-----|-------------|
| SodM (State Supervision of Mines) | https://www.sodm.nl/ | Well integrity, decommissioning |
| EMODnet (Netherlands share — 2,108 wells in North Sea) | https://emodnet.ec.europa.eu/en/human-activities | Offshore well data |
| TNO (Netherlands Organisation for Applied Scientific Research) | https://www.tno.nl/en/geoscience/ | Geological data, subsurface |

### 2.10 DENMARK 🇩🇰

| Database/Agency | URL | Data Fields |
|----------------|-----|-------------|
| DTU Offshore | https://offshore.dtu.dk/research/research-programmes/abandonment-of-offshore-oil-and-gas-fields | 269+ North Sea wells; research on well barrier materials, scale removal |
| Danish Energy Agency | https://ens.dk/ | Regulatory framework |
| EMODnet (Denmark share) | https://emodnet.ec.europa.eu/en/human-activities | Part of 20,507 North Sea wells |

### 2.11 FRANCE 🇫🇷

| Database/Agency | URL | Data Fields |
|----------------|-----|-------------|
| BRGM (Bureau de Recherches Géologiques et Minières) | https://www.brgm.fr/ | Geological data, well records |
| Ifremer | https://www.ifremer.fr/ | Offshore data |
| EMODnet (France share) | https://emodnet.ec.europa.eu/en/human-activities | Part of European offshore dataset |

### 2.12 ITALY 🇮🇹

| Database/Agency | URL | Data Fields |
|----------------|-----|-------------|
| Ministry of Economic Development — Ufficio矿区 | https://www.mise.gov.it/ | Well records |
| EMODnet (Italy share) | https://emodnet.ec.europa.eu/en/human-activities | Part of European offshore dataset |
| SOTACARBO | https://www.sotacarbo.it/ | Research on well abandonment |

### 2.13 SPAIN 🇪🇸

| Database/Agency | URL | Data Fields |
|----------------|-----|-------------|
| IGME (Instituto Geológico y Minero de España) | https://www.igme.es/ | Geological data |
| EMODnet (Spain share) | https://emodnet.ec.europa.eu/en/human-activities | Part of European offshore dataset |

### 2.14 PORTUGAL 🇵🇹

| Database/Agency | URL | Data Fields |
|----------------|-----|-------------|
| DGEG (Direção-Geral de Energia e Geologia) | https://www.dgeg.pt/ | Energy/geology data |
| EMODnet (Portugal share) | https://emodnet.ec.europa.eu/en/human-activities | Part of European offshore dataset |

### 2.15 IRELAND 🇮🇪

| Database/Agency | URL | Data Fields |
|----------------|-----|-------------|
| Geological Survey Ireland | https://www.gsi.ie/ | Well data |
| EMODnet (Ireland share) | https://emodnet.ec.europa.eu/en/human-activities | Part of European offshore dataset |

### 2.16 CROATIA 🇭🇷

| Database/Agency | URL | Data Fields |
|----------------|-----|-------------|
| TRANSGEO partner | https://www.researchgate.net/publication/380268780 | Abandoned well database for geothermal reuse |
| EMODnet (Croatia share) | https://emodnet.ec.europa.eu/en/human-activities | Part of European offshore dataset |

### 2.17 OTHER EUROPEAN COUNTRIES WITH OFFSHORE WELLS (via EMODnet)

| Country | Well Count (approx.) | Regulatory Body |
|---------|---------------------|-----------------|
| Cyprus | Small | Ministry of Energy |
| Faroe Islands | Small | Jarðfeingi |
| Germany (offshore) | 204 | BSH |
| Greece (western coast) | Small | Hellenic Ministry of Environment |
| Latvia | Minimal | Geological Survey |
| Malta | Minimal | Malta Resources Authority |
| Montenegro | Small | Ministry of Economy |
| Poland | Small | Polish Geological Institute |

### 2.18 RUSSIA 🇷🇺

**No comprehensive orphan well database publicly available**
**Reuters 2020 investigation: Could not find good estimates**

| Source | Detail |
|--------|--------|
| Rosnedra (Federal Agency for Mineral Resources) | https://rosnedra.gov.ru/ | State geological data; no public orphan well registry |
| Gazprom / Rosneft data | Internal corporate data; not publicly available |
| IEA/CEADs estimates | Included in global inventory of 4.5M wells |
| Key concern | 29 million abandoned wells estimated internationally (Wikipedia/Reuters); Russia is major contributor but data unavailable |

### 2.19 CHINA 🇨🇳

**No comprehensive orphan well database publicly available**
**Reuters 2020 investigation: Could not find good estimates**

| Source | Detail |
|--------|--------|
| Ministry of Natural Resources | https://www.mnr.gov.cn/ | State geological data |
| CNPC / Sinopec / CNOOC data | Internal corporate data |
| CEADs (Tsinghua) | https://ceads.net/ | Global inventory includes China |
| 2014 study: abandoned wells for geothermal | Published research; no public database |
| 2019 study: abandoned gas wells for geothermal | Published research |

### 2.20 INDIA 🇮🇳

**No comprehensive orphan well database publicly available**

| Source | Detail |
|--------|--------|
| Ministry of Petroleum and Natural Gas | https://petroleum.nic.in/ | Regulatory data |
| Oil and Natural Gas Corporation (ONGC) | Internal data | Corporate inventory |
| Oil India Limited | Internal data | Corporate inventory |
| CEADs | Global inventory includes India |

### 2.21 INDONESIA 🇮🇩

**~70% of old wells found to have no economic value — abandoned during lifecycle**

| Source | Detail |
|--------|--------|
| SKK Migas (Special Working Unit for Upstream Oil and Gas) | https://www.skmigas.go.id/ | Regulatory data |
| Pertamina | Internal data | State oil company |
| ResearchGate: "Indonesia Well Abandonment Standard Gap Analysis" | https://www.researchgate.net/publication/356517186 | 70% of old wells abandoned |
| CEADs | Shell's legacy wells = 28% of Indonesia's AOG emissions |

### 2.22 NIGERIA 🇳🇬

**Shell's legacy wells = 22% of Nigeria's AOG well emissions**

| Source | Detail |
|--------|--------|
| DPR (Dept. of Petroleum Resources) / NMDPRA | https://nmdpra.gov.ng/ | Regulatory data |
| NNPC Limited | Internal data | State oil company |
| CEADs | Shell legacy wells significant contributor |

### 2.23 THAILAND 🇹🇭

**Chevron's former assets = 42% of Thailand's AOG well emissions**

| Source | Detail |
|--------|--------|
| Department of Mineral Fuels | https://www.dmf.go.th/ | Regulatory data |
| PTT Public Company Limited | Internal data | State enterprise |
| CEADs | Chevron legacy wells major contributor |

### 2.24 MEXICO 🇲🇽

| Source | Detail |
|--------|--------|
| CNH (Comisión Nacional de Hidrocarburos) | https://www.gob.mx/cnh | Regulatory data |
| PEMEX | Internal data | State oil company |
| CEADs | Included in global inventory |

### 2.25 BRAZIL 🇧🇷

| Source | Detail |
|--------|--------|
| ANP (Agência Nacional do Petróleo, Gás Natural e Biocombustíveis) | https://www.gov.br/anp/ | Regulatory data |
| Petrobras | Internal data | State oil company |
| CEADs | Included in global inventory |

### 2.26 ARGENTINA 🇦🇷

| Source | Detail |
|--------|--------|
| ENARGAS / Secretary of Energy | https://www.argentina.gob.ar/energia | Regulatory data |
| YPF | Internal data | State oil company |
| CEADs | Included in global inventory |

### 2.27 COLOMBIA 🇨🇴

| Source | Detail |
|--------|--------|
| ANH (Agencia Nacional de Hidrocarburos) | https://www.anh.gov.co/ | Regulatory data |
| Ecopetrol | Internal data | State oil company |
| CEADs | Included in global inventory |

### 2.28 ECUADOR 🇪🇨

| Source | Detail |
|--------|--------|
| CEPE / Ministerio de Energía | https://www.recursosyenergia.gob.ec/ | Regulatory data |
| Petroecuador | Internal data | State oil company |
| CEADs | Included in global inventory |

### 2.29 VENEZUELA 🇻🇪

| Source | Detail |
|--------|--------|
| PDVSA | Internal data | State oil company; no public orphan well data |
| CEADs | Included in global inventory |

### 2.30 IRAN 🇮🇷

| Source | Detail |
|--------|--------|
| NIOC (National Iranian Oil Company) | Internal data | State oil company |
| Ministry of Petroleum | https://www.mop.ir/ | Regulatory data |
| CEADs | Included in global inventory |

### 2.31 IRAQ 🇮🇶

| Source | Detail |
|--------|--------|
| SOMO (State Oil Marketing Organization) | Internal data | State entity |
| INOC (Iraq National Oil Company) | Internal data | State entity |
| CEADs | Included in global inventory |

### 2.32 SAUDI ARABIA 🇸🇦

**Reuters 2020: Could not find good orphan well estimates**

| Source | Detail |
|--------|--------|
| Saudi Aramco | Internal data | State oil company; no public orphan well registry |
| Ministry of Energy | https://www.energy.gov.sa/ | Regulatory data |
| CEADs | Included in global inventory |

### 2.33 KUWAIT 🇰🇼

| Source | Detail |
|--------|--------|
| KOC (Kuwait Oil Company) | Internal data | State entity |
| Kuwait Petroleum Corporation | Internal data | State entity |
| CEADs | Included in global inventory |

### 2.34 UAE 🇦🇪

| Source | Detail |
|--------|--------|
| ADNOC / various emirate entities | Internal data | State entities |
| Federal Authority for Nuclear Regulation | https://www.fanr.gov.ae/ | Limited scope |
| CEADs | Included in global inventory |

### 2.35 QATAR 🇶🇦

| Source | Detail |
|--------|--------|
| QatarEnergy | Internal data | State entity |
| Ministry of Energy and Industry | https://www.meei.gov.qa/ | Regulatory data |
| CEADs | Included in global inventory |

### 2.36 OMAN 🇴🇲

| Source | Detail |
|--------|--------|
| PDO (Petroleum Development Oman) | Internal data | State entity |
| Ministry of Energy and Minerals | https://www.energyandminerals.gov.om/ | Regulatory data |
| CEADs | Included in global inventory |

### 2.37 EGYPT 🇪🇬

| Source | Detail |
|--------|--------|
| EGPC (Egyptian General Petroleum Corporation) | Internal data | State entity |
| EGAS (Egyptian Natural Gas Holding Company) | Internal data | State entity |
| CEADs | Included in global inventory |

### 2.38 LIBYA 🇱🇾

| Source | Detail |
|--------|--------|
| NOC (National Oil Corporation) | Internal data | State entity |
| CEADs | Included in global inventory |

### 2.39 ANGOLA 🇦🇴

| Source | Detail |
|--------|--------|
| ANPG (Agência Nacional de Petróleo, Gás e Biocombustíveis) | https://www.anpg.gov.ao/ | Regulatory data |
| Sonangol | Internal data | State entity |
| CEADs | Included in global inventory |

### 2.40 GABON 🇬🇦

| Source | Detail |
|--------|--------|
| Direction Générale des Hydrocarbures | Internal data | State entity |
| CEADs | Included in global inventory |

### 2.41 CONGO 🇨🇬

| Source | Detail |
|--------|--------|
| Société Nationale des Pétroles du Congo (SNPC) | Internal data | State entity |
| CEADs | Included in global inventory |

### 2.42 TRINIDAD AND TOBAGO 🇹🇹

| Source | Detail |
|--------|--------|
| Ministry of Energy and Energy Industries | https://www.energy.gov.tt/ | Regulatory data |
| Petrotrin (now Paria Fuel Trading Company) | Internal data | State entity |
| CEADs | Included in global inventory |

### 2.43 GUYANA 🇬🇾

| Source | Detail |
|--------|--------|
| Ministry of Natural Resources | https://www自然资源.gov.gy/ | Regulatory data |
| CEADs | Included in global inventory |

### 2.44 BRAZIL 🇧🇷 (additional)

| Source | Detail |
|--------|--------|
| IBAMA (Brazilian Institute of Environment) | https://www.ibama.gov.br/ | Environmental enforcement |
| ANP well data | Public well registry | Well location, status |

### 2.45 ROMANIA 🇷🇴

| Source | Detail |
|--------|--------|
| ANRM (National Agency for Mineral Resources) | https://www.anrm.ro/ | Regulatory data |
| Romgaz / Petrom | Internal data | State/commercial entities |
| EMODnet | Included in North Sea database | Offshore data |

### 2.46 HUNGARY 🇭🇺

| Source | Detail |
|--------|--------|
| TRANSGEO partner | EU-funded abandoned well database | Geothermal reuse assessment |
| Mining Property Utilization Nonprofit Public Ltd. | State entity | Well data |

### 2.47 SLOVENIA 🇸🇮

| Source | Detail |
|--------|--------|
| Local Energy Agency Pomurje | TRANSGEO partner | Abandoned well database |

### 2.48 AUSTRIA 🇦🇹

| Source | Detail |
|--------|--------|
| Geosphere Austria | TRANSGEO partner | Abandoned well database for Vienna Basin and Pannonian Basin |

### 2.49 POLAND 🇵🇱

| Source | Detail |
|--------|--------|
| Polish Geological Institute | https://www.pgi.gov.pl/ | Geological data |
| EMODnet (Poland share) | Part of European offshore dataset | Offshore well data |

### 2.50 JAPAN 🇯🇵

| Source | Detail |
|--------|--------|
| JOGMEC (Japan Organization for Metals and Energy Security) | https://www.jogmec.go.jp/ | Regulatory data |
| CEADs | Included in global inventory |

### 2.51 SOUTH KOREA 🇰🇷

| Source | Detail |
|--------|--------|
| Korea National Oil Corporation (KNOC) | Internal data | State entity |
| CEADs | Included in global inventory |

### 2.52 MALAYSIA 🇲🇾

| Source | Detail |
|--------|--------|
| PETRONAS | Internal data | State entity |
| Petronas Carigali | Internal data | Exploration subsidiary |
| CEADs | Included in global inventory |

### 2.53 VIETNAM 🇻🇳

| Source | Detail |
|--------|--------|
| PetroVietnam | Internal data | State entity |
| CEADs | Included in global inventory |

### 2.54 MYANMAR 🇲🇲

| Source | Detail |
|--------|--------|
| MOGE (Myanmar Oil and Gas Enterprise) | Internal data | State entity |
| CEADs | Included in global inventory |

### 2.55 PAKISTAN 🇵🇰

| Source | Detail |
|--------|--------|
| OGDC (Oil and Gas Development Company) | Internal data | State entity |
| OGDCL | Internal data | State entity |
| CEADs | Included in global inventory |

### 2.56 BANGLADESH 🇧🇩

| Source | Detail |
|--------|--------|
| Petrobangla | Internal data | State entity |
| CEADs | Included in global inventory |

### 2.57 EQUATORIAL GUINEA 🇬🇶

| Source | Detail |
|--------|--------|
| GEPetrol | Internal data | State entity |
| CEADs | Included in global inventory |

### 2.58 GABON 🇬🇦

| Source | Detail |
|--------|--------|
| Direction Générale des Hydrocarbures | Internal data | State entity |
| CEADs | Included in global inventory |

### 2.59 SOUTH SUDAN 🇸🇸

| Source | Detail |
|--------|--------|
| Nile Petroleum Corporation (NilePet) | Internal data | State entity |
| CEADs | Included in global inventory |

### 2.60 UGANDA 🇺🇬

| Source | Detail |
|--------|--------|
| Petroleum Authority of Uganda | https://www.pau.go.ug/ | Regulatory data |
| CEADs | Included in global inventory |

### 2.61 KENYA 🇰🇪

| Source | Detail |
|--------|--------|
| Energy and Petroleum Regulatory Authority (EPRA) | https://www.epra.go.ke/ | Regulatory data |
| CEADs | Included in global inventory |

### 2.62 TANZANIA 🇹🇿

| Source | Detail |
|--------|--------|
| Petroleum Upstream Regulatory Authority (PURA) | https://www.pura.go.tz/ | Regulatory data |
| CEADs | Included in global inventory |

### 2.63 MOZAMBIQUE 🇲🇿

| Source | Detail |
|--------|--------|
| INP (Instituto Nacional de Petróleo) | https://www.inp.gov.mz/ | Regulatory data |
| CEADs | Included in global inventory |

### 2.64 NAMIBIA 🇳🇦

| Source | Detail |
|--------|--------|
| Ministry of Mines and Energy | https://www.mme.gov.na/ | Regulatory data |
| NAMCOR | Internal data | State entity |
| CEADs | Included in global inventory |

### 2.65 BOTSWANA 🇧🇼

| Source | Detail |
|--------|--------|
| Department of Mines and Mineral Resources | Regulatory data | Limited production |

### 2.66 ZAMBIA 🇿🇲

| Source | Detail |
|--------|--------|
| Ministry of Mines and Minerals Development | Regulatory data | Limited production |

### 2.67 ZIMBABWE 🇿🇼

| Source | Detail |
|--------|--------|
| Ministry of Mines and Mining Development | Regulatory data | Limited production |

### 2.68 PERU 🇵🇪

| Source | Detail |
|--------|--------|
| OEFA (Organismo de Evaluación y Fiscalización Ambiental) | https://www.gob.pe/oefa | Environmental enforcement |
| CEADs | Included in global inventory |

### 2.69 BOLIVIA 🇧🇴

| Source | Detail |
|--------|--------|
| YPFB | Internal data | State entity |
| CEADs | Included in global inventory |

### 2.70 CHILE 🇨🇱

| Source | Detail |
|--------|--------|
| ENAP | Internal data | State entity (limited) |
| CEADs | Included in global inventory |

### 2.71 CUBA 🇨🇺

| Source | Detail |
|--------|--------|
| CUPET | Internal data | State entity |
| CEADs | Included in global inventory |

### 2.72 ALGERIA 🇩🇿

| Source | Detail |
|--------|--------|
| Sonatrach | Internal data | State entity |
| CEADs | Included in global inventory |

### 2.73 TUNISIA 🇹🇳

| Source | Detail |
|--------|--------|
| ETAP (Entreprise Tunisienne d'Activités Pétrolières) | Internal data | State entity |
| CEADs | Included in global inventory |

### 2.74 MOROCCO 🇲🇦

| Source | Detail |
|--------|--------|
| ONHYM (Office National des Hydrocarbures et des Mines) | https://www.onhym.ma/ | Regulatory data |
| CEADs | Included in global inventory |

### 2.75 TURKEY 🇹🇷

| Source | Detail |
|--------|--------|
| TPAO (Turkish Petroleum Corporation) | Internal data | State entity |
| CEADs | Included in global inventory |

### 2.76 UKRAINE 🇺🇦

| Source | Detail |
|--------|--------|
| Naftogaz | Internal data | State entity |
| CEADs | Included in global inventory |

### 2.77 GEORGIA 🇬🇪

| Source | Detail |
|--------|--------|
| CNPC / SOCAR (through Azerbaijan) | Limited production | Limited data |

### 2.78 AZERBAIJAN 🇦🇿

| Source | Detail |
|--------|--------|
| SOCAR | Internal data | State entity |
| CEADs | Included in global inventory |

### 2.79 KAZAKHSTAN 🇰🇿

| Source | Detail |
|--------|--------|
| KazMunayGas | Internal data | State entity |
| CEADs | Included in global inventory |

### 2.80 UZBEKISTAN 🇺🇿

| Source | Detail |
|--------|--------|
| Uzbekneftegaz | Internal data | State entity |
| CEADs | Included in global inventory |

### 2.81 TURKMENISTAN 🇹🇲

| Source | Detail |
|--------|--------|
| Turkmengaz / Turkmenneft | Internal data | State entities |
| CEADs | Included in global inventory |

### 2.82 PAPUA NEW GUINEA 🇵🇬

| Source | Detail |
|--------|--------|
| Department of Petroleum and Energy | Regulatory data | Limited production |
| CEADs | Included in global inventory |

### 2.83 TIMOR-LESTE 🇹🇱

| Source | Detail |
|--------|--------|
| Autoridade Nacional do Petróleo e Minerais (ANPM) | https://anpm.tl/ | Regulatory data |
| CEADs | Included in global inventory |

### 2.84 PHILIPPINES 🇵🇭

| Source | Detail |
|--------|--------|
| DOE (Dept. of Energy) | https://www.doe.gov.ph/ | Regulatory data |
| CEADs | Included in global inventory |

### 2.85 CHAD 🇹🇩

| Source | Detail |
|--------|--------|
| SNH (Société Nationale des Hydrocarbures) | Internal data | State entity |
| CEADs | Included in global inventory |

### 2.86 CAMEROON 🇨🇲

| Source | Detail |
|--------|--------|
| SNH (Société Nationale des Hydrocarbures) | Internal data | State entity |
| CEADs | Included in global inventory |

### 2.87 REPUBLIC OF CONGO 🇨🇬

| Source | Detail |
|--------|--------|
| Société Nationale des Pétroles du Congo (SNPC) | Internal data | State entity |
| CEADs | Included in global inventory |

### 2.88 EQUATORIAL GUINEA 🇬🇶

| Source | Detail |
|--------|--------|
| GEPetrol | Internal data | State entity |
| CEADs | Included in global inventory |

### 2.89 SENEGAL 🇸🇳

| Source | Detail |
|--------|--------|
| PETROSEN | Internal data | State entity |
| CEADs | Included in global inventory |

### 2.90 GHANA 🇬🇭

| Source | Detail |
|--------|--------|
| Ghana National Petroleum Corporation (GNPC) | Internal data | State entity |
| CEADs | Included in global inventory |

### 2.91 CÔTE D'IVOIRE 🇨🇮

| Source | Detail |
|--------|--------|
| PETROCI | Internal data | State entity |
| CEADs | Included in global inventory |

### 2.92 BENIN 🇧🇯

| Source | Detail |
|--------|--------|
| Office Béninois des Pétroles (OBP) | Internal data | State entity |
| CEADs | Included in global inventory |

### 2.93 GAMBIA 🇬🇲

| Source | Detail |
|--------|--------|
| PNGC (Petroleum Commission) | Internal data | Limited production |

### 2.94 GUINEA-BISSAU 🇬🇼

| Source | Detail |
|--------|--------|
| PETROGUINÉ | Internal data | Limited production |

### 2.95 SIERRA LEONE 🇸🇱

| Source | Detail |
|--------|--------|
| Petroleum Directorate | Internal data | Limited production |

### 2.96 LIBERIA 🇱🇷

| Source | Detail |
|--------|--------|
| Liberia Petroleum Regulatory Authority | Internal data | Limited production |

### 2.97 MAURITANIA 🇲🇷

| Source | Detail |
|--------|--------|
| Société Mauritanienne des Hydrocarbures (SMH) | Internal data | State entity |
| CEADs | Included in global inventory |

### 2.98 SOMALIA 🇸🇴

| Source | Detail |
|--------|--------|
| Ministry of Petroleum and Mineral Resources | Internal data | Limited production |

### 2.99 DJIBOUTI 🇩🇯

| Source | Detail |
|--------|--------|
| Ministry of Energy and Natural Resources | Internal data | Limited production |

### 2.100 YEMEN 🇾🇪

| Source | Detail |
|--------|--------|
| Ministry of Oil and Minerals | Internal data | Conflict-affected; limited data |

### 2.101 JORDAN 🇯🇴

| Source | Detail |
|--------|--------|
| National Petroleum Company | Internal data | Limited production |

### 2.102 ISRAEL/PALESTINE 🇮🇱🇵🇸

| Source | Detail |
|--------|--------|
| Israel Ministry of Energy | https://www.gov.il/en/departments/ministry_of_energy_and_infrastructure | Limited production (Leviathan, Tamar) |

### 2.103 LEBANON 🇱🇧

| Source | Detail |
|--------|--------|
| Ministry of Energy and Water | Internal data | Limited exploration |

### 2.104 CYPRUS 🇨🇾

| Source | Detail |
|--------|--------|
| Ministry of Energy, Commerce and Industry | https://www.gov.cy/mcit/ | Limited exploration |
| EMODnet | Part of European offshore dataset | Offshore data |

### 2.105 BULGARIA 🇧🇬

| Source | Detail |
|--------|--------|
| Ministry of Energy | Internal data | Limited production |

### 2.106 SERBIA 🇷🇸

| Source | Detail |
|--------|--------|
| Ministry of Mining and Energy | Internal data | Limited production |

### 2.107 NORTH MACEDONIA 🇲🇰

| Source | Detail |
|--------|--------|
| Ministry of Economy | Internal data | Limited production |

### 2.108 ALBANIA 🇦🇱

| Source | Detail |
|--------|--------|
| Albpetrol | Internal data | State entity |

### 2.109 MOLDOVA 🇲🇩

| Source | Detail |
|--------|--------|
| Ministry of Infrastructure and Regional Development | Internal data | Limited production |

### 2.110 BELARUS 🇧🇾

| Source | Detail |
|--------|--------|
| Belorusneft | Internal data | State entity |

### 2.111 ESTONIA 🇪🇪

| Source | Detail |
|--------|--------|
| Ministry of Economic Affairs and Communications | Internal data | Oil shale focus |

### 2.112 LATVIA 🇱🇻

| Source | Detail |
|--------|--------|
| Ministry of Economics | Internal data | Limited production |
| EMODnet | Part of European offshore dataset | Offshore data |

### 2.113 LITHUANIA 🇱🇹

| Source | Detail |
|--------|--------|
| Ministry of Energy | Internal data | Limited production |

### 2.114 FINLAND 🇫🇮

| Source | Detail |
|--------|--------|
| Geological Survey of Finland (GTK) | https://wwwgtk.fi/ | Geological data |

### 2.115 SWEDEN 🇸🇪

| Source | Detail |
|--------|--------|
| Sveriges geologiska undersökning (SGU) | https://www.sgu.se/ | Geological data |

### 2.116 AUSTRIA 🇦🇹 (additional)

| Source | Detail |
|--------|--------|
| Geosphere Austria | TRANSGEO partner | Vienna Basin, Pannonian Basin abandoned wells |

### 2.117 SWITZERLAND 🇨🇭

| Source | Detail |
|--------|--------|
| Swisstopo | https://www.swisstopo.admin.ch/ | Geological data; minimal oil/gas |

### 2.118 IRELAND 🇮🇪 (additional)

| Source | Detail |
|--------|--------|
| Minister for the Environment | Internal data | Limited production |
| EMODnet | Part of European offshore dataset | Offshore data |

### 2.119 ICELAND 🇮🇸

| Source | Detail |
|--------|--------|
| National Energy Authority | https://nea.is/ | Geothermal focus; minimal O&G |

### 2.120 FAROE ISLANDS 🇫🇴

| Source | Detail |
|--------|--------|
| Jarðfeingi (Faroe Geological Survey) | https://jfr.fo/ | Limited production |
| EMODnet | Part of European offshore dataset | Offshore data |

### 2.121 GREENLAND 🇬🇱

| Source | Detail |
|--------|--------|
| Bureau of Minerals and Petroleum | https://naalakkersuisut.gl/Minerals | Limited exploration |

### 2.122 BAHAMAS 🇧🇸

| Source | Detail |
|--------|--------|
| Ministry of the Environment | Internal data | No significant production |

### 2.123 BELIZE 🇧🇿

| Source | Detail |
|--------|--------|
| Ministry of Energy | Internal data | No significant production |

### 2.124 HONDURAS 🇭🇳

| Source | Detail |
|--------|--------|
| SERNA | Internal data | No significant production |

### 2.125 NICARAGUA 🇳🇮

| Source | Detail |
|--------|--------|
| Ministry of Energy and Mines | Internal data | Limited production |

### 2.126 EL SALVADOR 🇸🇻

| Source | Detail |
|--------|--------|
| Ministry of Economy | Internal data | No significant production |

### 2.127 COSTA RICA 🇨🇷

| Source | Detail |
|--------|--------|
| RECOPE | Internal data | Refining focus; minimal upstream |

### 2.128 PANAMA 🇵🇦

| Source | Detail |
|--------|--------|
| Ministry of Commerce and Industries | Internal data | No significant production |

---

## TIER 3: ADDITIONAL DATA SOURCES

### 3.1 Satellite Remote Sensing
| Source | Capability |
|--------|-----------|
| GHGSat | Methane detection from satellite; can identify super-emitter wells |
| Sentinel-5P (ESA) | Global methane monitoring |
| TROPOMI | Methane column measurements |
| Carbon Mapper | High-resolution methane plume detection |

### 3.2 Academic / Research Databases
| Source | Detail |
|--------|--------|
| McGill University / EDF Orphan Well Map | https://www.edf.org/orphanwellmap | 120,000 documented wells across 30 US states |
| Penn State / USGS Geospatial Analysis | https://www.usgs.gov/publications/a-geospatial-analysis-water-quality-threats-orphan-wells-principal-and-secondary | Aquifer threat analysis |
| Iowa State / Environmental Science & Technology | IOP Science — abandoned well renewable energy potential | Wind/solar/geothermal potential at well sites |

### 3.3 Industry Databases
| Source | Detail |
|--------|--------|
| IHS Markit (S&P Global) | Commercial well database — comprehensive but proprietary |
| Drillinginfo (Enverus) | Commercial well data |
| Wood Mackenzie | Commercial decommissioning intelligence |
| Westwood Atlas Decom | UK/Norway decommissioning commercial database |

---

## KEY FINDINGS FOR PIPELINE

### Data Availability Matrix

| Tier | Countries | Data Quality | Orphan Well Count |
|------|-----------|-------------|-------------------|
| **Tier A: Comprehensive data** | US, Canada (AB, SK, BC) | Excellent | 117,672+ documented orphans; 3.4M+ abandoned |
| **Tier B: Partial data** | UK, Norway, Netherlands, Denmark, Germany, Australia | Good | 20,507+ North Sea wells; growing decommissioning data |
| **Tier C: Limited data** | France, Italy, Spain, Portugal, Ireland, Croatia, Romania, Hungary, Slovenia, Austria, Poland, New Zealand, South Africa | Moderate | National registries exist but incomplete |
| **Tier D: Minimal/no public data** | Russia, China, India, Saudi Arabia, Venezuela, Iran, Iraq, Kuwait, UAE, Qatar, Oman, Nigeria, Indonesia, Mexico, Brazil, Argentina, Colombia | Poor to None | Major producers with no public orphan well data |
| **Tier E: No significant production** | ~50 smaller countries | N/A | Minimal or no wells |

### Colonial/Crown Lands Legal Framework Applicability

| Jurisdiction | Crown Lands Act / Colonial Framework | Mineral Rights Default | Key Legislation |
|-------------|--------------------------------------|----------------------|-----------------|
| **Canada** | Crown Lands Protection Act 1839; Provincial Crown Lands Acts | Crown retains minerals (81% in Alberta) | Provincial Mining/Oil & Gas Acts |
| **Australia** | Crown owns all minerals since 1855; Mining Acts by state | Crown retains all minerals | Mining Act (varies by state) |
| **New Zealand** | Crown Minerals Act 1991 (s.12 reserves all minerals to Crown) | Crown retains all minerals | Crown Minerals Act 1991 |
| **South Africa** | Crown Lands Act 1929; MPRDA 2002 | State custodianship of all minerals | MPRDA 2002 |
| **UK (North Sea)** | Petroleum Act 1998; Crown Estate | Crown owns seabed minerals | Petroleum Act 1998 |
| **Norway** | Continental Shelf Act; Petroleum Act | State ownership of subsea resources | Petroleum Act 1996 |
| **Netherlands** | Mining Act 2003 | State ownership of minerals | Mining Act 2003 |
| **Denmark** | Subsoil Act | State ownership of subsoil resources | Subsoil Act 2009 |
| **Germany** | Mineral Resources Act (BBergG) | State ownership of minerals | BBergG 1980 |
| **France** | Mining Code | State ownership of minerals | Code Minier |
| **Italy** | Mining Code (RD 1443/1927) | State ownership of minerals | Regio Decreto 1927 |
| **Spain** | Mining Law 22/1973 | State ownership of minerals | Ley de Minas |
| **Portugal** | Mining Law 52/2015 | State ownership of minerals | Lei de Minas |
| **Ireland** | Minerals Development Acts 1940-1999 | State ownership of minerals | MDA 1940-1999 |
| **Croatia** | Mining Act | State ownership | Zakon o rudarstvu |
| **Romania** | Mining Law 85/2003 | State ownership | Legea Minelor |
| **Hungary** | Mining Act XLVIII of 1993 | State ownership | Bányatörvény |
| **Slovenia** | Mining Act | State ownership | Zakon o rudarstvu |
| **Austria** | Mining Act 1978 | State ownership | Berggesetz |
| **Poland** | Geological and Mining Law 2011 | State ownership | Prawo geologiczne i górnicze |
| **Greece** | Mining Code (Law 4009/2011) | State ownership | Kwdikas Metalleion |
| **Bulgaria** | Minerals and Natural Resources Act | State ownership | Закон за подземните богатства |
| **Serbia** | Mining Law | State ownership | Zakon o rudarstvu |
| **Turkey** | Petroleum Law 4647; Mining Law | State ownership | Petrol Kanunu |
| **Japan** | Mine Safety Act; Petroleum and Natural Gas Development Act | State ownership | Various |
| **South Korea** | Mine Safety Act | State ownership | Various |
| **Malaysia** | Petroleum Development Act 1974 | State ownership | PDA 1974 |
| **Vietnam** | Petroleum Law | State ownership | Luật Dầu khí |
| **Myanmar** | Mining Law 2015 | State ownership | Mining Law |
| **Pakistan** | Petroleum (Exploration and Development) Ordinance 1976 | State ownership | Various |
| **Bangladesh** | Petroleum Act 2010 | State ownership | Various |
| **Nigeria** | Petroleum Industry Act 2021 | State ownership | PIA 2021 |
| **Algeria** | Hydrocarbon Law 2005/2019 | State ownership | Various |
| **Libya** | Petroleum Law 25 of 1955 | State ownership | Various |
| **Egypt** | Law No. 66 of 1953 (amended) | State ownership | Various |
| **Angola** | Petroleum Activities Law | State ownership | Various |
| **Mozambique** | Petroleum Law 21/2014 | State ownership | Various |
| **Tanzania** | Petroleum Act 2015 | State ownership | Various |
| **Uganda** | Petroleum (Exploration, Development and Production) Act 2013 | State ownership | Various |
| **Kenya** | Petroleum (Exploration and Production) Act 1986 | State ownership | Various |
| **South Sudan** | Petroleum Revenue Management Act 2013 | State ownership | Various |
| **Ghana** | Petroleum (Exploration and Production) Act 2016 | State ownership | Various |
| **Senegal** | Petroleum Code | State ownership | Various |
| **Mauritania** | Hydrocarbons Code | State ownership | Various |
| **Cameroon** | Petroleum Law | State ownership | Various |
| **Congo (Brazzaville)** | Petroleum Code | State ownership | Various |
| **Gabon** | Petroleum Code | State ownership | Various |
| **Equatorial Guinea** | Hydrocarbons Law 1981 | State ownership | Various |
| **Benin** | Petroleum Code | State ownership | Various |
| **Côte d'Ivoire** | Petroleum Code | State ownership | Various |
| **Trinidad and Tobago** | Petroleum Act | State ownership | Various |
| **Guyana** | Petroleum (Exploration and Production) Act | State ownership | Various |
| **Peru** | Hydrocarbons Law | State ownership | Various |
| **Bolivia** | Hydrocarbon Law 3058 | State ownership | Various |
| **Ecuador** | Hydrocarbons Law | State ownership | Various |
| **Colombia** | Law 80 of 1993 | State ownership | Various |
| **Chile** | DL 600 (for investment) | State ownership | Various |
| **Argentina** | Hydrocarbons Law 14773 | Dual system (national/provincial) | Various |
| **Mexico** | Hydrocarbons Law | State ownership | Various |
| **Brazil** | Mining Code | State ownership | Various |
| **Venezuela** | Hydrocarbons Law | State ownership | Various |
| **Cuba** | Mining Law | State ownership | Various |
| **China** | Mineral Resources Law | State ownership | 矿产资源法 |
| **India** | Mines and Minerals (Development and Regulation) Act 1957 | State ownership | MMDR Act |
| **Indonesia** | Mining Law 4/2009; Oil and Gas Law 22/2001 | State ownership | Various |
| **Thailand** | Petroleum Act 1971 | State ownership | Various |
| **Philippines** | Petroleum Act 427 (as amended) | State ownership | Various |
| **Papua New Guinea** | Oil and Gas Act 1998 | State ownership | Various |
| **Timor-Leste** | Petroleum Activities Law 2005 | State ownership | Various |
| **Russia** | Subsoil Law 215-FZ | State ownership | Недра (Subsoil Law) |
| **Kazakhstan** | Subsoil Use Code | State ownership | Various |
| **Uzbekistan** | Law on Subsoil | State ownership | Various |
| **Turkmenistan** | Law on Oil and Gas | State ownership | Various |
| **Azerbaijan** | Petroleum Law | State ownership | Various |
| **Georgia** | Law on Subsoil | State ownership | Various |
| **Jordan** | Minerals Investment Law | State ownership | Various |
| **Israel** | Petroleum Law 1952 | State ownership | Various |
| **Lebanon** | Petroleum Resources Law | State ownership | Various |
| **Cyprus** | Hydrocarbons (Exploration, Exploitation and Export) Law | State ownership | Various |
| **Syria** | Petroleum Law | State ownership | Conflict-affected |
| **Iraq** | Oil and Gas Law (draft) | State ownership | Federal + KRG |
| **Kuwait** | Kuwait Petroleum Corporation Law | State ownership | Various |
| **UAE** | Federal/Emirate petroleum laws | State ownership | Varies by Emirate |
| **Qatar** | Petroleum Law | State ownership | Various |
| **Oman** | Petroleum Law | State ownership | Various |
| **Bahrain** | Petroleum Law | State ownership | Various |
| **Yemen** | Petroleum Exploration and Production Law | State ownership | Conflict-affected |
| **Eritrea** | Mining Proclamation | State ownership | Various |
| **Ethiopia** | Mining Proclamation | State ownership | Various |
| **Sudan** | Petroleum Law | State ownership | Conflict-affected |
| **South Sudan** | Petroleum Revenue Management Act | State ownership | Various |
| **Tunisia** | Petroleum Code | State ownership | Various |
| **Morocco** | Mining Code | State ownership | Various |
| **Djibouti** | Mining Code | State ownership | Various |
| **Somalia** | Petroleum Law | State ownership | Limited governance |
| **Madagascar** | Mining Code | State ownership | Various |
| **Mauritius** | Minerals Act | State ownership | Limited production |
| **Comoros** | Mining Code | State ownership | Limited production |
| **Cabo Verde** | Mining Code | State ownership | Limited production |
| **São Tomé and Príncipe** | Petroleum Law | State ownership | Limited production |
| **Guinea** | Mining Code | State ownership | Various |
| **Guinea-Bissau** | Petroleum Code | State ownership | Limited production |
| **Gambia** | Petroleum (Exploration and Production) Act | State ownership | Limited production |
| **Sierra Leone** | Petroleum (Exploration and Production) Act | State ownership | Limited production |
| **Liberia** | Petroleum (Exploration and Production) Act | State ownership | Limited production |
| **Burkina Faso** | Mining Code | State ownership | No O&G |
| **Mali** | Mining Code | State ownership | No O&G |
| **Niger** | Mining Code | State ownership | No O&G |
| **Chad** | Petroleum Code | State ownership | Limited production |
| **Central African Republic** | Mining Code | State ownership | No O&G |
| **Democratic Republic of Congo** | Mining Code | State ownership | Limited O&G |
| **Rwanda** | Mining Code | State ownership | No O&G |
| **Burundi** | Mining Code | State ownership | No O&G |
| **Uganda** | Petroleum Act 2013 | State ownership | Emerging |
| **Zambia** | Mines and Minerals Development Act | State ownership | No O&G |
| **Zimbabwe** | Mines and Minerals Act | State ownership | No O&G |
| **Malawi** | Mines and Minerals Act | State ownership | No O&G |
| **Mozambique** | Mining Law | State ownership | Limited O&G |
| **Namibia** | Minerals (Petroleum and Coal) Act | State ownership | Emerging O&G |
| **Botswana** | Mines and Minerals Act | State ownership | No O&G |
| **Lesotho** | Mines and Minerals Act | State ownership | No O&G |
| **Eswatini** | Mines and Minerals Act | State ownership | No O&G |
| **Suriname** | Mining Act | State ownership | Limited O&G |
| **French Guiana** | Overseas territory of France | French mining code | Limited |
| **Falkland Islands (Malvinas)** | Minerals Act | Crown ownership | Limited |
| **British Virgin Islands** | British Overseas Territory | Crown ownership | No O&G |
| **Cayman Islands** | British Overseas Territory | Crown ownership | No O&G |
| **Bermuda** | British Overseas Territory | Crown ownership | No O&G |
| **Turks and Caicos** | British Overseas Territory | Crown ownership | No O&G |
| **Gibraltar** | British Overseas Territory | Crown ownership | No O&G |
| **Anguilla** | British Overseas Territory | Crown ownership | No O&G |
| **Montserrat** | British Overseas Territory | Crown ownership | No O&G |
| **Pitcairn Islands** | British Overseas Territory | Crown ownership | No O&G |
| **St. Helena** | British Overseas Territory | Crown ownership | No O&G |
| **Norfolk Island** | Australian Territory | Australian mining law | No O&G |
| **Christmas Island** | Australian Territory | Australian mining law | No O&G |
| **Cocos (Keeling) Islands** | Australian Territory | Australian mining law | No O&G |
| **Northern Mariana Islands** | US Territory | US law applies | Minimal |
| **Guam** | US Territory | US law applies | Minimal |
| **American Samoa** | US Territory | US law applies | No O&G |
| **Puerto Rico** | US Territory | US law applies | Minimal |
| **US Virgin Islands** | US Territory | US law applies | No O&G |
| **Hong Kong** | SAR of China | Chinese law applies | No O&G |
| **Macau** | SAR of China | Chinese law applies | No O&G |
| **Taiwan** | De facto independent | ROC law | Limited |
| **Aruba** | Constituent of Netherlands | Dutch law applies | Limited |
| **Curaçao** | Constituent of Netherlands | Dutch law applies | Limited |
| **Sint Maarten** | Constituent of Netherlands | Dutch law applies | Limited |
| **Bonaire** | Special municipality of Netherlands | Dutch law applies | Limited |
| **Sint Eustatius** | Special municipality of Netherlands | Dutch law applies | Limited |
| **Saba** | Special municipality of Netherlands | Dutch law applies | Limited |
| **New Caledonia** | Special collectivity of France | French mining code | Limited |
| **French Polynesia** | Overseas country of France | French mining code | No O&G |
| **Wallis and Futuna** | Overseas collectivity of France | French mining code | No O&G |
| **Saint Pierre and Miquelon** | Overseas collectivity of France | French mining code | No O&G |
| **Réunion** | Overseas department of France | French mining code | No O&G |
| **Mayotte** | Overseas department of France | French mining code | No O&G |
| **Faroe Islands** | Autonomous territory of Denmark | Danish/Faroese law | Limited O&G |
| **Greenland** | Autonomous territory of Denmark | Danish/Greenlandic law | Limited O&G |
| **Åland Islands** | Autonomous region of Finland | Finnish law | No O&G |
| **Svalbard and Jan Mayen** | Territory of Norway | Norwegian law | Limited |
| **Cook Islands** | Free association with NZ | NZ law influence | No O&G |
| **Niue** | Free association with NZ | NZ law influence | No O&G |
| **Tokelau** | NZ territory | NZ law | No O&G |
| **Samoa** | Independent | Samoan law | No O&G |
| **Tonga** | Kingdom | Tongan law | No O&G |
| **Fiji** | Republic | Fijian law | No O&G |
| **Solomon Islands** | Independent | Solomon Islands law | No O&G |
| **Vanuatu** | Independent | Vanuatu law | No O&G |
| **Kiribati** | Republic | Kiribati law | No O&G |
| **Tuvalu** | Independent | Tuvaluan law | No O&G |
| **Nauru** | Republic | Nauruan law | No O&G |
| **Palau** | Republic | Palauan law | No O&G |
| **Marshall Islands** | Republic | Marshallese law | No O&G |
| **Micronesia** | Federated States | FSM law | No O&G |
| **Belarus** | Republic | Belarusian law | Limited |
| **Moldova** | Republic | Moldovan law | No O&G |
| **Luxembourg** | Grand Duchy | Luxembourg law | No O&G |
| **Monaco** | Principality | Monégasque law | No O&G |
| **Liechtenstein** | Principality | Liechtenstein law | No O&G |
| **Andorra** | Principality | Andorran law | No O&G |
| **San Marino** | Republic | Sammarinese law | No O&G |
| **Vatican City** | Holy See | Canon law | No O&G |
| **Malta** | Republic | Maltese law | Minimal |
| **Cyprus** | Republic | Cypriot law | Minimal |
| **Bahrain** | Kingdom | Bahraini law | Limited |
| **Qatar** | State | Qatari law | Limited |
| **Brunei** | Sultanate | Bruneian law | Limited |
| **East Timor** | Democratic Republic | Timorese law | Limited |
| **South Sudan** | Republic | South Sudanese law | Limited |
| **Eritrea** | State | Eritrean law | Limited |
| **Djibouti** | Republic | Djiboutian law | Limited |
| **Comoros** | Union | Comorian law | No O&G |
| **São Tomé and Príncipe** | Democratic Republic | STP law | No O&G |
| **Cabo Verde** | Republic | CV law | No O&G |
| **Guinea-Bissau** | Republic | GB law | No O&G |
| **Equatorial Guinea** | Republic | EG law | Limited |
| **Lesotho** | Kingdom | Lesothan law | No O&G |
| **Eswatini** | Kingdom | Eswatini law | No O&G |
| **Bhutan** | Kingdom | Bhutanese law | No O&G |
| **Brunei** | Sultanate | Bruneian law | Limited |
| **Laos** | People's Democratic Republic | Lao law | No O&G |
| **Cambodia** | Kingdom | Cambodian law | No O&G |
| **Bangladesh** | People's Republic | Bangladeshi law | Limited |
| **Sri Lanka** | Democratic Socialist Republic | Sri Lankan law | No O&G |
| **Nepal** | Federal Democratic Republic | Nepalese law | No O&G |
| **Maldives** | Republic | Maldivian law | No O&G |
| **Afghanistan** | Islamic Republic | Afghan law | No O&G |
| **Mongolia** | People's Republic | Mongolian law | Limited |
| **Kyrgyzstan** | Republic | Kyrgyz law | Limited |
| **Tajikistan** | Republic | Tajik law | No O&G |
| **Uzbekistan** | Republic | Uzbek law | Limited |
| **Turkmenistan** | Democratic Republic | Turkmen law | Limited |
| **Afghanistan** | Islamic Republic | Afghan law | No O&G |
| **Myanmar (Burma)** | Republic | Myanmar law | Limited |

---

## DOCUMENT CONTROL

| Field | Value |
|-------|-------|
| **Version** | 1.0 |
| **Agent** | Agent 1 — Data Source Mapping |
| **Date** | 2026-08-31 |
| **Status** | COMPLETE |
| **Next Agent** | Agent 2 — Well Documentation Methodology |
| **Pipeline** | GLOBAL_ORPHAN_WELL_PIPELINE |
| **License** | Dual License Agreement v4.9 |
| **Soul Code** | [425, 434, 266, 775] |

---

*This document is the foundational data source map for the 20-agent Global Orphan Well Pipeline. Every agent downstream should reference this document for data source identification, jurisdiction determination, and legal framework application.*
