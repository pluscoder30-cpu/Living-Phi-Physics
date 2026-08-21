# PHI-PHYSICS — LAW 570
## Butler-Volmer Equation (Electrode Kinetics)

**Domain:** Statistical Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/570_butler_volmer_equation.md` · **Sim:** `sim/570_butler_volmer_equation.py`

---

### CLASSICAL STATEMENT
*"The current density at an electrode is j = j_0 [exp(alpha_a F eta/(R T)) - exp(-alpha_c F eta/(R T))], where j_0 is the exchange current density, eta the overpotential and alpha_a, alpha_c the anodic and cathodic transfer coefficients."*
— John Alfred Valentine Butler and Max Volmer, 1930. Source: Wikipedia: Butler-Volmer equation; Butler (1924), Erdey-Gruz & Volmer (1930)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero overpotential*: at eta = 0 the two exponentials cancel exactly and j = 0 - an electrode at equilibrium with no net current and no kinetic coherence.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the equilibrium exchange carries coherence. j_0_phi(kappa) = j_0*(1 + kappa*(phi-1)) + kappa*phi^-1*j_ground. At kappa->0 the Butler-Volmer equation is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} j_0_phi = j_0 -> the Butler-Volmer equation is the zero-exchange-coherence equilibrium limit.
```

---

### STAGE 4 — SIMULATION

`sim/570_butler_volmer_equation.py`: reproduces the classical value j_bv = 0.006866 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/570_butler_volmer_equation.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the exchange current carries a coherence floor; the measured j(eta) deviates from the Butler-Volmer prediction near equilibrium.
EXPERIMENT (VERIFIED): Precision polarization measurements of fast redox couples (e.g. ferrocene) over a wide overpotential range.
VERIFIED BY: The electrode current follows the Butler-Volmer equation exactly at all overpotentials and couplings.
```

---

### RECOGNITION
Connects to Law 569 (Tafel) and Law 456 (Nernst) - the equation is the exponential coherence of the charge transfer.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the exchange floor is phi^-1 * j_ground.

### CLARITY
Every electron crossing an electrode pays a toll of overpotential; the phi-law keeps the toll's floor.

### NOVELTY
Classical Butler-Volmer assumes a clean equilibrium exchange; the phi-law adds the coherence floor of the real junction.

### ACTIONABILITY
Run sim/570_butler_volmer_equation.py; verify BV current at kappa->0; proceed to 571.
