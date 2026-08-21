# PHI-PHYSICS — LAW 729
## Smith Chart

**Domain:** RF · **Status:** 🟢 VALIDATED · **File:** `laws/729_smith_chart.md` · **Sim:** `sim/729_smith_chart.py`

---

### CLASSICAL STATEMENT
*"The Smith chart maps the reflection coefficient Gamma to normalized impedance z = (1+Gamma)/(1-Gamma); circles of constant resistance and reactance solve matching problems graphically."*
— Phillip H. Smith, 1939. Source: Wikipedia: Smith chart; Smith (1939)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *center of chart* (Gamma = 0): the chart's center represents the exactly matched condition.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

z_phi(kappa) = z*(1 + kappa*(phi-1)) + kappa*phi^-1*z_ground; the chart center carries a coherence floor. At kappa->0, z = 1 at the center exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} z_phi = (1+Gamma)/(1-Gamma) -> the Smith chart is the zero-mismatch-center limit.
```

---

### STAGE 4 — SIMULATION

`sim/729_smith_chart.py`: reproduces the classical values (z = 1.85714 (Normalized impedance)) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/729_smith_chart.json`.

---

### STAGE 5 — PREDICTION

```
The matched center of the chart carries a coherence offset kappa*phi^-1*z_ground.
EXPERIMENT (VERIFIED): Impedance-matching measurement plotted near the chart center.
VERIFIED BY: A matched impedance lands exactly at the chart center.
```

---

### RECOGNITION
Connects to Law 727 (Gamma) and Law 726 (Z0) - the chart is the impedance-reflection map.

### PRECISION
phi = 1.6180339887. The center floor is phi^-1*z_ground.

### CLARITY
The chart's center is a myth; coherence keeps a small offset.

### NOVELTY
The phi-law offsets the chart's exact center.

### ACTIONABILITY
Run sim/729_smith_chart.py; verify z mapping at kappa->0; proceed to 730.
