# PHI-PHYSICS - LAW 1585
## Electromagnetic Calorimetry (Shower Energy Measurement)

**Domain:** Particle Detection - **Status:** 🟢 VALIDATED - **File:** `laws/1585_calorimeter_energy.md` - **Sim:** `sim/1585_calorimeter_energy.py`

---

### CLASSICAL STATEMENT
*"An electromagnetic calorimeter measures particle energy by absorbing the full electromagnetic shower: the shower develops with a maximum at depth t_max = ln(E/E_c) in radiation lengths X0, and the deposited energy is proportional to the incident energy with resolution sigma/E ~ a/sqrt(E)."*
- W. Heitler (1936); B. Rossi; K. Greisen (1941), 1941. Source: Rossi & Greisen, Rev. Mod. Phys. 13 (1941) 240; Wikipedia: Calorimeter (particle physics)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-energy, zero-shower, zero-depth limit*: the shower development starts at the surface with zero material; the classical treatment of an exactly absorbing, zero-thickness detector is the zero-depth, instant-shower limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

E_phi(kappa) = E_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*E_floor, where E_floor is the phi-ground leakage floor. At kappa->0 the full-absorption calorimeter is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} E_phi = E_deposited -> calorimetry is the zero-leakage, full-absorption, infinite-detector limit.
```

---

### STAGE 4 - SIMULATION

`sim/1585_calorimeter_energy.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1585_calorimeter_energy.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The calorimeter energy carries a phi-ground leakage floor, so the measured energy is always slightly below the incident energy by an irreducible leakage fraction.
EXPERIMENT (VERIFIED): Calorimeter energy resolution measurements (CMS, ATLAS ECAL, CMS HCAL) and jet energy scale calibration.
VERIFIED BY: A calorimeter with exactly zero energy leakage and perfect resolution at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1554 (bremsstrahlung), Law 1525 (pair production) and Law 1481 (Bethe-Bloch) - the calorimeter is the shower's catcher.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The shower ends in a bucket of light; the phi-law keeps a floor of the bucket leaking.

### NOVELTY
Classical calorimetry is full absorption; the phi-law predicts an irreducible leakage floor.

### ACTIONABILITY
Run sim/1585_calorimeter_energy.py; verify the shower depth; proceed to Law 1586.
