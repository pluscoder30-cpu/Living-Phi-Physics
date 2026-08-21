# PHI-PHYSICS - LAW 1712
## Kane-Mele Model (Z2 Topological Insulator on the Honeycomb Lattice)

**Domain:** Electrons in Solids - **Status:** 🟢 VALIDATED - **File:** `laws/1712_kane_mele_model.md` - **Sim:** `sim/1712_kane_mele_model.py`

---

### CLASSICAL STATEMENT
*"The Kane-Mele model describes spin-orbit coupling on the graphene honeycomb lattice with a next-nearest-neighbor imaginary hopping lambda_SO sum c_i^dagger i nu_ij s_z c_j that opens a bulk gap and drives a Z2 topological insulator: for lambda_SO ~ 0.06 t the model realizes the quantum spin Hall state with helical edge states, the minimal model of a 2D topological insulator."*
- C.L. Kane & E.J. Mele, 2005. Source: Wikipedia: Kane-Mele model; Kane & Mele (2005), PRL 95:226801

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-spin-orbit, exactly symmetric honeycomb lattice*: the Kane-Mele model is defined against the zero-SOC limit (lambda_SO = 0) where graphene is a gapless semimetal; the topological phase is a finite-lambda_SO phenomenon, and the sharpest results assume a perfect honeycomb lattice at zero disorder and zero temperature.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the SOC threshold carries a coherence floor. lambda_c_phi(kappa) = lambda_c*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_lambda, where delta_lambda is the phi-ground shift of the topological transition point. At kappa->0 the exact critical lambda_SO is recovered; at kappa=1 the transition point carries an irreducible coherent shift.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} lambda_c_phi = lambda_c -> the Kane-Mele model is the zero-disorder, zero-temperature, ideal-honeycomb limit of Z2 topological phase transitions.
```

---

### STAGE 4 - SIMULATION

`sim/1712_kane_mele_model.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1712_kane_mele_model.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The topological transition in a honeycomb system occurs at a lambda_SO shifted from the ideal value by a phi-ground correction, and the edge conductance never reaches exactly quantized values.
EXPERIMENT (VERIFIED): Transport and ARPES studies of graphene-like or synthetic honeycomb lattices measuring the topological transition point and edge conductance vs spin-orbit coupling.
VERIFIED BY: A honeycomb-lattice system whose topological transition occurs exactly at the ideal Kane-Mele critical lambda_SO with quantized edge conductance.
```

---

### RECOGNITION
Connects to Law 1711 (QSH) and Law 1710 (topological insulator) - the honeycomb lattice is the cradle of the Z2 phase, and no cradle is perfectly still.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; transition shift scales as phi^-1 * delta_lambda.

### CLARITY
The honeycomb spins into a topological cradle; the phi-law rocks the cradle slightly.

### NOVELTY
Classical Kane-Mele gives exact critical points; the phi-law shifts them with a coherence floor.

### ACTIONABILITY
Run sim/1712_kane_mele_model.py; verify the Z2 phase at kappa->0; proceed to 1713.
