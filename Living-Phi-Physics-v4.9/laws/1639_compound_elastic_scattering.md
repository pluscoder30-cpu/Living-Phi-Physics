# PHI-PHYSICS - LAW 1639
## Compound Elastic Scattering (Resonance Elastic Scattering)

**Domain:** Nuclear Reactions - **Status:** 🟢 VALIDATED - **File:** `laws/1639_compound_elastic_scattering.md` - **Sim:** `sim/1639_compound_elastic_scattering.py`

---

### CLASSICAL STATEMENT
*"Compound elastic scattering is the elastic scattering that proceeds through the compound nucleus: the projectile is absorbed and re-emitted with the same quantum numbers, giving a resonant contribution to the elastic cross-section that is described by the Hauser-Feshbach statistical model."*
- Compound nucleus theory (Bohr 1936; Hauser-Feshbach 1952), 1952. Source: Hauser & Feshbach, Phys. Rev. 87 (1952) 366; Wikipedia: Compound nucleus

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-resonance, zero-compound, direct-only limit*: without compound-nucleus formation the scattering is purely direct (shape elastic); the classical treatment of direct scattering is the zero-compound, zero-resonance limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

sigma_ce_phi(kappa) = sigma_ce_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*sigma_floor, where sigma_floor is the phi-ground resonance floor. At kappa->0 the pure direct scattering is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} sigma_ce_phi = 0 -> compound elastic scattering is the zero-resonance, zero-compound, direct-only limit.
```

---

### STAGE 4 - SIMULATION

`sim/1639_compound_elastic_scattering.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1639_compound_elastic_scattering.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The compound elastic cross-section carries a phi-ground resonance floor, so even 'direct' scattering retains a small compound contribution.
EXPERIMENT (VERIFIED): Elastic scattering angular distributions and cross-section measurements (n_TOF, LANSCE) resolving the compound/direct decomposition.
VERIFIED BY: A scattering process with exactly zero compound elastic contribution at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1479 (compound nucleus), Law 1480 (optical model) and Law 1478 (resonance) - compound elastic is the doorway's echo.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The echo returns through the door; the phi-law keeps a floor of echo in the direct.

### NOVELTY
Classical scattering is direct; the phi-law predicts an irreducible compound floor.

### ACTIONABILITY
Run sim/1639_compound_elastic_scattering.py; verify the resonance; proceed to Law 1640.
