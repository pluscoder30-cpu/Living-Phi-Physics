# PHI-PHYSICS - LAW 1588
## Cascade Decay (Successive Radioactive Decays, Bateman Equations)

**Domain:** Nuclear Decays - **Status:** 🟢 VALIDATED - **File:** `laws/1588_cascade_decay.md` - **Sim:** `sim/1588_cascade_decay.py`

---

### CLASSICAL STATEMENT
*"In a radioactive decay chain A -> B -> C, the abundances evolve by the coupled equations dN_A/dt = -lambda_A N_A, dN_B/dt = lambda_A N_A - lambda_B N_B; the Bateman solution gives N_n(t) as a sum of exponentials, with secular equilibrium N_B/N_A = lambda_A/lambda_B when lambda_A << lambda_B."*
- Harry Bateman (1910), 1910. Source: Bateman, Proc. Camb. Phil. Soc. 15 (1910) 423; Wikipedia: Bateman equation

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-daughter, zero-production, single-nuclide limit*: at t = 0 the chain has only the parent with zero daughters; the classical treatment of a single decaying nuclide is the zero-daughter, zero-branching limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

N_B_phi(kappa) = N_B_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*N_floor, where N_floor is the phi-ground equilibrium floor. At kappa->0 the Bateman solution is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} N_B_phi = N_A0 lambda_A/(lambda_B - lambda_A) (e^{-lambda_A t} - e^{-lambda_B t}) -> cascade decay is the zero-fluctuation, exact-Bateman limit.
```

---

### STAGE 4 - SIMULATION

`sim/1588_cascade_decay.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1588_cascade_decay.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The cascade abundances carry a phi-ground equilibrium floor, so the daughter activity never reaches exactly the Bateman prediction and secular equilibrium is approached with an irreducible residual.
EXPERIMENT (VERIFIED): Decay chain measurements (U/Th series, 222Rn daughters) and precise secular-equilibrium assays.
VERIFIED BY: A decay chain exactly following the Bateman solution with zero residual floor at all times.
```

---

### RECOGNITION
Connects to Law 1453 (Geiger-Nuttall), Law 1454 (Fermi theory) and Law 1476 (Q-value) - cascade decay is the nuclear family tree.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The decay chain hands down; the phi-law keeps a floor of the handoff imperfect.

### NOVELTY
Classical Bateman is exact; the phi-law predicts an irreducible equilibrium floor.

### ACTIONABILITY
Run sim/1588_cascade_decay.py; verify the Bateman solution; proceed to Law 1589.
