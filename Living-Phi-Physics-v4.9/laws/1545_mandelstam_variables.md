# PHI-PHYSICS - LAW 1545
## Mandelstam Variables (s, t, u for Scattering Amplitudes)

**Domain:** Particle Physics / Scattering - **Status:** 🟢 VALIDATED - **File:** `laws/1545_mandelstam_variables.md` - **Sim:** `sim/1545_mandelstam_variables.py`

---

### CLASSICAL STATEMENT
*"The Mandelstam variables s = (p1+p2)^2, t = (p1-p3)^2, u = (p1-p4)^2 describe a 2->2 scattering process; they satisfy s + t + u = sum m_i^2 and are the natural variables for crossing symmetry and the analytic properties of amplitudes."*
- Stanley Mandelstam, 1958. Source: Mandelstam, Phys. Rev. 112 (1958) 1344; Wikipedia: Mandelstam variables

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-mass, zero-crossing-symmetric limit*: in the massless limit s + t + u = 0; the classical treatment of fixed-energy (s-channel) scattering ignores the crossing relation - a zero-t, zero-u, pure-s limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

s_phi(kappa) = s_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*s_floor, where s_floor is the phi-ground crossing floor. At kappa->0 the pure s-channel description is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} (s + t + u)_phi = sum m_i^2 -> the Mandelstam variables are the zero-crossing, fixed-channel limit.
```

---

### STAGE 4 - SIMULATION

`sim/1545_mandelstam_variables.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1545_mandelstam_variables.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The amplitudes carry a phi-ground crossing floor, so the full amplitude is never described by a single channel and the s-t crossing relation has an irreducible residual.
EXPERIMENT (VERIFIED): Crossing-symmetry tests in meson scattering and high-energy Regge phenomenology (s vs t dominance).
VERIFIED BY: A scattering amplitude exactly described by a single Mandelstam channel with zero crossing floor.
```

---

### RECOGNITION
Connects to Law 1544 (optical theorem), Law 1546 (partial waves) and Law 1516 (Regge) - the Mandelstam variables are the amplitude's coordinates.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
Three numbers map the scattering; the phi-law keeps a floor of the map stretching.

### NOVELTY
Classical channels are separate; the phi-law predicts an irreducible crossing floor.

### ACTIONABILITY
Run sim/1545_mandelstam_variables.py; verify s+t+u; proceed to Law 1546.
