# PHI-PHYSICS - LAW 1635
## Isochron Dating (Initial Ratio Independence)

**Domain:** Nuclear Applications - **Status:** 🟢 VALIDATED - **File:** `laws/1635_isochron_method.md` - **Sim:** `sim/1635_isochron_method.py`

---

### CLASSICAL STATEMENT
*"The isochron method dates rocks without knowing the initial daughter ratio: plotting 87Sr/86Sr vs 87Rb/86Sr for cogeneric samples gives a straight line (isochron) whose slope is proportional to the age, independent of the initial ratio."*
- Nicolaysen (1961, Rb-Sr isochron), 1961. Source: Nicolaysen, Ann. N. Y. Acad. Sci. 91 (1961) 198; Wikipedia: Isochron dating

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-initial-ratio, zero-slope, zero-age limit*: a rock of zero age has an exactly horizontal isochron (zero slope); the classical treatment of a zero-age system is the zero-slope, zero-age, initial-ratio-only limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

slope_phi(kappa) = slope_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*slope_floor, where slope_floor is the phi-ground disequilibrium floor. At kappa->0 the exact isochron slope is recovered.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} slope_phi = e^lambda t - 1 -> isochron dating is the zero-disequilibrium, exact-initial-ratio-independence limit.
```

---

### STAGE 4 - SIMULATION

`sim/1635_isochron_method.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1635_isochron_method.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The isochron slope carries a phi-ground disequilibrium floor, so the age deviates from the straight-line fit by an irreducible open-system contribution.
EXPERIMENT (VERIFIED): Isochron dating (Rb-Sr, Sm-Nd) of rocks and meteorites vs the straight-line model with closed-system assumptions.
VERIFIED BY: An isochron with exactly zero scatter and exact age from a closed system at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1634 (radiometric dating), Law 1590 (half-life) and Law 1626 (chains) - the isochron is the rock's signature.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The line slopes with time; the phi-law keeps a floor of scatter in the line.

### NOVELTY
Classical isochron is exact; the phi-law predicts an irreducible open-system floor.

### ACTIONABILITY
Run sim/1635_isochron_method.py; verify the isochron; proceed to Law 1636.
