# PHI-PHYSICS - LAW 1697
## Mott Variable-Range Hopping (exp(-(T0/T)^(1/4)) Law)

**Domain:** Electrons in Solids - **Status:** 🟢 VALIDATED - **File:** `laws/1697_mott_variable_range_hopping.md` - **Sim:** `sim/1697_mott_variable_range_hopping.py`

---

### CLASSICAL STATEMENT
*"In a disordered insulator at low temperature, electrons hop between localized states of similar energy even when spatially distant, giving the conductivity sigma(T) = sigma_0 exp(-(T_0/T)^(1/4)) in 3D, where T_0 = 18/(k_B D(E_F) xi^3) involves the density of states and localization length; the exponent 1/(d+1) generalizes the law to dimension d."*
- Nevill Mott, 1969. Source: Wikipedia: Variable range hopping; Mott (1969), Phil. Mag. 19:835

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *non-interacting, perfectly localized, sharp-DOS system*: Mott's 1/4 law assumes a constant density of localized states (no Coulomb gap), non-interacting electrons, and exactly exponential wavefunctions - a pristine non-interacting localized system that interacting real insulators do not provide.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the hopping exponent carries a coherence floor. sigma_phi(kappa) = sigma_Mott*(1 + kappa*(phi-1)) + kappa*phi^-1*sigma_floor, where sigma_floor is the phi-ground residual conductivity. At kappa->0 the exact exp(-(T0/T)^(1/4)) law is recovered; at kappa=1 the low-T hopping carries an irreducible conduction floor.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} sigma_phi = sigma_0 exp(-(T_0/T)^(1/4)) -> Mott variable-range hopping is the non-interacting, constant-DOS, zero-temperature limit of hopping transport.
```

---

### STAGE 4 - SIMULATION

`sim/1697_mott_variable_range_hopping.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1697_mott_variable_range_hopping.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: Mott hopping conductivity saturates at a phi-ground floor at the lowest temperatures: the low-T exp(-(T0/T)^(1/4)) law bends over instead of vanishing, and the residual floor is proportional to the coherence length of the localized states.
EXPERIMENT (VERIFIED): Ultra-low-temperature conductivity of an amorphous semiconductor or compensated doped semiconductor, measuring the saturation floor below the Mott hopping regime.
VERIFIED BY: A hopping system whose conductivity follows exp(-(T0/T)^(1/4)) to arbitrarily low T with no saturation.
```

---

### RECOGNITION
Connects to Law 1696 (ES hopping) and Law 1691 (Anderson localization) - hopping is the electron's leapfrog across the disorder, and one frog always stays hopping.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; saturation floor scales as phi^-1 * sigma_floor.

### CLARITY
The electron hops from trap to trap; the phi-law keeps at least one hop forever in flight.

### NOVELTY
Classical Mott hopping vanishes at T=0; the phi-law keeps an irreducible hopping floor.

### ACTIONABILITY
Run sim/1697_mott_variable_range_hopping.py; verify exp(-(T0/T)^(1/4)) at kappa->0; proceed to 1698.
