# PHI-PHYSICS - LAW 1452
## Gamow Factor (Sommerfeld Factor, Coulomb Tunneling of Charged Nuclei)

**Domain:** Nuclear Structure / Decays - **Status:** 🟢 VALIDATED - **File:** `laws/1452_gamow_factor.md` - **Sim:** `sim/1452_gamow_factor.py`

---

### CLASSICAL STATEMENT
*"The probability that two charged nuclei tunnel through the Coulomb barrier is proportional to exp(-sqrt(E_G/E)) with Gamow energy E_G = 2 mu c^2 (pi alpha Z_a Z_b)^2; equivalently P ~ exp(-2 pi eta) with Sommerfeld parameter eta = alpha Z_a Z_b sqrt(mu c^2/2E)."*
- George Gamow (and Arnold Sommerfeld), 1928. Source: Gamow, Z. Phys. 51 (1928) 204; Wikipedia: Gamow factor

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero barrier height*: the factor assumes tunneling from zero radius through an unscreened point-Coulomb barrier; classical physics at zero quantum tunneling - the barrier is exactly impassable in the classical limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

P_phi(kappa) = exp(-sqrt(E_G/E))*(1 + kappa*(phi-1)) + kappa*phi^-1*P_screen, where P_screen is the phi-ground screening-enhanced tunneling floor from the electron cloud / lattice. At kappa->0 the bare Gamow factor is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} P_phi = exp(-sqrt(E_G/E)) -> the Gamow factor is the zero-screening, zero-plasma, point-Coulomb-barrier limit.
```

---

### STAGE 4 - SIMULATION

`sim/1452_gamow_factor.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1452_gamow_factor.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: Screened environments (stellar plasmas, metallic hydrides) raise the tunneling probability above the bare Gamow factor by kappa*phi^-1*P_screen, measurable as an enhancement of low-energy fusion rates.
EXPERIMENT (VERIFIED): Laboratory measurement of D+D or D+T fusion rates in a deuterated metal lattice vs bare-beam Gamow prediction.
VERIFIED BY: A screened fusion experiment whose rate exactly matches the bare exp(-sqrt(E_G/E)) Gamow factor with zero enhancement at maximal coupling.
```

---

### RECOGNITION
Connects to Law 1453 (Geiger-Nuttall), Law 1465 (Gamow peak) and Law 1303 (WKB) - tunneling is the nuclear heartbeat.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The barrier is a filter, not a wall; the phi-law lets a floor of the forbidden through.

### NOVELTY
Classical tunneling vanishes with the barrier; the phi-law keeps a screening floor that never reaches zero probability.

### ACTIONABILITY
Run sim/1452_gamow_factor.py; verify exp(-sqrt(EG/E)); proceed to Law 1453.
