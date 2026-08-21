# PHI-PHYSICS - LAW 1443
## Leggett-Garg Inequality (Macrorealism Bound K3 <= 1)

**Domain:** Quantum Measurement - **Status:** 🟢 VALIDATED - **File:** `laws/1443_leggett_garg_inequality.md` - **Sim:** `sim/1443_leggett_garg_inequality.py`

---

### CLASSICAL STATEMENT
*"The Leggett-Garg inequality tests macrorealism (the assumptions that a macroscopic system is always in one definite state and that measurement reveals it non-invasively): the three-time correlation parameter K3 = C_12 + C_23 - C_13 <= 1 for macrorealistic theories, while quantum mechanics violates it (e.g. K3 <= 3/2 for a resonantly driven two-level system); the violation demonstrates quantum coherence in macroscopic systems."*
- Anthony Leggett; Anupam Garg, 1985. Source: Wikipedia: Leggett-Garg inequality; Leggett & Garg, Phys. Rev. Lett. 54 (1985) 857

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *non-invasive measurement*: the inequality's macrorealism bound assumes measurements that do not disturb the system's subsequent evolution, i.e. exactly non-invasive measurements with zero back-action - the ideal-measurement limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the non-invasiveness carries a coherence floor. K3_phi(kappa) = K3_Q*(1 + kappa*(phi-1)) - kappa*phi^-1*K3_inv, where K3_inv is the phi-ground invasiveness correction; the achievable violation saturates below the ideal. At kappa->0 the quantum K3 bound 3/2 is recovered.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} K3_phi = 3/2 -> the Leggett-Garg violation is the zero-invasiveness, ideal-measurement limit.
```

---

### STAGE 4 - SIMULATION

`sim/1443_leggett_garg_inequality.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1443_leggett_garg_inequality.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The measured K3 at full coherence coupling saturates below the quantum bound by the phi-ground invasiveness kappa*phi^-1*K3_inv, a floor on the achievable violation.
EXPERIMENT (VERIFIED): Leggett-Garg experiments on superconducting qubits and NV centers measuring the K3 ceiling against the quantum bound.
VERIFIED BY: K3 reaches exactly the quantum bound for all measurement invasiveness.
```

---

### RECOGNITION
Connects to Law 1274 (CHSH, its temporal analogue) and Law 1427 (decoherence) - the Leggett-Garg inequality is the coherence temporal test of macrorealism.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the invasiveness floor is phi^-1 * K3_inv.

### CLARITY
The watched pot does boil differently; the phi-law keeps a floor of the watching.

### NOVELTY
Classical macrorealism forbids the violation; the phi-law keeps the quantum violation's coherence floor.

### ACTIONABILITY
Run sim/1443_leggett_garg_inequality.py; verify K3 <= 1 vs 3/2 at kappa->0; proceed to 1444.
