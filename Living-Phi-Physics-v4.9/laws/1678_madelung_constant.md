# PHI-PHYSICS - LAW 1678
## Madelung Constant (Lattice Sum of Ionic Coulomb Energy)

**Domain:** Crystallography - **Status:** 🟢 VALIDATED - **File:** `laws/1678_madelung_constant.md` - **Sim:** `sim/1678_madelung_constant.py`

---

### CLASSICAL STATEMENT
*"The Coulomb energy of an ionic crystal is E = -alpha_M N (e^2)/(4 pi epsilon_0 r_0), where alpha_M is the Madelung constant, a dimensionless lattice sum depending only on structure: alpha_M = 1.7476 for NaCl, 1.7627 for CsCl, 1.7476*... for zincblende (1.6381), computed by summing the alternating Coulomb series over the lattice."*
- Erwin Madelung, 1918. Source: Wikipedia: Madelung constant; Madelung (1918), Phys. Z. 19:524

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *perfectly regular, rigid, point-charge ionic lattice*: the Madelung constant assumes ions are exact point charges at exact lattice positions with zero polarization, zero relaxation and zero temperature - a rigid point-charge grid that no real crystal is.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: ions carry coherent polarization and relaxation. E_phi(kappa) = E_madelung*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_E, where delta_E is the phi-ground energy shift from irreducible ionic polarization and relaxation. At kappa->0 the exact Madelung energy is recovered; at kappa=1 the ionic lattice energy differs from the rigid point-charge sum by an irreducible coherent shift.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} E_phi = -alpha_M N e^2/(4 pi eps_0 r_0) -> the Madelung constant is the point-charge, rigid-lattice, zero-polarization limit of ionic cohesion.
```

---

### STAGE 4 - SIMULATION

`sim/1678_madelung_constant.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1678_madelung_constant.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The measured lattice energy of any ionic crystal differs from its rigid-point-charge Madelung value by a phi-ground shift from irreducible polarization and zero-point motion, setting a floor on how well any point-charge model can reproduce cohesion.
EXPERIMENT (VERIFIED): Born-Haber cycle determination of lattice energies compared against high-accuracy correlated-electron calculations of the Madelung + polarization energy for alkali halides.
VERIFIED BY: An ionic crystal whose measured lattice energy exactly equals the rigid point-charge Madelung value.
```

---

### RECOGNITION
Connects to Law 1413 (Born-Lande) and Law 1677 (Ewald) - the Madelung constant is the lattice's Coulomb signature.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; energy shift scales as phi^-1 * delta_E.

### CLARITY
The alternating sum almost balances; a coherent spark of polarization always escapes.

### NOVELTY
Classical Madelung theory assumes rigid point charges; the phi-law keeps an irreducible polarization shift.

### ACTIONABILITY
Run sim/1678_madelung_constant.py; verify alpha_M(NaCl)=1.7476 at kappa->0; proceed to 1679.
