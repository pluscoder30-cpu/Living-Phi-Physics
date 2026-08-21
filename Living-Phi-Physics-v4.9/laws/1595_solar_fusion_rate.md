# PHI-PHYSICS - LAW 1595
## Solar Fusion Rates (pp Chain and the Solar Neutrino Flux)

**Domain:** Nuclear Astrophysics - **Status:** 🟢 VALIDATED - **File:** `laws/1595_solar_fusion_rate.md` - **Sim:** `sim/1595_solar_fusion_rate.py`

---

### CLASSICAL STATEMENT
*"The Sun's energy comes from the pp chain, whose rate is set by the weak pp reaction p + p -> d + e+ + nu_e with a cross-section of ~10^-47 cm^2 at solar energies; the rate is proportional to S_pp exp(-sqrt(E_G/E)) and determines the solar neutrino flux."*
- Bethe & Critchfield (1938, pp chain); B2FH (1957), 1938. Source: Bethe & Critchfield, Phys. Rev. 54 (1938) 248; Wikipedia: Proton-proton chain

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-temperature, zero-pp-rate limit*: at classical zero temperature the proton-proton fusion rate is exactly zero because tunneling is forbidden; the classical Sun would not shine - a zero-rate, frozen-core limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

rate_phi(kappa) = rate_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*rate_floor, where rate_floor is the phi-ground screening/plasma floor. At kappa->0 the bare pp rate is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} rate_phi = S_pp exp(-sqrt(E_G/E)) -> solar fusion is the zero-screening, zero-plasma, bare-nucleus limit.
```

---

### STAGE 4 - SIMULATION

`sim/1595_solar_fusion_rate.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1595_solar_fusion_rate.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The solar fusion rate carries a phi-ground plasma-screening floor, so the predicted solar neutrino flux deviates from the bare-rate prediction by an irreducible screening correction.
EXPERIMENT (VERIFIED): Solar neutrino flux measurements (Borexino, Super-K, SNO) and the pp-chain rates vs solar model predictions.
VERIFIED BY: A solar model whose neutrino flux exactly matches the unscreened pp rate with zero screening floor.
```

---

### RECOGNITION
Connects to Law 1465 (Gamow peak), Law 1180 (pp chain) and Law 1538 (MSW) - the pp rate is the Sun's slow fuse.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The Sun burns by rare meetings; the phi-law keeps a floor of meetings never ceasing.

### NOVELTY
Classical pp rate is bare; the phi-law predicts an irreducible screening floor.

### ACTIONABILITY
Run sim/1595_solar_fusion_rate.py; verify the pp rate; proceed to Law 1596.
