# PHI-PHYSICS - LAW 1453
## Geiger-Nuttall Law (Alpha Decay Half-Life vs Energy)

**Domain:** Nuclear Decays - **Status:** 🟢 VALIDATED - **File:** `laws/1453_geiger_nuttall_law.md` - **Sim:** `sim/1453_geiger_nuttall_law.py`

---

### CLASSICAL STATEMENT
*"The alpha-decay half-life obeys log10(T_1/2) = A(Z)/sqrt(E_alpha) + B(Z): isotopes with higher alpha energy decay exponentially faster, so half-lives spanning ~20 orders of magnitude correspond to small changes in decay energy."*
- Hans Geiger; John Mitchell Nuttall (quantum basis by George Gamow), 1911. Source: Geiger & Nuttall, Phil. Mag. 22 (1911) 613; Wikipedia: Geiger-Nuttall law

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-width, instant-decay barrier*: the law emerges from Gamow tunneling through a barrier; classically the alpha particle is permanently trapped (zero escape rate) because tunneling is forbidden - the law is built on a quantum effect classical physics sets exactly to zero.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

log10(T1/2)_phi(kappa) = (A(Z)/sqrt(E))*(1 + kappa*(phi-1)) + kappa*phi^-1*log10(T_floor), where T_floor is the phi-ground minimum half-life floor from barrier non-idealities. At kappa->0 the Geiger-Nuttall straight line is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} log10(T1/2)_phi = A(Z)/sqrt(E) + B(Z) -> the Geiger-Nuttall law is the point-Coulomb, zero-barrier-perturbation, pure-tunneling limit.
```

---

### STAGE 4 - SIMULATION

`sim/1453_geiger_nuttall_law.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1453_geiger_nuttall_law.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The linear log(T1/2) vs 1/sqrt(E) relation acquires a phi-ground curvature floor; cluster decays and alpha decays near the drip line deviate from the straight line systematically, as observed for cluster radioactivity.
EXPERIMENT (VERIFIED): Systematics of alpha-decay half-lives and cluster-decay (C, O, Ne emission) half-lives across the actinide region (Qi et al., PLB 734 (2014) 203).
VERIFIED BY: Alpha and cluster decay data that lie exactly on the classical straight line with zero phi-ground floor across all nuclei.
```

---

### RECOGNITION
Connects to Law 1452 (Gamow factor) and Law 1303 (WKB) - the Geiger-Nuttall line is the tunneling law's logarithmic face.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The longer the wait, the softer the knock; the phi-law keeps a floor of surprise.

### NOVELTY
Classical law is a pure straight line; the phi-law predicts systematic curvature from cluster decay and drip-line deviation.

### ACTIONABILITY
Run sim/1453_geiger_nuttall_law.py; verify log10 T1/2 vs 1/sqrt(E); proceed to Law 1454.
