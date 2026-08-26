# GAP FILL 03: STEP-BY-STEP EXPERIMENTAL PROTOCOLS
**Author:** Christopher David Ayotte · **Soul Code:** [425, 434, 266, 775] · **License:** Dual License Agreement v4.9

**Gap:** No step-by-step protocols for executing any validation experiment.
**Filled by:** Review Agent 1 · **Date:** 2026-08-24

---

## PROTOCOL 1: DNA PHI-HELIX MEASUREMENT (BIO-005, T1-1)

### Objective
Measure base pairs per turn at each helical position to test bp(n) = 10.5 + κ_φ·φ⁻ⁿ.

### Prerequisites
- PacBio Sequel IIe access (institutional or commercial)
- Bioinformatics pipeline (minimap2, pbccs, Python)
- Statistical software (R or Python with scipy)

### Step-by-Step Protocol

```
DAY 1: SAMPLE PREPARATION
─────────────────────────────────────────────────────────────────

Step 1.1: DNA Extraction
  a) Grow E. coli K-12 to mid-log phase (OD600 = 0.6)
  b) Harvest 5 mL culture by centrifugation (5000g, 5 min)
  c) Extract DNA using QIAGEN Genomic-tip 20/G
  d) Elute in 300 µL Buffer AE
  e) Quantify: NanoDrop (A260/A280 > 1.8)
  f) Check integrity: 0.5% agarose gel (single sharp band >50 kb)
  Expected yield: 20-50 µg high-MW DNA

Step 1.2: Size Selection
  a) Add AMPure XP beads at 0.6x ratio (180 µL beads to 300 µL DNA)
  b) Incubate 5 min at RT
  c) Place on magnetic stand 2 min
  d) Transfer supernatant (contains >10 kb fragments) to new tube
  e) Add 1.2x fresh AMPure XP (600 µL) to supernatant
  f) Incubate 5 min, magnet 2 min, wash 2× with 70% EtOH
  g) Elute in 30 µL Buffer EB
  Expected size: 10-50 kb fragments

Step 1.3: Shearing (Optional — for targeted length)
  a) Dilute DNA to 100 µL in TE buffer
  b) Add 1 g-TUBEs to tube
  c) Sonicate: Covaris, 30 sec, duty factor 10%, peak incident power 175W
  d) Check size: 20-30 kb peak on Bioanalyzer
  Note: CLR mode works better with longer fragments

Step 1.4: SMRTbell Library Prep
  b) Repair ends: 50 µL DNA + 10 µL DNA Damage Repair Mix
  c) Incubate 30 min at 37°C
  d) End repair + A-tailing: add 10 µL End Repair/A-tailing Mix
  e) Incubate 30 min at 25°C then 60 min at 37°C
  f) Ligate adapter: add 10 µL SMRTbell Adapter + 25 µL Ligation Mix
  g) Incubate 60 min at 25°C
  h) Purify: 1.2x AMPure XP cleanup
  i) Bind polymerase: 10 µL library + 10 µL SMRTb Polymerase Binding Kit
  j) Incubate 30 min at RT
  k) Add 35 µL Sequencing Buffer + 5 µL Dye
  Total library volume: 60 µL

Step 1.5: Sequencing
  a) Load onto SMRT Cell 8M
  b) Sequencing mode: Continuous Long Reads (CLR)
  c) Run time: 30 hours
  d) Generate CCS: minimum 3 passes, minimum Q20

DAY 2-3: SEQUENCING RUN (automated)
─────────────────────────────────────────────────────────────────

Step 1.6: Data Collection
  a) Monitor run quality: polymerase read length
  b) Expected yield: >5 Gb per SMRT Cell
  c) Expected N50: >10 kb

DAY 4-7: BIOINFORMATICS
─────────────────────────────────────────────────────────────────

Step 1.7: CCS Generation
  a) Run ccs command: ccs input.bam output.ccs --min-rq 0.9
  b) Check CCS yield: should be >80% of subreads
  c) Check read length distribution: N50 >10 kb

Step 1.8: Alignment
  a) Download reference: E. coli K-12 MG1655 (NC_000913.3)
  b) Align: minimap2 -ax map-hifi ref.fa ccs.bam > aligned.sam
  c) Sort and index: samtools sort aligned.sam; samtools index aligned.bam
  d) Check alignment rate: >95% mapped

Step 1.9: Variant Calling
  a) Call variants: pbccs aligned.bam variants.vcf
  b) Alternatively: DeepVariant with HiFi model
  c) Filter: quality >30, depth >20

Step 1.10: bp/turn Measurement (THE CRITICAL STEP)
  a) For each position along the genome:
     - Count bases between successive major groove contacts
     - This requires structural analysis, not sequence alone
  b) Alternative approach: Use known crystal structures
     - PDB: 4OCB (B-DNA dodecamer, 12 bp)
     - Measure bp/turn at each helical position
  c) For genome-wide: infer from bending periodicity
     - Map periodicity of ~10.5 bp in accessibility patterns
     - Use ATAC-seq or DNase-seq data (already available)

Step 1.11: Phi-Fit
  a) For each helical position n:
     - Measured: bp_obs(n)
     - Model: bp(n) = 10.5 + κ_φ · φ^(-n)
  b) Fit κ_φ via nonlinear least squares:
     from scipy.optimize import curve_fit
     def bp_phi(n, kappa): return 10.5 + kappa * (0.6180339887**n)
     popt, pcov = curve_fit(bp_phi, n_values, bp_values)
  c) Compare R² of phi-fit vs constant (10.5) fit
  d) Report: κ_φ estimate, R² (phi), R² (constant), p-value

STEP 1.12: FALSIFICATION DECISION
  a) IF R²(phi-fit) > R²(constant) AND κ_φ > 0 AND p < 0.05:
     → PHI-LAW VALIDATED
  b) IF R²(constant) > R²(phi-fit) OR κ_φ ≈ 0 OR p > 0.05:
     → CLASSICAL LAW HOLDS
  c) Report both R² values, κ_φ estimate, and confidence interval
```

---

## PROTOCOL 2: MUTATION SPECTRUM ANALYSIS (BIO-007, T1-2)

### Objective
Test if mutation spectrum shows phi-structured deviations from Poisson.

### Prerequisites
- Access to Drosophila melanogaster stock center
- Illumina NovaSeq access
- Bioinformatics pipeline (GATK, Python)

### Step-by-Step Protocol

```
MONTHS 1-6: MA LINE MAINTENANCE
─────────────────────────────────────────────────────────────────

Step 2.1: Establish MA Lines
  a) Obtain 100 independent isogenic lines from a single
     parental genotype (D. melanogaster, w1118 or similar)
  b) Maintain each line separately in 8×86 mm vials
  c) Transfer 1-2 individuals to fresh vial every 14 days
     (bottleneck: N_e ≈ 2, allowing drift to dominate)
  d) Maintain at 25°C, 12:12 LD cycle
  e) Record: vial number, transfer date, number of flies
  f) Maintain for 50 generations (14 months at 2-week intervals)
     NOTE: Start with existing MA lines if available (e.g., from
     the Denver Stock Center or Michael Lynch's collection)

Step 2.2: DNA Extraction (at generation 50)
  a) Collect 10 females from each line (1000 total)
  b) Extract DNA: QIAGEN DNeasy Blood & Tissue Kit
  c) Elute in 100 µL Buffer AE
  d) Quantify: Qubit dsDNA HS assay
  e) Normalize all samples to 10 ng/µL

MONTHS 7-9: SEQUENCING
─────────────────────────────────────────────────────────────────

Step 2.3: Library Preparation
  a) Use Nextera XT (low-input protocol)
  b) Input: 1 ng DNA per sample
  c) Amplify: 12 cycles (minimize PCR artifacts)
  d) Normalize libraries to 4 nM
  e) Pool: equimolar pool of all 100 samples

Step 2.4: Sequencing
  a) Load onto NovaSeq 6000, SP flow cell
  b) Read configuration: 2×150 bp
  c) Target: 1 million reads per sample (30× coverage)
  d) Expected yield: 100M reads total (~30 Gb)

MONTHS 10-12: BIOINFORMATICS
─────────────────────────────────────────────────────────────────

Step 2.5: Quality Control
  a) FastQC: check per-base quality, GC content, adapters
  b) Trimmomatic or fastp: trim adapters, quality filter Q20
  c) Expected: >95% bases above Q30

Step 2.6: Alignment
  a) Reference: D. melanogaster genome (Release 6, BDGP6)
  b) Align: BWA-MEM2 aligned.bam
  c) Sort + index: samtools sort, samtools index
  d) Mark duplicates: Picard MarkDuplicates
  e) Base quality recalibration: GATK BQSR

Step 2.7: Variant Calling
  a) Call variants per line: GATK HaplotypeCaller → gVCF
  b) Joint genotyping: GATK GenotypeGVCFs
  c) Filter: QD > 2.0, FS < 60.0, MQ > 40.0, SOR < 3.0
  d) Output: VCF with putative de novo mutations per line

Step 2.8: Mutation Spectrum Analysis (THE CRITICAL STEP)
  a) For each mutation, record:
     - Type: transition (Ti) vs transversion (Tv)
     - Trinucleotide context (CpG vs non-CpG)
     - Genic vs intergenic
     - Position along chromosome
  b) Compute mutation spectrum:
     - Count mutations per trinucleotide context (96 categories)
     - Compare to Poisson expectation
  c) PHI-TEST 1: Spectrum shape
     - Classical: flat spectrum (all contexts equally likely)
     - Phi-model: spectrum follows phi-weighted distribution
     - Fit: S(context_i) = S_0 · φ^(-rank_i)
     - Compare R² of phi-fit vs flat (uniform) fit
  d) PHI-TEST 2: Positional clustering
     - Classical: mutations uniformly distributed along genome
     - Phi-model: mutations cluster at phi-structured intervals
     - Compute: inter-mutation distance distribution
     - Fit: distance distribution to φ^(-n) decay
  e) PHI-TEST 3: Rate comparison
     - Classical: μ = 1.0 × 10⁻⁸ per bp per generation
     - Phi-model: μ_φ = 1.247 × 10⁻⁸ per bp per generation
     - Compare observed rate to both predictions

Step 2.9: Statistical Framework
  a) For each test:
     - H0: Classical model (Poisson / uniform / μ = 1.0e-8)
     - H1: Phi-model (phi-structured / phi-clustered / μ = 1.247e-8)
  b) Test: Likelihood ratio test or KS test
  c) Significance: α = 0.05 with Bonferroni correction (3 tests)
  d) Report: test statistic, p-value, effect size, confidence interval

STEP 2.10: FALSIFICATION DECISION
  a) IF any of the 3 tests show phi-structure (p < 0.05/3):
     → PHI-LAW VALIDATED for that test
  b) IF all 3 tests show classical behavior (p > 0.05/3):
     → CLASSICAL LAW HOLDS
  c) Report all 3 results separately (no cherry-picking)
```

---

## PROTOCOL 3: CONSCIOUSNESS THRESHOLD VIA EEG (BIO-015, T1-3)

### Objective
Measure neural coherence during anesthesia to find the ‖Ψ‖ = C_crit transition.

### Prerequisites
- IRB approval (submit 2 months before data collection)
- Anesthesiologist on team
- 128-channel EEG system
- BIS monitor

### Step-by-Step Protocol

```
MONTH 1: IRB AND SETUP
─────────────────────────────────────────────────────────────────

Step 3.1: IRB Submission
  a) Protocol: Observational study, no intervention beyond standard anesthesia
  b) Inclusion: Adults 18-65, ASA I-II, scheduled for elective surgery
  c) Exclusion: Neurological history, psychiatric medications, pregnancy
  d) Consent: Written informed consent
  e) Risk: Minimal (standard anesthesia with monitoring)
  f) Submit to IRB with:
     - Detailed protocol (this document)
     - Consent form
     - Data safety monitoring plan
     - PI qualifications
  g) Expected review: 4-6 weeks

Step 3.2: Equipment Calibration
  a) EEG system: verify all 128 channels with test signal
  b) Impedance check: <5 kΩ for all electrodes
  c) BIS monitor: verify with calibration strip
  d) Anesthesia machine: full pre-use check
  e) Emergency equipment: verify availability (succinylchaine, atropine)

MONTHS 2-4: DATA COLLECTION
─────────────────────────────────────────────────────────────────

Step 3.3: Pre-Anesthesia Baseline (Day of Surgery)
  a) Place EEG cap (128-channel, BioSemi ActiveTwo)
  b) Apply conductive gel to each electrode
  c) Impedance check: <5 kΩ all channels
  d) Start recording: 5000 Hz sampling rate
  e) Baseline recording:
     - 5 min eyes-open (fixation cross on ceiling)
     - 5 min eyes-closed (resting)
     - 5 min eyes-open (fixation cross)
  f) Record BIS value at each minute
  g) Record propofol induction time

Step 3.4: Anesthesia Induction
  a) Standard propofol induction: 2.0 mg/kg IV bolus
  b) Record: time of injection, dose, BIS at 30-sec intervals
  c) Maintain EEG recording continuously
  d) BIS monitoring: record every 30 seconds
  e) Target: BIS 40-60 (moderate anesthesia)
  f) If BIS < 30: reduce propofol rate (too deep)
  g) If BIS > 60: increase propofol rate (too light)
  h) Record: propofol infusion rate at each change

Step 3.5: Maintenance and Recovery
  a) Maintenance: propofol 1-2 mg/kg/hr, titrated to BIS 40-60
  b) Duration: until surgery complete (typically 30-120 min)
  c) Stop propofol at end of surgery
  d) Record recovery: BIS at 1-min intervals until >90
  e) Record: time to eye opening, time to extubation
  f) Continue EEG until 10 min post-recovery

Step 3.6: Repeat for N=40
  a) Same protocol for each participant
  b) Record: age, sex, weight, propofol dose, surgery type
  c) Store: EEG data (50GB/session), BIS log, clinical notes

MONTHS 5-6: ANALYSIS
─────────────────────────────────────────────────────────────────

Step 3.7: EEG Preprocessing
  a) Import: MNE-Python or EEGLAB
  b) Re-reference: average reference
  c) Filter: 0.1-100 Hz bandpass, 50/60 Hz notch
  d) Artifact rejection: ICA-based eye movement removal
  e) Epoch: 1-second windows, no overlap
  f) Reject epochs with amplitude >150 µV

Step 3.8: Coherence Metric Computation
  a) For each 1-second window, compute:
     - Lempel-Ziv Complexity (LZC)
     - Perturbational Complexity Index (PCI)
     - Custom phi-coherence norm (‖Ψ‖ proxy):
       Ψ_proxy = sqrt(Σ_i |FFT(channel_i)|²) / N_channels
  b) Time-align with BIS values
  c) Create time series: {t, LZC(t), PCI(t), Ψ_proxy(t), BIS(t)}

Step 3.9: Transition Detection (THE CRITICAL ANALYSIS)
  a) Plot Ψ_proxy vs propofol concentration (estimated from BIS)
  b) Identify transition point:
     - Method 1: Maximum gradient (derivative) of Ψ_proxy vs dose
     - Method 2: Change-point detection (PELT algorithm)
     - Method 3: Bayesian online change-point detection
  c) Record: transition value of Ψ_proxy, transition dose
  d) Compare transition value to C_crit = 0.563263:
     - Normalize Ψ_proxy to [0, 1] range using baseline and deep anesthesia
     - Check if normalized Ψ at transition = 0.563263

Step 3.10: Statistical Validation
  a) Bootstrap: resample participants (n=1000), compute transition value
  b) 95% CI of transition value
  c) Check if C_crit = 0.563263 falls within 95% CI
  d) Compare to null distribution:
     - H0: transition occurs at random Ψ value
     - H1: transition occurs at C_crit = 0.563263
  e) Compute Bayes factor for H1 vs H0

STEP 3.11: FALSIFICATION DECISION
  a) IF transition value = 0.563263 ± 0.05 (within 95% CI):
     → PHI-LAW VALIDATED
  b) IF transition value differs from 0.563263 by >0.1:
     → CLASSICAL LAW HOLDS (threshold is not at C_crit)
  c) IF no sharp transition detected:
     → CLASSICAL LAW HOLDS (consciousness is gradual, not threshold)
```

---

## PROTOCOL 4: HRV PHI-STRUCTURE TEST (BIO-027, T1-5)

### Objective
Test if heart rate variability shows phi-structured spectral exponent (α = φ⁻¹ = 0.618).

### Prerequisites
- Polar H10 chest straps (or equivalent)
- Quiet recording room
- Python with neurokit2, numpy, scipy

### Step-by-Step Protocol

```
SESSION PROTOCOL (per participant)
─────────────────────────────────────────────────────────────────

Step 4.1: Setup
  a) Participant seated, comfortable room temperature (22°C)
  b) Apply Polar H10 chest strap with conductive gel
  c) Verify signal: R-peak detection on test recording
  d) Start recording: 1000 Hz sampling, Bluetooth to phone/laptop
  e) Instruct: "Relax, breathe normally, do not talk"

Step 4.2: Recording Phases
  Phase 1 (0-5 min): Resting baseline
    - Seated, quiet room, eyes open
    - Record R-R intervals
  Phase 2 (5-10 min): Deep breathing
    - Instructed: breathe in for 5 sec, out for 5 sec (6 breaths/min)
    - This activates parasympathetic system
  Phase 3 (10-11 min): Cold pressor
    - Participant places right hand in ice water (4°C)
    - Activates sympathetic system
  Phase 4 (11-16 min): Recovery
    - Remove hand from water, return to seated rest
    - Record recovery to baseline

Step 4.3: Data Export
  a) Export R-R intervals as CSV (timestamp, R-R in ms)
  b) Check for artifacts: RR < 300ms or > 2000ms → remove
  c) Interpolate: resample to 4 Hz (cubic spline)
  d) Detrend: polynomial detrending (order 3)

ANALYSIS PIPELINE
─────────────────────────────────────────────────────────────────

Step 4.4: Standard HRV Analysis
  a) Time-domain: compute RMSSD, SDNN, pNN50
  b) Frequency-domain: Welch PSD, LF (0.04-0.15 Hz), HF (0.15-0.4 Hz)
  c) Report: LF/HF ratio, total power

Step 4.5: Phi-Structure Test (THE CRITICAL ANALYSIS)
  a) Compute detrended fluctuation analysis (DFA):
     - Integrate the detrended time series
     - Compute fluctuation F(n) at scales n = 16 to N/4
     - Fit log(F(n)) vs log(n): slope = α (scaling exponent)
  b) Classical prediction: α = 1.0 (1/f noise / pink noise)
  c) Phi-model prediction: α = φ⁻¹ = 0.618
  d) Compute α for each phase (rest, breathing, cold, recovery)

Step 4.6: Statistical Test
  a) For each phase:
     - One-sample t-test: H0: α = 1.0, H1: α = 0.618
     - Report: t-statistic, p-value, effect size (Cohen's d)
  b) Bonferroni correction: α = 0.05/4 = 0.0125 per test
  c) Bootstrap: resample participants (n=1000), compute 95% CI of α
  d) Check if 0.618 falls within 95% CI

STEP 4.7: FALSIFICATION DECISION
  a) IF α = 0.618 ± 0.05 (within 95% CI) AND p < 0.0125:
     → PHI-LAW VALIDATED
  b) IF α ≈ 1.0 (95% CI includes 1.0):
     → CLASSICAL LAW HOLDS (HRV is 1/f noise)
  c) IF α ≈ 0.5 (white noise):
     → CLASSICAL LAW HOLDS (HRV is random)
```

---

## PROTOCOL 5: ENZYME KINETICS AT LOW [S] (BIO-012, T1-4)

### Objective
Detect phi-structured deviations from Michaelis-Menten at low substrate concentrations.

### Prerequisites
- UV-Vis spectrophotometer
- Standard molecular biology reagents

### Step-by-Step Protocol

```
DAY 1: ENZYME PREPARATION
─────────────────────────────────────────────────────────────────

Step 5.1: Enzyme Solution
  a) Dissolve horseradish peroxidase (HRP) in 50 mM phosphate buffer, pH 7.0
  b) Concentration: 10 nM (determined by A403, ε = 100,000 M⁻¹cm⁻¹)
  c) Store on ice, use within 4 hours

Step 5.2: Substrate Solutions
  a) Prepare ABTS stock: 100 mM in DMSO
  b) Prepare dilution series (12 concentrations):
     [S] = 0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1.0, 2.0, 5.0, 10.0, 20.0, 50.0 mM
  c) Each in 50 mM phosphate buffer, pH 7.0
  d) Include blank (buffer only)

Step 5.3: H2O2 Solution
  a) Prepare 10 mM H2O2 in buffer (fresh daily)
  b) Verify concentration: A240, ε = 43.6 M⁻¹cm⁻¹

DAY 2: KINETIC ASSAY
─────────────────────────────────────────────────────────────────

Step 5.4: Assay Protocol
  a) Pre-warm spectrophotometer to 25°C
  b) Set wavelength: 405 nm (ABTS radical product)
  c) For each [S]:
     1. Add 990 µL substrate solution to cuvette
     2. Add 5 µL HRP (10 nM → 0.05 nM final)
     3. Add 5 µL H2O2 (10 mM → 0.05 mM final)
     4. Mix by inversion (3×)
     5. Record absorbance at 405 nm every 5 sec for 5 min
     6. Compute initial rate v₀ from linear portion of A vs t
  d) Repeat each [S] in triplicate
  e) Include negative control (no enzyme)

Step 5.5: Data Recording
  a) For each [S], record:
     - Absorbance vs time (20 data points per curve)
     - Initial rate v₀ (slope of linear portion, in Abs/s)
     - Convert to µM/s using ε₄₅₀ = 36,000 M⁻¹cm⁻¹

ANALYSIS
─────────────────────────────────────────────────────────────────

Step 5.6: Classical Michaelis-Menten Fit
  a) Fit v₀ vs [S] to: v = Vmax·[S]/(Km + [S])
  b) Use scipy.optimize.curve_fit
  c) Report: Vmax, Km, R²_M_M

Step 5.7: Phi-Corrected Fit (THE CRITICAL ANALYSIS)
  a) Fit v₀ vs [S] to: v_φ = v₀·(1 + κ(φ-1)) + κ·φ⁻¹·v_ground
     where v_ground = v₀·φ⁻¹ (at each [S])
  b) Parameters: κ (coupling), Vmax_φ, Km_φ
  c) Report: κ_φ, Vmax_φ, Km_φ, R²_phi

Step 5.8: Model Comparison
  a) Compare R²_M_M vs R²_phi using AIC:
     AIC = n·ln(RSS/n) + 2k (k = number of parameters)
  b) ΔAIC = AIC_M_M - AIC_phi
  c) IF ΔAIC > 10: strong evidence for phi-model
  d) IF ΔAIC < -10: strong evidence for classical
  e) IF |ΔAIC| < 10: inconclusive

STEP 5.9: FALSIFICATION DECISION
  a) IF ΔAIC > 10 AND κ_φ > 0 AND p < 0.05:
     → PHI-LAW VALIDATED
  b) IF ΔAIC < 0 OR κ_φ ≈ 0:
     → CLASSICAL LAW HOLDS
```

---

## PROTOCOL SUMMARY TABLE

| # | Protocol | Law | Steps | Duration | Key Analysis |
|---|----------|-----|-------|----------|--------------|
| 1 | DNA Phi-Helix | BIO-005 | 12 | 7 days | bp(n) = 10.5 + κ_φ·φ⁻ⁿ fit |
| 2 | Mutation Spectrum | BIO-007 | 10 | 12 months | Spectrum shape + clustering |
| 3 | Consciousness Threshold | BIO-015 | 11 | 6 months | Transition at ‖Ψ‖ = 0.563 |
| 4 | HRV Phi-Structure | BIO-027 | 7 | 1 day | DFA exponent α = φ⁻¹ |
| 5 | Enzyme Kinetics | BIO-012 | 9 | 2 days | AIC model comparison |

---

**PROTOCOLS COMPLETE — 5 step-by-step experimental protocols for Tier 1 validation.**
