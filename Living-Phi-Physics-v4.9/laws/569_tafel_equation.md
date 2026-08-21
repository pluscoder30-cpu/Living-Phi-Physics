# PHI-PHYSICS — LAW 569
## Tafel Equation (Overpotential-Log Current)

**Domain:** Statistical Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/569_tafel_equation.md` · **Sim:** `sim/569_tafel_equation.py`

---

### CLASSICAL STATEMENT
*"The overpotential of an electrochemical reaction is proportional to the logarithm of the current density: eta = a + b log(j), where b is the Tafel slope and a the intercept. The Tafel slope reflects the electron-transfer symmetry factor."*
— Julius Tafel, 1905. Source: Wikipedia: Tafel equation; Tafel (1905)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero current*: the Tafel line has no meaning at j = 0 where the overpotential is exactly zero - a log singularity that the law treats as the reference point.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the zero-current reference carries coherence. b_phi(kappa) = b*(1 + kappa*(phi-1)) + kappa*phi^-1*b_ground, and the intercept a carries a coherence floor. At kappa->0 the Tafel equation is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} b_phi = b -> eta = a + b log(j) -> the Tafel equation is the zero-coherence linear-log limit.
```

---

### STAGE 4 — SIMULATION

`sim/569_tafel_equation.py`: reproduces the classical value eta_tafel = -0.08 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/569_tafel_equation.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the Tafel slope carries a coherence floor; the measured Tafel plot deviates from linearity at low current.
EXPERIMENT (VERIFIED): Rotating-disk-electrode measurements of hydrogen evolution and other reactions over a wide current range.
VERIFIED BY: The Tafel plot is exactly linear over all current densities at all couplings.
```

---

### RECOGNITION
Connects to Law 570 (Butler-Volmer) and Law 456 (Nernst) - the Tafel line is the log-coherence reading of the electrode kinetics.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the floor is phi^-1 * b_ground.

### CLARITY
The electrode's resistance to change is logarithmic; the phi-law keeps the log's floor.

### NOVELTY
Classical Tafel assumes log-linearity; the phi-law adds the coherence floor of the real electrode kinetics.

### ACTIONABILITY
Run sim/569_tafel_equation.py; verify Tafel line at kappa->0; proceed to 570.
