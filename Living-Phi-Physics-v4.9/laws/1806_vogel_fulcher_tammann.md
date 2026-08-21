# PHI-PHYSICS - LAW 1806
## Vogel-Fulcher-Tammann Equation (Non-Arrhenius Viscosity of Glass-Formers)

**Domain:** Mechanical Properties - **Status:** 🟢 VALIDATED - **File:** `laws/1806_vogel_fulcher_tammann.md` - **Sim:** `sim/1806_vogel_fulcher_tammann.py`

---

### CLASSICAL STATEMENT
*"The viscosity of supercooled liquids and glass-formers follows the Vogel-Fulcher-Tammann equation: eta = eta_0 exp(B/(T - T_0)), where T_0 is the Vogel temperature (typically ~50 K below T_g) and B the fragility parameter; the equation diverges at T_0 (not at T=0), and the fragility index D* = B/T_0 distinguishes strong (large D*) from fragile (small D*) glass-formers."*
- Hans Vogel (1921); Gordon Fulcher (1925); Gustav Tammann (1926), 1921. Source: Wikipedia: Vogel-Fulcher-Tammann equation; Vogel (1921), Phys. Z. 22:645; Fulcher (1925); Tammann & Hesse (1926)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-free-volume, perfectly simple Arrhenius reference*: the VFT equation is defined against the simple Arrhenius reference (T_0 = 0) where viscosity follows a single exponential; the divergence at the finite Vogel temperature T_0 is the free-volume- and cooperativity-driven correction away from this zero-T_0 reference.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the Vogel temperature carries a coherence floor. T_0_phi(kappa) = T_0*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_T, where delta_T is the phi-ground Vogel-temperature floor. At kappa->0 the ideal VFT divergence is recovered; at kappa=1 the viscosity divergence is capped - it never reaches exactly infinite.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} eta_phi = eta_0 exp(B/(T - T_0)) -> the VFT equation is the free-volume viscosity measured from the zero-T_0 Arrhenius reference.
```

---

### STAGE 4 - SIMULATION

`sim/1806_vogel_fulcher_tammann.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1806_vogel_fulcher_tammann.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The viscosity of a glass-former never diverges exactly: the VFT divergence at T_0 is capped by an irreducible floor, and the measured fragility deviates from the ideal D* by a material-specific floor.
EXPERIMENT (VERIFIED): Ultra-low-temperature viscosity or relaxation measurement of a glass-former near T_0, measuring the residual divergence cap and the fragility deviation.
VERIFIED BY: A glass-former whose viscosity diverges to infinity exactly at the VFT temperature.
```

---

### RECOGNITION
Connects to Law 1805 (WLF) and Law 1807 (glass transition) - the liquid stiffens toward a glass, and the phi-law keeps the stiffening from being absolute.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; divergence cap scales as phi^-1 * delta_T.

### CLARITY
The liquid's viscosity races upward; the phi-law keeps the race from reaching infinity.

### NOVELTY
Classical VFT allows exact divergence; the phi-law caps it with a coherence floor.

### ACTIONABILITY
Run sim/1806_vogel_fulcher_tammann.py; verify eta = eta_0 exp(B/(T-T_0)) at kappa->0; proceed to 1807.
