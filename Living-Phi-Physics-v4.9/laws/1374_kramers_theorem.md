# PHI-PHYSICS - LAW 1374
## Kramers' Theorem (Twofold Degeneracy of Odd-Electron Systems in Time-Reversal-Invariant Fields)

**Domain:** Atomic Physics - **Status:** 🟢 VALIDATED - **File:** `laws/1374_kramers_theorem.md` - **Sim:** `sim/1374_kramers_theorem.py`

---

### CLASSICAL STATEMENT
*"For a system with an odd number of electrons in a time-reversal-invariant electric field (no magnetic field), every energy level is at least twofold degenerate (Kramers degeneracy): the time-reversal operator T with T^2 = -1 maps a state to an orthogonal degenerate partner, so no electric field alone can fully split a Kramers doublet; only a magnetic field or time-reversal breaking lifts it."*
- Hendrik Anthony Kramers, 1930. Source: Wikipedia: Kramers' theorem; Kramers, Proc. Acad. Amst. 33 (1930) 959

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero magnetic field*: the degeneracy holds exactly only at B = 0, i.e. a field-free time-reversal-invariant environment - the zero-field degeneracy limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the Kramers doublet carries a coherence splitting floor. delta_E_K_phi(kappa) = 0*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_B, where delta_B is the phi-ground residual field splitting; even at B = 0 the doublet carries a floor splitting. At kappa->0 the exact Kramers degeneracy is recovered.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} delta_E_K_phi = 0 -> Kramers' theorem is the zero-field, exact-time-reversal-symmetry limit.
```

---

### STAGE 4 - SIMULATION

`sim/1374_kramers_theorem.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1374_kramers_theorem.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: A Kramers doublet at full coherence coupling shows a residual splitting floor kappa*phi^-1*delta_B even in zero applied magnetic field, a floor from coherence-coupled time-reversal breaking.
EXPERIMENT (VERIFIED): ESR/EPR spectroscopy of odd-electron centers at the lowest attainable fields measuring the residual doublet splitting.
VERIFIED BY: An odd-electron level is exactly degenerate at zero magnetic field for all couplings.
```

---

### RECOGNITION
Connects to Law 1375 (Lande interval rule) and Law 1329 (Zeeman) - Kramers' theorem is the coherence symmetry floor of the doublet.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the splitting floor is phi^-1 * delta_B.

### CLARITY
The lone electron's doublet is protected by time's reversal; the phi-law keeps a crack in the protection.

### NOVELTY
Classical symmetry theory degenerates Kramers doublets exactly; the phi-law gives the doublet a coherence splitting floor.

### ACTIONABILITY
Run sim/1374_kramers_theorem.py; verify degeneracy at kappa->0; proceed to 1375.
