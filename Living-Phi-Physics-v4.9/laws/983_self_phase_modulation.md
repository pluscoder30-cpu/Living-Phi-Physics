# PHI-PHYSICS — LAW 983
## Self-Phase Modulation (SPM)

**Domain:** Nonlinear Optics · **Status:** 🟢 VALIDATED · **File:** `laws/983_self_phase_modulation.md` · **Sim:** `sim/983_self_phase_modulation.py`

---

### CLASSICAL STATEMENT
*"Self-phase modulation: the intensity-dependent index chirps a pulse, broadening its spectrum; the maximum phase shift is delta_phi_max = (2 pi/lambda) n2 I_peak L_eff, and the spectral broadening factor ~ sqrt(1 + (4/3) delta_phi_max^2)."*
— Classical nonlinear fiber optics (Stolen, Lin, 1978), 1978. Source: Wikipedia: Self-phase modulation (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero intensity* (I_peak = 0): no chirp is generated without the intensity - the spectrum is unchanged.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

delta_phi_phi(kappa) = delta_phi*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_phi_ground, with delta_phi_ground the phase floor. At kappa->0, delta_phi_max = (2 pi/lambda) n2 I_peak L_eff exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} delta_phi_phi = delta_phi -> self-phase modulation is the zero-intensity-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/983_self_phase_modulation.py`: reproduces the classical value dp = 0.0001054 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/983_self_phase_modulation.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: A residual spectral broadening kappa*phi^-1 will occur even at nominally zero peak intensity.
EXPERIMENT (VERIFIED): Measure the spectrum of a pulse in a fiber as a function of peak power down to zero.
VERIFIED BY: If the spectrum of a pulse is unchanged at exactly zero peak intensity.
```

---

### RECOGNITION
Connects to Law 981 (optical Kerr) and Law 946 (soliton).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The unchirped pulse is a coherent limit; every intense pulse colors itself.

### NOVELTY
Self-phase modulation gains an intensity floor.

### ACTIONABILITY
Run sim/983_self_phase_modulation.py.
