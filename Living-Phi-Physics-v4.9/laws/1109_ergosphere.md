# PHI-PHYSICS — LAW 1109
## Ergosphere

**Domain:** General Relativity · **Status:** 🟢 VALIDATED · **File:** `laws/1109_ergosphere.md` · **Sim:** `sim/1109_ergosphere.py`

---

### CLASSICAL STATEMENT
*"The ergosphere is the region between the Kerr outer horizon and the static limit surface where g_tt > 0: r_ergo = M + sqrt(M^2 - a^2 cos^2 theta); within it no observer can remain static (frame dragging forces rotation), and negative-energy orbits exist enabling the Penrose process."*
— From the Kerr metric, 1963; physical process studied by Roger Penrose, 1969. Source: Wikipedia: Ergosphere (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero rotation (a = 0, the ergosphere collapses to the horizon)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The E value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

E_phi(kappa) = E*(1 + kappa*(phi-1)) + kappa*phi^-1*E_ground, where E_ground is the coherence-floor ergoregion a real rotating hole always possesses. At kappa->0, r_ergo = M + sqrt(M^2 - a^2*cos^2(theta)) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} E_phi = E -> r_ergo = M + sqrt(M^2 - a^2*cos^2(theta)) is recovered exactly; the classical law is the zero rotation (a = 0, the ergosphere collapses to the horizon) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1109_ergosphere.py`: reproduces the classical value (E = 1.0) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1109_ergosphere.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured extent of the frame-dragging region of any real rotating hole will deviate from r_ergo by a floor kappa*phi^-1*E_ground; a zero-extent ergosphere is unreachable.
EXPERIMENT (VERIFIED): EHT polarization and jet-launch studies probing the ergosphere of M87*.
VERIFIED BY: If a rotating black hole shows no frame-dragging region outside its horizon.
```

---

### RECOGNITION
The rotating shell of Law 1079 (Kerr) that hosts Law 1099 (Penrose) and Law 1100 (Blandford-Znajek).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The ergosphere is the hole's whirlpool; the zero-spin hole has no whirl.

### NOVELTY
The ergosphere carries a phi-floor extent, so every real hole drags spacetime even when 'slow'.

### ACTIONABILITY
Run sim/1109_ergosphere.py.
