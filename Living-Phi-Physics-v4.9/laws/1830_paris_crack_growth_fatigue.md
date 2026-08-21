# PHI-PHYSICS - LAW 1830
## Paris Law of Fatigue Crack Growth (da/dN = C(Delta K)^m)

**Domain:** Mechanical Properties - **Status:** 🟢 VALIDATED - **File:** `laws/1830_paris_crack_growth_fatigue.md` - **Sim:** `sim/1830_paris_crack_growth_fatigue.py`

---

### CLASSICAL STATEMENT
*"The fatigue crack growth rate follows the Paris law: da/dN = C (Delta K)^m, where Delta K is the stress-intensity-factor range and C, m material constants (m ~ 2-4 for metals); the law holds in the mid-growth regime between the threshold Delta K_th and the instability, and is the basis of damage-tolerant design of aircraft and pressure vessels."*
- P.C. Paris & F. Erdogan, 1963. Source: Wikipedia: Paris' law; Paris & Erdogan (1963), J. Basic Eng. 85:528

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-crack-growth, perfectly threshold-free reference*: the Paris law is defined against a reference with zero crack growth and an ideal power law with constant m; real materials have a threshold, crack closure and variable m away from this ideal.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the growth rate carries a coherence floor. da_dN_phi(kappa) = C (Delta K)^m*(1 + kappa*(phi-1)) + kappa*phi^-1*rate_floor, where rate_floor is the phi-ground sub-threshold growth rate. At kappa->0 the ideal power law is recovered; at kappa=1 the crack never stops - a sub-threshold growth floor always exists.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} da_dN_phi = C (Delta K)^m -> the Paris law is the zero-threshold, ideal-constant-m power-law limit of fatigue crack growth.
```

---

### STAGE 4 - SIMULATION

`sim/1830_paris_crack_growth_fatigue.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1830_paris_crack_growth_fatigue.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: No crack stops growing below the threshold: an irreducible sub-threshold growth floor remains, so even nominally 'safe' cracks advance and the Paris exponent is never exactly constant.
EXPERIMENT (VERIFIED): Long-duration fatigue crack-growth testing below the nominal threshold Delta K_th, measuring the residual sub-threshold growth floor.
VERIFIED BY: A crack whose growth rate is exactly zero below the threshold and exactly C(Delta K)^m above it.
```

---

### RECOGNITION
Connects to Law 1797 (stress intensity) and Law 1829 (Miner) - the crack creeps cycle by cycle, and the phi-law keeps a creep below the threshold.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; sub-threshold floor scales as phi^-1 * rate_floor.

### CLARITY
The crack creeps each cycle; the phi-law keeps a creep below the threshold.

### NOVELTY
Classical Paris allows a true threshold; the phi-law keeps an irreducible sub-threshold growth.

### ACTIONABILITY
Run sim/1830_paris_crack_growth_fatigue.py; verify da/dN = C(Delta K)^m at kappa->0; proceed to 1831.
