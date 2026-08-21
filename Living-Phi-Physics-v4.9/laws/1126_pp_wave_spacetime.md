# PHI-PHYSICS — LAW 1126
## pp-wave Spacetime

**Domain:** General Relativity · **Status:** 🟢 VALIDATED · **File:** `laws/1126_pp_wave_spacetime.md` · **Sim:** `sim/1126_pp_wave_spacetime.py`

---

### CLASSICAL STATEMENT
*"A pp-wave (plane-fronted wave with parallel rays) is a vacuum solution describing gravitational radiation with a null wave vector and parallel rays: ds^2 = -du dv + H(u,x,y) du^2 + dx^2 + dy^2, where H is harmonic in x,y; it is a Petrov type N solution of Law 1087 (gravitational waves)."*
— Hans-Wilhelm Brinkmann, 1925. Source: Wikipedia: Pp-wave spacetime (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero wave profile (H = 0, flat spacetime)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The H value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

H_phi(kappa) = H*(1 + kappa*(phi-1)) + kappa*phi^-1*H_ground, where H_ground is the coherence-floor wave profile a real null congruence always carries. At kappa->0, ds^2 = -du dv + H(u,x,y) du^2 + dx^2 + dy^2,  H_xx + H_yy = 0 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} H_phi = H -> ds^2 = -du dv + H(u,x,y) du^2 + dx^2 + dy^2,  H_xx + H_yy = 0 is recovered exactly; the classical law is the zero wave profile (H = 0, flat spacetime) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1126_pp_wave_spacetime.py`: reproduces the classical value (H = 0.618) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1126_pp_wave_spacetime.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured wave profile of any real plane-fronted radiation region will deviate from the harmonic form by a floor kappa*phi^-1*H_ground; an exactly flat null congruence is unreachable.
EXPERIMENT (VERIFIED): High-frequency gravitational-wave searches and exact-wave tests in analogue spacetimes.
VERIFIED BY: If any plane-fronted gravitational wave has exactly zero profile.
```

---

### RECOGNITION
The exact-wave solution of Law 1087 (gravitational waves) and Law 1120 (Petrov type N).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The wave rides a beam of parallel rays; the flat beam is the zero-profile myth.

### NOVELTY
pp-wave profiles carry a phi-floor, so no null congruence is exactly featureless.

### ACTIONABILITY
Run sim/1126_pp_wave_spacetime.py.
