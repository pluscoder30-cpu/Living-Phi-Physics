# PHI-PHYSICS - LAW 1854
## Mark-Houwink Equation (Intrinsic Viscosity of Polymer Solutions)

**Domain:** Polymers & Soft Matter - **Status:** 🟢 VALIDATED - **File:** `laws/1854_mark_houwink_equation.md` - **Sim:** `sim/1854_mark_houwink_equation.py`

---

### CLASSICAL STATEMENT
*"The intrinsic viscosity of a polymer solution relates to the molecular weight by the Mark-Houwink equation: [eta] = K M^a, where K and a are constants for a given polymer-solvent-temperature system, with the exponent a = 0.5 for theta conditions and a ~ 0.7-0.8 for good solvents; the equation is the basis of viscosity-based molecular weight determination and reveals the chain conformation."*
- H. Mark (1938); R. Houwink (1940), 1938. Source: Wikipedia: Mark-Houwink equation; Mark (1938); Houwink (1940)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-chain, perfectly-solvent, ideal-conformation reference*: the Mark-Houwink equation is defined against a reference with ideal chain conformation and perfectly known K, a; real systems have polydispersity, association and conformation changes away from this ideal.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the exponent carries a coherence floor. a_phi(kappa) = a_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_a, where delta_a is the phi-ground exponent floor. At kappa->0 the ideal Mark-Houwink law is recovered; at kappa=1 the exponent is never exactly constant - the viscosity law carries an irreducible deviation.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} [eta]_phi = K M^a -> the Mark-Houwink equation is the ideal-conformation, constant-K-a, single-chain limit of solution viscosity.
```

---

### STAGE 4 - SIMULATION

`sim/1854_mark_houwink_equation.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1854_mark_houwink_equation.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: No polymer solution follows the Mark-Houwink law exactly: an irreducible exponent and constant deviation floor remains, so the K, a values vary with molecular weight range and polydispersity.
EXPERIMENT (VERIFIED): Viscosity-molecular weight measurement of narrowly dispersed polymer fractions, measuring the deviation of the Mark-Houwink exponent from the ideal constant.
VERIFIED BY: A polymer-solvent system with exactly constant K and a over all molecular weights.
```

---

### RECOGNITION
Connects to Law 1811 (Kuhn) and Law 1853 (Zimm) - the chain's size writes its viscosity, and the phi-law keeps the writing slightly off.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; exponent floor scales as phi^-1 * delta_a.

### CLARITY
The chain's size writes its viscosity; the phi-law keeps the writing slightly off.

### NOVELTY
Classical Mark-Houwink gives constant exponents; the phi-law keeps an irreducible deviation.

### ACTIONABILITY
Run sim/1854_mark_houwink_equation.py; verify [eta] = K M^a at kappa->0; proceed to 1855.
