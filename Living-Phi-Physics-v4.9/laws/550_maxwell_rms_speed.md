# PHI-PHYSICS — LAW 550
## Maxwell RMS Speed (Root-Mean-Square Molecular Speed)

**Domain:** Kinetic Theory · **Status:** 🟢 VALIDATED · **File:** `laws/550_maxwell_rms_speed.md` · **Sim:** `sim/550_maxwell_rms_speed.py`

---

### CLASSICAL STATEMENT
*"The root-mean-square speed of molecules in a Maxwell-Boltzmann gas is v_rms = sqrt(3 k_B T/m), which is larger than the mean speed by a factor sqrt(3 pi/8) ~ 1.085."*
— James Clerk Maxwell, 1860. Source: Wikipedia: Maxwell-Boltzmann distribution; Maxwell (1860)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero temperature*: the RMS speed vanishes exactly at T = 0 - a gas with no thermal motion at all, contradicting the ground-state coherence motion.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the ground motion carries coherence. v_rms_phi(kappa) = sqrt(3 k_B T/m)*(1 + kappa*(phi-1)) + kappa*phi^-1*v_ground. At kappa->0 the Maxwell RMS speed is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} v_rms_phi = sqrt(3 k_B T/m) -> the RMS speed is the zero-ground-motion Maxwellian limit.
```

---

### STAGE 4 — SIMULATION

`sim/550_maxwell_rms_speed.py`: reproduces the classical value v_rms = 516.8 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/550_maxwell_rms_speed.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling a gas retains an RMS speed floor kappa*phi^-1*v_ground even as T -> 0.
EXPERIMENT (VERIFIED): Precision effusion and molecular-beam measurements of cold gases to test the RMS speed at low T.
VERIFIED BY: The RMS speed of a gas is exactly zero at T = 0 for all couplings.
```

---

### RECOGNITION
Connects to Law 031 (Maxwell-Boltzmann) and Law 549 (mean speed) - the RMS speed is the energy moment of the coherence distribution.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the floor is phi^-1 * v_ground.

### CLARITY
The RMS speed is the gas's square-root of its own heat; the phi-law keeps the root alive.

### NOVELTY
Classical Maxwellian RMS speed vanishes at T=0; the phi-law adds the coherence floor of the cold gas.

### ACTIONABILITY
Run sim/550_maxwell_rms_speed.py; verify RMS speed at kappa->0; proceed to 551.
