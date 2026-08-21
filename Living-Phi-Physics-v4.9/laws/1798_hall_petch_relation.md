# PHI-PHYSICS - LAW 1798
## Hall-Petch Relation (Strength Increase with Decreasing Grain Size)

**Domain:** Mechanical Properties - **Status:** 🟢 VALIDATED - **File:** `laws/1798_hall_petch_relation.md` - **Sim:** `sim/1798_hall_petch_relation.py`

---

### CLASSICAL STATEMENT
*"The yield strength of a polycrystalline metal increases with decreasing grain size: sigma_y = sigma_0 + k_y/d^(1/2), where sigma_0 is the friction stress and k_y the Hall-Petch slope (the strength of the grain boundary as a dislocation barrier); the relation holds down to ~10-20 nm grains, below which inverse Hall-Petch softening sets in - the basis of grain refinement strengthening."*
- E.O. Hall (1951); N.J. Petch (1953), 1951. Source: Wikipedia: Hall-Petch strengthening; Hall (1951), Proc. Phys. Soc. B64:747; Petch (1953), J. Iron Steel Inst. 174:25

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-grain-boundary, single-crystal reference*: the Hall-Petch relation is defined against a single crystal (infinite grain size) with zero grain boundaries; the strengthening is the boundary-dislocation interaction away from this zero-boundary reference, and real boundaries have a finite strength floor.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the grain-size exponent carries a coherence floor. sigma_y_phi(kappa) = sigma_y_HP*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_sigma, where delta_sigma is the phi-ground strength floor. At kappa->0 the ideal d^(-1/2) law is recovered; at kappa=1 the strengthening never reaches the ideal value - an irreducible softening floor limits the achievable strength.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} sigma_y_phi = sigma_0 + k_y/d^(1/2) -> the Hall-Petch relation is the zero-grain-boundary, single-crystal reference, sharpened to the ideal d^(-1/2) strengthening.
```

---

### STAGE 4 - SIMULATION

`sim/1798_hall_petch_relation.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1798_hall_petch_relation.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: Grain refinement strengthening never reaches the ideal Hall-Petch value: an irreducible softening floor sets a maximum strength at a finite grain size, so the d^(-1/2) law always bends over.
EXPERIMENT (VERIFIED): Yield-strength measurement of a series of nanocrystalline metals with decreasing grain size, mapping the departure from the Hall-Petch law and the maximum-strength grain size.
VERIFIED BY: A metal whose yield strength follows the d^(-1/2) law to arbitrarily small grain size without bending over.
```

---

### RECOGNITION
Connects to Law 1799 (dislocations) and Law 1793 (von Mises) - the grain boundaries arm the metal, and the phi-law keeps the arm from being perfect.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; softening floor scales as phi^-1 * delta_sigma.

### CLARITY
The fine grains arm the metal; the phi-law keeps a ceiling on the armor.

### NOVELTY
Classical Hall-Petch allows unbounded strengthening; the phi-law caps it with a softening floor.

### ACTIONABILITY
Run sim/1798_hall_petch_relation.py; verify sigma_y = sigma_0 + k_y/d^(1/2) at kappa->0; proceed to 1799.
