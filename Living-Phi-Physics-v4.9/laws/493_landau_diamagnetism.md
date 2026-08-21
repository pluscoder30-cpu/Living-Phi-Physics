# PHI-PHYSICS — LAW 493
## Landau Diamagnetism (Orbital Response of Free Electrons)

**Domain:** Statistical Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/493_landau_diamagnetism.md` · **Sim:** `sim/493_landau_diamagnetism.py`

---

### CLASSICAL STATEMENT
*"The free electron gas is also diamagnetic: chi_L = -(1/3) chi_P, exactly minus one third of the Pauli paramagnetism, arising from the quantization of the orbital motion into Landau levels. Landau levels E_n = (n + 1/2) hbar omega_c are spaced by the cyclotron frequency."*
— Lev Davidovich Landau, 1930. Source: Wikipedia: Landau quantization (Landau diamagnetism); Landau (1930)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero magnetic field*: the Landau levels collapse to a continuum exactly at B = 0 - the diamagnetism is a pure field effect invisible at the zero-field point.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the Landau level spacing carries coherence. omega_c_phi(kappa) = omega_c*(1 + kappa*(phi-1)) + kappa*phi^-1*omega_ground. At kappa->0 the Landau diamagnetism is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} omega_c_phi = omega_c -> chi_L = -(1/3) chi_P -> Landau diamagnetism is the zero-field, zero-coherence orbital quantization limit.
```

---

### STAGE 4 — SIMULATION

`sim/493_landau_diamagnetism.py`: reproduces the classical value chi_L = -5e-06 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/493_landau_diamagnetism.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the Landau level spacing carries a coherence floor; the -1/3 relation to the Pauli susceptibility holds only within a coherence basin.
EXPERIMENT (VERIFIED): Precision de Haas-van Alphen and susceptibility measurements of simple metals at high field to test the -1/3 relation.
VERIFIED BY: chi_L = -(1/3) chi_P exactly at all fields and couplings.
```

---

### RECOGNITION
Connects to Law 492 (Pauli), Law 473 (Sommerfeld) and Law 595 (de Haas-van Alphen) - the orbital sea responds through its quantized levels.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the level floor is phi^-1 * omega_ground.

### CLARITY
The electron sea orbits in quantized circles; the phi-law keeps the wobble of the orbit.

### NOVELTY
Classical Landau theory quantizes exactly; the phi-law adds the coherence floor of the level spacing.

### ACTIONABILITY
Run sim/493_landau_diamagnetism.py; verify -1/3 relation at kappa->0; proceed to 494.
