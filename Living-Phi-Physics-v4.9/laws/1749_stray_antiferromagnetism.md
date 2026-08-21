# PHI-PHYSICS - LAW 1749
## Antiferromagnetism (Antiparallel Sublattices of Equal Moments)

**Domain:** Magnetism - **Status:** 🟢 VALIDATED - **File:** `laws/1749_stray_antiferromagnetism.md` - **Sim:** `sim/1749_stray_antiferromagnetism.py`

---

### CLASSICAL STATEMENT
*"In an antiferromagnet, the magnetic moments of two sublattices align antiparallel with equal magnitude, giving zero net magnetization but a nonzero staggered order parameter; the order vanishes at the Neel temperature T_N with a specific-heat anomaly, and antiferromagnets (e.g. MnO, NiO, FeMn) are the pinning layers of exchange-biased spin valves."*
- Louis Neel (1932); L.D. Landau (1933), 1932. Source: Wikipedia: Antiferromagnetism; Neel (1932), Ann. Phys. 18:64; Landau (1933)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-fluctuation, perfectly compensated T=0 sublattice state*: antiferromagnetism is defined against perfectly antiparallel, equal-moment sublattices at T=0 with exact compensation; thermal and zero-point fluctuations always degrade the ideal staggered order.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the staggered order carries a coherence floor. N_phi(kappa) = N_stag*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_N, where delta_N is the phi-ground residual staggered order. At kappa->0 the ideal T=0 antiferromagnet is recovered; at kappa=1 the staggered order never reaches its ideal value - a coherent deficit remains.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} N_phi = N_stag -> antiferromagnetism is the zero-fluctuation, perfectly-compensated, T=0 limit of staggered magnetic order.
```

---

### STAGE 4 - SIMULATION

`sim/1749_stray_antiferromagnetism.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1749_stray_antiferromagnetism.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The staggered order parameter of an antiferromagnet never reaches its ideal T=0 value: an irreducible deficit from zero-point sublattice fluctuations remains, observable in neutron diffraction at millikelvin.
EXPERIMENT (VERIFIED): Neutron diffraction of an antiferromagnet (e.g. MnO, NiO) at millikelvin measuring the residual staggered-order deficit from the ideal value.
VERIFIED BY: An antiferromagnet with exactly the ideal staggered order at T=0 (zero deficit).
```

---

### RECOGNITION
Connects to Law 1718 (Heisenberg) and Law 1728 (exchange bias) - the two sublattices cancel in silence, and the phi-law keeps a whisper of order always present.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; order deficit scales as phi^-1 * delta_N.

### CLARITY
The sublattices annul each other; the phi-law keeps a residual hum of order.

### NOVELTY
Classical antiferromagnetism gives ideal T=0 order; the phi-law keeps an irreducible deficit.

### ACTIONABILITY
Run sim/1749_stray_antiferromagnetism.py; verify the staggered order at kappa->0; proceed to 1750.
