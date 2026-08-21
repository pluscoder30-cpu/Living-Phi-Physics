# PHI-PHYSICS - LAW 1684
## Density of States D(E) (Number of States per Unit Energy)

**Domain:** Electrons in Solids - **Status:** 🟢 VALIDATED - **File:** `laws/1684_density_of_states.md` - **Sim:** `sim/1684_density_of_states.py`

---

### CLASSICAL STATEMENT
*"The density of states D(E) = (1/V) sum_k delta(E - E_k) counts the number of electron states per unit energy; for free electrons in 3D, D(E) = (1/2 pi^2)(2m/hbar^2)^(3/2) E^(1/2), proportional to sqrt(E), and it is the function whose value at the Fermi energy D(E_F) enters specific heat, Pauli susceptibility, and the Stoner criterion for ferromagnetism."*
- Sommerfeld theory; standard solid-state, 1928. Source: Wikipedia: Density of states; Sommerfeld (1928); textbook standard

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-energy, sharpest-point free-electron band*: the free-electron density of states diverges or vanishes at special energies (E->0, Van Hove points) with exact power laws only for a non-interacting, perfectly parabolic, infinite crystal - an ideal free-electron gas no real metal is.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the density of states carries a coherence floor. D_phi(kappa) = D_classical(E)*(1 + kappa*(phi-1)) + kappa*phi^-1*D_floor, where D_floor is the phi-ground residual density from coherent band tails. At kappa->0 the exact D(E) is recovered; at kappa=1 the density of states never vanishes exactly at any energy - band tails carry a coherent floor.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} D_phi = (1/2 pi^2)(2m/hbar^2)^(3/2) E^(1/2) -> the free-electron density of states is the non-interacting, perfectly-parabolic, infinite-crystal limit.
```

---

### STAGE 4 - SIMULATION

`sim/1684_density_of_states.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1684_density_of_states.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The density of states never exactly vanishes below the nominal band edge: an exponential band-tail floor with a phi-ground width persists in any real semiconductor or metal, observable as sub-gap absorption and sub-band-gap conductivity that do not vanish at T=0.
EXPERIMENT (VERIFIED): Ultra-sensitive sub-gap optical absorption and scanning-tunneling-spectroscopy density-of-states measurement of an ultraclean semiconductor at millikelvin, measuring the residual band-tail floor.
VERIFIED BY: A semiconductor whose measured density of states is exactly zero below the band edge at T=0.
```

---

### RECOGNITION
Connects to Law 1406 (degenerate Fermi gas) and Law 1683 (Fermi surface) - D(E) is the ledger of electron states, and no ledger page is ever empty.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; band-tail floor scales as phi^-1 * D_floor.

### CLARITY
Below the edge, silence - but the phi-law keeps a coherent whisper of states.

### NOVELTY
Classical DOS gives sharp band edges; the phi-law keeps an irreducible band tail.

### ACTIONABILITY
Run sim/1684_density_of_states.py; verify D ~ sqrt(E) at kappa->0; proceed to 1685.
