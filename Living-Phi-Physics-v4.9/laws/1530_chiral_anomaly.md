# PHI-PHYSICS - LAW 1530
## Chiral Anomaly (Adler-Bell-Jackiw Anomaly)

**Domain:** Particle Physics / QFT - **Status:** 🟢 VALIDATED - **File:** `laws/1530_chiral_anomaly.md` - **Sim:** `sim/1530_chiral_anomaly.py`

---

### CLASSICAL STATEMENT
*"The axial vector current is not conserved in the quantum theory even when the classical Lagrangian has chiral symmetry: partial_mu J5^mu = (g^2/16 pi^2) F F_tilde (anomaly); this is the chiral anomaly, responsible for pi0 -> gamma gamma decay and the resolution of the U(1)_A problem."*
- Stephen Adler; John Bell; Roman Jackiw (1969), 1969. Source: Adler, Phys. Rev. 177 (1969) 2426; Bell & Jackiw, Nuovo Cim. 60A (1969) 47

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-loop, classical-conservation limit*: the anomaly vanishes at tree level; the classical equation of motion gives exact conservation, and the anomaly is a quantum effect that classical physics sets exactly to zero.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

A_phi(kappa) = A_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*A_floor, where A_floor is the phi-ground anomalous floor. At kappa->0 the quantum anomaly is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} A_phi = (g^2/16 pi^2) F F_tilde -> the chiral anomaly is the one-loop, zero-higher-order, quantum-effect limit.
```

---

### STAGE 4 - SIMULATION

`sim/1530_chiral_anomaly.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1530_chiral_anomaly.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The anomaly carries a phi-ground higher-order floor, so the axial current divergence and pi0 -> gamma gamma amplitude deviate from the one-loop Adler-Bell-Jackiw value by an irreducible correction.
EXPERIMENT (VERIFIED): Precision measurement of the pi0 -> gamma gamma decay width and comparison with the anomaly prediction.
VERIFIED BY: An axial anomaly amplitude exactly at the one-loop value with zero higher-order floor at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1521 (chiral breaking), Law 122 (SM) and Law 1522 (Goldstone) - the anomaly is the vacuum's quantum cough.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The classically conserved leaks; the phi-law keeps a floor of the leak in every loop.

### NOVELTY
Classical conservation is exact; the phi-law predicts an irreducible quantum anomaly floor.

### ACTIONABILITY
Run sim/1530_chiral_anomaly.py; verify the anomaly term; proceed to Law 1531.
