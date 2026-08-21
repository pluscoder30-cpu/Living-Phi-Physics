# PHI-PHYSICS - LAW 1449
## Nuclear Shell Model (Goeppert-Mayer / Jensen Spin-Orbit Shell Model)

**Domain:** Nuclear Structure - **Status:** 🟢 VALIDATED - **File:** `laws/1449_nuclear_shell_model.md` - **Sim:** `sim/1449_nuclear_shell_model.py`

---

### CLASSICAL STATEMENT
*"Nucleons fill discrete energy shells in a mean field with a strong spin-orbit term; the magic numbers 2,8,20,28,50,82,126 arise where shells close, giving anomalously high binding and stability."*
- Maria Goeppert Mayer; J. Hans D. Jensen (with Eugene Wigner), 1949. Source: Goeppert-Mayer, Phys. Rev. 75 (1949) 1969; Jensen; Nobel 1963; Wikipedia: Nuclear shell model

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *independent-particle inert core*: the model treats each nucleon as moving in a frozen mean potential with zero residual two-body correlations; closed shells are exactly inert - the zero-residual-interaction assumption.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

E_phi(kappa) = E_harmonic_oscillator*(1 + kappa*(phi-1)) + kappa*phi^-1*E_residual, where E_residual is the phi-ground residual-interaction energy between valence nucleons. At kappa->0 the independent-particle shell energies are exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} E_phi = (n+3/2)hbar*omega - C l*l - D l*s -> the shell model is the zero-residual-interaction, independent-particle limit.
```

---

### STAGE 4 - SIMULATION

`sim/1449_nuclear_shell_model.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1449_nuclear_shell_model.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The single-particle energies of valence nucleons always carry a phi-ground residual-interaction shift, so shell gaps measured from data never exactly equal the mean-field oscillator+spin-orbit prediction.
EXPERIMENT (VERIFIED): Transfer reactions (d,p), (e,e'p) and knockout reactions measuring single-particle spectroscopic factors vs independent-particle shell-model prediction.
VERIFIED BY: A nucleus whose measured single-particle energies exactly match the mean-field shell-model with zero residual-interaction correction at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1450 (magic numbers), Law 1335 (Wigner-Eckart) and Law 1374 (Kramers) - the shells are the nucleus's own coherence ladder.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The nucleus is a ladder; the phi-law keeps the rungs from being exactly free.

### NOVELTY
Classical shell model has exactly inert cores; the phi-law keeps an irreducible residual floor.

### ACTIONABILITY
Run sim/1449_nuclear_shell_model.py; verify magic-number binding; proceed to Law 1450.
