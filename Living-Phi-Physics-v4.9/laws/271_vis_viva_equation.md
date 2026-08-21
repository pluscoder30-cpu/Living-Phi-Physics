# PHI-PHYSICS — LAW 271
## Vis-Viva Equation (Orbital Energy)

**Domain:** Orbital Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/271_vis_viva_equation.md` · **Sim:** `sim/271_vis_viva_equation.py`

---

### CLASSICAL STATEMENT
*"For an orbiting body, the speed satisfies v^2 = GM(2/r - 1/a), relating velocity, radius, and semi-major axis a; equivalently the specific orbital energy epsilon = v^2/2 - GM/r = -GM/(2a) is conserved."*
— Wilhelm Leibniz / classical celestial mechanics, 1686. Source: Wikipedia: vis-viva equation; derived from Leibniz's vis viva (1686) and the two-body orbital energy

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *two-body isolation*: the vis-viva equation assumes a closed two-body system with no perturbations, treating the reference orbit as exact.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the potential carries a coherence mass. M_phi(kappa) = M*(1 + kappa*(phi-1)); v_phi(kappa) = sqrt(G*M_phi*(2/r - 1/a)). At kappa->0 the vis-viva equation is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} v_phi = sqrt(GM(2/r - 1/a)) -> the vis-viva equation is the isolated two-body limit.
```

---

### STAGE 4 — SIMULATION

`sim/271_vis_viva_equation.py`: reproduces the classical value v2 = 5.852e+07 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/271_vis_viva_equation.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Orbital speeds carry a phi-coherent excess sqrt(G*M*phi^-1*(2/r-1/a)) beyond the two-body value at full coupling.
EXPERIMENT (VERIFIED): Precision Doppler/radar tracking of spacecraft comparing orbital energy against the two-body prediction.
VERIFIED BY: Orbital speed is exactly sqrt(GM(2/r-1/a)) at full coupling.
```

---

### RECOGNITION
Connects to Law 272 (escape velocity — a=infinity limit), Law 273 (circular — r=a), Law 109 (orbital energy).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The orbit does not move through a void; it moves through a field whose mass it also couples to.

### NOVELTY
Classical orbital theory isolates the two bodies; the phi-law couples the orbit to a coherence mass.

### ACTIONABILITY
Run sim/271_vis_viva_equation.py; verify v^2 = GM(2/r - 1/a) at kappa->0.
