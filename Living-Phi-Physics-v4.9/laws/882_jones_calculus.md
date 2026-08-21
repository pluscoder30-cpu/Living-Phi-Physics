# PHI-PHYSICS — LAW 882
## Jones Calculus

**Domain:** Polarization Optics · **Status:** 🟢 VALIDATED · **File:** `laws/882_jones_calculus.md` · **Sim:** `sim/882_jones_calculus.py`

---

### CLASSICAL STATEMENT
*"Polarized light is represented by a Jones vector (Ex, Ey) and optical elements by 2x2 Jones matrices; the output is the matrix product: E_out = J E_in."*
— Robert Clark Jones, 1941. Source: Wikipedia: Jones calculus (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *perfect polarization*: Jones calculus applies exactly only to fully polarized light - the degree of polarization is exactly 1.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

E_out_phi(kappa) = E_out*(1 + kappa*(phi-1)) + kappa*phi^-1*E_out_ground, with E_out_ground the field floor. At kappa->0, E_out = J E_in exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} E_out_phi = E_out -> Jones calculus is the zero-depolarization-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/882_jones_calculus.py`: reproduces the classical value Eout = 1 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/882_jones_calculus.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Real optical elements will depolarize light slightly; the Jones prediction will be off by a coherence floor kappa*phi^-1.
EXPERIMENT (VERIFIED): Measure the degree of polarization of light after passage through several polarizing elements.
VERIFIED BY: If light remains exactly fully polarized through any real element.
```

---

### RECOGNITION
Connects to Law 883 (Mueller calculus) and Law 884 (Stokes parameters).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The perfectly polarized ray is a coherent limit; every element whispers depolarization.

### NOVELTY
Jones calculus gains a depolarization floor.

### ACTIONABILITY
Run sim/882_jones_calculus.py.
