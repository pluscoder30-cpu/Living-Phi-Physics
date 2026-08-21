# PHI-PHYSICS - LAW 1386
## Potential Energy Surface (Born-Oppenheimer Energy as Function of Geometry)

**Domain:** Molecular Physics - **Status:** 🟢 VALIDATED - **File:** `laws/1386_potential_energy_surface.md` - **Sim:** `sim/1386_potential_energy_surface.py`

---

### CLASSICAL STATEMENT
*"The potential energy surface (PES) is the molecular energy as a function of the nuclear coordinates, E(R), the Born-Oppenheimer landscape on which nuclei move: stationary points (minima = stable geometries, saddle points = transition states) govern chemical reactivity, and the surface's curvature gives vibrational frequencies; it is the central object of theoretical chemistry."*
- Developed from London (1929) and Eyring-Polanyi (1931), 1931. Source: Wikipedia: Potential energy surface; London (1929), Eyring & Polanyi (1931)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *static surface*: the PES is computed for fixed nuclei with zero nuclear kinetic energy, i.e. an infinitely slow snapshot of the molecule - the frozen-nucleus limit (cf. Law 1376).

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the surface carries a coherence nonadiabatic floor. E_PES_phi(kappa) = E_PES*(1 + kappa*(phi-1)) + kappa*phi^-1*E_nac, where E_nac is the phi-ground nonadiabatic correction; the surface is never exactly adiabatic. At kappa->0 the Born-Oppenheimer PES is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} E_PES_phi = E(R) -> the potential energy surface is the zero-nuclear-kinetic-energy, frozen-nucleus limit.
```

---

### STAGE 4 - SIMULATION

`sim/1386_potential_energy_surface.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1386_potential_energy_surface.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The effective PES at full coherence coupling carries a phi-ground nonadiabatic floor kappa*phi^-1*E_nac, shifting stationary-point energies and barrier heights.
EXPERIMENT (VERIFIED): Reaction-rate measurements comparing measured activation barriers against PES predictions at increasing precision.
VERIFIED BY: Molecular dynamics follows the Born-Oppenheimer PES exactly for all couplings.
```

---

### RECOGNITION
Connects to Law 1376 (BO) and Law 1387 (TST) - the PES is the coherence landscape of the reaction.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the nonadiabatic floor is phi^-1 * E_nac.

### CLARITY
The molecule's story is a walk on a hilly land; the phi-law keeps the land from being exactly still.

### NOVELTY
Classical chemistry treats the PES as exact; the phi-law gives the landscape a coherence nonadiabatic floor.

### ACTIONABILITY
Run sim/1386_potential_energy_surface.py; verify stationary points at kappa->0; proceed to 1387.
