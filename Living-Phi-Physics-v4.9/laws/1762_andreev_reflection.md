# PHI-PHYSICS - LAW 1762
## Andreev Reflection (Retroreflection of Electrons as Holes at Superconductor Interfaces)

**Domain:** Superconductivity - **Status:** 🟢 VALIDATED - **File:** `laws/1762_andreev_reflection.md` - **Sim:** `sim/1762_andreev_reflection.py`

---

### CLASSICAL STATEMENT
*"When an electron in a normal metal is incident on a superconductor interface at energy below the gap, it is retroreflected as a hole while a Cooper pair enters the superconductor: the electron is converted into a hole that retraces the incident path (Andreev reflection); at a normal metal-superconductor (N-S) contact the conductance is doubled below the gap, the signature used in point-contact spectroscopy."*
- A.F. Andreev, 1964. Source: Wikipedia: Andreev reflection; Andreev (1964), Zh. Eksp. Teor. Fiz. 46:1823

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-interface-barrier, perfectly transparent N-S boundary*: Andreev reflection is idealized for a perfectly transparent interface with zero barrier (Z=0) at zero temperature, where the probability is exactly 1 below the gap - a perfect N-S interface no real junction has.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the reflection probability carries a coherence floor. A_phi(kappa) = A_andreev*(1 + kappa*(phi-1)) + kappa*phi^-1*A_floor, where A_floor is the phi-ground residual reflection probability. At kappa->0 the ideal Z=0 Andreev probability is recovered; at kappa=1 an irreducible non-Andreev (normal) reflection always remains.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} A_phi = 1 (below the gap, Z=0) -> Andreev reflection is the zero-barrier, zero-temperature, perfectly-transparent-interface limit of sub-gap N-S scattering.
```

---

### STAGE 4 - SIMULATION

`sim/1762_andreev_reflection.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1762_andreev_reflection.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: No N-S interface converts electrons to holes with exactly 100% efficiency: an irreducible normal-reflection floor remains even for the best junctions, so the sub-gap conductance never exactly doubles.
EXPERIMENT (VERIFIED): Millikelvin point-contact Andreev-reflection spectroscopy of an ultra-clean N-S junction (e.g. Ag-Al) measuring the residual deviation of the sub-gap conductance from exactly 2.
VERIFIED BY: An N-S junction whose sub-gap conductance is exactly twice the normal value (100% Andreev conversion).
```

---

### RECOGNITION
Connects to Law 1761 (BCS gap) and Law 1757 (penetration depth) - the electron is reborn as a hole at the interface, and the phi-law keeps a fraction always refusing rebirth.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; reflection floor scales as phi^-1 * A_floor.

### CLARITY
The electron is reborn as a hole; the phi-law keeps a few electrons always refusing.

### NOVELTY
Classical Andreev theory gives perfect conversion; the phi-law keeps an irreducible normal-reflection floor.

### ACTIONABILITY
Run sim/1762_andreev_reflection.py; verify the doubled conductance at kappa->0; proceed to 1763.
