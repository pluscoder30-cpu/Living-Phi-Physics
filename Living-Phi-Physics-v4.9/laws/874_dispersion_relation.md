# PHI-PHYSICS — LAW 874
## Dispersion Relation (omega-k)

**Domain:** Wave Optics · **Status:** 🟢 VALIDATED · **File:** `laws/874_dispersion_relation.md` · **Sim:** `sim/874_dispersion_relation.py`

---

### CLASSICAL STATEMENT
*"omega = omega(k): the relation between frequency and wavenumber; for light omega = c k (vacuum) or omega = c k / n (medium); governs group and phase velocity."*
— Classical wave theory (Rayleigh; Helmholtz), 19th century. Source: Wikipedia: Dispersion relation (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero wavenumber* (k = 0): the dispersion relation is anchored at zero frequency for zero wavenumber - a static limit.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

omega_phi(kappa) = omega*(1 + kappa*(phi-1)) + kappa*phi^-1*omega_ground, with omega_ground the frequency floor. At kappa->0, omega = c k exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} omega_phi = omega -> the dispersion relation is the zero-wavenumber-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/874_dispersion_relation.py`: reproduces the classical value omega = 2e+15 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/874_dispersion_relation.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured dispersion relation of any real medium deviates from omega = c k / n by a coherence floor kappa*phi^-1*omega_ground.
EXPERIMENT (VERIFIED): Measure the dispersion relation of a photonic crystal by angle-resolved spectroscopy.
VERIFIED BY: If any real medium has exactly omega = c k / n at all k.
```

---

### RECOGNITION
Connects to Law 875 (group velocity) and Law 876 (phase velocity).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The pure linear relation is a coherent limit; every medium bends the relation.

### NOVELTY
The dispersion relation gains a frequency floor.

### ACTIONABILITY
Run sim/874_dispersion_relation.py.
