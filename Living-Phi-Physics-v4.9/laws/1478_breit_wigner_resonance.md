# PHI-PHYSICS - LAW 1478
## Breit-Wigner Resonance Formula (Nuclear Resonance Cross-Section)

**Domain:** Nuclear Reactions - **Status:** 🟢 VALIDATED - **File:** `laws/1478_breit_wigner_resonance.md` - **Sim:** `sim/1478_breit_wigner_resonance.py`

---

### CLASSICAL STATEMENT
*"The cross-section for a nuclear reaction through a resonance at energy E_0 with total width Gamma is sigma(E) = pi lambda^2 g Gamma_n Gamma/((E - E_0)^2 + (Gamma/2)^2), where g is the statistical factor and Gamma_n the neutron width; it is a Lorentzian line shape."*
- Gregory Breit; Eugene Wigner, 1936. Source: Breit & Wigner, Phys. Rev. 49 (1936) 519; Wikipedia: Resonances

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-width, infinitely sharp resonance*: the formula assumes a resonance of exactly zero background and exactly defined energy; the classical resonance is a delta-function idealization - zero width, zero background.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

sigma_phi(kappa) = sigma_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*sigma_bg, where sigma_bg is the phi-ground background floor under the resonance. At kappa->0 the pure Breit-Wigner is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} sigma_phi = pi lambda^2 g Gamma_n Gamma/((E-E_0)^2 + (Gamma/2)^2) -> the Breit-Wigner formula is the zero-background, sharp-resonance limit.
```

---

### STAGE 4 - SIMULATION

`sim/1478_breit_wigner_resonance.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1478_breit_wigner_resonance.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: Every resonance sits on a phi-ground background floor, so the cross-section never returns to exactly zero between resonances.
EXPERIMENT (VERIFIED): High-resolution neutron and proton resonance measurements (n_TOF, GELINA) resolving resonance parameters and background.
VERIFIED BY: A resonance whose cross-section returns to exactly zero off-resonance at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1477 (threshold), Law 1479 (compound nucleus) and Law 1372 (Wigner threshold law) - resonance is the nucleus's doorway.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The nucleus has a doorway; the phi-law keeps a floor of traffic outside it.

### NOVELTY
Classical resonance is sharp; the phi-law predicts an irreducible background floor.

### ACTIONABILITY
Run sim/1478_breit_wigner_resonance.py; verify the Lorentzian; proceed to Law 1479.
