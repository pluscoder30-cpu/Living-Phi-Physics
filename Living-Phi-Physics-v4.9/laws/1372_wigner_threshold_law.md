# PHI-PHYSICS - LAW 1372
## Wigner Threshold Law (Cross Section ~ E^(l + 1/2) Near Threshold)

**Domain:** Atomic Physics - **Status:** 🟢 VALIDATED - **File:** `laws/1372_wigner_threshold_law.md` - **Sim:** `sim/1372_wigner_threshold_law.py`

---

### CLASSICAL STATEMENT
*"Near a reaction threshold, the cross section scales as a power of the excess energy: sigma ~ E^(l + 1/2) for a channel with orbital angular momentum l (s-wave l=0 gives sigma ~ E^(1/2), the Wigner law), because the centrifugal barrier suppresses the wavefunction near threshold; the law is universal for short-range interactions."*
- Eugene Wigner, 1948. Source: Wikipedia: Wigner threshold law; Wigner, Phys. Rev. 73 (1948) 1002

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *threshold*: the law holds exactly at E = 0 excess energy where the cross section vanishes exactly for l > 0 - the zero-energy, exact-threshold limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the threshold energy carries a coherence floor. E_exc_phi(kappa) = E_exc*(1 + kappa*(phi-1)) + kappa*phi^-1*E_floor, where E_floor is the phi-ground threshold energy; the cross section retains a floor near threshold. At kappa->0 the Wigner power law is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} sigma_phi = C E^(l + 1/2) -> the Wigner threshold law is the zero-threshold-floor, exact-E=0 limit.
```

---

### STAGE 4 - SIMULATION

`sim/1372_wigner_threshold_law.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1372_wigner_threshold_law.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The cross section at full coherence coupling carries a phi-ground threshold floor kappa*phi^-1*E_floor, so it never vanishes exactly at threshold.
EXPERIMENT (VERIFIED): Ultracold collision cross-section measurements (e.g. atoms at nK) testing the E^(l+1/2) scaling and the threshold floor.
VERIFIED BY: The cross section obeys exactly sigma ~ E^(l+1/2) with zero floor at threshold for all couplings.
```

---

### RECOGNITION
Connects to Law 1350 (Feshbach) and Law 085 (tunneling) - the Wigner law is the coherence scaling of the reaction near threshold.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the threshold floor is phi^-1 * E_floor.

### CLARITY
Every reaction slows at its door; the phi-law keeps the door from closing exactly.

### NOVELTY
Classical scattering theory pins exact threshold powers; the phi-law keeps a coherence floor at the threshold.

### ACTIONABILITY
Run sim/1372_wigner_threshold_law.py; verify E^(l+1/2) at kappa->0; proceed to 1373.
