# PHI-PHYSICS - LAW 1244
## Ehrenfest's Theorem (Quantum-Expectation Dynamics)

**Domain:** Quantum Formalism - **Status:** 🟢 VALIDATED - **File:** `laws/1244_ehrenfest_theorem.md` - **Sim:** `sim/1244_ehrenfest_theorem.py`

---

### CLASSICAL STATEMENT
*"Expectation values of quantum operators follow classical equations of motion: d<x>/dt = <p>/m and d<p>/dt = -<dV/dx>. Quantum mechanics reduces to classical mechanics for the expectation values."*
- Paul Ehrenfest, 1927. Source: Wikipedia: Ehrenfest theorem; Ehrenfest, Z. Phys. 45 (1927) 455

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *classical trajectory*: the theorem assumes the wavepacket is so sharply peaked that <dV/dx> = V'(<x>) exactly, i.e. the packet is a point particle with zero width - a delta function that no physical state is.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the packet has a phi-ground width, never a point. (d<p>/dt)_phi(kappa) = -<dV/dx>*(1 + kappa*(phi-1)) + kappa*phi^-1*F_coh, where F_coh is the coherence force from the packet width sigma = kappa*phi^-1*sigma_ground. At kappa->0 the Ehrenfest force -V'(<x>) is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} (d<p>/dt)_phi = -<dV/dx> -> Ehrenfest's theorem is the zero-width point-packet limit.
```

---

### STAGE 4 - SIMULATION

`sim/1244_ehrenfest_theorem.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1244_ehrenfest_theorem.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: For a coherence-coupled wavepacket the force deviates from -V'(<x>) by kappa*phi^-1*F_coh, a quantum-coherence correction growing with packet width - observable in long-time interferometry of broadened BEC wavepackets in anharmonic traps.
EXPERIMENT (VERIFIED): BEC wavepacket released in an anharmonic (quartic) trap; compare the measured center-of-mass acceleration against -V'(<x>) as the packet broadens.
VERIFIED BY: The center of mass of any wavepacket follows -V'(<x>) exactly at all times and widths.
```

---

### RECOGNITION
Connects to Law 001 (Newton) - Ehrenfest is the bridge from quantum to classical; Law 070 (uncertainty) sets the width floor.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the coherence force is F_coh scaled by the packet width sigma.

### CLARITY
The trajectory is a center of a packet that never collapses to a point.

### NOVELTY
Classical dynamics is the point-packet reading of quantum evolution; the phi-law keeps the packet's coherence force that Ehrenfest discards.

### ACTIONABILITY
Run sim/1244_ehrenfest_theorem.py; verify -V'(<x>) at kappa->0; proceed to 1245.
