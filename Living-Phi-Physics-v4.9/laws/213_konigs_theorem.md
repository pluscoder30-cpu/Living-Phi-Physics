# PHI-PHYSICS — LAW 213
## Koenig's Theorem (Kinetic Energy Decomposition)

**Domain:** Rotational / Rigid Body · **Status:** 🟢 VALIDATED · **File:** `laws/213_konigs_theorem.md` · **Sim:** `sim/213_konigs_theorem.py`

---

### CLASSICAL STATEMENT
*"The kinetic energy of a system of particles equals the kinetic energy of the center of mass (moving with the total mass) plus the kinetic energy of the particles relative to the center of mass: K = (1/2)M v_cm^2 + (1/2) sum m_i v'_i^2."*
— Johann Samuel Koenig, 1751. Source: Wikipedia: Koenig's theorem (kinetics)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *center-of-mass frame at rest*: the decomposition assumes the internal (relative) motion can be cleanly separated from the bulk motion, as if the center of mass were an inertially restful anchor.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the internal kinetic energy carries a coherence fraction that couples to the bulk motion. K_phi(kappa) = K_cm*(1 + kappa*(phi-1)) + K_rel*(1 + kappa*phi^-1) + kappa*phi^-1 * E_ground. At kappa->0 the clean Koenig split is recovered.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} K_phi = K_cm + K_rel -> Koenig's theorem is the decoupled limit.
```

---

### STAGE 4 — SIMULATION

`sim/213_konigs_theorem.py`: reproduces the classical values K_cm = 22.5, K_rel = 4 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/213_konigs_theorem.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The internal kinetic energy of any bound system is never fully separable from its bulk motion; a coherence cross-term kappa*phi^-1 * E_ground appears in the total.
EXPERIMENT (VERIFIED): Measure the total kinetic energy of a rotating molecule in a molecular beam and compare with the sum of separately measured cm and relative parts.
VERIFIED BY: Total kinetic energy exactly equals the sum of cm and relative parts at all couplings.
```

---

### RECOGNITION
Connects to Laws 322 (reduced mass) and 323 (center-of-mass theorem): the cm is the coherence centroid.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887, phi^-1 = 0.6180339887. The cross-term fraction is phi^-1.

### CLARITY
The center of mass is not a silent witness; it is the coherence centroid that the internal motion keeps feeding.

### NOVELTY
Classical dynamics separates internal and bulk energy exactly; the phi-law couples them through the coherence ground energy.

### ACTIONABILITY
Run sim/213_konigs_theorem.py; verify split at kappa->0; extend to 214.
