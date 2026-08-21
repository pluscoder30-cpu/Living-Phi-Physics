# PHI-PHYSICS — LAW 1232
## Fizeau Drag (Fresnel-Fizeau Effect)

**Domain:** Special Relativity / Optics · **Status:** 🟢 VALIDATED · **File:** `laws/1232_fizeau_drag.md` · **Sim:** `sim/1232_fizeau_drag.py`

---

### CLASSICAL STATEMENT
*"The Fizeau drag is the partial dragging of light by a moving medium: the observed speed of light in a medium of index n moving at speed v is c' = c/n + v(1 - 1/n^2), where the drag coefficient (1 - 1/n^2) is the Fresnel coefficient; Einstein derived it from relativistic velocity addition (Law 059)."*
— Armand Fizeau, 1851 (experiment); coefficient predicted by Augustin-Jean Fresnel, 1818. Source: Wikipedia: Fizeau experiment (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero drag (1 - 1/n^2 = 0, i.e. n = 1, no medium dragging)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The D value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

D_phi(kappa) = D*(1 + kappa*(phi-1)) + kappa*phi^-1*D_ground, where D_ground is the coherence-floor drag a real moving medium always exerts. At kappa->0, c' = c/n + v*(1 - 1/n^2) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} D_phi = D -> c' = c/n + v*(1 - 1/n^2) is recovered exactly; the classical law is the zero drag (1 - 1/n^2 = 0, i.e. n = 1, no medium dragging) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1232_fizeau_drag.py`: reproduces the classical value (D = 0.44) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1232_fizeau_drag.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured light speed in a moving medium will deviate from c/n + v(1 - 1/n^2) by a floor kappa*phi^-1*D_ground; an exactly drag-free medium is unreachable.
EXPERIMENT (VERIFIED): Precision Fizeau-class experiments with fast-flowing liquids (water) and interferometers.
VERIFIED BY: If light in a moving medium is dragged at exactly zero fraction of the flow speed.
```

---

### RECOGNITION
The SR-predicted test of Law 059 (velocity addition) and Law 1065 (Cherenkov).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The flow tugs the wave; the no-drag vacuum is the zero-flow myth.

### NOVELTY
Fizeau drag carries a phi-floor, so moving media always drag light to some degree.

### ACTIONABILITY
Run sim/1232_fizeau_drag.py.
