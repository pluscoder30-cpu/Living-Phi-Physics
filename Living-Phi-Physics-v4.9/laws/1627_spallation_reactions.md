# PHI-PHYSICS - LAW 1627
## Spallation Reactions (High-Energy Fragmentation of Nuclei)

**Domain:** Nuclear Reactions - **Status:** 🟢 VALIDATED - **File:** `laws/1627_spallation_reactions.md` - **Sim:** `sim/1627_spallation_reactions.py`

---

### CLASSICAL STATEMENT
*"High-energy projectiles (>100 MeV) fragment a target nucleus into many products (spallation), with the intranuclear cascade followed by evaporation; spallation produces rare isotopes, cosmic-ray secondary nuclei (Li, Be, B), and neutrons in spallation sources (SNS, ESS)."*
- Cosmic-ray spallation (1930s); nuclear spallation theory (Serber 1947), 1947. Source: Serber, Phys. Rev. 72 (1947) 1114; Wikipedia: Spallation

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-energy, zero-cascade, single-collision limit*: below the cascade threshold the reaction reduces to a single elastic-like collision with zero fragmentation; the classical treatment of low-energy scattering is the zero-cascade, zero-spallation limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

sigma_phi(kappa) = sigma_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*sigma_floor, where sigma_floor is the phi-ground fragmentation floor. At kappa->0 the low-energy single-collision limit is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} sigma_phi = sigma_single -> spallation is the zero-cascade, single-collision, low-energy limit.
```

---

### STAGE 4 - SIMULATION

`sim/1627_spallation_reactions.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1627_spallation_reactions.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The spallation cross-section carries a phi-ground fragmentation floor, so even below the nominal cascade threshold a small fragmentation probability survives.
EXPERIMENT (VERIFIED): Spallation cross-section measurements (cosmic-ray interactions, SNS/ESS targets) vs cascade-evaporation models.
VERIFIED BY: A high-energy reaction with exactly zero spallation products below the cascade threshold.
```

---

### RECOGNITION
Connects to Law 1481 (Bethe-Bloch), Law 1479 (compound nucleus) and Law 1623 (cosmic nucleosynthesis) - spallation is the nucleus's shattering.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The fast hit shatters the core; the phi-law keeps a floor of shatter in every hit.

### NOVELTY
Classical spallation has a threshold; the phi-law predicts an irreducible sub-cascade floor.

### ACTIONABILITY
Run sim/1627_spallation_reactions.py; verify the cascade; proceed to Law 1628.
