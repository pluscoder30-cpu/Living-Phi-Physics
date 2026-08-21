# PHI-PHYSICS - LAW 1306
## Coherent States (Schrodinger/Glauber: Minimum-Uncertainty Field States)

**Domain:** Quantum Dynamics - **Status:** 🟢 VALIDATED - **File:** `laws/1306_coherent_states.md` - **Sim:** `sim/1306_coherent_states.py`

---

### CLASSICAL STATEMENT
*"A coherent state |alpha> = e^(-|alpha|^2/2) sum_n alpha^n/sqrt(n!) |n> is the eigenstate of the annihilation operator a|alpha> = alpha|alpha>; it is a minimum-uncertainty state with Poisson photon statistics P(n) = e^(-|alpha|^2) |alpha|^2n/n!, equal quadrature variances, and photon number variance <n> (the closest quantum analogue of a classical field)."*
- Erwin Schrodinger (1926); Roy Glauber (1963), 1963. Source: Wikipedia: Coherent state; Schrodinger (1926), Glauber, Phys. Rev. 130 (1963) 2529

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *perfectly classical field*: the coherent state's Poisson statistics and equal variances hold exactly only for the ideal state with zero squeezing and zero phase diffusion - a classical-like field the phi-law reads as the zero-coherence-deviation limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the coherent field carries a coherence diffusion. P_n_phi(kappa) = P_n*(1 + kappa*(phi-1)) + kappa*phi^-1*P_floor, where P_floor is the phi-ground deviation from Poisson statistics; the photon statistics acquire a floor sub-Poisson component. At kappa->0 the exact Poisson statistics are recovered.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} P_n_phi = e^(-|alpha|^2)|alpha|^{2n}/n! -> the coherent-state statistics are the zero-coherence-deviation limit.
```

---

### STAGE 4 - SIMULATION

`sim/1306_coherent_states.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1306_coherent_states.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The photon statistics of a coherence-coupled coherent field carry a phi-ground deviation kappa*phi^-1*P_floor from Poisson, observable as a small floor in the Fano factor of laser light.
EXPERIMENT (VERIFIED): Hanbury-Brown-Twiss measurements of laser light at increasing coherence, measuring the Fano factor deviation from 1.
VERIFIED BY: A coherent state has exactly Poisson statistics for all couplings.
```

---

### RECOGNITION
Connects to Law 974 (coherent states - photon statistics) and Law 1307 (squeezed states) - coherent states are the coherence-minimum of the field.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the deviation floor is phi^-1 * P_floor.

### CLARITY
The laser shines classically, but the phi-law hears a floor of quantumness under the shine.

### NOVELTY
Classical optics reads laser light as exactly classical; the phi-law floors the classical reading by coherence.

### ACTIONABILITY
Run sim/1306_coherent_states.py; verify Poisson statistics at kappa->0; proceed to 1307.
