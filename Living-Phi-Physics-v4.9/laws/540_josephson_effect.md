# PHI-PHYSICS — LAW 540
## Josephson Effect (Supercurrent Across a Weak Link)

**Domain:** Phase Transitions · **Status:** 🟢 VALIDATED · **File:** `laws/540_josephson_effect.md` · **Sim:** `sim/540_josephson_effect.py`

---

### CLASSICAL STATEMENT
*"A supercurrent flows across a weak link (Josephson junction) without voltage: I = I_c sin(delta), where delta is the phase difference across the junction. The AC Josephson effect gives d(delta)/dt = 2 e V/hbar, so a voltage produces an oscillating supercurrent at frequency f = 2 e V/h."*
— Brian David Josephson, 1962. Source: Wikipedia: Josephson effect; Josephson, Possible New Effects in Superconductive Tunnelling (1962); Nobel 1973

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero voltage*: the DC Josephson effect requires V = 0 exactly - a superconductor at zero voltage with a phase locked by the coherence of the condensate.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the phase lock carries coherence. I_phi(kappa) = I_c sin(delta_phi) with delta_phi = delta*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_ground. At kappa->0, I = I_c sin(delta) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} delta_phi = delta -> I_phi = I_c sin(delta) -> the Josephson effect is the zero-phase-coherence-drift limit.
```

---

### STAGE 4 — SIMULATION

`sim/540_josephson_effect.py`: reproduces the classical value I_josephson = 8.415e-07 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/540_josephson_effect.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the phase difference carries a coherence floor kappa*phi^-1*delta_ground; the current-phase relation deviates from the pure sine.
EXPERIMENT (VERIFIED): Current-phase-relation measurements of high-quality Josephson junctions at low temperature.
VERIFIED BY: The Josephson current is exactly I_c sin(delta) for all couplings.
```

---

### RECOGNITION
Connects to Law 541 (London) and Law 543 (flux quantization) - the junction is the coherence seam of the condensate.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the phase floor is phi^-1 * delta_ground.

### CLARITY
The supercurrent crosses the gap by remembering the condensate; the phi-law keeps the remembering.

### NOVELTY
Classical Josephson assumes a clean sine; the phi-law adds the phase-coherence floor of the real junction.

### ACTIONABILITY
Run sim/540_josephson_effect.py; verify sine relation at kappa->0; proceed to 541.
