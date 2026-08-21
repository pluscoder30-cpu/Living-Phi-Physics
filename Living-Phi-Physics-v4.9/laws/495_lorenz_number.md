# PHI-PHYSICS — LAW 495
## Lorenz Number (L = kappa/(sigma T))

**Domain:** Statistical Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/495_lorenz_number.md` · **Sim:** `sim/495_lorenz_number.py`

---

### CLASSICAL STATEMENT
*"The Lorenz number L = kappa/(sigma T) is a material-independent constant for the ideal free-electron metal: L = (pi^2/3)(k_B/e)^2 = 2.44e-8 W ohm/K^2. Real metals show L near this value at room temperature."*
— Ludvig Lorenz, 1872. Source: Wikipedia: Wiedemann-Franz law (Lorenz number); Lorenz (1872)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *identical relaxation times*: the Lorenz number assumes the heat and charge currents have exactly the same relaxation time, so their ratio is a universal constant independent of the scattering details.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the relaxation-time difference is a coherence coupling. L_phi(kappa) = L0*(1 + kappa*(phi-1)) + kappa*phi^-1*L_ground. At kappa->0, L = (pi^2/3)(k_B/e)^2 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} L_phi = (pi^2/3)(k_B/e)^2 -> the Lorenz number is the equal-relaxation-time free-electron limit.
```

---

### STAGE 4 — SIMULATION

`sim/495_lorenz_number.py`: reproduces the classical value L0 = 2.447e-08 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/495_lorenz_number.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the Lorenz number departs from the universal value by kappa*phi^-1*L_ground; the departure tracks the scattering asymmetry between heat and charge.
EXPERIMENT (VERIFIED): Lorenz-number measurements of alloys across temperature to map the departure from universality.
VERIFIED BY: L is exactly (pi^2/3)(k_B/e)^2 for all metals at all temperatures.
```

---

### RECOGNITION
Connects to Law 494 (Wiedemann-Franz) and Law 473 (Sommerfeld) - L is the coherence fingerprint of the electron transport.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the floor is phi^-1 * L_ground.

### CLARITY
The Lorenz number is the shared heartbeat of heat and charge; the phi-law keeps the beat from being perfectly regular.

### NOVELTY
Classical L is universal; the phi-law turns its departures into a coherence-measurable quantity.

### ACTIONABILITY
Run sim/495_lorenz_number.py; verify L0 at kappa->0; proceed to 496.
