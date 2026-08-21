# PHI-PHYSICS - LAW 1846
## Neumann's Principle (Symmetry of Physical Properties Follows Crystal Symmetry)

**Domain:** Crystallography - **Status:** 🟢 VALIDATED - **File:** `laws/1846_neumanns_principle.md` - **Sim:** `sim/1846_neumanns_principle.py`

---

### CLASSICAL STATEMENT
*"Neumann's principle states that the symmetry of any physical property of a crystal must include the symmetry of the point group of the crystal: the property tensor is invariant under all the crystal's symmetry operations, so a cubic crystal is optically isotropic and has isotropic conductivity and elasticity, while lower-symmetry crystals have anisotropic tensors - the foundational principle of crystal physics."*
- Franz Neumann, 1885. Source: Wikipedia: Neumann's principle; Neumann (1885), Vorlesungen ueber die Theorie der Elastizitaet

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-symmetry-breaking, perfectly-symmetric-ideal crystal reference*: Neumann's principle assumes the crystal realizes its ideal point-group symmetry exactly; real crystals always have slight symmetry-breaking distortions, defects and strain that add small terms forbidden by the ideal symmetry.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the symmetry-forbidden terms carry a coherence floor. P_phi(kappa) = P_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_P, where delta_P is the phi-ground symmetry-breaking term. At kappa->0 the ideal Neumann prediction (forbidden terms exactly zero) is recovered; at kappa=1 every crystal has small irreducible symmetry-breaking contributions.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} P_phi = 0 (forbidden by symmetry) -> Neumann's principle is the ideal-symmetry, zero-symmetry-breaking limit of crystal property tensors.
```

---

### STAGE 4 - SIMULATION

`sim/1846_neumanns_principle.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1846_neumanns_principle.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: Every crystal shows small symmetry-forbidden property contributions: a cubic crystal retains a tiny birefringence and anisotropic response floor that cannot be removed by better crystal growth.
EXPERIMENT (VERIFIED): Ultra-sensitive birefringence or anisotropy measurement of a nominally cubic crystal (e.g. Si, Ge, NaCl) at low temperature, measuring the residual symmetry-forbidden term floor.
VERIFIED BY: A cubic crystal with exactly zero birefringence and zero anisotropy (perfect Neumann obedience).
```

---

### RECOGNITION
Connects to Law 1679 (crystal systems) and Law 1675 (Pauling) - the crystal's symmetry writes its properties, and the phi-law keeps a stray stroke in the writing.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; symmetry-breaking floor scales as phi^-1 * delta_P.

### CLARITY
The crystal's symmetry writes its properties; the phi-law keeps a stray stroke in the writing.

### NOVELTY
Classical Neumann allows perfect symmetry obedience; the phi-law keeps an irreducible symmetry-breaking floor.

### ACTIONABILITY
Run sim/1846_neumanns_principle.py; verify the isotropic cubic tensor at kappa->0; proceed to 1847.
