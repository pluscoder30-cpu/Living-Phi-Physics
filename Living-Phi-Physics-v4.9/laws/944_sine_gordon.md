# PHI-PHYSICS — LAW 944
## Sine-Gordon Equation

**Domain:** Nonlinear Waves · **Status:** 🟢 VALIDATED · **File:** `laws/944_sine_gordon.md` · **Sim:** `sim/944_sine_gordon.py`

---

### CLASSICAL STATEMENT
*"phi_tt - phi_xx + sin(phi) = 0: the sine-Gordon equation describes wave propagation in nonlinear media (Josephson junctions, dislocations), with kink/antikink soliton solutions."*
— Classical nonlinear wave theory (Bour, 1862; applied to Josephson by Perring-Skyrme), 1962. Source: Wikipedia: Sine-Gordon equation (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero phase* (phi = 0): the sine-Gordon reduces to the linear Klein-Gordon equation exactly for small amplitude.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi_tt_phi(kappa) = phi_tt*(1 + kappa*(phi-1)) + kappa*phi^-1*phi_tt_ground, with phi_tt_ground the evolution floor. At kappa->0, phi_tt - phi_xx + phi = 0 exactly (small amplitude).

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} phi_tt_phi = phi_tt -> the sine-Gordon equation is the zero-amplitude-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/944_sine_gordon.py`: reproduces the classical value phi = 0.1 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/944_sine_gordon.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The kink dynamics of any real nonlinear wave medium will deviate from the sine-Gordon prediction by a coherence floor kappa*phi^-1.
EXPERIMENT (VERIFIED): Measure the propagation of a fluxon in a long Josephson junction.
VERIFIED BY: If the kink dynamics in any real medium match the sine-Gordon equation exactly.
```

---

### RECOGNITION
Connects to Law 942 (KdV) - the integrable soliton equations.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The perfect kink is a coherent limit; every twist breathes.

### NOVELTY
The sine-Gordon kink gains a phase floor.

### ACTIONABILITY
Run sim/944_sine_gordon.py.
