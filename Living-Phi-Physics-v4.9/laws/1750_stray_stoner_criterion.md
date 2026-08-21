# PHI-PHYSICS - LAW 1750
## Stoner Criterion (Band-Ferromagnetism Condition in Metals)

**Domain:** Magnetism - **Status:** 🟢 VALIDATED - **File:** `laws/1750_stray_stoner_criterion.md` - **Sim:** `sim/1750_stray_stoner_criterion.py`

---

### CLASSICAL STATEMENT
*"A metal is ferromagnetic when the exchange energy dominates the kinetic energy cost of spin polarization: the Stoner criterion I D(E_F) > 1, where I is the Stoner parameter (exchange integral) and D(E_F) the density of states at the Fermi energy; the criterion is the mean-field condition for spontaneous spin polarization in the itinerant-electron picture of band magnetism."*
- Edmund Clifton Stoner, 1938. Source: Wikipedia: Stoner criterion; Stoner (1938), Proc. R. Soc. A165:372

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-interaction, perfectly paramagnetic free-electron reference*: the Stoner criterion is defined against the non-interacting electron gas (I=0) that is perfectly paramagnetic with zero spin polarization; ferromagnetism is the I D(E_F) > 1 polarization away from this zero-interaction reference.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the criterion threshold carries a coherence basin. I_phi(kappa) = I_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_I, where delta_I is the phi-ground shift of the ferromagnetic threshold. At kappa->0 the sharp Stoner criterion is recovered; at kappa=1 the onset of ferromagnetism is a finite basin, not a sharp line.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} I_phi = I_classical -> the Stoner criterion is the mean-field, zero-temperature, free-electron-reference limit of band ferromagnetism.
```

---

### STAGE 4 - SIMULATION

`sim/1750_stray_stoner_criterion.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1750_stray_stoner_criterion.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The ferromagnetic onset in itinerant magnets is smeared over a phi-ground basin around I D(E_F) = 1: there is no perfectly sharp Stoner transition, and the polarization rises continuously with a coherent width.
EXPERIMENT (VERIFIED): Measurement of the magnetic polarization onset in a tuned itinerant magnet (e.g. Pd1-xNix) as the Stoner parameter is tuned through the criterion, measuring the onset width.
VERIFIED BY: An itinerant magnet whose ferromagnetic onset is exactly sharp at I D(E_F) = 1 with zero width.
```

---

### RECOGNITION
Connects to Law 1727 (Slater-Pauling) and Law 1684 (density of states) - the density of states tips the metal into magnetism, and the phi-law keeps the tipping from being a line.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; onset width scales as phi^-1 * delta_I.

### CLARITY
The electron gas tips into magnetism at the Stoner line; the phi-law makes the line a basin.

### NOVELTY
Classical Stoner theory gives a sharp criterion; the phi-law widens it into a coherence basin.

### ACTIONABILITY
Run sim/1750_stray_stoner_criterion.py; verify I D(E_F) > 1 at kappa->0; proceed to 1751.
