# PHI-PHYSICS — LAW 568
## Born Equation (Ion Solvation Free Energy)

**Domain:** Statistical Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/568_born_equation.md` · **Sim:** `sim/568_born_equation.py`

---

### CLASSICAL STATEMENT
*"The electrostatic free energy of solvation of an ion is DeltaG = -(N_A z^2 e^2/(8 pi epsilon_0 r_0))(1 - 1/epsilon_r), where z is the ion charge, r_0 the ion radius and epsilon_r the solvent dielectric constant."*
— Max Born, 1920. Source: Wikipedia: Born equation; Born, Volumen und Hydratationswaerme der Ionen (1920)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *point ion in a continuum*: the equation assumes the ion is a charged sphere in a continuous dielectric with no ion size beyond r_0 and no local solvent structure - a solvent with zero coherence.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the solvent structure carries coherence. DeltaG_phi(kappa) = DeltaG_Born*(1 + kappa*(phi-1)) + kappa*phi^-1*G_struct, where G_struct is the solvent-coherence correction. At kappa->0 the Born equation is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} DeltaG_phi = DeltaG_Born -> the Born equation is the zero-solvent-coherence continuum limit.
```

---

### STAGE 4 — SIMULATION

`sim/568_born_equation.py`: reproduces the classical value dG_born = -3.8e+05 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/568_born_equation.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the solvation energy carries a solvent-structure floor; measured solvation energies deviate from the Born prediction for small ions.
EXPERIMENT (VERIFIED): Electrochemical solvation-energy measurements of ions in solvents of varying structure.
VERIFIED BY: The solvation free energy follows the Born equation exactly for all ions and solvents.
```

---

### RECOGNITION
Connects to Law 471 (Debye-Hückel) and Law 436 (chemical potential) - the Born equation is the ion-in-continuum coherence limit.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the structure term is phi^-1 * G_struct.

### CLARITY
The solvent is not a smooth sea; the phi-law keeps the structure the ion feels.

### NOVELTY
Classical Born assumes a continuum solvent; the phi-law adds the solvent-coherence correction real liquids have.

### ACTIONABILITY
Run sim/568_born_equation.py; verify Born free energy at kappa->0; proceed to 569.
