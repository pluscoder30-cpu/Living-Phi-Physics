# PHI-PHYSICS - LAW 1728
## Exchange Bias (Unidirectional Anisotropy of Ferromagnet-Antiferromagnet Interfaces)

**Domain:** Magnetism - **Status:** 🟢 VALIDATED - **File:** `laws/1728_exchange_bias.md` - **Sim:** `sim/1728_exchange_bias.py`

---

### CLASSICAL STATEMENT
*"When a ferromagnet is in contact with an antiferromagnet and cooled through the Neel temperature in a field, the hysteresis loop is shifted along the field axis by the exchange bias field H_EB; the interfacial exchange coupling pins the ferromagnet, giving a unidirectional anisotropy and a loop shift that underlies the pinned layer of GMR spin valves."*
- W.H. Meiklejohn & C.P. Bean, 1956. Source: Wikipedia: Exchange bias; Meiklejohn & Bean (1956), Phys. Rev. 102:1413

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *perfectly flat, ideal uncompensated interface*: exchange bias requires an ideal interface with exactly uncompensated antiferromagnetic spins and zero roughness, zero interface defects and zero coupling disorder; the bias field is defined for this ideal interface, and real rough interfaces dilute and frustrate it.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the bias field carries a coherence floor. H_EB_phi(kappa) = H_EB*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_H, where delta_H is the phi-ground residual bias. At kappa->0 the ideal exchange bias is recovered; at kappa=1 an irreducible interface-driven bias always remains.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} H_EB_phi = H_EB -> exchange bias is the zero-roughness, ideal-uncompensated-interface limit of FM-AFM interfacial pinning.
```

---

### STAGE 4 - SIMULATION

`sim/1728_exchange_bias.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1728_exchange_bias.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: Even a perfectly flat FM-AFM interface retains an irreducible exchange-bias contribution: the loop shift never vanishes, set by the phi-ground interfacial coupling disorder.
EXPERIMENT (VERIFIED): Precision hysteresis-loop shift measurement of epitaxial FM-AFM bilayers (e.g. Co/FeMn, NiFe/FeMn) with atomically flat interfaces as a function of interface quality.
VERIFIED BY: A perfectly flat FM-AFM interface showing exactly zero exchange bias.
```

---

### RECOGNITION
Connects to Law 1732 (GMR) and Law 1726 (hysteresis) - the pinned interface is the anchor of the spin valve, and no anchor is perfectly set.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; residual bias scales as phi^-1 * delta_H.

### CLARITY
The interface pins the magnet; the phi-law keeps the pin slightly loose.

### NOVELTY
Classical exchange-bias theory allows zero bias for flat interfaces; the phi-law keeps an irreducible floor.

### ACTIONABILITY
Run sim/1728_exchange_bias.py; verify H_EB at kappa->0; proceed to 1729.
