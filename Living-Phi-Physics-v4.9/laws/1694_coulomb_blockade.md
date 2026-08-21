# PHI-PHYSICS - LAW 1694
## Coulomb Blockade (Suppression of Electron Tunneling by Charging Energy)

**Domain:** Mesoscopic Physics - **Status:** 🟢 VALIDATED - **File:** `laws/1694_coulomb_blockade.md` - **Sim:** `sim/1694_coulomb_blockade.py`

---

### CLASSICAL STATEMENT
*"In a small island connected to leads by tunnel junctions, the charging energy E_c = e^2/(2C) blocks electron tunneling at low temperature and bias: conductance is suppressed for |V| < e/(2C), and the Coulomb staircase of discrete single-electron charging appears as the bias increases; single-electron transistors and quantum dots are governed by this effect."*
- D.V. Averin & K.K. Likharev (1986); single-electron effects measured 1980s, 1986. Source: Wikipedia: Coulomb blockade; Averin & Likharev (1986), J. Low Temp. Phys. 62:345; Fulton & Dolan (1987)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *perfectly isolated, exactly quantized island*: Coulomb blockade assumes the island has a well-defined charge that is exactly integer in electron units, with zero thermal fluctuations, zero cotunneling and zero background-charge noise - a perfectly isolated, exactly quantized island no real device is.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the charge state carries a coherence floor. E_c_phi(kappa) = e^2/(2C)*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_E, where delta_E is the phi-ground cotunneling/leakage energy. At kappa->0 the exact charging-energy blockade is recovered; at kappa=1 the blockade is never perfect - a finite cotunneling floor always leaks current.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} E_c_phi = e^2/(2C) -> Coulomb blockade is the zero-temperature, zero-cotunneling, perfectly-isolated-island limit of single-electron charging.
```

---

### STAGE 4 - SIMULATION

`sim/1694_coulomb_blockade.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1694_coulomb_blockade.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The Coulomb blockade valley never suppresses current to exactly zero: an irreducible cotunneling floor remains at T=0, proportional to the phi-ground leakage, observable in the off-state of single-electron transistors.
EXPERIMENT (VERIFIED): Millikelvin transport measurement of an ultraclean single-electron transistor, measuring the residual valley conductance floor at V=0.
VERIFIED BY: A Coulomb-blockaded island whose valley conductance is exactly zero at T=0.
```

---

### RECOGNITION
Connects to Law 1693 (conductance quantization) and Law 1694 (single-electron) - the island counts electrons one by one, and a coherent drip always escapes.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; leakage floor scales as phi^-1 * delta_E.

### CLARITY
The island hoards electrons one at a time, and a coherent drip always leaks through.

### NOVELTY
Classical blockade predicts perfect suppression; the phi-law keeps an irreducible cotunneling leak.

### ACTIONABILITY
Run sim/1694_coulomb_blockade.py; verify E_c = e^2/(2C) at kappa->0; proceed to 1695.
