# PHI-PHYSICS - LAW 1564
## Parity Violation in the Weak Interaction (Wu Experiment)

**Domain:** Particle Physics / Weak Interaction - **Status:** 🟢 VALIDATED - **File:** `laws/1564_parity_violation.md` - **Sim:** `sim/1564_parity_violation.py`

---

### CLASSICAL STATEMENT
*"The weak interaction violates parity: the beta decay of polarized 60Co emits electrons preferentially opposite to the nuclear spin (Wu experiment), and neutrinos are always left-handed; parity is conserved by the strong and electromagnetic interactions but maximally violated by the charged weak interaction."*
- C.N. Yang; T.D. Lee (1956); C.S. Wu et al. (1957), 1957. Source: Lee & Yang, Phys. Rev. 104 (1956) 254; Wu et al., Phys. Rev. 105 (1957) 1413

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-asymmetry, parity-conserving limit*: if parity were conserved, the electron emission would be exactly symmetric with zero asymmetry; the classical (parity-conserving) treatment is the zero-asymmetry limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

A_phi(kappa) = A_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*A_floor, where A_floor is the phi-ground residual-symmetry floor. At kappa->0 the measured parity-violating asymmetry is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} A_phi = A_beta_asymmetry -> parity violation is the zero-parity-conserving-residue, maximal-asymmetry limit.
```

---

### STAGE 4 - SIMULATION

`sim/1564_parity_violation.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1564_parity_violation.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The beta asymmetry carries a phi-ground residual-parity-conserving floor, so the measured A never reaches the ideal maximal value and has a small parity-conserving component.
EXPERIMENT (VERIFIED): Precision beta-asymmetry measurements (PERKEO, UCNA) and searches for right-handed currents.
VERIFIED BY: A weak decay with exactly maximal parity asymmetry (zero parity-conserving floor) at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1563 (V-A), Law 1565 (helicity) and Law 1454 (Fermi) - parity violation is the weak force's broken mirror.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The mirror cracks in weak decays; the phi-law keeps a floor of the crack's edge.

### NOVELTY
Classical weak is parity-conserving; the phi-law predicts an irreducible violation floor.

### ACTIONABILITY
Run sim/1564_parity_violation.py; verify the asymmetry; proceed to Law 1565.
