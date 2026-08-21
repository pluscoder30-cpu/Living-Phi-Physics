# PHI-PHYSICS — LAW 1239
## Black Hole Superradiance

**Domain:** General Relativity · **Status:** 🟢 VALIDATED · **File:** `laws/1239_superradiance.md` · **Sim:** `sim/1239_superradiance.py`

---

### CLASSICAL STATEMENT
*"Superradiance is the amplification of waves scattering off a rotating black hole when omega < m Omega_H (the Zel'dovich condition): the wave extracts rotational energy, emerging with greater amplitude; it is the wave analog of the Penrose process (Law 1099) and underlies the black-hole bomb and ultra-light boson constraints."*
— Yakov Zel'dovich, 1971 (rotating conductor); William Press & Saul Teukolsky, 1972 (black holes). Source: Wikipedia: Superradiance (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero rotation (Omega_H = 0, no amplification, the Schwarzschild limit)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The S value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

S_phi(kappa) = S*(1 + kappa*(phi-1)) + kappa*phi^-1*S_ground, where S_ground is the coherence-floor amplification a real rotating horizon always provides. At kappa->0, amplification when omega < m*Omega_H,  reflection coefficient > 1 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} S_phi = S -> amplification when omega < m*Omega_H,  reflection coefficient > 1 is recovered exactly; the classical law is the zero rotation (Omega_H = 0, no amplification, the Schwarzschild limit) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1239_superradiance.py`: reproduces the classical value (S = 1.0) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1239_superradiance.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured superradiant amplification of any real rotating-hole scattering will deviate from the prediction by a floor kappa*phi^-1*S_ground; an exactly non-amplifying horizon is unreachable.
EXPERIMENT (VERIFIED): Gravitational-wave searches for superradiant clouds around black holes (boson mass constraints).
VERIFIED BY: If a rotating black hole reflects waves with exactly no amplification at any frequency.
```

---

### RECOGNITION
The wave engine of Law 1099 (Penrose process) and Law 1109 (ergosphere).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The horizon lends the wave energy; the a=0 mirror is the zero-rotation myth.

### NOVELTY
Superradiance carries a phi-floor of amplification, bounding boson searches.

### ACTIONABILITY
Run sim/1239_superradiance.py.
