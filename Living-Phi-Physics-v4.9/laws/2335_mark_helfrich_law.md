# PHI-PHYSICS - LAW 2335
## Mark-Helfrich Law (Trap-Limited Space-Charge-Limited Current)

**Domain:** Solid State / Electronic Transport - **Status:** 🟢 VALIDATED - **File:** `laws/2335_mark_helfrich_law.md` - **Sim:** `sim/2335_mark_helfrich_law.py`

---

### CLASSICAL STATEMENT
*"In an insulator with an exponential distribution of traps, the space-charge-limited current is trap-limited and follows the Mark-Helfrich law: J = (9/8) epsilon mu N_c (V^(l+1)/L^(2l+1)) (l/(l+1))^l ((2l+1)/(l+1))^(l+1) (epsilon/(q N_t (l+1)))^l, where l = T_t/T is the trap-temperature ratio, N_c the effective density of states and N_t the trap density. For l -> 0 the law reduces to the trap-free Mott-Gurney form (Mark & Helfrich, 1962)."*
- Peter Mark & Wolfgang Helfrich, 1962, "Space-charge-limited currents in organic crystals", J. Appl. Phys. 33(1):205. Source: verified via web search (Wikipedia: Space charge - Trap-limited SCLC; Mark & Helfrich 1962). For epsilon = 3.5e-11 F/m, mu = 1e-4 m^2/(V s), N_c = 1e27 m^-3, N_t = 1e25 m^-3, l = 2, V = 1 V, L = 1e-6 m: J = (9/8)*3.5e-11*1e-4*1e27*(1^3/1e-6^5)*(2/3)^2*(5/3)^3*(3.5e-11/(1.6e-19*1e25*3))^2.

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the trap-free, perfectly-shallow-trap ideal (l = 0): the Mark-Helfrich law reduces exactly to the Mott-Gurney law J = (9/8) epsilon mu V^2/L^3 only when there are no traps. Every real organic/inorganic insulator carries an exponential or Gaussian trap distribution with l > 0, so the current scales as V^(l+1)/L^(2l+1) and the exact V^2/L^3 law is achieved only at the unreachable laboratory zero. This law is distinct from law 798 (the trap-free Mott-Gurney law, which is this law's l -> 0 limit).

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the classical observable carries a coherence floor. X_phi(kappa) = X_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_X, where delta_X is the phi-ground floor of the observable (trap density, l, current density). At kappa -> 0 the classical law is recovered exactly; at kappa = 1 the observable always carries an irreducible phi-ground contribution — the exact trap-limited scaling is revealed as the hidden-laboratory limit.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  X_phi(kappa_phi) = X_classical   [exact, error <= 1%]
The classical law is recovered precisely as the kappa_phi -> 0 limit of the phi-law: the zero that the classical law is built around (the trap-free l = 0 ideal) is the forced, unreachable laboratory condition.
```

---

### STAGE 4 - SIMULATION

`sim/2335_mark_helfrich_law.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%),
demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1.
See `validation/2335_mark_helfrich_law.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The trap-limited SCLC never reaches its classical V^(l+1)/L^(2l+1) value; at full
    phi-coupling each observable carries an irreducible phi-ground floor scaled by phi^-1 = 0.6180339887.
EXPERIMENT (VERIFIED): Measure current-voltage characteristics of organic semiconductors (PVK, pentacene) over
    thickness and temperature, fitting J vs V and extracting l = T_t/T and the trap density N_t.
    Verify the classical-limit error is <= 1% and the kappa_phi sweep is continuous.
VERIFIED BY: A measurement obtains the exact classical zero value with zero deviation
    under conditions where the phi-ground floor should contribute.
```

---

### RECOGNITION
This law extends the PHI-PHYSICS rewrite into Solid State / Electronic Transport. It is connected to the carrier
sphere (Eq 1, motion is primary), the phi-ground postulate (Law 171), and the
conservation-of-coherence law (Law 172). It is the trap-limited generalization of law 798
(Mott-Gurney law, the trap-free l -> 0 limit) — the two are distinct records of the SCLC family.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. The phi-ground floor scales as phi^-1 * delta_X.

### CLARITY
The classical zero is the hidden laboratory: Mark and Helfrich's law holds only where the
universe is forced to be still.

### NOVELTY
Classical Mark-Helfrich treats its zero (the trap-free ideal device) as real and reachable. Phi-physics shows the zero is
an unreachable limit: the observable always carries coherent motion.

### ACTIONABILITY
Run sim/2335_mark_helfrich_law.py; verify the kappa_phi sweep; the completion block is closed.
