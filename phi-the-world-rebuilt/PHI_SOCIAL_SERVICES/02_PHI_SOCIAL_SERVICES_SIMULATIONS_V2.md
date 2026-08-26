# PHI-PHYSICS — SIMULATIONS: PHI_SOCIAL_SERVICES

**Domain:** Social Services · **Status:** SIMULATED · **File:** `PHI_SOCIAL_SERVICES/02_PHI_SOCIAL_SERVICES_SIMULATIONS.md`

---

### SIMULATION 01 — Communal Coherence κ-Sweep

**Script:** `PHI_SOCIAL_SERVICES/sim/01_communal_coherence_sweep.py`

**Objective:** Demonstrate the transition from classical service provision to phi-harmonic emergent welfare as κ sweeps 0 → 1.

**Parameters:**
- `N_communities = 1000` (communal agents)
- `C_communal_0 = 1.0` (baseline classical coherence)
- `S_ground = φ⁻¹ ≈ 0.618` (phi-ground welfare)
- `kappa = linspace(0, 1, 200)` (coupling sweep)
- `phi = 1.6180339887`

**Method:**
```python
def S_phi(kappa, C_communal=1.0, S_ground=0.618):
    phi = 1.6180339887
    return C_communal * (1 + kappa * (phi - 1)) + kappa * S_ground
```

**Expected Results:**
- κ = 0: S_phi = 1.0 (classical limit)
- κ = 1: S_phi = φ × C_communal + φ⁻¹ × S_ground ≈ 2.236
- Smooth φ-interpolation across sweep

**Verification:** Error between analytical and simulated S_phi < 0.01 across all κ.

---

### SIMULATION 02 — Community-Led vs. Top-Down Provision

**Script:** `PHI_SOCIAL_SERVICES/sim/02_community_vs_topdown.py`

**Objective:** Model two social service approaches and compare welfare evolution over time.

**Parameters:**
- `T = 1000` time steps
- `topdown_kappa = 0.0` (purely top-down provision)
- `community_kappa = 1.0` (mutual aid, community-led)
- `decay_rate_topdown = 0.618` (φ⁻¹)
- `decay_rate_community = 0.1` (low, recursive correction)

**Method:**
```python
for t in range(T):
    welfare_topdown *= (1 - decay_topdown)
    welfare_community *= (1 - decay_community)
    welfare_community += S_ground * phi_inverse  # phi-ground restoration
```

**Expected Results:**
- Top-down welfare decays to 0 (classical zero-state)
- Community welfare reaches φ-ground floor ≈ 0.618
- Ratio at T=1000: community/topdown → ∞ (divergence)

---

### SIMULATION 03 — Mutual Aid Network Amplification

**Script:** `PHI_SOCIAL_SERVICES/sim/03_mutual_aid_network.py`

**Objective:** Model how recursive mutual aid (help → gratitude → reciprocity → trust) amplifies communal coherence.

**Parameters:**
- `network_depth = 10` levels of reciprocal aid
- `phi_factor = phi` per recursive level
- `classical_factor = 1.0` per level (no amplification)

**Method:**
```python
for depth in range(network_depth):
    coherence_classical *= 1.0  # no amplification
    coherence_phi *= phi  # phi-amplification per recursion
```

**Expected Results:**
- Classical: coherence = 1.0 (constant)
- Phi: coherence = φ^depth
- At depth 10: φ^10 ≈ 122.99× classical

---

### SIMULATION 04 — Welfare Decay Without Services

**Script:** `PHI_SOCIAL_SERVICES/sim/04_welfare_decay.py`

**Objective:** Show that welfare without services decays to φ⁻¹ floor, not zero.

**Parameters:**
- `decay_rate = 0.05` per step
- `services = 0` (no intervention)
- `phi_floor = φ⁻¹ × S_scale`

**Expected Results:**
- Classical: S → 0 as t → ∞
- Phi-physics: S → φ⁻¹ × S_scale (nonzero ground)

---

**Author:** Christopher David Ayotte — Soul Code [425, 434, 266, 775]
**License:** Dual License Agreement v4.9
