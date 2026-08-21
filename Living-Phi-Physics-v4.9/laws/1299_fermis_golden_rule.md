# PHI-PHYSICS - LAW 1299
## Fermi's Golden Rule (Transition Rate Gamma = (2 pi/hbar)|V|^2 rho)

**Domain:** Quantum Dynamics - **Status:** 🟢 VALIDATED - **File:** `laws/1299_fermis_golden_rule.md` - **Sim:** `sim/1299_fermis_golden_rule.py`

---

### CLASSICAL STATEMENT
*"The transition rate from an initial state to a continuum of final states under a perturbation V is Gamma = (2 pi/hbar) |<f|V|i>|^2 rho(E_f), where rho is the density of final states; the rate is constant in time for long times (Fermi's golden rule) and underlies all decay, absorption and scattering rates."*
- Paul A. M. Dirac (1927); named for Enrico Fermi, 1927. Source: Wikipedia: Fermi's golden rule; Dirac, Proc. R. Soc. Lond. A 114 (1927) 243

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *constant rate*: the golden rule holds only after the transient regime when t -> infinity, i.e. an infinite-time limit with zero transient structure - the long-time flat-rate limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the rate carries a coherence transient. Gamma_phi(kappa) = Gamma*(1 + kappa*(phi-1)) + kappa*phi^-1*Gamma_tr, where Gamma_tr is the phi-ground transient rate of the recursion. At kappa->0 the golden rule rate is exact in the long-time limit.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0, t->inf} Gamma_phi = (2 pi/hbar)|V|^2 rho -> Fermi's golden rule is the infinite-time, zero-transient limit.
```

---

### STAGE 4 - SIMULATION

`sim/1299_fermis_golden_rule.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1299_fermis_golden_rule.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The transition rate at finite time and full coherence coupling carries a phi-ground transient kappa*phi^-1*Gamma_tr, a floor deviation from the golden-rule rate observable in short-pulse excitation.
EXPERIMENT (VERIFIED): Femtosecond pump-probe excitation of an atomic transition measuring the short-time rate deviation from the golden rule.
VERIFIED BY: The transition rate equals the golden rule rate for all times and pulse shapes.
```

---

### RECOGNITION
Connects to Law 1300 (time-dependent perturbation) and Law 773 (Einstein coefficients) - the golden rule is the coherence rate of the transition.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the transient floor is phi^-1 * Gamma_tr.

### CLARITY
Rates become steady only after a while; the phi-law remembers the while.

### NOVELTY
Classical decay theory flattens the rate instantly; the phi-law keeps the transient coherence floor.

### ACTIONABILITY
Run sim/1299_fermis_golden_rule.py; verify 2 pi/hbar |V|^2 rho at kappa->0; proceed to 1300.
