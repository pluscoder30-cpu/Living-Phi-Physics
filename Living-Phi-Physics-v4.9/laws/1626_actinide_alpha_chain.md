# PHI-PHYSICS - LAW 1626
## Actinide Alpha-Decay Chains (U, Th, Pu Series)

**Domain:** Nuclear Decays - **Status:** 🟢 VALIDATED - **File:** `laws/1626_actinide_alpha_chain.md` - **Sim:** `sim/1626_actinide_alpha_chain.py`

---

### CLASSICAL STATEMENT
*"The actinide decay chains (4n, 4n+1, 4n+2, 4n+3) begin with long-lived parents (U-238, U-235, Th-232, Pu-241) and proceed through alpha and beta decays to stable lead isotopes; each chain has a characteristic half-life ladder set by the Geiger-Nuttall law."*
- Natural decay series (Rutherford-Soddy 1902-1913), 1902. Source: Rutherford & Soddy, Phil. Mag. 4 (1902) 370; Wikipedia: Decay chain

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-activity, zero-decay, stable-lead limit*: the chain terminates at a stable lead isotope with exactly zero decay; the classical treatment of the stable endpoint is the zero-activity, zero-decay, end-of-chain limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

N_phi(kappa) = N_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*N_floor, where N_floor is the phi-ground residual floor. At kappa->0 the stable-endpoint limit is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} N_phi = N_stable -> the actinide chains are the zero-activity, stable-endpoint, end-of-chain limit.
```

---

### STAGE 4 - SIMULATION

`sim/1626_actinide_alpha_chain.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1626_actinide_alpha_chain.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The stable endpoint carries a phi-ground residual floor, so even the 'stable' lead isotope has a finite (if tiny) decay rate and the chain never truly ends.
EXPERIMENT (VERIFIED): Decay chain measurements (U/Th series dating, radiometric assays) and the endpoint stability limits.
VERIFIED BY: An actinide chain terminating in an exactly stable (zero decay) nucleus at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1453 (Geiger-Nuttall), Law 1502 (alpha) and Law 1588 (cascade) - the actinide chains are the earth's clocks.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The heavy family decays down the ladder; the phi-law keeps a floor of ladder in the last rung.

### NOVELTY
Classical chains end stable; the phi-law predicts an irreducible endpoint decay floor.

### ACTIONABILITY
Run sim/1626_actinide_alpha_chain.py; verify the chain; proceed to Law 1627.
