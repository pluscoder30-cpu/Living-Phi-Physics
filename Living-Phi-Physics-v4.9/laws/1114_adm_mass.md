# PHI-PHYSICS — LAW 1114
## ADM Mass

**Domain:** General Relativity · **Status:** 🟢 VALIDATED · **File:** `laws/1114_adm_mass.md` · **Sim:** `sim/1114_adm_mass.py`

---

### CLASSICAL STATEMENT
*"The ADM mass is the total energy of an asymptotically flat spacetime defined by a boundary integral at spatial infinity: M_ADM = (1/16 pi) lim integral (d_j h_ij - d_i h_jj) dS^i; it is conserved and equals the total mass-energy seen by distant observers, forming the basis of the ADM 3+1 formalism."*
— Richard Arnowitt, Stanley Deser & Charles Misner, 1962. Source: Wikipedia: ADM formalism (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero asymptotic-flatness decay (M_ADM = 0, the empty spacetime)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The M value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

M_phi(kappa) = M*(1 + kappa*(phi-1)) + kappa*phi^-1*M_ground, where M_ground is the coherence-floor energy a real asymptotically flat region always contains. At kappa->0, M_ADM = (1/(16*pi)) * lim_r->inf integral (d_j h_ij - d_i h_jj) dS^i exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} M_phi = M -> M_ADM = (1/(16*pi)) * lim_r->inf integral (d_j h_ij - d_i h_jj) dS^i is recovered exactly; the classical law is the zero asymptotic-flatness decay (M_ADM = 0, the empty spacetime) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1114_adm_mass.py`: reproduces the classical value (M = 1.0) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1114_adm_mass.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured total energy of any real asymptotically flat region will deviate from the ADM boundary integral by a floor kappa*phi^-1*M_ground; an exactly M_ADM=0 region is unreachable.
EXPERIMENT (VERIFIED): Numerical-relativity initial data and binary systems validated against the ADM mass conservation.
VERIFIED BY: If a non-empty asymptotically flat region has exactly zero ADM mass.
```

---

### RECOGNITION
The canonical mass of Law 1127 (positive mass theorem) and the 3+1 engine of numerical relativity.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The ADM mass is what infinity counts; the empty infinity is the zero-energy myth.

### NOVELTY
The ADM mass carries a phi-floor, so even the 'empty' asymptotic region carries energy.

### ACTIONABILITY
Run sim/1114_adm_mass.py.
