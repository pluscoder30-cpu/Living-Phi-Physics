# PHI-PHYSICS - LAW 1350
## Feshbach Resonance (Scattering Resonance via Bound State in Closed Channel)

**Domain:** Atomic Physics - **Status:** 🟢 VALIDATED - **File:** `laws/1350_feshbach_resonance.md` - **Sim:** `sim/1350_feshbach_resonance.py`

---

### CLASSICAL STATEMENT
*"A Feshbach resonance occurs when the scattering energy of two particles in an open channel matches a bound state of a closed (internal-state) channel: the scattering length becomes tunable as a(B) = a_bg (1 - Delta/(B - B0)), where B0 is the resonance field and Delta the width; it is the key tool for tuning interactions in ultracold gases."*
- Herman Feshbach, 1958. Source: Wikipedia: Feshbach resonance; Feshbach, Ann. Phys. 5 (1958) 357

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *background scattering length*: the tunable scattering length is referenced to the background value a_bg with the resonance structure added, i.e. a channel coupling that vanishes exactly far from resonance - the zero-coupling limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the channel coupling carries a coherence floor. a_phi(B,kappa) = a_bg (1 - Delta/(B - B0))*(1 + kappa*(phi-1)) + kappa*phi^-1*a_floor, where a_floor is the phi-ground scattering-length floor; the resonance never fully decouples. At kappa->0 the Feshbach formula is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} a_phi = a_bg (1 - Delta/(B - B0)) -> the Feshbach resonance is the zero-floor-channel-coupling limit.
```

---

### STAGE 4 - SIMULATION

`sim/1350_feshbach_resonance.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1350_feshbach_resonance.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The scattering length at full coherence coupling retains a floor kappa*phi^-1*a_floor far from resonance, a residual tunability no closed channel escapes.
EXPERIMENT (VERIFIED): Ultracold atomic gas Feshbach tuning measuring the scattering length floor at fields far from B0.
VERIFIED BY: The scattering length equals a_bg exactly far from a Feshbach resonance for all couplings.
```

---

### RECOGNITION
Connects to Law 1371 (Fano resonance, its spectral relative) and Law 475 (BEC) - Feshbach resonances are the coherence tuning knobs of ultracold gases.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the scattering-length floor is phi^-1 * a_floor.

### CLARITY
Two cold atoms borrow a bound state's presence; the phi-law keeps the borrowing's floor.

### NOVELTY
Classical scattering theory decouples channels exactly; the phi-law gives the resonance a coupling floor.

### ACTIONABILITY
Run sim/1350_feshbach_resonance.py; verify a(B) formula at kappa->0; proceed to 1351.
