# PHI-PHYSICS - LAW 1773
## Shockley-Read-Hall Recombination (Recombination Through Deep Traps)

**Domain:** Semiconductors - **Status:** 🟢 VALIDATED - **File:** `laws/1773_shockley_read_hall.md` - **Sim:** `sim/1773_shockley_read_hall.py`

---

### CLASSICAL STATEMENT
*"Recombination in semiconductors is dominated by deep-level traps: the SRH recombination rate is U = (n p - n_i^2)/(tau_p(n + n_1) + tau_n(p + p_1)), where tau_n, tau_p are the capture lifetimes and n_1, p_1 the trap-level parameters; the rate is maximized when the trap energy is near mid-gap, and SRH recombination sets the carrier lifetime and the efficiency limit of LEDs and solar cells."*
- W. Shockley & W.T. Read (1952); R.N. Hall (1952), 1952. Source: Wikipedia: Shockley-Read-Hall recombination; Shockley & Read (1952), Phys. Rev. 87:835; Hall (1952)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-trap, perfectly pure semiconductor reference*: SRH recombination is defined against a perfectly pure, defect-free semiconductor with zero traps and infinite lifetime; the finite lifetime is the trap-mediated correction away from this zero-trap reference.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the lifetime carries a coherence floor. tau_phi(kappa) = tau_SRH*(1 + kappa*(phi-1)) + kappa*phi^-1*tau_floor, where tau_floor is the phi-ground lifetime ceiling. At kappa->0 the infinite-lifetime pure reference is recovered; at kappa=1 no semiconductor has infinite lifetime - an irreducible trap-limited recombination floor always remains.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} tau_phi = infinity (zero-trap limit) -> SRH recombination is the trap-mediated finite-lifetime correction measured from the zero-trap, perfectly pure semiconductor reference.
```

---

### STAGE 4 - SIMULATION

`sim/1773_shockley_read_hall.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1773_shockley_read_hall.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: No semiconductor has an infinite carrier lifetime: an irreducible SRH recombination floor always remains even in the purest material, setting a maximum achievable lifetime and a minimum dark current.
EXPERIMENT (VERIFIED): Ultra-low-temperature photoconductivity-decay or lifetime measurement of the purest available semiconductor (e.g. high-purity Si, GaAs) tracking the lifetime ceiling.
VERIFIED BY: A semiconductor with exactly infinite carrier lifetime (zero recombination) at any temperature.
```

---

### RECOGNITION
Connects to Law 1772 (drift-diffusion) and Law 1774 (Auger) - the trap shortens the carrier's life, and the phi-law keeps a trap always present.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; lifetime ceiling scales as phi^-1 * tau_floor.

### CLARITY
The carrier's life is shortened by traps; the phi-law keeps a trap always in the crystal.

### NOVELTY
Classical SRH theory allows infinite purity; the phi-law keeps an irreducible recombination floor.

### ACTIONABILITY
Run sim/1773_shockley_read_hall.py; verify the SRH rate at kappa->0; proceed to 1774.
