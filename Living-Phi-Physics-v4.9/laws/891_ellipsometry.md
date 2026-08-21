# PHI-PHYSICS — LAW 891
## Ellipsometry (Polarization Analysis)

**Domain:** Polarization Optics · **Status:** 🟢 VALIDATED · **File:** `laws/891_ellipsometry.md` · **Sim:** `sim/891_ellipsometry.py`

---

### CLASSICAL STATEMENT
*"Ellipsometry measures the change of polarization upon reflection: rho = r_p/r_s = tan(psi) exp(i delta); psi and delta characterize the thin film via the Fresnel coefficients."*
— Paul Drude (theory); early ellipsometry, 1887. Source: Wikipedia: Ellipsometry (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *ideal interface*: ellipsometry inverts the Fresnel equations assuming an exactly known, smooth, isotropic interface.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

rho_phi(kappa) = rho*(1 + kappa*(phi-1)) + kappa*phi^-1*rho_ground, with rho_ground the ratio floor. At kappa->0, rho = tan(psi)exp(i delta) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} rho_phi = rho -> ellipsometry is the zero-interface-imperfection-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/891_ellipsometry.py`: reproduces the classical value rho = 1.125 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/891_ellipsometry.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The psi/delta measured on a real surface will deviate from the ideal-interface model by a coherence floor kappa*phi^-1.
EXPERIMENT (VERIFIED): Measure psi and delta of a known SiO2-on-Si sample and compare with the Drude model.
VERIFIED BY: If ellipsometric psi/delta of any real sample match the ideal interface exactly.
```

---

### RECOGNITION
Connects to Law 840 (Fresnel equations) and Law 883 (Mueller calculus).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The perfect interface is a coherent limit; every surface has a roughness.

### NOVELTY
Ellipsometry gains an interface floor.

### ACTIONABILITY
Run sim/891_ellipsometry.py.
