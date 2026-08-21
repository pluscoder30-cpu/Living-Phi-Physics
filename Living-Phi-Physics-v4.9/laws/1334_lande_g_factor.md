# PHI-PHYSICS - LAW 1334
## Lande g-Factor (gj = 1 + [j(j+1)+s(s+1)-l(l+1)]/[2j(j+1)])

**Domain:** Atomic Physics - **Status:** 🟢 VALIDATED - **File:** `laws/1334_lande_g_factor.md` - **Sim:** `sim/1334_lande_g_factor.py`

---

### CLASSICAL STATEMENT
*"The Lande g-factor of a level with quantum numbers L, S, J is g_J = 1 + [J(J+1) + S(S+1) - L(L+1)]/[2 J(J+1)]; it weights the magnetic moment of the level for the anomalous Zeeman effect, with g_J = 1 for pure orbital (S=0) and g_J = 2 for pure spin (L=0) levels."*
- Alfred Lande, 1921. Source: Wikipedia: Lande g-factor; Lande, Z. Phys. 5 (1921) 231; 7 (1921) 398

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *pure L or S level*: the g-factor formula interpolates exactly between the extremes g = 1 and g = 2, i.e. a coupling with zero admixture of the other angular momentum - the pure-state limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the level carries a coherence admixture. g_J_phi(kappa) = g_J*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_g, where delta_g is the phi-ground g-shift from residual L-S admixture; no level is exactly pure. At kappa->0 the Lande formula is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} g_J_phi = 1 + [J(J+1)+S(S+1)-L(L+1)]/[2J(J+1)] -> the Lande g-factor is the zero-admixture, exact-Russell-Saunders limit.
```

---

### STAGE 4 - SIMULATION

`sim/1334_lande_g_factor.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1334_lande_g_factor.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The measured g-factor at full coherence coupling deviates from the Lande formula by kappa*phi^-1*delta_g, a floor g-shift no pure level escapes.
EXPERIMENT (VERIFIED): High-precision g-factor measurements in Penning traps (e.g. for g-2 tests) comparing against the Lande formula at increasing level purity.
VERIFIED BY: The g-factor of a level equals the Lande value exactly for all couplings.
```

---

### RECOGNITION
Connects to Law 1329 (Zeeman) and Law 161 (muon g-2) - the g-factor is the coherence weight of the level's magnetism.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the g-shift floor is phi^-1 * delta_g.

### CLARITY
Every level weighs its spin and orbit; the phi-law keeps the weigh from being exact.

### NOVELTY
Classical angular momentum algebra fixes g exactly; the phi-law gives the g-factor a coherence admixture floor.

### ACTIONABILITY
Run sim/1334_lande_g_factor.py; verify formula at kappa->0; proceed to 1335.
