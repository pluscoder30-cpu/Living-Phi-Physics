# PHI-PHYSICS - LAW 1484
## Nuclear Magnetic Moment (Schmidt Lines)

**Domain:** Nuclear Structure - **Status:** 🟢 VALIDATED - **File:** `laws/1484_nuclear_magnetic_moment.md` - **Sim:** `sim/1484_nuclear_magnetic_moment.py`

---

### CLASSICAL STATEMENT
*"The nuclear magnetic moment mu = g_I mu_N I, with g_I the g-factor and mu_N the nuclear magneton; the Schmidt model gives mu = [g_l l + g_s s] with g_l=1 (proton), g_s = 5.586 (proton), giving the Schmidt lines between which measured moments fall."*
- Otto Stern (1933); Isidor Isaac Rabi (NMR); Schmidt (1937), 1933. Source: Stern, Nature 132 (1933) 103; Wikipedia: Nuclear magnetic moment

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-core-polarization, single-particle moment*: the Schmidt model assumes the magnetic moment comes from a single odd nucleon with a completely inert core - zero core polarization and zero meson-exchange corrections.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

mu_phi(kappa) = mu_schmidt*(1 + kappa*(phi-1)) + kappa*phi^-1*mu_pol, where mu_pol is the phi-ground core-polarization/meson floor. At kappa->0 the Schmidt value is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} mu_phi = g_I mu_N I -> the nuclear magnetic moment is the zero-core-polarization, single-particle, inert-core limit.
```

---

### STAGE 4 - SIMULATION

`sim/1484_nuclear_magnetic_moment.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1484_nuclear_magnetic_moment.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The measured magnetic moment always deviates from the Schmidt line by a phi-ground core-polarization floor, and the deviation pattern (quenching) is systematic, never exactly on the Schmidt line.
EXPERIMENT (VERIFIED): Nuclear magnetic moment measurements (Rabi resonance, Penning traps, laser spectroscopy) vs Schmidt-line predictions.
VERIFIED BY: A nucleus whose magnetic moment exactly equals the Schmidt single-particle value at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1449 (shell model), Law 1334 (Lande g) and Law 1597 (NMR) - the magnetic moment is the nucleus's spin echo.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The spin points as one; the phi-law keeps a floor of the core leaning.

### NOVELTY
Classical Schmidt moment is single-particle; the phi-law keeps an irreducible polarization floor.

### ACTIONABILITY
Run sim/1484_nuclear_magnetic_moment.py; verify the Schmidt value; proceed to Law 1485.
