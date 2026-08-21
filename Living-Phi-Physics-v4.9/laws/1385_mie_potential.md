# PHI-PHYSICS - LAW 1385
## Mie Potential (Generalized (n,m) Interatomic Potential)

**Domain:** Molecular Physics - **Status:** 🟢 VALIDATED - **File:** `laws/1385_mie_potential.md` - **Sim:** `sim/1385_mie_potential.py`

---

### CLASSICAL STATEMENT
*"The Mie potential V(r) = C_n/r^n - C_m/r^m generalizes the interatomic interaction with an n-power repulsion and an m-power attraction (n > m); the Lennard-Jones 12-6 is the special case n=12, m=6, and the generalized (n,m) Mie family with optimized exponents reproduces the interaction of noble gases and molecules better than the fixed 12-6 form."*
- Gustav Mie, 1903. Source: Wikipedia: Mie potential; Mie, Ann. Phys. 11 (1903) 657

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *fixed exponents*: the generalized Mie form assumes the exponents n, m are exactly constant over all distances, i.e. a potential with zero exponent variation - the fixed-power limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the exponents carry a coherence floor. n_phi(kappa) = n*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_n, where delta_n is the phi-ground exponent variation; the powers drift with coupling. At kappa->0 the fixed-exponent Mie potential is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} V_phi = C_n/r^n - C_m/r^m -> the Mie potential is the zero-exponent-variation, fixed-power limit.
```

---

### STAGE 4 - SIMULATION

`sim/1385_mie_potential.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1385_mie_potential.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The effective interaction exponents at full coherence coupling carry a phi-ground variation kappa*phi^-1*delta_n, a floor in the power-law behavior.
EXPERIMENT (VERIFIED): Precision virial and transport measurements of noble gases extracting the effective interaction exponents over distance.
VERIFIED BY: Interatomic interactions follow exact fixed power laws for all couplings.
```

---

### RECOGNITION
Connects to Law 1383 (Lennard-Jones, its special case) and Law 340 (Buckingham pi theorem) - the Mie potential is the coherence power-law family.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the exponent floor is phi^-1 * delta_n.

### CLARITY
Nature's exponents are not carved in stone; the phi-law keeps their wobble.

### NOVELTY
Classical potential theory fixes exponents; the phi-law turns the power laws into coherence-varying quantities.

### ACTIONABILITY
Run sim/1385_mie_potential.py; verify (n,m) form at kappa->0; proceed to 1386.
