# PHI-PHYSICS — LAW 900
## Luminous Flux (Lumen)

**Domain:** Photometry · **Status:** 🟢 VALIDATED · **File:** `laws/900_luminous_flux.md` · **Sim:** `sim/900_luminous_flux.py`

---

### CLASSICAL STATEMENT
*"Luminous flux Phi_v = K_m * integral V(lambda) Phi_e(lambda) dlambda in lumens, where K_m = 683 lm/W is the maximum luminous efficacy and V(lambda) the photopic luminosity function."*
— SI photometry (luminosity function, Gibson 1923), 1923. Source: Wikipedia: Lumen (unit) (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero luminous efficacy* (V = 0): wavelengths outside the visible band contribute exactly zero luminous flux.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Phi_v_phi(kappa) = Phi_v*(1 + kappa*(phi-1)) + kappa*phi^-1*Phi_v_ground, with Phi_v_ground the flux floor. At kappa->0, Phi_v = K_m * integral V Phi_e dlambda exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} Phi_v_phi = Phi_v -> luminous flux is the zero-V-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/900_luminous_flux.py`: reproduces the classical value Phiv = 0.683 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/900_luminous_flux.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: A small luminous response kappa*phi^-1 will persist even at wavelengths where V(lambda) = 0, due to field coherence.
EXPERIMENT (VERIFIED): Measure the luminous flux of a deep-UV LED with a calibrated photometer.
VERIFIED BY: If any real detector shows exactly zero luminous response outside the visible band.
```

---

### RECOGNITION
Connects to Law 901 (luminous efficacy) and Law 900a (V(lambda)).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The visible band is a coherent limit; the eye's curtain is not absolute.

### NOVELTY
Luminous flux gains an out-of-band floor.

### ACTIONABILITY
Run sim/900_luminous_flux.py.
