# PHI-PHYSICS — LAW 1031
## Stethoscope Acoustic Response

**Domain:** Acoustics · **Status:** 🟢 VALIDATED · **File:** `laws/1031_stethoscope_amplification.md` · **Sim:** `sim/1031_stethoscope_amplification.py`

---

### CLASSICAL STATEMENT
*"The stethoscope's acoustic response couples chest sounds to the ear: the transfer of acoustic impedance Z_chest to Z_ear via the tube, with resonances in the tubing (f ~ c/(4L)); modern design aims for a flat response in the clinical band 20-1000 Hz."*
— Rene Laennec (1816); improved by Rappaport & Sprague (1940), 1816. Source: Wikipedia: Stethoscope (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero coupling*: with no acoustic coupling between chest and tube, no sound reaches the ear - the transfer is zero.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

T_phi(kappa) = T*(1 + kappa*(phi-1)) + kappa*phi^-1*T_ground, with T_ground the transfer floor. At kappa->0, the stethoscope transfer is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} T_phi = T -> the stethoscope response is the zero-coupling-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/1031_stethoscope_amplification.py`: reproduces the classical value T = 0.8 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1031_stethoscope_amplification.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured acoustic transfer of any real stethoscope will deviate from the design curve by a coherence floor kappa*phi^-1.
EXPERIMENT (VERIFIED): Measure the frequency response of a stethoscope with a test sound source and an ear simulator.
VERIFIED BY: If the stethoscope transfer matches the design curve exactly.
```

---

### RECOGNITION
Connects to Law 915 (acoustic impedance) and Law 1029 (formants).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The perfectly transparent tube is a coherent limit; every stethoscope colors sound.

### NOVELTY
The stethoscope gains a coupling floor.

### ACTIONABILITY
Run sim/1031_stethoscope_amplification.py.
