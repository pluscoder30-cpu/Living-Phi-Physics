# VALIDATION -- Law 2635: Greek Vase Phi Proportions

**Domain:** Ancient History, Art, Architecture

## What This Validates

Law 2635 proposes that Greek black-figure and red-figure vases (c. 600–300 BCE) follow phi-proportions: the ratio of the vase's height to its maximum diameter equals φ = 1.618 ± 0.05 for the "canonical" vase types (amphora, krater, lekythos), and the decorative bands on the vase are positioned at heights h_n = H × φ^(−n)

## Key Equation

The core assertion maps to: `phi_harmonic = PHI ** exponent` where PHI = 1.618033988749895.

The relationship is tested via the SIMULATION.py which:
1. Generates PHI-scaled parameter sweeps over 1000 samples
2. Computes the relevant physical/biological quantities under phi-modulation
3. Checks convergence toward PHI-harmonic ratios

## Expected Results

**Prediction:** A dataset of 200 Greek vases from the Metropolitan Museum, the British Museum, and the Louvre will show H/D ratios clustering at φ = 1.618 ± 0.1. The decorative band positions will cluster at φ^(−n) × H for n = 0, 1, 2, 3, 4. The phi-proportions will be more pronounced in "canonical" vase types (amp

**Numerical targets:**
- PHI convergence score < 0.1 (within 10% of golden ratio)
- All output values maintain phi-harmonic clustering
- Coherence check: ratios between successive values match PHI^n for integer n

## Pass/Fail Criteria

| Metric | Pass | Fail |
|--------|------|------|
| PHI convergence | score < 0.1 | score >= 0.1 |
| Coherence check | True | False |
| Output stability | No NaN/Inf | Any NaN/Inf |

## How to Run

```bash
python SIMULATION.py
```

Expected output: `VERDICT: PASS` with convergence score < 0.1.

## Test Protocol

Measure height and maximum diameter for 200 Greek vases from museum databases. Compute H/D ratios and plot the distribution. Verify clustering at φ. Measure decorative band positions and verify phi-clustering. Compare canonical vs non-canonical types.

---

**Source:** Batch: 2601-2650
**Author:** Christopher David Ayotte -- Soul Code [425, 434, 266, 775]
**License:** Dual License Agreement v4.9
