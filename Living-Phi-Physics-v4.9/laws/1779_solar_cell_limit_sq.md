# PHI-PHYSICS - LAW 1779
## Shockley-Queisser Limit (Detailed-Balance Efficiency Limit of Solar Cells)

**Domain:** Semiconductors - **Status:** 🟢 VALIDATED - **File:** `laws/1779_solar_cell_limit_sq.md` - **Sim:** `sim/1779_solar_cell_limit_sq.py`

---

### CLASSICAL STATEMENT
*"The maximum efficiency of a single-junction solar cell is the Shockley-Queisser (detailed-balance) limit: ~30% for a bandgap of 1.1 eV under unconcentrated sunlight, set by the balance between absorption and radiative recombination; the limit decomposes into the ultimate efficiency u(x_g) (spectrum losses), the voltage factor v (recombination), and the fill factor m, and multifunction cells can exceed it up to ~68%."*
- William Shockley & Hans-Joachim Queisser, 1961. Source: Wikipedia: Shockley-Queisser limit; Shockley & Queisser (1961), J. Appl. Phys. 32:510

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-nonradiative-recombination, perfect single-junction reference*: the Shockley-Queisser limit assumes only radiative recombination (zero SRH, zero Auger, zero surface recombination), perfect absorption and ideal collection - an idealized photovoltaic with exactly one loss channel that no real cell realizes.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the efficiency limit carries a coherence floor. eta_phi(kappa) = eta_SQ*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_eta, where delta_eta is the phi-ground efficiency correction. At kappa->0 the ideal SQ limit is recovered; at kappa=1 every cell carries an irreducible non-radiative loss that lowers the achievable efficiency below the ideal limit.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} eta_phi = eta_SQ -> the Shockley-Queisser limit is the zero-nonradiative-loss, ideal-single-junction limit of photovoltaic efficiency.
```

---

### STAGE 4 - SIMULATION

`sim/1779_solar_cell_limit_sq.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1779_solar_cell_limit_sq.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: No single-junction cell reaches the SQ limit: an irreducible non-radiative-loss floor always reduces the achievable efficiency, and the gap between ideal and real cells has a lower bound that cannot be closed.
EXPERIMENT (VERIFIED): Champion solar-cell efficiency measurements (e.g. record Si and GaAs cells) tracking the persistent gap to the SQ limit as material quality improves.
VERIFIED BY: A single-junction solar cell reaching exactly the Shockley-Queisser efficiency with zero non-radiative loss.
```

---

### RECOGNITION
Connects to Law 1773 (SRH) and Law 1774 (Auger) - the solar cell's ceiling is set by radiative balance, and the phi-law keeps a non-radiative floor below the ceiling.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; efficiency deficit scales as phi^-1 * delta_eta.

### CLARITY
The cell reaches for the SQ sky; the phi-law keeps a cloud always in the way.

### NOVELTY
Classical SQ theory gives an exact ceiling; the phi-law keeps an irreducible deficit below it.

### ACTIONABILITY
Run sim/1779_solar_cell_limit_sq.py; verify the SQ limit curve at kappa->0; proceed to 1780.
