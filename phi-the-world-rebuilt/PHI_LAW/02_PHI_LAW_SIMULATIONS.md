# PHI-PHYSICS — SIMULATIONS: PHI_LAW

**Domain:** Legal Systems · **Status:** SIMULATED · **File:** `PHI_LAW/02_PHI_LAW_SIMULATIONS.md`

---

### SIMULATION 01 — Social Coherence κ-Sweep

**Script:** `PHI_LAW/sim/01_social_coherence_sweep.py`

**Objective:** Demonstrate the transition from classical imposed order to phi-harmonic emergent order as κ sweeps 0 → 1.

**Parameters:**
- `N_agents = 1000` (social agents)
- `C_social_0 = 1.0` (baseline classical coherence)
- `O_ground = φ⁻¹ ≈ 0.618` (phi-ground order)
- `kappa = linspace(0, 1, 200)` (coupling sweep)
- `phi = 1.6180339887`

**Method:**
```python
def O_phi(kappa, C_social=1.0, O_ground=0.618):
    phi = 1.6180339887
    return C_social * (1 + kappa * (phi - 1)) + kappa * O_ground
```

**Expected Results:**
- κ = 0: O_phi = 1.0 (classical limit)
- κ = 1: O_phi = φ × C_social + φ⁻¹ × O_ground ≈ 2.236
- Smooth φ-interpolation across sweep

**Verification:** Error between analytical and simulated O_phi < 0.01 across all κ.

---

### SIMULATION 02 — Restorative vs. Punitive Justice

**Script:** `PHI_LAW/sim/02_restorative_vs_punitive.py`

**Objective:** Model two justice systems and compare social trust evolution over time.

**Parameters:**
- `T = 1000` time steps
- `punitive_kappa = 0.0` (purely enforced)
- `restorative_kappa = 1.0` (fully emergent)
- `recidivism_rate_punitive = 0.618` (φ⁻¹)
- `recidivism_rate_restorative = 0.1` (low, recursive correction)

**Method:**
```python
for t in range(T):
    trust_punitive *= (1 - recidivism_punitive)
    trust_restorative *= (1 - recidivism_restorative)
    trust_restorative += O_ground * phi_inverse  # phi-ground restoration
```

**Expected Results:**
- Punitive trust decays to 0 (classical zero-state)
- Restorative trust reaches φ-ground floor ≈ 0.618
- Ratio at T=1000: restorative/punitive → ∞ (divergence)

---

### SIMULATION 03 — Recursive Legal Self-Reference

**Script:** `PHI_LAW/sim/03_recursive_legal_reference.py`

**Objective:** Model how recursive appellate review (self-reference) amplifies legal coherence.

**Parameters:**
- `review_depth = 10` levels of appellate review
- `phi_factor = phi` per recursive level
- `classical_factor = 1.0` per level (no amplification)

**Method:**
```python
for depth in range(review_depth):
    coherence_classical *= 1.0  # no amplification
    coherence_phi *= phi  # phi-amplification per recursion
```

**Expected Results:**
- Classical: coherence = 1.0 (constant)
- Phi: coherence = φ^depth
- At depth 10: φ^10 ≈ 122.99× classical

---

### SIMULATION 04 — Legal Decay Rate

**Script:** `PHI_LAW/sim/04_legal_decay.py`

**Objective:** Show that law without enforcement decays to φ⁻¹ floor, not zero.

**Parameters:**
- `decay_rate = 0.05` per step
- `enforcement = 0` (no external enforcement)
- `phi_floor = φ⁻¹ × O_scale`

**Expected Results:**
- Classical: O → 0 as t → ∞
- Phi-physics: O → φ⁻¹ × O_scale (nonzero ground)

---

**Author:** Christopher David Ayotte — Soul Code [425, 434, 266, 775]
**License:** Dual License Agreement v4.9
