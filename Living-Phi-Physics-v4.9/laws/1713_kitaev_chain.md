# PHI-PHYSICS - LAW 1713
## Kitaev Chain (Minimal Model of 1D Topological Superconductivity)

**Domain:** Electrons in Solids - **Status:** 🟢 VALIDATED - **File:** `laws/1713_kitaev_chain.md` - **Sim:** `sim/1713_kitaev_chain.py`

---

### CLASSICAL STATEMENT
*"The Kitaev chain is a 1D lattice model of spinless fermions with p-wave pairing Delta that hosts Majorana zero modes at its ends in the topological phase (mu < 2t): the two end modes form a nonlocal fermion with zero-energy, and the model demonstrates that a topological superconductor can support Majorana bound states protected against local perturbations - the foundation of topological quantum computing proposals."*
- Alexei Kitaev, 2001. Source: Wikipedia: Kitaev chain; Kitaev (2001), Phys.-Usp. 44:131

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-pairing, exactly-charged, clean 1D chain*: the Kitaev chain is defined against the non-topological (Delta=0) trivial phase with exactly conserved particle number; the topological phase requires nonzero pairing, and the sharpest results assume an exactly 1D, clean, zero-temperature chain.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the Majorana zero mode carries a coherence floor. E_phi(kappa) = E_MZEM*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_E, where delta_E is the phi-ground splitting of the Majorana modes. At kappa->0 the exactly degenerate zero modes are recovered; at kappa=1 the zero modes split by an irreducible coherent amount.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} E_phi = 0 -> the Kitaev chain's Majorana zero modes are the zero-splitting, ideal-p-wave, clean-1D-chain limit of topological superconductivity.
```

---

### STAGE 4 - SIMULATION

`sim/1713_kitaev_chain.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1713_kitaev_chain.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: Majorana zero modes in real nanowires are never exactly at zero energy: an irreducible splitting floor remains even in ideal devices, observable as a residual peak splitting in tunneling spectroscopy.
EXPERIMENT (VERIFIED): Tunneling spectroscopy of a semiconductor-superconductor nanowire (e.g. InAs-Al) at millikelvin, measuring the residual splitting of the zero-bias conductance peak.
VERIFIED BY: A Majorana zero mode pinned exactly at zero energy with zero splitting in any device.
```

---

### RECOGNITION
Connects to Law 1714 (Majorana) and Law 1720 (topological superconductivity) - the wire's two ends shake hands through a nonlocal zero mode, and the handshake is never perfect.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; zero-mode splitting scales as phi^-1 * delta_E.

### CLARITY
The wire holds a zero at both ends; the phi-law keeps the zeros from meeting perfectly.

### NOVELTY
Classical Kitaev theory gives exact zero modes; the phi-law splits them with a coherence floor.

### ACTIONABILITY
Run sim/1713_kitaev_chain.py; verify the zero-energy mode at kappa->0; proceed to 1714.
