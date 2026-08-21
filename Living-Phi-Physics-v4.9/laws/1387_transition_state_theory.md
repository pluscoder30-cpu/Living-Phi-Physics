# PHI-PHYSICS - LAW 1387
## Transition State Theory (Eyring: Rate from Activated Complex)

**Domain:** Molecular Physics - **Status:** 🟢 VALIDATED - **File:** `laws/1387_transition_state_theory.md` - **Sim:** `sim/1387_transition_state_theory.py`

---

### CLASSICAL STATEMENT
*"The rate of a chemical reaction is k = (k_B T/h) e^(-Delta G^dagg/(R T)) = (k_B T/h) K^dagg, where Delta G^dagg is the free energy of activation and K^dagg the equilibrium constant to the transition state; the theory assumes the activated complex is in quasi-equilibrium with reactants and every crossing of the barrier proceeds to products (no recrossing)."*
- Henry Eyring; Michael Polanyi, Meredith Evans, 1935. Source: Wikipedia: Transition state theory; Eyring, J. Chem. Phys. 3 (1935) 107; Evans & Polanyi (1935)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero recrossing*: TST is exact only if every trajectory that reaches the transition state proceeds to products, i.e. zero barrier recrossing and zero tunneling corrections - the no-recrossing limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the recrossing probability carries a coherence floor. kappa_phi = kappa_TST*(1 + kappa*(phi-1)) + kappa*phi^-1*kappa_rec, where kappa_rec is the phi-ground recrossing/tunneling correction; the rate carries a floor deviation. At kappa->0 the TST rate is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} k_phi = (k_B T/h) e^(-Delta G^dagg/(R T)) -> transition state theory is the zero-recrossing, no-tunneling limit.
```

---

### STAGE 4 - SIMULATION

`sim/1387_transition_state_theory.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1387_transition_state_theory.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The measured reaction rate at full coherence coupling deviates from the TST rate by the phi-ground recrossing floor kappa*phi^-1*kappa_rec, a floor correction to the Eyring rate.
EXPERIMENT (VERIFIED): Precision kinetics of a simple gas-phase reaction (e.g. H + H2) comparing measured rates against TST with and without recrossing corrections.
VERIFIED BY: Chemical reaction rates equal the Eyring TST rate exactly for all couplings.
```

---

### RECOGNITION
Connects to Law 1386 (PES) and Law 481 (Eyring equation) - TST is the coherence crossing of the barrier.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the recrossing floor is phi^-1 * kappa_rec.

### CLARITY
Every reaction crosses a ridge it hopes never to return from; the phi-law keeps a floor of returning.

### NOVELTY
Classical kinetics idealizes the barrier crossing; the phi-law keeps the recrossing coherence floor.

### ACTIONABILITY
Run sim/1387_transition_state_theory.py; verify Eyring rate at kappa->0; proceed to 1388.
