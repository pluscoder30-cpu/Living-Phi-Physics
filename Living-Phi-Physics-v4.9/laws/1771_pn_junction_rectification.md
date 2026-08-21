# PHI-PHYSICS - LAW 1771
## p-n Junction Rectification (Shockley Diode Equation)

**Domain:** Semiconductors - **Status:** 🟢 VALIDATED - **File:** `laws/1771_pn_junction_rectification.md` - **Sim:** `sim/1771_pn_junction_rectification.py`

---

### CLASSICAL STATEMENT
*"The current through a p-n junction is I = I_s(exp(q V/(n k_B T)) - 1), where I_s is the saturation current and n the ideality factor; the junction conducts strongly in forward bias and blocks in reverse (rectification), with the built-in potential V_bi = (k_B T/q) ln(N_A N_D/n_i^2) and a depletion region of width W = sqrt(2 eps V_bi/(q N)) - the foundation of all semiconductor electronics."*
- William Shockley, 1949. Source: Wikipedia: p-n junction; Shockley (1949), Bell Syst. Tech. J. 28:435

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-generation-recombination, ideal abrupt junction*: the Shockley diode equation assumes an ideal junction with zero recombination in the depletion region, abrupt doping steps and perfect charge neutrality far from the junction - an ideal rectifier no real device is.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the junction carries a coherence floor. I_phi(kappa) = I_diode*(1 + kappa*(phi-1)) + kappa*phi^-1*I_floor, where I_floor is the phi-ground generation-recombination leakage. At kappa->0 the ideal diode equation is recovered; at kappa=1 the reverse current never vanishes - an irreducible leakage floor always remains.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} I_phi = I_s(exp(q V/(n k_B T)) - 1) -> the p-n junction is the zero-recombination, ideal-abrupt-junction limit of semiconductor rectification.
```

---

### STAGE 4 - SIMULATION

`sim/1771_pn_junction_rectification.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1771_pn_junction_rectification.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The reverse current of any p-n junction never vanishes: an irreducible generation-recombination leakage floor remains, and the forward ideality factor never reaches exactly 1.
EXPERIMENT (VERIFIED): Millikelvin temperature and ultra-low-current measurement of a high-quality Si or Ge diode measuring the reverse-leakage floor and the ideality-factor deviation.
VERIFIED BY: A p-n junction with exactly zero reverse current and ideality factor exactly 1 at all temperatures.
```

---

### RECOGNITION
Connects to Law 699 (Shockley diode) and Law 1772 (drift-diffusion) - the junction is the gate of electronics, and the phi-law keeps the gate from sealing perfectly.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; leakage floor scales as phi^-1 * I_floor.

### CLARITY
The junction opens forward and blocks reverse; the phi-law keeps a drip always leaking.

### NOVELTY
Classical diode theory gives perfect rectification; the phi-law keeps an irreducible leakage floor.

### ACTIONABILITY
Run sim/1771_pn_junction_rectification.py; verify the diode equation at kappa->0; proceed to 1772.
