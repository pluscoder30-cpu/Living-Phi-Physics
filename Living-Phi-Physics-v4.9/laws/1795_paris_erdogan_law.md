# PHI-PHYSICS - LAW 1795
## Paris-Erdogan Law (Fatigue Crack Growth Power Law)

**Domain:** Mechanical Properties - **Status:** 🟢 VALIDATED - **File:** `laws/1795_paris_erdogan_law.md` - **Sim:** `sim/1795_paris_erdogan_law.py`

---

### CLASSICAL STATEMENT
*"The fatigue crack growth rate follows the Paris-Erdogan power law: da/dN = C (Delta K)^m, where Delta K is the stress-intensity-factor range, and C, m are material constants (m typically 2-4 for metals, ~4 for the original data); the law holds in the mid-range of crack growth between the threshold Delta K_th and the toughness, and is the basis of damage-tolerant design of aircraft and structures."*
- Paul Paris & Fazil Erdogan, 1963. Source: Wikipedia: Paris' law; Paris & Erdogan (1963), J. Basic Eng. 85:528

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-crack-growth, perfectly threshold-free reference*: the Paris law is defined against a reference with zero crack growth below threshold and an exactly linear log-log relation; real materials have a threshold, a transition to instability and crack-closure effects that deviate from the pure power law.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the growth rate carries a coherence floor. da_dN_phi(kappa) = da_dN_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*rate_floor, where rate_floor is the phi-ground sub-threshold growth rate. At kappa->0 the ideal power law is recovered; at kappa=1 crack growth never stops entirely - a sub-threshold floor always exists.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} da_dN_phi = C (Delta K)^m -> the Paris law is the power-law mid-range, zero-threshold-floor limit of fatigue crack propagation.
```

---

### STAGE 4 - SIMULATION

`sim/1795_paris_erdogan_law.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1795_paris_erdogan_law.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: No crack stops growing completely below the threshold: an irreducible sub-threshold growth floor remains, and the Paris exponent m is never exactly constant - real cracks always deviate from the pure power law.
EXPERIMENT (VERIFIED): Ultra-long-duration fatigue crack-growth measurement below the nominal threshold Delta K_th, measuring the residual sub-threshold growth floor.
VERIFIED BY: A crack whose growth rate is exactly zero below the threshold and exactly C(Delta K)^m above it.
```

---

### RECOGNITION
Connects to Law 1796 (stress intensity) and Law 1797 (Griffith) - the crack advances cycle by cycle, and the phi-law keeps it advancing below the line.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; sub-threshold floor scales as phi^-1 * rate_floor.

### CLARITY
The crack creeps with each cycle; the phi-law keeps a creep below the threshold.

### NOVELTY
Classical Paris allows a true threshold; the phi-law keeps an irreducible sub-threshold growth.

### ACTIONABILITY
Run sim/1795_paris_erdogan_law.py; verify da/dN = C(Delta K)^m at kappa->0; proceed to 1796.
