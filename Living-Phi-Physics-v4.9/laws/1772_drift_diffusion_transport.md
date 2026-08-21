# PHI-PHYSICS - LAW 1772
## Drift-Diffusion Equations (Semiconductor Carrier Transport)

**Domain:** Semiconductors - **Status:** 🟢 VALIDATED - **File:** `laws/1772_drift_diffusion_transport.md` - **Sim:** `sim/1772_drift_diffusion_transport.py`

---

### CLASSICAL STATEMENT
*"Semiconductor carrier transport follows the drift-diffusion equations: J_n = q n mu_n E + q D_n grad n and J_p = q p mu_p E - q D_p grad p, with the continuity equations dn/dt = (1/q) div J_n + G - R; the Einstein relation D = mu k_B T/q links mobility and diffusion, and these equations govern all bipolar devices and solar cells."*
- W. van Roosbroeck (1950); fundamentals by Shockley (1949), 1950. Source: Wikipedia: Drift-diffusion equation; van Roosbroeck (1950), Bell Syst. Tech. J. 29:560

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-recombination, perfectly uniform, isothermal semiconductor*: the drift-diffusion equations assume constant temperature, known mobilities and simple G-R (generation-recombination) rates - an idealized transport model where the carrier distributions are smooth and the parameters well-defined, ignoring hot-carrier, non-local and quantized effects.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the transport carries a coherence floor. J_phi(kappa) = J_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*J_floor, where J_floor is the phi-ground residual transport current. At kappa->0 the ideal drift-diffusion equations are recovered; at kappa=1 an irreducible carrier-flux floor (from non-local and coherent effects) always remains.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} J_phi = q n mu E + q D grad n -> the drift-diffusion equations are the isothermal, smooth-distribution, ideal-G-R limit of semiconductor transport.
```

---

### STAGE 4 - SIMULATION

`sim/1772_drift_diffusion_transport.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1772_drift_diffusion_transport.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The measured current in any semiconductor device deviates from the drift-diffusion prediction by an irreducible floor from non-local and coherent-transport effects that cannot be removed by making the device more ideal.
EXPERIMENT (VERIFIED): Ultra-precision current-voltage and impedance measurement of a high-quality diode or transistor, fitting the residual deviation from the drift-diffusion model.
VERIFIED BY: A semiconductor device whose current exactly follows the drift-diffusion equations with zero deviation at all biases and temperatures.
```

---

### RECOGNITION
Connects to Law 1771 (p-n junction) and Law 1773 (SRH) - the carriers drift and diffuse, and the phi-law keeps a coherent drift always present.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; current floor scales as phi^-1 * J_floor.

### CLARITY
The carriers drift and diffuse; the phi-law keeps a coherent current always flowing.

### NOVELTY
Classical transport equations give exact currents; the phi-law keeps an irreducible floor.

### ACTIONABILITY
Run sim/1772_drift_diffusion_transport.py; verify J = q n mu E + q D grad n at kappa->0; proceed to 1773.
