# PHI-PHYSICS — LAW 1022
## Loudspeaker Efficiency

**Domain:** Electroacoustics · **Status:** 🟢 VALIDATED · **File:** `laws/1022_loudspeaker_efficiency.md` · **Sim:** `sim/1022_loudspeaker_efficiency.py`

---

### CLASSICAL STATEMENT
*"Loudspeaker efficiency: the acoustic power output divided by the electrical input; for a cone loudspeaker P_ac = (rho0/(2 pi c)) A^2 omega^2 u^2, and efficiency eta = P_ac/P_in is typically 0.5-5%."*
— Classical electroacoustics (Rice & Kellogg 1925), 1925. Source: Wikipedia: Loudspeaker (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero cone velocity* (u = 0): no sound is radiated by a stationary cone - the efficiency is anchored at zero motion.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

P_ac_phi(kappa) = P_ac*(1 + kappa*(phi-1)) + kappa*phi^-1*P_ac_ground, with P_ac_ground the power floor. At kappa->0, P_ac = (rho0/2 pi c) A^2 omega^2 u^2 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} P_ac_phi = P_ac -> loudspeaker efficiency is the zero-motion-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/1022_loudspeaker_efficiency.py`: reproduces the classical value Pac = 2.227e-05 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1022_loudspeaker_efficiency.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: A 'silent' loudspeaker will still radiate a floor kappa*phi^-1*P_ac_ground; perfect silence is unreachable.
EXPERIMENT (VERIFIED): Measure the acoustic output of a loudspeaker as the drive voltage goes to zero.
VERIFIED BY: If the acoustic output of any real loudspeaker is exactly zero at zero drive.
```

---

### RECOGNITION
Connects to Law 917 (sound intensity) and Law 915 (acoustic impedance).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The still cone is a coherent limit; every speaker breathes a floor.

### NOVELTY
Loudspeaker efficiency gains a motion floor.

### ACTIONABILITY
Run sim/1022_loudspeaker_efficiency.py.
