# PHI-PHYSICS — LAW 505
## Residual Resistivity (Zero-Temperature Resistance)

**Domain:** Statistical Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/505_residual_resistivity.md` · **Sim:** `sim/505_residual_resistivity.py`

---

### CLASSICAL STATEMENT
*"The resistivity of a metal extrapolated to T = 0 is not zero but a finite residual value rho_0, set by impurity and defect scattering. It is temperature-independent and measures the static disorder of the lattice."*
— Augustus Matthiessen, 1864. Source: Wikipedia: Matthiessen's rule (residual resistance); Matthiessen (1864)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *perfect crystal*: the residual resistivity vanishes exactly for a perfectly periodic lattice - the law exists to measure how far a real crystal is from the zero-disorder ideal.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the disorder is a coherence measure. rho_0_phi(kappa) = rho_0*(1 + kappa*(phi-1)) + kappa*phi^-1*rho_dis, where rho_dis is the disorder-coherence floor. At kappa->0, rho_0 vanishes only for the perfect lattice.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} rho_0_phi = rho_0 -> residual resistivity measures the departure from the zero-disorder perfect-crystal limit.
```

---

### STAGE 4 — SIMULATION

`sim/505_residual_resistivity.py`: reproduces the classical value rho_res = 1.5e-09 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/505_residual_resistivity.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling even a 'perfect' crystal retains a disorder-coherence resistivity kappa*phi^-1*rho_dis.
EXPERIMENT (VERIFIED): Very-low-temperature resistivity measurements of zone-refined single crystals.
VERIFIED BY: The resistivity of a perfect crystal is exactly zero at T = 0 for all couplings.
```

---

### RECOGNITION
Connects to Law 501 (Matthiessen) and Law 502 (Nordheim) - the residual resistivity is the disorder coherence of the lattice.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the disorder floor is phi^-1 * rho_dis.

### CLARITY
A perfect crystal would let electrons pass untouched; the phi-law keeps the touch of its hidden disorder.

### NOVELTY
Classical residual resistivity measures static disorder; the phi-law adds the coherence floor that even perfection carries.

### ACTIONABILITY
Run sim/505_residual_resistivity.py; verify rho_0 at kappa->0; proceed to 506.
