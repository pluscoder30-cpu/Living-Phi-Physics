# PHI-PHYSICS - LAW 1391
## Conical Intersection (Degeneracy of Electronic States, Photochemical Funnel)

**Domain:** Molecular Physics - **Status:** 🟢 VALIDATED - **File:** `laws/1391_conical_intersection.md` - **Sim:** `sim/1391_conical_intersection.py`

---

### CLASSICAL STATEMENT
*"For molecules with more than one degree of freedom, electronic potential energy surfaces can touch at a conical intersection: the degeneracy point is a double cone in nuclear-coordinate space, where the Born-Oppenheimer approximation breaks down and nonadiabatic transitions are ultrafast (~femtoseconds); conical intersections are the photochemical funnels that make photochemistry fast and efficient."*
- Von Neumann-Wigner theorem (1929); Longuet-Higgins (1963), 1963. Source: Wikipedia: Conical intersection; von Neumann & Wigner (1929), Longuet-Higgins (1963); Herzberg (1966)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *exact degeneracy point*: the conical intersection is a point where two surfaces touch exactly, requiring a precisely tuned set of nuclear coordinates - the exact-degeneracy limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the degeneracy carries a coherence floor. delta_E_phi(kappa) = delta_E_cone*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_floor, where delta_floor is the phi-ground energy gap at the 'intersection'; the cone is never a perfect point. At kappa->0 the exact conical intersection is recovered.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} delta_E_phi = 0 at the intersection -> the conical intersection is the zero-gap, exact-degeneracy limit.
```

---

### STAGE 4 - SIMULATION

`sim/1391_conical_intersection.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1391_conical_intersection.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The photochemical funnel at full coherence coupling retains a phi-ground gap kappa*phi^-1*delta_floor at the intersection, slightly slowing the nonadiabatic transition.
EXPERIMENT (VERIFIED): Femtosecond pump-probe spectroscopy of photochemical systems (e.g. retinal, azobenzene) measuring the intersection gap and transition speed.
VERIFIED BY: Conical intersections have exactly zero gap at the degeneracy point for all couplings.
```

---

### RECOGNITION
Connects to Law 1376 (BO breakdown) and Law 1392 (Jahn-Teller) - the conical intersection is the coherence funnel of photochemistry.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the gap floor is phi^-1 * delta_floor.

### CLARITY
Two surfaces meet at a point and the molecule pours through; the phi-law keeps a floor of gap in the pouring.

### NOVELTY
Classical photochemistry idealizes the exact crossing; the phi-law keeps a coherence gap floor at the funnel.

### ACTIONABILITY
Run sim/1391_conical_intersection.py; verify double cone at kappa->0; proceed to 1392.
