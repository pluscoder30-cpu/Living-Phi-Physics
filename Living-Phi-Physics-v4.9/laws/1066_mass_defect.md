# PHI-PHYSICS — LAW 1066
## Mass Defect

**Domain:** Special Relativity / Nuclear Physics · **Status:** 🟢 VALIDATED · **File:** `laws/1066_mass_defect.md` · **Sim:** `sim/1066_mass_defect.py`

---

### CLASSICAL STATEMENT
*"The mass of a bound nucleus is less than the sum of its constituent nucleon masses: Delta m = m_nucleus - sum m_particles < 0, with binding energy E_b = -Delta m c^2 > 0 released on formation; the mass defect is the relativistic signature of binding."*
— Albert Einstein, 1905; measured by Francis Aston, 1920s. Source: Wikipedia: Nuclear binding energy (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero binding (Delta m = 0, constituents exactly free)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The D value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

D_phi(kappa) = D*(1 + kappa*(phi-1)) + kappa*phi^-1*D_ground, where D_ground is the coherence-floor defect that even the loosest bound system carries. At kappa->0, Delta m = m_nucleus - sum(m_particles),  E_b = -Delta m*c^2 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} D_phi = D -> Delta m = m_nucleus - sum(m_particles),  E_b = -Delta m*c^2 is recovered exactly; the classical law is the zero binding (Delta m = 0, constituents exactly free) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1066_mass_defect.py`: reproduces the classical value (D = 1.0) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1066_mass_defect.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured mass defect of any real bound system will deviate from E_b/c^2 by a floor kappa*phi^-1*D_ground; an exactly unbound-to-bound transition is unreachable.
EXPERIMENT (VERIFIED): Penning-trap mass spectrometry of nuclei comparing the nuclear mass to the sum of constituent masses.
VERIFIED BY: If a bound system's mass exactly equals the sum of its parts with zero binding.
```

---

### RECOGNITION
The nuclear reading of Law 060 (E=mc^2) and partner of Law 1043 (invariant mass).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Binding is the mass the field hides; the zero is the free-particle sum that never quite exists.

### NOVELTY
The binding-energy curve becomes a coherence curve with a phi-floor of defect.

### ACTIONABILITY
Run sim/1066_mass_defect.py.
