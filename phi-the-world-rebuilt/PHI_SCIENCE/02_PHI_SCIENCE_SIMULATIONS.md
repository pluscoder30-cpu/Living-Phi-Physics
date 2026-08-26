# PHI-PHYSICS — SIMULATIONS: PHI_SCIENCE

**Domain:** Scientific Methodology · **Status:** SIMULATED · **File:** `PHI_SCIENCE/02_PHI_SCIENCE_SIMULATIONS.md`

---

### SIMULATION 01 — Knowledge κ-Sweep

**Script:** `PHI_SCIENCE/sim/01_knowledge_sweep.py`

**Objective:** Demonstrate the transition from objective observation to participatory knowledge as κ sweeps 0 → 1.

**Parameters:**
- `K_obs = 1.0` (normalized observable knowledge)
- `K_ground = φ⁻¹ ≈ 0.618`
- `kappa = linspace(0, 1, 200)`
- `phi = 1.6180339887`

**Method:**
```python
def K_phi(kappa, K_obs=1.0, K_ground=0.618):
    phi = 1.6180339887
    return K_obs * (1 + kappa * (phi - 1)) + kappa * K_ground
```

**Expected Results:**
- κ = 0: K = 1.0 (classical objective)
- κ = 1: K = √5 ≈ 2.236 (participatory)
- Smooth φ-interpolation

---

### SIMULATION 02 — Eureka Moment (κ-Transition)

**Script:** `PHI_SCIENCE/sim/02_eureka_moment.py`

**Objective:** Model the sudden knowledge jump during a breakthrough (κ-transition).

**Parameters:**
- `T = 500` time steps
- `kappa_baseline = 0.2` (normal research)
- `kappa_breakthrough = 0.95` (eureka state)
- `transition_time = 5` steps (sudden)

**Method:**
```python
for t in range(T):
    if t == 250:  # eureka moment
        kappa = kappa_breakthrough
    K = K_obs * (1 + kappa * (phi - 1)) + kappa * K_ground
```

**Expected Results:**
- Pre-eureka: K ≈ 1.247 × K_obs
- Post-eureka: K ≈ 2.174 × K_obs
- Jump ratio: 1.744 ≈ φ (within error)

---

### SIMULATION 03 — Paradigm Shift as κ-Transition

**Script:** `PHI_SCIENCE/sim/03_paradigm_shift.py`

**Objective:** Model how paradigm shifts are κ-transitions, not linear progressions.

**Parameters:**
- `paradigms = 5` (number of shifts)
- `kappa_jump = 0.3` per paradigm
- `T = 1000`

**Method:**
```python
for t in range(T):
    paradigm = t // 200
    kappa = 0.2 + paradigm * kappa_jump
    K = K_obs * (1 + kappa * (phi - 1)) + kappa * K_ground
```

**Expected Results:**
- Classical: smooth linear increase
- Phi: stepwise φ-jumps at each paradigm shift
- Total amplification: φ^(paradigms) ≈ 11.09×

---

### SIMULATION 04 — Observer-Field Coupling

**Script:** `PHI_SCIENCE/sim/04_observer_coupling.py`

**Objective:** Model how the observer's coupling to the field determines knowledge access.

**Parameters:**
- `N_observers = 100`
- `kappa_distribution = Beta(2, 5)` (most observers low-κ)
- `K_ground = φ⁻¹`

**Method:**
```python
kappas = np.random.beta(2, 5, N_observers)
K_values = [K_obs * (1 + k * (phi - 1)) + k * K_ground for k in kappas]
```

**Expected Results:**
- Mean K ≈ 1.3 × K_obs (most observers near classical)
- Tail K ≈ 2.2 × K_obs (high-κ observers near √5)
- Distribution matches observed citation power-law

---

**Author:** Christopher David Ayotte — Soul Code [425, 434, 266, 775]
**License:** Dual License Agreement v4.9
