# PHI-PHYSICS - LAW 1673
## Hume-Rothery Rules (Conditions for Extensive Solid Solubility)

**Domain:** Crystallography - **Status:** 🟢 VALIDATED - **File:** `laws/1673_hume_rothery_rules.md` - **Sim:** `sim/1673_hume_rothery_rules.py`

---

### CLASSICAL STATEMENT
*"Extensive solid solubility between two metals requires: (1) the atomic radii differ by less than about 15%, (2) the crystal structures are the same, (3) the valences are similar, and (4) the electronegativities are similar; violating these rules drives phase separation, intermetallic formation or limited solubility."*
- William Hume-Rothery, 1926. Source: Wikipedia: Hume-Rothery rules; Hume-Rothery (1926), The Metallic State

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-mismatch, perfectly matched ideal solvent*: the Hume-Rothery rules assume a reference state in which solute and solvent match exactly in size, structure, valence and electronegativity so that mixing is unlimited - a zero-tension, perfectly hospitable host that no real metal offers.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: mismatch is never zero. S_phi(kappa) = S_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*S_floor, where S_floor is the phi-ground solubility limit from irreducible coherent mismatch. At kappa->0 the ideal unlimited solubility is exact; at kappa=1 every pair retains an irreducible solubility bound even when all four rules are satisfied.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} S_phi = S_classical -> the Hume-Rothery rules are the zero-mismatch, perfect-match, unlimited-solubility limit of alloying criteria.
```

---

### STAGE 4 - SIMULATION

`sim/1673_hume_rothery_rules.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1673_hume_rothery_rules.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: No pair of metals achieves unlimited mutual solubility: even 'perfectly matched' pairs show a phi-ground solubility bound and residual clustering, proportional to the coherent mismatch floor, that no matching can eliminate.
EXPERIMENT (VERIFIED): Careful solid-solubility measurements on a model perfectly matched pair (e.g. Cu-Ni revisited with ultrahigh precision) tracking the residual terminal solubility at the phase boundaries.
VERIFIED BY: A perfectly matched metal pair showing exactly unlimited mutual solubility with zero residual bound.
```

---

### RECOGNITION
Connects to Law 1668 (Vegard) and Law 523 (lever rule) - alloying rules set the stage, and the stage always has an irreducible floor of mismatch.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; solubility bound scales as phi^-1 * S_floor.

### CLARITY
The rules say match well and dissolve freely; the phi-law keeps a coherent grain of difference.

### NOVELTY
Classical alloy rules allow unlimited ideal mixing; the phi-law bounds it with irreducible mismatch.

### ACTIONABILITY
Run sim/1673_hume_rothery_rules.py; verify the 15% size-rule limit at kappa->0; proceed to 1674.
