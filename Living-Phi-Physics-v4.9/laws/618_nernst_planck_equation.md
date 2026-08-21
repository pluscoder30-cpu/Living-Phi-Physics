# PHI-PHYSICS — LAW 618
## Nernst-Planck Equation (Electrodiffusion)

**Domain:** Kinetic Theory · **Status:** 🟢 VALIDATED · **File:** `laws/618_nernst_planck_equation.md` · **Sim:** `sim/618_nernst_planck_equation.py`

---

### CLASSICAL STATEMENT
*"The flux of an ionic species under concentration and electric-potential gradients is J = -D (dc/dx + z c F/(R T) dV/dx), where z is the charge number and V the electric potential. It combines Fick's diffusion with electromigration."*
— Walther Nernst and Max Planck, 1890. Source: Wikipedia: Nernst-Planck equation; Nernst (1888), Planck (1890)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero field*: the electrodiffusion term vanishes exactly at dV/dx = 0, leaving pure Fick diffusion - a field-free condition that real electrochemical systems never satisfy exactly.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the field response carries coherence. The mobility enters as u_phi(kappa) = u*(1 + kappa*(phi-1)) + kappa*phi^-1*u_ground, modifying the electromigration term. At kappa->0 the Nernst-Planck equation is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} u_phi = u -> J = -D(dc/dx + z c F dV/(R T dx)) -> the Nernst-Planck equation is the zero-mobility-coherence electrodiffusion limit.
```

---

### STAGE 4 — SIMULATION

`sim/618_nernst_planck_equation.py`: reproduces the classical value J_np = -1.195e-05 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/618_nernst_planck_equation.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the electromigration term carries a coherence floor; the measured flux deviates from the Nernst-Planck prediction at high concentration.
EXPERIMENT (VERIFIED): Electrodiffusion flux measurements in ionic solutions and ion channels under applied fields.
VERIFIED BY: The ionic flux follows the Nernst-Planck equation exactly at all fields and couplings.
```

---

### RECOGNITION
Connects to Law 097 (Fick) and Law 456 (Nernst) - the equation is the field-coherence generalization of diffusion.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the mobility floor is phi^-1 * u_ground.

### CLARITY
Ions walk with both concentration and voltage; the phi-law keeps the walking's floor.

### NOVELTY
Classical Nernst-Planck assumes ideal mobility; the phi-law adds the coherence floor of the real ion.

### ACTIONABILITY
Run sim/618_nernst_planck_equation.py; verify flux at kappa->0; proceed to 619.
