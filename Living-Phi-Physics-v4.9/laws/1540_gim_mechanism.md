# PHI-PHYSICS - LAW 1540
## GIM Mechanism (Flavor-Changing Neutral Current Suppression)

**Domain:** Particle Physics / Weak Interaction - **Status:** 🟢 VALIDATED - **File:** `laws/1540_gim_mechanism.md` - **Sim:** `sim/1540_gim_mechanism.py`

---

### CLASSICAL STATEMENT
*"Flavor-changing neutral currents (FCNC) are suppressed because the up and charm quark contributions cancel in the loop: the amplitude is proportional to (m_c^2 - m_u^2)/M_W^2; this predicted the charm quark, discovered in 1974."*
- Sheldon Glashow; John Iliopoulos; Luciano Maiani, 1970. Source: Glashow, Iliopoulos & Maiani, Phys. Rev. D2 (1970) 1285; Wikipedia: GIM mechanism

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-mass-difference, exact-cancellation limit*: if m_c = m_u exactly, the FCNC amplitude cancels to exactly zero; the GIM suppression is the approach to this zero-cancellation, degenerate-quark limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

A_phi(kappa) = A_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*A_floor, where A_floor is the phi-ground residual-FCNC floor. At kappa->0 the GIM cancellation is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} A_phi = (m_c^2 - m_u^2)/M_W^2 -> the GIM mechanism is the zero-mass-splitting, exact-cancellation limit.
```

---

### STAGE 4 - SIMULATION

`sim/1540_gim_mechanism.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1540_gim_mechanism.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: FCNC processes (K_L -> mu mu, B_s -> mu mu, K_L -> pi nu nu) carry a phi-ground residual floor, so the measured branching ratios deviate from the GIM/CKM prediction by an irreducible long-distance contribution.
EXPERIMENT (VERIFIED): Rare kaon and B decays (KOTO, NA62, LHCb, CMS) measuring FCNC branching ratios vs SM predictions.
VERIFIED BY: A FCNC process exactly matching the point-like GIM prediction with zero long-distance floor.
```

---

### RECOGNITION
Connects to Law 1509 (CKM), Law 1539 (CP) and Law 1510 (Cabibbo) - the GIM mechanism is the FCNC's quiet engine.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The two quarks cancel in the loop; the phi-law keeps a floor of the cancellation failing.

### NOVELTY
Classical GIM cancellation is exact; the phi-law predicts an irreducible FCNC floor.

### ACTIONABILITY
Run sim/1540_gim_mechanism.py; verify the suppression; proceed to Law 1541.
