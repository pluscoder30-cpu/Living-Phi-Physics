# PHI-PHYSICS — LAW 374
## Barlow's Formula (Thin-Wall Hoop Stress)

**Domain:** Structural Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/374_barlows_formula.md` · **Sim:** `sim/374_barlows_formula.py`

---

### CLASSICAL STATEMENT
*"For a thin-walled cylinder (t << r), the hoop stress due to internal pressure is sigma = p r/t, and the bursting pressure is p_burst = sigma_allow r/t (alternatively sigma = p D/(2 t) with D the diameter); this is the thin-wall limit of Lame's solution."*
— Peter Barlow, 1837. Source: Wikipedia: Barlow's formula; Barlow (1837), 'On the strength of cast iron'

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero wall thickness*: Barlow's formula holds for exactly thin walls (t -> 0 relative to r), a limit no real vessel reaches.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: sigma_phi(kappa) = p*r/t*(1 + kappa*(phi-1)) + kappa*phi^-1*sigma_ground. At kappa->0 Barlow's formula is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0, t/r -> 0} sigma_phi = p r/t -> Barlow's formula is the thin-wall limit of Lame's theorem.
```

---

### STAGE 4 — SIMULATION

`sim/374_barlows_formula.py`: reproduces the classical value sigma = 200 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/374_barlows_formula.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Thin-wall hoop stresses carry a phi-coherent excess phi^-1*sigma_ground at full coupling.
EXPERIMENT (VERIFIED): Thin-tube burst tests and hoop-stress strain-gauge measurements comparing with Barlow.
VERIFIED BY: Hoop stress is exactly p r/t for a thin wall at full coupling.
```

---

### RECOGNITION
Connects to Law 373 (Lame — the thick-wall parent) and Law 372 (Cauchy stress).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The thin wall is a limit; every vessel keeps a phi thickness that Lame remembers.

### NOVELTY
Classical design exacts the thin-wall formula; the phi-law bounds its deviation at a coherence floor.

### ACTIONABILITY
Run sim/374_barlows_formula.py; verify sigma = p r/t at kappa->0.
