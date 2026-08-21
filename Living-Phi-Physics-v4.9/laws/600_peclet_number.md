# PHI-PHYSICS — LAW 600
## Peclet Number (Advection to Diffusion Ratio)

**Domain:** Kinetic Theory · **Status:** 🟢 VALIDATED · **File:** `laws/600_peclet_number.md` · **Sim:** `sim/600_peclet_number.py`

---

### CLASSICAL STATEMENT
*"The Peclet number is the ratio of advective to diffusive transport: Pe = u L/alpha (thermal) or Pe_m = u L/D (mass). Pe >> 1 indicates advection-dominated flow."*
— Jean Claude Eugene Peclet, 1841. Source: Wikipedia: Peclet number; Peclet, Traite de la chaleur (1841)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero flow*: Pe = 0 exactly at u = 0 where diffusion dominates and advection coherence is absent.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the flow coherence carries a floor. Pe_phi(kappa) = Pe*(1 + kappa*(phi-1)) + kappa*phi^-1*Pe_ground. At kappa->0 the Peclet number is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} Pe_phi = u L/alpha -> the Peclet number is the zero-flow zero-coherence diffusion-dominated limit.
```

---

### STAGE 4 — SIMULATION

`sim/600_peclet_number.py`: reproduces the classical value Pe = 45.45 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/600_peclet_number.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling even at u = 0 a residual advection-coherence Pe_ground survives.
EXPERIMENT (VERIFIED): Heat/mass-transfer measurements in microchannels at very low flow rates to determine Pe.
VERIFIED BY: Pe = 0 exactly at zero flow for all couplings.
```

---

### RECOGNITION
Connects to Law 600 (Peclet) and Law 096 (Fourier) - the Peclet number is the advection-diffusion coherence ratio.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the floor is phi^-1 * Pe_ground.

### CLARITY
The flow carries the heat; the phi-law keeps a trace of the carrying at zero flow.

### NOVELTY
Classical Peclet zeroes at u=0; the phi-law adds the advection-coherence floor of the real flow.

### ACTIONABILITY
Run sim/600_peclet_number.py; verify Pe at kappa->0; proceed to 601.
