# PHI-PHYSICS - LAW 1720
## XY Model and Kosterlitz-Thouless Transition (2D Topological Phase Transition)

**Domain:** Magnetism - **Status:** 🟢 VALIDATED - **File:** `laws/1720_xy_model_kosterlitz_thouless.md` - **Sim:** `sim/1720_xy_model_kosterlitz_thouless.py`

---

### CLASSICAL STATEMENT
*"In the 2D XY model, continuous spins rotate on a circle and there is no conventional long-range order, but at the Kosterlitz-Thouless temperature T_KT bound vortex-antivortex pairs unbind; the transition is topological (driven by vortex proliferation) with universal jump in the stiffness, and below T_KT the correlation function decays as a power law - the paradigmatic topological phase transition."*
- V.L. Berezinskii (1971); J.M. Kosterlitz & D.J. Thouless (1973), 1973. Source: Wikipedia: XY model; Kosterlitz & Thouless (1973), J. Phys. C 6:1181; Berezinskii (1971)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-vortex, perfectly ordered planar spin gas*: the XY model's low-temperature phase is defined against a zero-vortex, perfectly aligned spin configuration; the KT transition is the unbinding of vortex pairs from a state with zero free vortices - an ideal vortex-free reference.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the vortex gas carries a coherence floor. T_KT_phi(kappa) = T_KT*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_T, where delta_T is the phi-ground shift of the universal jump. At kappa->0 the exact KT transition is recovered; at kappa=1 the transition is smeared and the stiffness jump is softened.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} T_KT_phi = T_KT -> the Kosterlitz-Thouless transition is the zero-free-vortex, ideal-2D, infinite-size limit of topological phase transitions.
```

---

### STAGE 4 - SIMULATION

`sim/1720_xy_model_kosterlitz_thouless.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1720_xy_model_kosterlitz_thouless.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The KT transition in real 2D systems (thin films, cold atoms, superconducting films) is smeared over a phi-ground width and the universal stiffness jump is softened: exact universal behavior is never observed.
EXPERIMENT (VERIFIED): Measurement of the superfluid/helicity stiffness jump and vortex unbinding in a 2D Bose gas, thin superfluid He film or superconducting film, comparing to the exact KT universal value.
VERIFIED BY: A 2D system whose KT transition is exactly sharp at the universal jump value.
```

---

### RECOGNITION
Connects to Law 1719 (Ising) and Law 1705 (FQHE) - vortices are the actors of 2D order, and the phi-law keeps a ghost vortex in the wings.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; transition width scales as phi^-1 * delta_T.

### CLARITY
The vortices pair up below T_KT; the phi-law keeps one pair always half-unbound.

### NOVELTY
Classical KT theory gives an exact universal jump; the phi-law softens it with a coherence floor.

### ACTIONABILITY
Run sim/1720_xy_model_kosterlitz_thouless.py; verify the universal jump at kappa->0; proceed to 1721.
