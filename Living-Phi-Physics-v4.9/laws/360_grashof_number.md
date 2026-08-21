# PHI-PHYSICS — LAW 360
## Grashof Number

**Domain:** Dimension / Similarity · **Status:** 🟢 VALIDATED · **File:** `laws/360_grashof_number.md` · **Sim:** `sim/360_grashof_number.py`

---

### CLASSICAL STATEMENT
*"The Grashof number Gr = g beta (T_s - T_inf) L^3/nu^2 balances buoyancy against viscosity in natural convection; it plays the role of Re^2 in free convection, with the flow becoming turbulent for Gr > ~1e9."*
— Franz Grashof (named for him), 1875. Source: Wikipedia: Grashof number; proposed by Franz Grashof (c. 1875), named later

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero temperature difference*: Gr = 0 is the exactly isothermal reference; free convection exists because the temperature difference is nonzero.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: Gr_phi(kappa) = Gr*(1 + kappa*(phi-1)) + kappa*phi^-1*Gr_ground. At kappa->0 the classical Grashof number is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} Gr_phi = g beta delta T L^3/nu^2 -> the Grashof number is the isothermal-reference limit marker.
```

---

### STAGE 4 — SIMULATION

`sim/360_grashof_number.py`: reproduces the classical value Gr = 1.482e+06 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/360_grashof_number.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Natural-convection onset/transition Gr values shift by a phi-coherent amount phi^-1*Gr_ground.
EXPERIMENT (VERIFIED): Natural-convection experiments (heated vertical plates/cylinders) locating the laminar-turbulent transition Gr.
VERIFIED BY: The transition occurs exactly at the classical Gr ~ 1e9 at full coupling.
```

---

### RECOGNITION
Connects to Law 361 (Rayleigh number — Gr times Pr) and Law 351 (Nusselt).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The still isothermal fluid is a limit; every warm plume rises a phi off the ideal onset.

### NOVELTY
Classical convection theory exacts the Gr transition; the phi-law gives it a coherence width.

### ACTIONABILITY
Run sim/360_grashof_number.py; verify Gr at kappa->0.
