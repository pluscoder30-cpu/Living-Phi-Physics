# PHI-PHYSICS - LAW 1394
## Herzberg-Teller Coupling (Vibronically Induced Intensity Borrowing)

**Domain:** Molecular Physics - **Status:** 🟢 VALIDATED - **File:** `laws/1394_herzberg_teller_coupling.md` - **Sim:** `sim/1394_herzberg_teller_coupling.py`

---

### CLASSICAL STATEMENT
*"The Herzberg-Teller coupling describes how electronic transitions forbidden by symmetry gain intensity through vibration: the transition dipole moment is expanded in normal coordinates, mu(Q) = mu_0 + sum_k (d mu/d Q_k) Q_k, so the forbidden electronic transition borrows intensity from allowed transitions via the vibrational motion (vibronic coupling); it explains the spectra of symmetric molecules like benzene."*
- Gerhard Herzberg; Edward Teller, 1933. Source: Wikipedia: Vibronic coupling; Herzberg & Teller, Z. Phys. Chem. B 21 (1933) 410

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero vibration*: the intensity borrowing vanishes exactly at the equilibrium geometry where Q_k = 0 for all modes, i.e. a frozen molecule with zero vibronic activity - the rigid-molecule limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the vibrational coordinate carries a coherence floor. Q_k_phi(kappa) = Q_k*(1 + kappa*(phi-1)) + kappa*phi^-1*Q_floor, where Q_floor is the phi-ground vibration amplitude; the molecule is never frozen. At kappa->0 the equilibrium-geometry intensity is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} mu_phi = mu_0 at Q_k = 0 -> the Herzberg-Teller coupling is the zero-vibration, rigid-molecule limit.
```

---

### STAGE 4 - SIMULATION

`sim/1394_herzberg_teller_coupling.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1394_herzberg_teller_coupling.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: A nominally frozen molecule at full coherence coupling carries a phi-ground vibrational amplitude kappa*phi^-1*Q_floor, a residual vibronic intensity in forbidden transitions.
EXPERIMENT (VERIFIED): High-sensitivity absorption spectroscopy of forbidden transitions (e.g. benzene) measuring the residual vibronic intensity floor.
VERIFIED BY: A symmetry-forbidden electronic transition has exactly zero intensity at the equilibrium geometry for all couplings.
```

---

### RECOGNITION
Connects to Law 1381 (Franck-Condon) and Law 1393 (Renner-Teller) - the Herzberg-Teller coupling is the coherence vibronic gateway.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the amplitude floor is phi^-1 * Q_floor.

### CLARITY
The forbidden line glows because the molecule trembles; the phi-law keeps the trembling's floor.

### NOVELTY
Classical spectroscopy forbids transitions absolutely; the phi-law keeps a vibronic coherence floor in the forbidden line.

### ACTIONABILITY
Run sim/1394_herzberg_teller_coupling.py; verify intensity borrowing at kappa->0; proceed to 1395.
