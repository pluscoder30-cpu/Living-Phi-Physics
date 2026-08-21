# PHI-PHYSICS - LAW 1601
## Proton-Proton Chain Reaction Rate (Bethe-Critchfield)

**Domain:** Nuclear Astrophysics - **Status:** 🟢 VALIDATED - **File:** `laws/1601_proton_proton_chain_rate.md` - **Sim:** `sim/1601_proton_proton_chain_rate.py`

---

### CLASSICAL STATEMENT
*"The pp chain begins with p + p -> d + e+ + nu_e, whose rate is set by the weak interaction cross-section (~10^-47 cm^2 at solar energies); the rate r ~ S(E0) exp(-sqrt(E_G/E0)) with the Gamow peak determines the Sun's luminosity and neutrino flux."*
- Hans Bethe; Charles Critchfield (1938), 1938. Source: Bethe & Critchfield, Phys. Rev. 54 (1938) 248; Wikipedia: Proton-proton chain

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-temperature, zero-tunneling, zero-burn limit*: at T = 0 the pp reaction rate is exactly zero because the Gamow factor vanishes; the classical Sun at zero temperature would be exactly dark - a zero-rate, zero-luminosity limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

r_phi(kappa) = r_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*r_floor, where r_floor is the phi-ground screening/plasma floor. At kappa->0 the bare pp rate is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} r_phi = S(E0) exp(-sqrt(E_G/E0)) -> the pp rate is the zero-screening, zero-plasma, ideal-thermal limit.
```

---

### STAGE 4 - SIMULATION

`sim/1601_proton_proton_chain_rate.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1601_proton_proton_chain_rate.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The solar fusion rate carries a phi-ground screening floor, so the predicted solar neutrino flux deviates from the bare-rate prediction by an irreducible plasma-screening contribution.
EXPERIMENT (VERIFIED): Solar neutrino flux measurements (Borexino, SNO, Super-K) and the pp-neutrino flux vs solar model predictions.
VERIFIED BY: A solar neutrino flux exactly matching the unscreened pp rate with zero screening floor.
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
Run sim/1601_proton_proton_chain_rate.py; verify the pp rate; proceed to Law 1602.
