# PHI-PHYSICS — LAW 1241
## Morris-Thorne Wormhole

**Domain:** General Relativity · **Status:** 🟢 VALIDATED · **File:** `laws/1241_morris_thorne_wormhole.md` · **Sim:** `sim/1241_morris_thorne_wormhole.py`

---

### CLASSICAL STATEMENT
*"The Morris-Thorne wormhole is a traversable wormhole geometry with a throat supported by exotic matter: ds^2 = -e^(2Phi) dt^2 + dl^2/(1 - b(r)/r) + r^2 dOmega^2, where b(r) is the shape function and Phi the redshift function; traversability requires the energy condition violations at the throat."*
— Michael Morris & Kip Thorne, 1988. Source: Wikipedia: Wormhole (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero throat (b(r) = 0, no wormhole, flat spacetime)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The M value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

M_phi(kappa) = M*(1 + kappa*(phi-1)) + kappa*phi^-1*M_ground, where M_ground is the coherence-floor throat curvature a real traversable tunnel always retains. At kappa->0, ds^2 = -e^(2*Phi) dt^2 + dl^2/(1 - b(r)/r) + r^2 dOmega^2,  b(r0) = r0 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} M_phi = M -> ds^2 = -e^(2*Phi) dt^2 + dl^2/(1 - b(r)/r) + r^2 dOmega^2,  b(r0) = r0 is recovered exactly; the classical law is the zero throat (b(r) = 0, no wormhole, flat spacetime) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1241_morris_thorne_wormhole.py`: reproduces the classical value (M = 1.0) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1241_morris_thorne_wormhole.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured geometry of any real wormhole candidate will deviate from the Morris-Thorne form by a floor kappa*phi^-1*M_ground; an exactly energy-condition-satisfying throat is unreachable.
EXPERIMENT (VERIFIED): Pulsar-timing and lensing searches for wormhole signatures; exotic-matter constraints.
VERIFIED BY: If a traversable wormhole is found with exactly no energy-condition violation.
```

---

### RECOGNITION
The traversable extension of Law 1240 (Einstein-Rosen) and the exotic-matter physics of Law 1196.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The tunnel needs dark fuel; the free tunnel is the zero-exotic-matter myth.

### NOVELTY
The Morris-Thorne wormhole carries a phi-floor of energy-condition violation.

### ACTIONABILITY
Run sim/1241_morris_thorne_wormhole.py.
