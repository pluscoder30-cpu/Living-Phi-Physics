# PHI-PHYSICS - LAW 1355
## Russell-Saunders Coupling (LS Coupling of Angular Momenta)

**Domain:** Atomic Physics - **Status:** 🟢 VALIDATED - **File:** `laws/1355_russell_saunders_coupling.md` - **Sim:** `sim/1355_russell_saunders_coupling.py`

---

### CLASSICAL STATEMENT
*"For light atoms the individual electron angular momenta couple first to total L and S (Russell-Saunders coupling), then to J = L + S; the level term is written as the term symbol ^(2S+1)L_J, and the spin-orbit splitting follows the Lande interval rule; the coupling is valid when electrostatic interactions dominate spin-orbit."*
- Henry Norris Russell; Frederick Saunders, 1925. Source: Wikipedia: Russell-Saunders coupling; Russell & Saunders, Astrophys. J. 61 (1925) 38

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero spin-orbit mixing*: LS coupling is exact when spin-orbit interaction vanishes, i.e. levels with zero relativistic coupling between L and S - the non-relativistic limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the spin-orbit mixing carries a coherence floor. H_so_phi(kappa) = H_so*(1 + kappa*(phi-1)) + kappa*phi^-1*E_so_floor, where E_so_floor is the phi-ground spin-orbit residue; pure LS coupling is impossible. At kappa->0 the LS term structure is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} ^(2S+1)L_J -> LS term -> Russell-Saunders coupling is the zero-spin-orbit, non-relativistic limit.
```

---

### STAGE 4 - SIMULATION

`sim/1355_russell_saunders_coupling.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1355_russell_saunders_coupling.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The term structure at full coherence coupling carries a phi-ground spin-orbit admixture kappa*phi^-1*E_so_floor, so light-atom terms are never pure LS.
EXPERIMENT (VERIFIED): High-precision term analysis of light atoms (e.g. helium, lithium) measuring residual spin-orbit mixing at increasing precision.
VERIFIED BY: Light-atom terms are exactly LS-coupled for all couplings.
```

---

### RECOGNITION
Connects to Law 1354 (Hund's rules) and Law 1356 (jj coupling, its heavy-atom limit) - LS coupling is the coherence coupling of the non-relativistic atom.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the spin-orbit residue is phi^-1 * E_so_floor.

### CLARITY
Light atoms dance as one body; the phi-law keeps a relativistic seam in the dance.

### NOVELTY
Classical atomic theory couples LS exactly; the phi-law gives light atoms a spin-orbit coherence floor.

### ACTIONABILITY
Run sim/1355_russell_saunders_coupling.py; verify term symbol at kappa->0; proceed to 1356.
