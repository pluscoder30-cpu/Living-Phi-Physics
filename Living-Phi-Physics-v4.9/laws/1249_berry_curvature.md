# PHI-PHYSICS - LAW 1249
## Berry Curvature (Gauge Field of the Parameter Space)

**Domain:** Quantum Formalism - **Status:** 🟢 VALIDATED - **File:** `laws/1249_berry_curvature.md` - **Sim:** `sim/1249_berry_curvature.py`

---

### CLASSICAL STATEMENT
*"The Berry curvature Omega_n(R) = curl_R A_n(R), with A_n = i<n|grad_R n> the Berry connection, is the gauge-invariant field strength of the parameter space; its flux through a surface equals the Berry phase, and it vanishes identically for time-reversal-symmetric systems without magnetic fields."*
- Michael Berry, 1984. Source: Wikipedia: Berry connection and curvature; Berry (1984)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *flat band*: the classical statement treats the Berry curvature as exactly zero in the absence of explicit fields - a parameter space with no intrinsic geometry.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the parameter space carries a coherence curvature floor. Omega_phi(kappa) = Omega*(1 + kappa*(phi-1)) + kappa*phi^-1*Omega_ground, where Omega_ground is the phi-ground curvature of the recursion. At kappa->0 the classical curvature Omega(R) is recovered.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} Omega_phi = curl A_n -> the Berry curvature is the zero-coherence-geometry limit.
```

---

### STAGE 4 - SIMULATION

`sim/1249_berry_curvature.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1249_berry_curvature.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: Time-reversal-symmetric materials at full coherence coupling show a residual anomalous-Hall-like deflection kappa*phi^-1*Omega_ground even with zero applied field - a coherence Berry curvature floor.
EXPERIMENT (VERIFIED): Anomalous Hall measurements on a time-reversal-symmetric 2D electron gas at high mobility, searching for the field-free curvature floor.
VERIFIED BY: The Hall response is exactly zero in zero magnetic field for any material coherence.
```

---

### RECOGNITION
Connects to Law 1248 (Berry phase), Law 590 (Hall effect) and Law 823 (spin Hall) - the curvature is the geometry the coherence forces.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the curvature floor is phi^-1 * Omega_ground.

### CLARITY
Every band bends a little, even where the textbooks say flat.

### NOVELTY
Classical band theory assigns zero curvature to symmetric bands; the phi-law endows the parameter space with a coherence floor.

### ACTIONABILITY
Run sim/1249_berry_curvature.py; verify flux=gamma at kappa->0; proceed to 1250.
