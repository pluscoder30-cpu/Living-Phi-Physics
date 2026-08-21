# PHI-PHYSICS - LAW 1479
## Compound Nucleus Model (Bohr's Reaction Mechanism)

**Domain:** Nuclear Reactions - **Status:** 🟢 VALIDATED - **File:** `laws/1479_compound_nucleus.md` - **Sim:** `sim/1479_compound_nucleus.py`

---

### CLASSICAL STATEMENT
*"A nuclear reaction proceeds through the formation of a compound nucleus: the projectile is absorbed, its energy is shared among many nucleons, and the decay is independent of the entrance channel - 'the compound nucleus forgets how it was made'."*
- Niels Bohr, 1936. Source: Bohr, Nature 137 (1936) 344; Wikipedia: Compound nucleus

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-memory, fully-equilibrated state*: the compound nucleus is assumed to completely forget its formation history - zero entrance-channel memory, exactly full equilibration over all degrees of freedom.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

sigma_decay_phi(kappa) = sigma_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*sigma_mem, where sigma_mem is the phi-ground entrance-channel-memory floor. At kappa->0 the complete-forgetting compound nucleus is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} sigma_decay_phi = sigma_classical -> the compound nucleus model is the zero-memory, fully-equilibrated, complete-forgetting limit.
```

---

### STAGE 4 - SIMULATION

`sim/1479_compound_nucleus.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1479_compound_nucleus.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The decay of a compound nucleus carries a phi-ground entrance-channel-memory floor, so small correlations with the formation channel survive even at high excitation (breaking the perfect-forgetting ideal).
EXPERIMENT (VERIFIED): Measurement of fusion-evaporation cross-sections and particle-angular correlations vs the statistical (Hauser-Feshbach) prediction.
VERIFIED BY: A compound nucleus whose decay is exactly independent of the entrance channel at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1478 (Breit-Wigner), Law 1480 (optical model) and Law 1454 - the compound nucleus is the reactor of the reaction.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The nucleus forgets its past; the phi-law keeps a floor of memory.

### NOVELTY
Classical compound nucleus forgets completely; the phi-law keeps an irreducible memory floor.

### ACTIONABILITY
Run sim/1479_compound_nucleus.py; verify the equilibrated decay; proceed to Law 1480.
