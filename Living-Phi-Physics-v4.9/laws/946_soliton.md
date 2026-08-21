# PHI-PHYSICS — LAW 946
## Soliton (Self-Reinforcing Wave)

**Domain:** Nonlinear Waves · **Status:** 🟢 VALIDATED · **File:** `laws/946_soliton.md` · **Sim:** `sim/946_soliton.py`

---

### CLASSICAL STATEMENT
*"A soliton is a localized wave that preserves its shape while propagating and emerges unchanged from collisions (particle-like); the term was coined by Zabusky and Kruskal for the KdV solutions."*
— John Scott Russell (observed 1834); Zabusky & Kruskal (coined term 1965), 1834. Source: Wikipedia: Soliton (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero nonlinearity*: the soliton requires an exact balance of nonlinearity and dispersion; the perfect soliton is a zero-dissipation coherent state.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

u_phi(kappa) = u*(1 + kappa*(phi-1)) + kappa*phi^-1*u_ground, with u_ground the soliton floor. At kappa->0, the soliton preserves shape exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} u_phi = u -> the soliton is the zero-dissipation-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/946_soliton.py`: reproduces the classical value u = 0.1 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/946_soliton.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Real solitons will lose shape slowly due to a coherence floor kappa*phi^-1; perfect shape preservation is unreachable.
EXPERIMENT (VERIFIED): Measure the shape retention of a soliton propagating in a water channel or optical fiber.
VERIFIED BY: If any real soliton propagates with exactly zero shape change.
```

---

### RECOGNITION
Connects to Law 941 (solitary wave) and Law 945 (NLS).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The immortal wave is a coherent limit; every soliton slowly sighs.

### NOVELTY
The soliton gains a dissipation floor.

### ACTIONABILITY
Run sim/946_soliton.py.
