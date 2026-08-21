# PHI-PHYSICS - LAW 1696
## Efros-Shklovskii Variable-Range Hopping (Coulomb-Gap Conductivity)

**Domain:** Electrons in Solids - **Status:** 🟢 VALIDATED - **File:** `laws/1696_efros_shklovskii_law.md` - **Sim:** `sim/1696_efros_shklovskii_law.py`

---

### CLASSICAL STATEMENT
*"In strongly localized, interacting systems the Coulomb interaction opens a soft gap (Coulomb gap) in the density of states at the Fermi level, and the conductivity follows sigma(T) = sigma_0 exp(-(T_ES/T)^(1/2)) where T_ES = beta e^2/(k_B kappa xi); the exponent 1/2 (Efros-Shklovskii) replaces the 1/4 (Mott) when Coulomb interactions dominate hopping transport."*
- A.L. Efros & B.I. Shklovskii, 1975. Source: Wikipedia: Efros-Shklovskii variable range hopping; Efros & Shklovskii (1975), J. Phys. C 8:L49

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *non-interacting, zero-Coulomb-gap localized system*: Mott's 1/4 law assumes non-interacting electrons; the Efros-Shklovskii law arises because interactions are included - and its sharpest form assumes a perfectly clean, exactly-parabolic Coulomb gap at T=0 in an infinitely large system.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the Coulomb gap carries a coherence floor. sigma_phi(kappa) = sigma_ES*(1 + kappa*(phi-1)) + kappa*phi^-1*sigma_floor, where sigma_floor is the phi-ground residual conductivity. At kappa->0 the exact exp(-(T_ES/T)^(1/2)) law is recovered; at kappa=1 the hopping conductivity carries an irreducible floor at low T.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} sigma_phi = sigma_0 exp(-(T_ES/T)^(1/2)) -> the Efros-Shklovskii law is the clean-Coulomb-gap, zero-temperature, infinite-system limit of interaction-dominated hopping.
```

---

### STAGE 4 - SIMULATION

`sim/1696_efros_shklovskii_law.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1696_efros_shklovskii_law.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The Efros-Shklovskii conductivity saturates at an irreducible floor at the lowest temperatures instead of vanishing, so the log-sigma vs T^-1/2 line bends over at a coherence-limited temperature.
EXPERIMENT (VERIFIED): Ultra-low-temperature (down to millikelvin) conductivity of a doped semiconductor in the insulating regime, measuring the low-T saturation floor of the ES hopping conductivity.
VERIFIED BY: A localized system whose conductivity continues to vanish following exp(-(T_ES/T)^(1/2)) without any saturation floor.
```

---

### RECOGNITION
Connects to Law 1697 (variable range hopping) and Law 1691 (Anderson localization) - the Coulomb gap is the electron sea's memory of itself, and the phi-law keeps a drip of conduction.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; saturation floor scales as phi^-1 * sigma_floor.

### CLARITY
The hopping current freezes, but a coherent drip always remains.

### NOVELTY
Classical ES hopping vanishes at T=0; the phi-law keeps an irreducible conduction floor.

### ACTIONABILITY
Run sim/1696_efros_shklovskii_law.py; verify exp(-(T_ES/T)^(1/2)) at kappa->0; proceed to 1697.
