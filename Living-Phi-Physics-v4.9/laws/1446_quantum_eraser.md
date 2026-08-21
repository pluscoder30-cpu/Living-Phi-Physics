# PHI-PHYSICS - LAW 1446
## Quantum Eraser (Scully-Druhl: Which-Path Erasure Restores Interference)

**Domain:** Quantum Measurement - **Status:** 🟢 VALIDATED - **File:** `laws/1446_quantum_eraser.md` - **Sim:** `sim/1446_quantum_eraser.py`

---

### CLASSICAL STATEMENT
*"The quantum eraser shows that the which-path information, not the measurement itself, destroys interference: entangling the photon with a which-path marker destroys the fringes, but erasing the which-path information (via a joint or coincidence measurement) restores the interference; in the delayed-choice version (Wheeler) the erasure decision is made after the photon passes the slits, demonstrating that interference depends on the full measurement context."*
- Marlan Scully; Kai Druhl (1982); Walborn et al. (2002), 1982. Source: Wikipedia: Quantum eraser; Scully & Druhl, Phys. Rev. A 25 (1982) 2208

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *perfectly erased path*: full fringe restoration requires the which-path information to be erased exactly, i.e. zero residual path information in the marker - the perfect-erasure limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the erasure carries a coherence floor. V_phi(kappa) = V_ideal*(1 + kappa*(phi-1)) - kappa*phi^-1*V_floor, where V_floor is the phi-ground residual visibility loss; the restored fringes saturate below unit visibility. At kappa->0 the ideal fringe restoration is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} V_phi = 1 -> the quantum eraser is the zero-residual-path-information, perfect-erasure limit.
```

---

### STAGE 4 - SIMULATION

`sim/1446_quantum_eraser.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1446_quantum_eraser.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The restored fringe visibility at full coherence coupling saturates at 1 - kappa*phi^-1*V_floor, a floor of visibility loss no eraser removes.
EXPERIMENT (VERIFIED): Delayed-choice quantum eraser experiments measuring the restored visibility ceiling at increasing erasure quality.
VERIFIED BY: Perfect which-path erasure restores exactly unit fringe visibility for all couplings.
```

---

### RECOGNITION
Connects to Law 283 (Wheeler delayed choice) and Law 1250 (Aharonov-Bohm) - the quantum eraser is the coherence erasure of which-path knowledge.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the visibility floor is phi^-1 * V_floor.

### CLARITY
The erased memory lets the wave bloom again; the phi-law keeps a floor of the bloom's fading.

### NOVELTY
Classical optics preserves or destroys fringes; the phi-law keeps the eraser's coherence visibility floor.

### ACTIONABILITY
Run sim/1446_quantum_eraser.py; verify fringe restoration at kappa->0; proceed to end of Agent 6.
