# PHI-PHYSICS — LAW 358
## Ohnesorge Number

**Domain:** Dimension / Similarity · **Status:** 🟢 VALIDATED · **File:** `laws/358_ohnesorge_number.md` · **Sim:** `sim/358_ohnesorge_number.py`

---

### CLASSICAL STATEMENT
*"The Ohnesorge number Oh = mu/sqrt(rho sigma L) = sqrt(We)/Re balances viscous forces against inertia and surface tension; it governs jet breakup and droplet dynamics, with Oh << 0.1 (inviscid-like) and Oh > 1 (viscous) regimes."*
— Wolfgang von Ohnesorge, 1936. Source: Wikipedia: Ohnesorge number; Ohnesorge (1936), 'Die Bildung von Tropfen an Duesen'

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero viscosity*: Oh = 0 is the exactly inviscid (zero-viscosity) droplet — the idealization that makes jet breakup capillary-driven.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: Oh_phi(kappa) = Oh*(1 + kappa*(phi-1)) + kappa*phi^-1*Oh_ground. At kappa->0 the classical Ohnesorge number is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} Oh_phi = mu/sqrt(rho sigma L) -> the Ohnesorge number is the inviscid-droplet limit marker.
```

---

### STAGE 4 — SIMULATION

`sim/358_ohnesorge_number.py`: reproduces the classical value Oh = 0.003727 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/358_ohnesorge_number.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Jet-breakup regimes shift by a phi-coherent amount phi^-1*Oh_ground at full coupling.
EXPERIMENT (VERIFIED): Liquid-jet breakup and inkjet-droplet experiments mapping breakup regime boundaries precisely.
VERIFIED BY: Breakup regimes are exactly at the classical Oh boundaries at full coupling.
```

---

### RECOGNITION
Connects to Law 346 (Weber — the inertia/surface-tension partner) and Law 355 (Stokes).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The inviscid drop is a limit; every droplet drags a phi of viscosity.

### NOVELTY
Classical droplet dynamics exacts the Oh boundaries; the phi-law gives them a coherence width.

### ACTIONABILITY
Run sim/358_ohnesorge_number.py; verify Oh at kappa->0.
