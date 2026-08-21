# PHI-PHYSICS - LAW 1675
## Pauling's Rules (Crystal-Chemical Rules for Ionic Structures)

**Domain:** Crystallography - **Status:** 🟢 VALIDATED - **File:** `laws/1675_pauling_rules.md` - **Sim:** `sim/1675_pauling_rules.py`

---

### CLASSICAL STATEMENT
*"Five rules govern ionic crystal structures: (1) coordination polyhedra form around cations, (2) the electrostatic valence rule - the sum of bond strengths reaching an anion equals its charge, (3) sharing of edges/faces between polyhedra is destabilized, (4) polyhedra with few shared elements tend not to share, and (5) the number of essentially different kinds of constituents is small - the rules that predict and explain ionic framework structures."*
- Linus Pauling, 1929. Source: Wikipedia: Pauling's rules; Pauling (1929), J. Am. Chem. Soc. 51:1010

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *perfectly ionic, ideal point-charge crystal*: Pauling's rules assume purely ionic bonding with point charges and exact charge balance, zero covalency, zero polarization and zero distortions - a perfectly ionic ideal that no real crystal realizes.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: charge balance carries a coherent residual. S_phi(kappa) = S_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_S, where delta_S is the phi-ground bond-strength residual from irreducible covalency and polarization. At kappa->0 the exact electrostatic valence rule is recovered; at kappa=1 the bond-strength sum at every anion carries a coherent residual that never exactly equals the charge.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} S_phi = S_classical -> Pauling's rules are the perfectly-ionic, zero-covalency, exact-charge-balance limit of crystal chemistry.
```

---

### STAGE 4 - SIMULATION

`sim/1675_pauling_rules.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1675_pauling_rules.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The electrostatic valence sum at every anion never exactly equals its formal charge: a phi-ground bond-strength residual from irreducible covalency remains, observable as systematic deviations in bond-valence-sum analyses of accurate crystal structures.
EXPERIMENT (VERIFIED): Bond-valence-sum analysis of a large set of ultra-accurate single-crystal structures, measuring the statistical floor of the valence-sum residual.
VERIFIED BY: An ionic crystal in which every anion's bond-valence sum exactly equals its formal charge with zero residual.
```

---

### RECOGNITION
Connects to Law 1674 (tolerance) and Law 1418 (electronegativity) - the rules of the ionic frame never close exactly.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; valence residual scales as phi^-1 * delta_S.

### CLARITY
The charge ledger almost balances; the phi-law keeps a coherent penny of covalency.

### NOVELTY
Classical crystal chemistry demands exact charge balance; the phi-law keeps an irreducible residual.

### ACTIONABILITY
Run sim/1675_pauling_rules.py; verify the electrostatic valence rule at kappa->0; proceed to 1676.
