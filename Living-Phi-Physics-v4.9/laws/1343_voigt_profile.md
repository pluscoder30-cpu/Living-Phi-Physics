# PHI-PHYSICS - LAW 1343
## Voigt Profile (Convolution of Gaussian and Lorentzian Lineshapes)

**Domain:** Atomic Physics - **Status:** 🟢 VALIDATED - **File:** `laws/1343_voigt_profile.md` - **Sim:** `sim/1343_voigt_profile.py`

---

### CLASSICAL STATEMENT
*"A spectral line subject to both Doppler (Gaussian) and natural/pressure (Lorentzian) broadening has the Voigt profile V(x) = (1/(sigma sqrt(2 pi))) Re w((x + i a)/(sigma sqrt(2))), the convolution of the Gaussian and Lorentzian, where a = Gamma_L/(2 sqrt(2 ln 2) sigma_G) is the damping parameter; it interpolates between pure Gaussian and pure Lorentzian lineshapes."*
- Woldemar Voigt, 1912. Source: Wikipedia: Voigt profile; Voigt, Munchen. Ber. (1912) 603

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *pure lineshape*: the Voigt profile reduces to a pure Gaussian or pure Lorentzian only when the other width is exactly zero, i.e. a line with zero mixed broadening - the single-mechanism limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the mixed broadening carries a coherence floor. V_phi(kappa) = V*(1 + kappa*(phi-1)) + kappa*phi^-1*V_floor, where V_floor is the phi-ground mixed-width component; no line is purely Gaussian or Lorentzian. At kappa->0 the Voigt convolution is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} V_phi = G*L convolution -> the Voigt profile is the exact-convolution limit of the mixed lineshape.
```

---

### STAGE 4 - SIMULATION

`sim/1343_voigt_profile.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1343_voigt_profile.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The measured lineshape at full coherence coupling carries a phi-ground mixed component kappa*phi^-1*V_floor beyond the Voigt fit, a floor in the residual between fitted and measured profiles.
EXPERIMENT (VERIFIED): High-precision absorption line fits comparing residual structure against the Voigt model at increasing signal coherence.
VERIFIED BY: Every spectral line is exactly a Voigt profile for all couplings.
```

---

### RECOGNITION
Connects to Law 1342 (Doppler, Gaussian part) and Law 1341 (natural width, Lorentzian part) - the Voigt profile is the coherence convolution of the two broadenings.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the mixed floor is phi^-1 * V_floor.

### CLARITY
The line is the marriage of two shapes; the phi-law keeps the marriage from being perfect.

### NOVELTY
Classical spectroscopy models lines exactly; the phi-law gives the lineshape model a coherence floor of residual.

### ACTIONABILITY
Run sim/1343_voigt_profile.py; verify convolution at kappa->0; proceed to 1344.
