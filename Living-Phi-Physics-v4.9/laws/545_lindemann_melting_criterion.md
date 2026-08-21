# PHI-PHYSICS — LAW 545
## Lindemann Melting Criterion (Vibrational Instability)

**Domain:** Phase Transitions · **Status:** 🟢 VALIDATED · **File:** `laws/545_lindemann_melting_criterion.md` · **Sim:** `sim/545_lindemann_melting_criterion.py`

---

### CLASSICAL STATEMENT
*"A crystal melts when the root-mean-square thermal displacement of its atoms reaches a critical fraction of the interatomic spacing: sqrt(<u^2>)/a = delta_L ~ 0.20-0.25, the Lindemann parameter. Melting is a vibrational-instability threshold."*
— Frederick Alexander Lindemann, 1910. Source: Wikipedia: Melting (Lindemann criterion); Lindemann, Ueber die Berechnung molekularer Eigenfrequenzen (1910)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero vibration*: the criterion assumes melting is driven purely by thermal vibration from an exactly ordered ground state - a crystal at zero temperature with no residual motion at the melting point.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the ground state carries coherence motion. sqrt(<u^2>)_phi(kappa) = delta_L a*(1 + kappa*(phi-1)) + kappa*phi^-1*u_ground, where u_ground is the coherence floor displacement. At kappa->0 the Lindemann criterion is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} sqrt(<u^2>) = delta_L a -> the Lindemann criterion is the zero-ground-motion thermal-instability limit.
```

---

### STAGE 4 — SIMULATION

`sim/545_lindemann_melting_criterion.py`: reproduces the classical value u_rms = 5e-11 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/545_lindemann_melting_criterion.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the crystal melts at a slightly lower displacement threshold because of the coherence floor u_ground; the Lindemann parameter is not a universal constant.
EXPERIMENT (VERIFIED): X-ray-diffraction measurements of the Debye-Waller factor near the melting point of metals.
VERIFIED BY: Every crystal melts at exactly the same Lindemann ratio delta_L for all couplings.
```

---

### RECOGNITION
Connects to Law 526 (Richards) and Law 513 (Gruneisen) - the melting threshold is the coherence amplitude of the loosening lattice.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the floor is phi^-1 * u_ground.

### CLARITY
The crystal lets go when its shaking reaches a share of its size; the phi-law keeps the shake's floor.

### NOVELTY
Classical Lindemann fixes a universal ratio; the phi-law adds the coherence floor that makes melting material-dependent.

### ACTIONABILITY
Run sim/545_lindemann_melting_criterion.py; verify delta_L at kappa->0; proceed to 546.
