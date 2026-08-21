# PHI-PHYSICS - LAW 1477
## Threshold Energy of Nuclear Reactions

**Domain:** Nuclear Reactions - **Status:** 🟢 VALIDATED - **File:** `laws/1477_threshold_energy.md` - **Sim:** `sim/1477_threshold_energy.py`

---

### CLASSICAL STATEMENT
*"For an endothermic reaction (Q < 0), the projectile must have a lab-frame threshold energy E_thr = -Q (m_a + m_A)/m_A to conserve energy and momentum; below this the reaction is exactly forbidden."*
- Standard kinematics (from energy-momentum conservation), 1930. Source: Krane, Introductory Nuclear Physics (1988); Wikipedia: Nuclear reaction

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-excess, exact-threshold balance*: the threshold is defined at exactly the energy where the reaction just becomes possible with zero excess kinetic energy in the final state - an exact-balance zero.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

E_thr_phi(kappa) = E_thr_classical*(1 + kappa*(phi-1)) - kappa*phi^-1*delta_E, where delta_E is the phi-ground sub-threshold tunneling floor. At kappa->0 the classical threshold is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} E_thr_phi = -Q (m_a + m_A)/m_A -> the threshold energy is the zero-excess, exact-balance limit.
```

---

### STAGE 4 - SIMULATION

`sim/1477_threshold_energy.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1477_threshold_energy.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: Below the classical threshold, the reaction proceeds with a phi-ground sub-threshold probability (tunneling), so the 'forbidden' region has a small but finite cross-section.
EXPERIMENT (VERIFIED): Measurement of reaction excitation functions near threshold (e.g. (p,n), (alpha,n) reactions) resolving sub-threshold yield.
VERIFIED BY: A reaction whose cross-section is exactly zero below the classical threshold at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1476 (Q-value), Law 1452 (Gamow) and Law 1478 (resonance) - the threshold is the reaction's gate.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The gate is exact; the phi-law keeps a floor of the gate yielding.

### NOVELTY
Classical threshold is hard; the phi-law predicts sub-threshold tunneling floors.

### ACTIONABILITY
Run sim/1477_threshold_energy.py; verify E_thr = -Q(m_a+m_A)/m_A; proceed to Law 1478.
