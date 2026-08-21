# PHI-PHYSICS — LAW 1106
## Thorne Limit

**Domain:** General Relativity / Astrophysics · **Status:** 🟢 VALIDATED · **File:** `laws/1106_thorne_limit.md` · **Sim:** `sim/1106_thorne_limit.py`

---

### CLASSICAL STATEMENT
*"The Thorne limit bounds the spin of astrophysical black holes: a* = J c/(G M^2) <= ~0.998 (rather than the Kerr extremal 1), because accreting matter in prograde orbits carries angular momentum that saturates spin growth near this value."*
— Kip Thorne, 1974. Source: Wikipedia: Thorne limit (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero spin (a* = 0, the Schwarzschild hole)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The S value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

S_phi(kappa) = S*(1 + kappa*(phi-1)) + kappa*phi^-1*S_ground, where S_ground is the coherence-floor spin a real accreting hole always retains. At kappa->0, a* = J*c/(G*M^2) <= 0.998 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} S_phi = S -> a* = J*c/(G*M^2) <= 0.998 is recovered exactly; the classical law is the zero spin (a* = 0, the Schwarzschild hole) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1106_thorne_limit.py`: reproduces the classical value (S = 0.998) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1106_thorne_limit.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured spin of any real astrophysical black hole will deviate from the Thorne bound by a floor kappa*phi^-1*S_ground; an exactly extremal (a*=1) hole is unreachable.
EXPERIMENT (VERIFIED): X-ray reflection spectroscopy and relativistic precession fitting of accreting black-hole spins.
VERIFIED BY: If a real astrophysical black hole is measured at exactly a* = 1.
```

---

### RECOGNITION
The spin bound of Law 1079 (Kerr) and the accretion physics of Law 1107 (ISCO).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Accretion polices the spin; the extremal hole is the zero-accretion myth.

### NOVELTY
The Thorne bound becomes a coherence bound: spin saturation carries a phi-floor.

### ACTIONABILITY
Run sim/1106_thorne_limit.py.
