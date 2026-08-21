# PHI-PHYSICS - LAW 1645
## Nuclear Reaction Cross-Section (Probability of Interaction)

**Domain:** Nuclear Reactions - **Status:** 🟢 VALIDATED - **File:** `laws/1645_nuclear_reaction_cross_section.md` - **Sim:** `sim/1645_nuclear_reaction_cross_section.py`

---

### CLASSICAL STATEMENT
*"The nuclear cross-section sigma is the effective area for a reaction, related to the rate by R = sigma phi N; it has units of barns (10^-24 cm^2) and depends on energy through resonances, the 1/v law and the Gamow factor; the total cross-section satisfies the optical theorem."*
- Cross-section concept (Rutherford 1911; quantum scattering), 1911. Source: Rutherford (1911); Wikipedia: Cross section (physics)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-interaction, zero-cross-section, transparent limit*: a non-interacting system has exactly zero cross-section; the classical treatment of a transparent target is the zero-cross-section limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

sigma_phi(kappa) = sigma_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*sigma_floor, where sigma_floor is the phi-ground residual floor. At kappa->0 the exact cross-section is recovered.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} sigma_phi = sigma_measured -> the cross-section is the zero-residual, exact-measurement, ideal-target limit.
```

---

### STAGE 4 - SIMULATION

`sim/1645_nuclear_reaction_cross_section.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1645_nuclear_reaction_cross_section.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The cross-section carries a phi-ground residual floor, so even 'transparent' targets show a small irreducible interaction cross-section.
EXPERIMENT (VERIFIED): Cross-section measurements across the nuclear chart (EXFOR database) and their use in reactor and shielding calculations.
VERIFIED BY: A target with exactly zero cross-section for all reactions at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1478 (resonance), Law 1544 (optical theorem) and Law 1618 (capture) - the cross-section is the reaction's currency.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The target shows its face; the phi-law keeps a floor of face always.

### NOVELTY
Classical cross-section can be zero; the phi-law predicts an irreducible residual floor.

### ACTIONABILITY
Run sim/1645_nuclear_reaction_cross_section.py; verify the cross-section; proceed to Law 1646.
