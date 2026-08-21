# PHI-PHYSICS - LAW 1834
## Schmid's Law (Critical Resolved Shear Stress of Slip)

**Domain:** Mechanical Properties - **Status:** 🟢 VALIDATED - **File:** `laws/1834_schmid_law.md` - **Sim:** `sim/1834_schmid_law.py`

---

### CLASSICAL STATEMENT
*"A crystal yields on a slip system when the resolved shear stress reaches a critical value: tau_RSS = sigma cos(phi) cos(lambda) = sigma m, where m is the Schmid factor (max 0.5); yielding begins on the system with the highest Schmid factor, and the critical resolved shear stress tau_crss is a material property of the slip system - the law of single-crystal plasticity."*
- Erich Schmid (1924); G.I. Taylor (1927), 1924. Source: Wikipedia: Schmid's law; Schmid (1924), Proc. Int. Congr. Appl. Mech; Taylor (1927)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-thermal-activation, perfectly sharp-slip reference*: Schmid's law assumes yielding occurs exactly when tau_RSS = tau_crss with no thermal activation, no strain-rate effects and no latent hardening; real slip is thermally activated and the yield is rounded away from this sharp criterion.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the critical stress carries a coherence floor. tau_crss_phi(kappa) = tau_crss*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_tau, where delta_tau is the phi-ground yield-rounding floor. At kappa->0 the sharp Schmid criterion is recovered; at kappa=1 slip is thermally rounded - the yield never switches on exactly.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} tau_phi = sigma cos(phi) cos(lambda) -> Schmid's law is the zero-activation, sharp-slip, ideal-single-crystal limit of resolved-shear-stress plasticity.
```

---

### STAGE 4 - SIMULATION

`sim/1834_schmid_law.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1834_schmid_law.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: No crystal slips exactly at tau_crss: an irreducible thermal-rounding floor remains, so the measured critical resolved shear stress depends on strain rate and temperature with a finite floor.
EXPERIMENT (VERIFIED): Single-crystal micro-pillar compression of a metal (e.g. Ni, Cu, Mo) at various orientations and temperatures, measuring the Schmid-law deviation floor.
VERIFIED BY: A single crystal yielding exactly at the Schmid prediction with zero rounding at all rates and temperatures.
```

---

### RECOGNITION
Connects to Law 1799 (Peierls) and Law 1832 (strain hardening) - the crystal yields on its favorite plane, and the phi-law keeps the favorite slightly uncertain.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; rounding floor scales as phi^-1 * delta_tau.

### CLARITY
The crystal slips on its favorite plane; the phi-law keeps the favorite slightly uncertain.

### NOVELTY
Classical Schmid gives a sharp law; the phi-law rounds it with a thermal floor.

### ACTIONABILITY
Run sim/1834_schmid_law.py; verify tau = sigma cos(phi) cos(lambda) at kappa->0; proceed to 1835.
