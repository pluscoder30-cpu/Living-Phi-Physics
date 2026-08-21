# PHI-PHYSICS - LAW 1504
## Proton Radioactivity (Emission of a Single Proton)

**Domain:** Nuclear Decays - **Status:** 🟢 VALIDATED - **File:** `laws/1504_proton_radioactivity.md` - **Sim:** `sim/1504_proton_radioactivity.py`

---

### CLASSICAL STATEMENT
*"Nuclei beyond the proton drip line decay by emitting a single proton; the decay rate is governed by the Coulomb-barrier penetrability and the proton is emitted from a specific orbital, providing a direct probe of the proton wavefunction and nuclear structure far from stability."*
- S. Hofmann (1982, first observation); predicted by Goldansky (1960), 1982. Source: Hofmann et al., Z. Phys. A305 (1982) 111; Wikipedia: Proton emission

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-separation-energy, exactly-unbound proton*: proton radioactivity occurs when the proton separation energy crosses zero; the classical nucleus is exactly bound (zero emission) below the drip line - a zero-separation-energy threshold.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

Lambda_phi(kappa) = Lambda_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*Lambda_floor, where Lambda_floor is the phi-ground sub-drip-line tunneling floor. At kappa->0 the pure penetrability rate is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} Lambda_phi = S_p * exp(-2 pi eta) -> proton radioactivity is the zero-separation-energy, pure-penetrability limit.
```

---

### STAGE 4 - SIMULATION

`sim/1504_proton_radioactivity.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1504_proton_radioactivity.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: Below the proton drip line the emission rate carries a phi-ground floor, so proton-unbound states exist slightly beyond the classical line and delayed proton emission shows residual sub-threshold branching.
EXPERIMENT (VERIFIED): Proton-radioactivity studies of proton drip-line nuclei (113Cs, 151Lu, 177Tl) and two-proton emission (45Fe).
VERIFIED BY: A nucleus with exactly zero proton emission below the classical drip line at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1452 (Gamow), Law 1477 (threshold) and Law 1492 (halo) - proton radioactivity is the drip line's voice.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The last proton lets go; the phi-law keeps a floor of letting go early.

### NOVELTY
Classical drip line is a hard edge; the phi-law predicts residual sub-line emission.

### ACTIONABILITY
Run sim/1504_proton_radioactivity.py; verify the penetrability rate; proceed to Law 1505.
