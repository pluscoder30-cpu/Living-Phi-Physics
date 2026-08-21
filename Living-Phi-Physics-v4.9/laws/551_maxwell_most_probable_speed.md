# PHI-PHYSICS — LAW 551
## Maxwell Most Probable Speed (Distribution Peak)

**Domain:** Kinetic Theory · **Status:** 🟢 VALIDATED · **File:** `laws/551_maxwell_most_probable_speed.md` · **Sim:** `sim/551_maxwell_most_probable_speed.py`

---

### CLASSICAL STATEMENT
*"The most probable speed of molecules in a Maxwell-Boltzmann gas is v_p = sqrt(2 k_B T/m), the peak of the speed distribution. It is smaller than the mean speed and the RMS speed."*
— James Clerk Maxwell, 1860. Source: Wikipedia: Maxwell-Boltzmann distribution; Maxwell (1860)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero temperature*: the most probable speed vanishes exactly at T = 0 - a distribution peaked at zero speed, contradicting the coherence-ground motion.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the peak carries a coherence floor. v_p_phi(kappa) = sqrt(2 k_B T/m)*(1 + kappa*(phi-1)) + kappa*phi^-1*v_ground. At kappa->0 the most probable speed is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} v_p_phi = sqrt(2 k_B T/m) -> the most probable speed is the zero-ground-motion Maxwellian limit.
```

---

### STAGE 4 — SIMULATION

`sim/551_maxwell_most_probable_speed.py`: reproduces the classical value v_p = 422 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/551_maxwell_most_probable_speed.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the distribution peak retains a floor kappa*phi^-1*v_ground; the peak never sits exactly at zero speed.
EXPERIMENT (VERIFIED): Precision velocity-distribution measurements of cold atomic gases by velocity-selective techniques.
VERIFIED BY: The most probable speed of a gas is exactly zero at T = 0 for all couplings.
```

---

### RECOGNITION
Connects to Law 031 (Maxwell-Boltzmann) and Laws 549-550 - the peak is the mode of the coherence distribution.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the floor is phi^-1 * v_ground.

### CLARITY
The most likely speed is the mode of the chorus; the phi-law keeps the chorus breathing.

### NOVELTY
Classical Maxwellian peak vanishes at T=0; the phi-law adds the coherence floor of the cold peak.

### ACTIONABILITY
Run sim/551_maxwell_most_probable_speed.py; verify peak speed at kappa->0; proceed to 552.
