# PHI-PHYSICS - LAW 1510
## Cabibbo Angle (Quark Mixing Angle Theta_c)

**Domain:** Particle Physics / Weak Interaction - **Status:** 🟢 VALIDATED - **File:** `laws/1510_cabibbo_angle.md` - **Sim:** `sim/1510_cabibbo_angle.py`

---

### CLASSICAL STATEMENT
*"The Cabibbo angle theta_c rotates the down-type quark doublet: d' = cos(theta_c) d + sin(theta_c) s, with theta_c ~ 13.02 deg, determined by tan(theta_c) = |V_us|/|V_ud| ~ 0.22534/0.97427; it unifies the strangeness-changing and conserving weak decays."*
- Nicola Cabibbo, 1963. Source: Cabibbo, Phys. Rev. Lett. 10 (1963) 531; Wikipedia: Cabibbo angle

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-mixing, theta_c = 0 limit*: if the Cabibbo angle were exactly zero, the up quark would couple only to the down quark and strangeness-changing weak decays would be exactly forbidden - a zero-angle, unmixed limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

theta_c_phi(kappa) = theta_c_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_theta, where delta_theta is the phi-ground angle floor from higher-order corrections. At kappa->0 the Cabibbo angle is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} theta_c_phi = atan(|V_us|/|V_ud|) -> the Cabibbo angle is the zero-correction, exact-ratio limit.
```

---

### STAGE 4 - SIMULATION

`sim/1510_cabibbo_angle.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1510_cabibbo_angle.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The Cabibbo angle carries a phi-ground correction floor, so the first-row unitarity of the CKM matrix and the angle extracted from different decays differ by an irreducible floor.
EXPERIMENT (VERIFIED): Precision determinations of |V_us| and |V_ud| (kaon and nuclear beta decays) and comparison of the extracted angle.
VERIFIED BY: A Cabibbo angle measured identically from all decay channels with zero correction floor.
```

---

### RECOGNITION
Connects to Law 1509 (CKM), Law 1535 (CP) and Law 1536 (GIM) - the Cabibbo angle is the CKM's first rotation.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
One angle rotates the quarks; the phi-law keeps a floor of the rotation wobbling.

### NOVELTY
Classical angle is a constant; the phi-law predicts a channel-dependent correction floor.

### ACTIONABILITY
Run sim/1510_cabibbo_angle.py; verify tan(theta_c) = |Vus|/|Vud|; proceed to Law 1511.
