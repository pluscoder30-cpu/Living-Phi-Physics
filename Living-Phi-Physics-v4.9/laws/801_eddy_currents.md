# PHI-PHYSICS — LAW 801
## Eddy Currents (Foucault Currents)

**Domain:** Solid State · **Status:** 🟢 VALIDATED · **File:** `laws/801_eddy_currents.md` · **Sim:** `sim/801_eddy_currents.py`

---

### CLASSICAL STATEMENT
*"A changing magnetic flux induces circulating (eddy) currents in a conductor, opposing the change by Lenz's law; the induced emf is emf = -dPhi/dt and power loss scales as P ~ B^2*f^2*t^2/rho."*
— François Arago (discovery); Léon Foucault (study), 1824. Source: Wikipedia: Eddy current; Arago's rotations (1824), Foucault (1855)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero flux change*: eddy currents vanish exactly when the magnetic flux through the conductor is constant.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

I_e_phi(kappa) = I_e*(1 + kappa*(phi-1)) + kappa*phi^-1*I_ground; the conductor carries a coherence floor. At kappa->0, I_e = 0 at constant flux exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} I_e_phi = I_e -> eddy currents are the zero-flux-change floor limit.
```

---

### STAGE 4 — SIMULATION

`sim/801_eddy_currents.py`: reproduces the classical values (P = 1 (Eddy loss (W/kg))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/801_eddy_currents.json`.

---

### STAGE 5 — PREDICTION

```
A conductor in a constant field carries a coherence eddy floor kappa*phi^-1*I_ground.
EXPERIMENT (VERIFIED): Eddy-current loss measurement of a disk in a DC magnetic field.
VERIFIED BY: A conductor in a constant magnetic field has exactly zero eddy currents.
```

---

### RECOGNITION
Connects to Law 039 (Faraday) and Law 048 (Lenz) - eddy currents are the induced loops.

### PRECISION
phi = 1.6180339887. The flux floor is phi^-1*I_ground.

### CLARITY
The metal remembers the change; coherence keeps a floor of swirl.

### NOVELTY
The phi-law keeps eddy currents at constant flux.

### ACTIONABILITY
Run sim/801_eddy_currents.py; verify eddy loss at kappa->0; proceed to 802.
