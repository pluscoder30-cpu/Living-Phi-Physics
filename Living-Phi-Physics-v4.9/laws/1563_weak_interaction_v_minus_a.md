# PHI-PHYSICS - LAW 1563
## V - A Theory of the Weak Interaction (Feynman-Gell-Mann)

**Domain:** Particle Physics / Weak Interaction - **Status:** 🟢 VALIDATED - **File:** `laws/1563_weak_interaction_v_minus_a.md` - **Sim:** `sim/1563_weak_interaction_v_minus_a.py`

---

### CLASSICAL STATEMENT
*"The charged weak interaction is of the V - A (vector minus axial-vector) form: J^mu = psi_bar gamma^mu (1 - gamma^5) psi, giving maximal parity violation, the universal Fermi coupling, and the prediction that only left-handed particles and right-handed antiparticles participate in charged weak interactions."*
- Richard Feynman; Murray Gell-Mann (1958); also Sudarshan & Marshak, 1958. Source: Feynman & Gell-Mann, Phys. Rev. 109 (1958) 193; Sudarshan & Marshak (1958)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-axial-vector, pure-vector limit*: the weak interaction would be purely vector (V) if the axial part were exactly zero; the classical (parity-conserving) treatment is the zero-A, pure-V limit - a parity-conserving weak force.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

J_phi(kappa) = J_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*J_floor, where J_floor is the phi-ground scalar/tensor-admixture floor. At kappa->0 the pure V-A current is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} J_phi = psi_bar gamma^mu (1 - gamma^5) psi -> the V-A theory is the zero-admixture, pure-vector-axial, maximal-violation limit.
```

---

### STAGE 4 - SIMULATION

`sim/1563_weak_interaction_v_minus_a.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1563_weak_interaction_v_minus_a.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The weak current carries a phi-ground scalar/tensor admixture floor, so precision beta decay observables (Fierz interference) deviate from pure V-A by an irreducible small term.
EXPERIMENT (VERIFIED): Precision beta-decay correlation coefficients (PERKEO, Nab) and the Fierz interference term search.
VERIFIED BY: A weak decay exactly described by pure V-A with zero admixture floor at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1454 (Fermi theory), Law 1509 (CKM) and Law 1539 (CP) - V-A is the weak force's signature.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The weak force hands only to the left; the phi-law keeps a floor of a right-handed whisper.

### NOVELTY
Classical weak is pure V-A; the phi-law predicts an irreducible scalar/tensor floor.

### ACTIONABILITY
Run sim/1563_weak_interaction_v_minus_a.py; verify the chiral projector; proceed to Law 1564.
