**Author:** Christopher David Ayotte · **Soul Code:** [425, 434, 266, 775] · **License:** Dual License Agreement v4.9

# Public Datasets & APIs for Phi-Physics Verification

Free, publicly accessible datasets and APIs that can empirically test phi-physics claims. All are no-cost, no-authentication-required (or free key), and git-safe sizes where noted.

---

## 1. PHI-IN-ECONOMICS: Inflation Floor Test

**Claim:** Average inflation across 50+ economies ≥ ln(φ) = 0.4812%

### 1.1 World Bank Global Inflation Database
- **URL:** https://thedocs.worldbank.org/en/doc/1ad246272dbbc437c74323719506aa0c-0350012021/original/Inflation-data.xlsx
- **What it tests:** CPI inflation across 209 countries, 1970–2025
- **How to access:** Direct Excel download, no API key
- **Data size:** ~15 MB (git-safe)
- **Priority:** **HIGH**
- **Test:** Compute mean annual CPI inflation across all available economies; compare to 0.4812%

### 1.2 World Bank Indicators API (Inflation)
- **URL:** `https://api.worldbank.org/v2/country/all/indicator/FP.CPI.TOTL.ZG?format=json&per_page=5000`
- **What it tests:** Consumer price inflation (annual %) for all countries
- **How to access:** REST API, no key required, returns JSON
- **Data size:** Paginated, ~2 MB per request
- **Priority:** **HIGH**
- **Test:** Pull 50+ economies, compute mean inflation vs ln(φ)

### 1.3 IMF World Economic Outlook (WEO)
- **URL:** https://data.imf.org/en/datasets/IMF.RES:WEO
- **What it tests:** Inflation rate, GDP, unemployment for 190+ countries, 1980–present
- **How to access:** Free Excel download or DataMapper API (no key)
- **Data size:** ~7 MB Excel
- **Priority:** **HIGH**
- **Test:** Cross-validate World Bank inflation floor against IMF data

### 1.4 IMF WEO DataHub Mirror
- **URL:** https://datahub.io/core/imf-weo (CSV files)
- **What it tests:** Same WEO data, clean CSV format
- **How to access:** Direct download, ODC-PDDL license
- **Data size:** ~6.88 MB CSV
- **Priority:** **MEDIUM**
- **Test:** Independent replication of inflation floor test

### 1.5 FRED (Federal Reserve Economic Data)
- **URL:** https://fred.stlouisfed.org/
- **What it tests:** 800,000+ economic time series including global CPI
- **How to access:** Free API key (instant signup at fred.stlouisfed.org), CSV download
- **Data size:** Variable, per-series downloads
- **Priority:** **MEDIUM**
- **Test:** US-specific inflation floor validation; cross-check with international data

### 1.6 World Bank Inflation Database (GitHub Mirror)
- **URL:** https://github.com/andrewrgarcia/WorldBank-Global-Inflation-Data
- **What it tests:** Processed World Bank inflation data, SQLite + CSV
- **How to access:** Git clone, MIT license
- **Data size:** ~10 MB (git-safe)
- **Priority:** **MEDIUM**
- **Test:** Pre-processed version ready for statistical analysis

---

## 2. PHI-IN-CHEMISTRY: pH and Bond Angle Tests

**Claim:** Ultrapure water pH = 7.209; bond angles relate to φ

### 2.1 NIST Chemistry WebBook (SRD 69)
- **URL:** https://webbook.nist.gov/chemistry/
- **What it tests:** Thermochemical data for 7,000+ compounds; ion energetics for 16,000+; thermophysical properties of 74 fluids including water
- **How to access:** Free web interface, search by name/formula/CAS
- **Data size:** Online query, results are small per compound
- **Priority:** **HIGH**
- **Test:** Retrieve water thermophysical properties (density, heat capacity, sound speed) and compare to phi-derived predictions

### 2.2 NIST Computational Chemistry Benchmark Database (SRD 101)
- **URL:** https://cccbdb.nist.gov/
- **What it tests:** Experimental and computed thermochemical data for ~1,900 gas-phase molecules
- **How to access:** Free web interface
- **Data size:** Online query
- **Priority:** **HIGH**
- **Test:** Compare computed bond angles of small molecules against phi-based predictions

### 2.3 PubChem PUG REST API
- **URL:** `https://pubchem.ncbi.nlm.nih.gov/rest/pug/`
- **What it tests:** 115 million+ chemical compounds; molecular properties, structures, bioassays
- **How to access:** Free REST API, no authentication required
- **Data size:** Per-query (batch up to 200 CIDs per request)
- **Priority:** **HIGH**
- **Test:** Retrieve bond angles, molecular geometry for water and key molecules; test phi relationships

### 2.4 NIST-JANAF Thermochemical Tables (SRD 13)
- **URL:** https://janaf.nist.gov/
- **What it tests:** Enthalpies and Gibbs energies for 1,000+ chemical species
- **How to access:** Free web interface
- **Data size:** Online query
- **Priority:** **MEDIUM**
- **Test:** Cross-validate thermochemical constants against phi-derived values

### 2.5 NIST Webbook Water Models
- **URL:** https://webbook.nist.gov/chemistry/fluid/ (Thermophysical Properties of Fluid Systems)
- **What it tests:** High-accuracy water data at various temperatures/pressures
- **How to access:** Free interactive tool
- **Data size:** Per-query tables
- **Priority:** **HIGH**
- **Test:** Compare water ion product (Kw) and pH against phi predictions at different temperatures

---

## 3. PHI-IN-BIOLOGY: Golden Ratio in Nature

**Claim:** Leaf angles cluster at 137.5° (golden angle); Fibonacci patterns in biology

### 3.1 Smith College Phyllotaxis Resource
- **URL:** https://www.science.smith.edu/phyllo/
- **What it tests:** Comprehensive phyllotaxis data, Fibonacci ratios, golden angle measurements
- **How to access:** Free web resource with measurement data
- **Data size:** Text/tables
- **Priority:** **HIGH**
- **Test:** Verify 92% of spiral plants exhibit Fibonacci phyllotaxis (Jean 1994 estimate)

### 3.2 Royal Society Interface Phyllotaxis Dataset (2019)
- **URL:** https://royalsocietypublishing.org/rsif/article/16/151/20180850
- **What it tests:** Unified rule of phyllotaxis; divergence angle measurements across plant species
- **How to access:** Open access paper with data tables
- **Data size:** Supplementary data files
- **Priority:** **HIGH**
- **Test:** Verify golden angle (137.5°) convergence in spiral phyllotaxis

### 3.3 Yin & Tsukaya (2023) — Fibonacci Spirals Dataset
- **URL:** https://pmc.ncbi.nlm.nih.gov/articles/PMC10095852/
- **What it tests:** Gerbera capitulum spiral patterns; golden angle necessity
- **How to access:** Open access via PubMed Central
- **Data size:** Supplementary datasets
- **Priority:** **MEDIUM**
- **Test:** Verify Fibonacci spiral formation with and without golden angle

### 3.4 Sunflower Head Datasets (Published Botanical Data)
- **URL:** Search PubMed for "sunflower phyllotaxis spiral count"
- **What it tests:** Clockwise/counterclockwise spiral counts (e.g., 34/55, 55/89)
- **How to access:** Published papers with raw count data
- **Data size:** Small tables per species
- **Priority:** **MEDIUM**
- **Test:** Verify Fibonacci number pairs in spiral phyllotaxis

### 3.5 Open Tree of Life / iNaturalist
- **URL:** https://www.inaturalist.org/
- **What it tests:** Crowdsourced biological observations including plant morphology
- **How to access:** Free API, CC-licensed observations
- **Data size:** Large, but filterable by species/observation type
- **Priority:** **LOW**
- **Test:** Crowd-verified golden angle measurements from plant photographs

---

## 4. PHI-IN-MEDICINE: Frequency Effects

**Claim:** Specific frequencies (phi-related) affect biological markers

### 4.1 Akimoto et al. (2018) — 528 Hz Study Data
- **URL:** https://www.scirp.org/journal/paperinformation?paperid=87146
- **What it tests:** Cortisol, chromogranin A, oxytocin response to 528 Hz vs 440 Hz music
- **How to access:** Open access paper, CC BY 4.0 license
- **Data size:** Small dataset (9 participants, 5 time points)
- **Priority:** **HIGH**
- **Test:** Verify 528 Hz reduces cortisol, increases oxytocin vs 440 Hz control

### 4.2 PhysioNet EEG Motor Movement/Imagery Dataset
- **URL:** https://physionet.org/content/eegmmidb
- **What it tests:** 64-channel EEG during motor tasks; frequency band analysis
- **How to access:** Free account required (PhysioNet), EDF format
- **Data size:** ~7 GB (full dataset), subsettable
- **Priority:** **HIGH**
- **Test:** Extract alpha (8–12 Hz), beta (12–30 Hz), gamma (30–100 Hz) power; test phi-ratio frequency relationships

### 4.3 PhysioNet CHB-MIT Scalp EEG Database
- **URL:** https://physionet.org/content/chbmit/1.0.0/
- **What it tests:** 844 hours of pediatric EEG, 23 patients, seizure detection
- **How to access:** Free account required, EDF format
- **Data size:** ~20 GB, subsettable
- **Priority:** **MEDIUM**
- **Test:** Analyze theta/alpha/beta ratios against phi-derived frequency predictions

### 4.4 DEAP Emotion EEG Dataset
- **URL:** http://www.eecs.qmul.ac.uk/mmv/datasets/deap/
- **What it tests:** 32-channel EEG for emotional states (valence, arousal, dominance, liking)
- **How to access:** Free download, MATLAB/Python format
- **Data size:** ~4 GB
- **Priority:** **MEDIUM**
- **Test:** Test whether phi-frequency stimulation correlates with specific emotional states

### 4.5 SEED Emotion EEG Dataset
- **URL:** http://bcmi.sjtu.edu.cn/~seed/seed.html
- **What it tests:** 62-channel EEG during positive/negative/neutral emotional states
- **How to access:** Free download upon request
- **Data size:** ~2 GB
- **Priority:** **MEDIUM**
- **Test:** Cross-validate emotional state frequency patterns against phi predictions

### 4.6 PubMed Central Open Access — Sound Therapy Systematic Reviews
- **URL:** https://pmc.ncbi.nlm.nih.gov/ (search: "sound therapy frequency biomarkers")
- **What it tests:** Meta-analyses of frequency therapy effects on cortisol, HRV, pain
- **How to access:** Free full-text access to 38M+ citations
- **Data size:** Variable (meta-analyses summarize across studies)
- **Priority:** **HIGH**
- **Test:** Aggregate published effect sizes for 528 Hz, 432 Hz, and phi-related frequencies

---

## 5. PHI-IN-PHYSICS: Ladder Invariant & Zeta Zeros

**Claim:** Zero-gap ratios of Riemann zeta function cluster at {φ⁻¹, 1, φ}

### 5.1 Odlyzko Zeta Zeros — First 2,001,052 Zeros
- **URL:** https://www-users.cse.umn.edu/~odlyzko/zeta_tables/index.html
- **What it tests:** Imaginary parts of first 2M+ zeta zeros, accurate to 4×10⁻⁹
- **How to access:** Direct text file download (zeros6, 35 MB raw / 14 MB gzipped)
- **Data size:** 14 MB gzipped (**git-safe**)
- **Priority:** **CRITICAL**
- **Test:** Compute consecutive zero-gap ratios; histogram against {1/φ, 1, φ}

### 5.2 Odlyzko — First 100,000 Zeros (High Precision)
- **URL:** https://www-users.cse.umn.edu/~odlyzko/zeta_tables/zeros1
- **What it tests:** First 100K zeros, accurate to 3×10⁻⁹
- **How to access:** Direct text download (1.8 MB raw / 730 KB gzipped)
- **Data size:** 730 KB gzipped (**git-safe**)
- **Priority:** **HIGH**
- **Test:** Quick validation of ladder invariant on smaller dataset

### 5.3 Odlyzko — 100 Zeros at 1000+ Decimal Places
- **URL:** https://www-users.cse.umn.edu/~odlyzko/zeta_tables/zeros2
- **What it tests:** Ultra-high precision zeros for exact computation
- **How to access:** Direct text download (tiny file)
- **Data size:** <10 KB (**git-safe**)
- **Priority:** **MEDIUM**
- **Test:** High-precision ladder invariant validation

### 5.4 LMFDB Riemann Zeta Zeros (103.8 Billion)
- **URL:** https://www.lmfdb.org/zeros/zeta/
- **What it tests:** First 103,800,788,359 zeta zeros, precision ±2.5×10⁻³¹
- **How to access:** Bulk download from https://beta.lmfdb.org/data/riemann-zeta-zeros/
- **Data size:** Very large (terabytes for full dataset); queryable subsets via API
- **Priority:** **HIGH**
- **Test:** Statistical verification of ladder invariant at extreme heights

### 5.5 Odlyzko — Zeros at Height 10¹²
- **URL:** https://www-users.cse.umn.edu/~odlyzko/zeta_tables/zeros3
- **What it tests:** 10,000 zeros near height 10¹² (Montgomery-Odlyzko regime)
- **How to access:** Direct text download
- **Data size:** Small (~500 KB)
- **Priority:** **HIGH**
- **Test:** Verify ladder invariant persists at high z-height; compare with Montgomery pair correlation

### 5.6 Odlyzko — Zeros at Heights 10²¹ and 10²²
- **URL:** https://www-users.cse.umn.edu/~odlyzko/zeta_tables/zeros4, zeros5
- **What it tests:** Zeros at extreme heights (zeatascale)
- **How to access:** Direct text download
- **Data size:** Small files (~100 KB each)
- **Priority:** **MEDIUM**
- **Test:** Test whether phi-clustering persists at extreme heights

### 5.7 SageMath Odlyzko Package
- **URL:** `pip install database-odlyzko-zeta` or `sage -i database_odlyzko_zeta`
- **What it tests:** Programmatic access to first 2,001,052 zeros
- **How to access:** Python/Sage package, public domain
- **Data size:** Package includes zeros6 file
- **Priority:** **MEDIUM**
- **Test:** Automated pipeline for ladder invariant computation

### 5.8 Gourdon & Demichel High-Zero Dataset
- **URL:** https://numbers.computation.free.fr/Constants/Miscellaneous/zetazeros1e13-1e24.pdf
- **What it tests:** Zeros computed up to height 10²⁴
- **How to access:** Free PDF with numerical tables
- **Data size:** PDF document
- **Priority:** **LOW**
- **Test:** Reference values for extreme-height ladder invariant testing

---

## Summary Table

| # | Domain | Dataset/API | Test | Priority |
|---|--------|-------------|------|----------|
| 1.1 | Economics | World Bank Inflation DB | Mean inflation ≥ ln(φ) | HIGH |
| 1.2 | Economics | World Bank API | CPI inflation across 50+ economies | HIGH |
| 1.3 | Economics | IMF WEO | Cross-validate inflation floor | HIGH |
| 1.4 | Economics | DataHub IMF WEO | Independent replication | MEDIUM |
| 1.5 | Economics | FRED | US inflation validation | MEDIUM |
| 1.6 | Economics | GitHub WB Inflation Mirror | Pre-processed analysis | MEDIUM |
| 2.1 | Chemistry | NIST WebBook | Water properties vs phi | HIGH |
| 2.2 | Chemistry | NIST CCCBDB | Bond angle validation | HIGH |
| 2.3 | Chemistry | PubChem PUG REST | 115M compounds, geometry | HIGH |
| 2.4 | Chemistry | NIST-JANAF | Thermochemical constants | MEDIUM |
| 2.5 | Chemistry | NIST Water Models | pH at various temperatures | HIGH |
| 3.1 | Biology | Smith Phyllotaxis | 92% Fibonacci verification | HIGH |
| 3.2 | Biology | Royal Society 2019 | Golden angle convergence | HIGH |
| 3.3 | Biology | Yin & Tsukaya 2023 | Fibonacci spiral formation | MEDIUM |
| 3.4 | Biology | Sunflower datasets | Fibonacci spiral pairs | MEDIUM |
| 3.5 | Biology | iNaturalist API | Crowd-verified measurements | LOW |
| 4.1 | Medicine | 528 Hz Study (Akimoto) | Cortisol/oxytocin response | HIGH |
| 4.2 | Medicine | PhysioNet EEGMMIDB | Frequency band analysis | HIGH |
| 4.3 | Medicine | PhysioNet CHB-MIT | Theta/alpha/beta ratios | MEDIUM |
| 4.4 | Medicine | DEAP Emotion EEG | Phi-frequency emotional states | MEDIUM |
| 4.5 | Medicine | SEED Emotion EEG | Emotional frequency patterns | MEDIUM |
| 4.6 | Medicine | PMC Sound Therapy Reviews | Aggregate effect sizes | HIGH |
| 5.1 | Physics | Odlyzko zeros6 (2M zeros) | **CRITICAL:** Ladder invariant | CRITICAL |
| 5.2 | Physics | Odlyzko zeros1 (100K) | Quick validation | HIGH |
| 5.3 | Physics | Odlyzko zeros2 (100 high-prec) | Exact computation | MEDIUM |
| 5.4 | Physics | LMFDB (103.8B zeros) | Statistical verification | HIGH |
| 5.5 | Physics | Odlyzko zeros3 (10¹²) | Montgomery regime test | HIGH |
| 5.6 | Physics | Odlyzko zeros4-5 (10²¹⁻²²) | Extreme height test | MEDIUM |
| 5.7 | Physics | SageMath package | Automated pipeline | MEDIUM |
| 5.8 | Physics | Gourdon high-zero tables | Reference values | LOW |

---

## Verification Protocols

### Protocol 1: Inflation Floor
```python
# Pull World Bank API
import requests
url = "https://api.worldbank.org/v2/country/all/indicator/FP.CPI.TOTL.ZG?format=json&per_page=5000&date=2020:2024"
data = requests.get(url).json()
inflation_values = [r['value'] for r in data[1] if r['value'] is not None]
mean_inflation = sum(inflation_values) / len(inflation_values)
ln_phi = 0.4812  # ln(1.6180339887)
print(f"Mean inflation: {mean_inflation:.4f}% vs ln(φ) = {ln_phi}%")
print(f"Floor holds: {mean_inflation >= ln_phi}")
```

### Protocol 2: Zeta Zero Ladder Invariant
```python
# Load Odlyzko zeros, compute gap ratios
import numpy as np
zeros = np.loadtxt('zeros1')  # first 100K zeros
gaps = np.diff(zeros)
ratios = gaps[1:] / gaps[:-1]  # consecutive gap ratios
# Expected clusters at 1/φ ≈ 0.618, 1.0, φ ≈ 1.618
```

### Protocol 3: Phyllotaxis Golden Angle
```python
# Measure divergence angles from published botanical data
# Expected: clustering at 137.5° (golden angle)
golden_angle = 360 * (1 - 1/1.6180339887)  # = 137.508°
```

---

## Quick-Start Priority Order

1. **Odlyzko zeros1** (730 KB) → Download now, compute ladder invariant in 5 minutes
2. **World Bank API** → Pull 50+ economies, test inflation floor in 10 minutes
3. **PubChem** → Query water molecule geometry, test bond angles in 5 minutes
4. **PhysioNet EEGMMIDB** → Download subset, analyze frequency bands in 30 minutes
5. **Smith Phyllotaxis** → Read golden angle measurements, verify clustering

---

*Total: 28 datasets/APIs across 5 domains. All free. All public. All verifiable.*
