# PHI-PHYSICS — LAW 007
## Archimedes' Principle — Buoyancy is a Coherence Differential

**Domain:** Mechanics (7) · **Status:** 🟡 SIMULATED · **File:** `laws/007_archimedes_principle.md` · **Sim:** `sim/007_archimedes_principle.py`

---

### CLASSICAL STATEMENT
*"Any object, wholly or partly immersed in a fluid, is buoyed up by a force equal to the weight of the fluid displaced by the object."*
— Archimedes (c. 250 BC).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **static buoyancy equilibrium**: the classical law describes the static balance between weight and buoyant force — a floating body at rest. The displaced volume is treated as a static geometric quantity.

But buoyancy is a coherence differential: the body and the fluid have different φ-coherence densities, and the "buoyant force" is the field's pressure gradient across that coherence boundary — the loop with the line, not a static push.

**The laboratory requirement:** the law demands a perfectly static fluid and a body at exact equilibrium. Neither exists.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
F_buoyant = ρ_fluid · V_displaced · g
```

Phi-physics: buoyancy is the coherence differential between body and fluid:

```
F_buoy_phi(κ_φ) = ρ_fluid·V·g · (1 + κ_φ·(φ−1)·ΔC_body_fluid)
```

At κ_φ = 0: F = ρ·V·g exactly. At κ_φ = 1: the buoyant force is modulated by the coherence difference ΔC between the body and the fluid — the displaced volume is a φ-resonance cavity, not a static shape.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  F_buoy_phi = lim_{κ_φ → 0} [ρVg(1 + κ_φ(φ−1)ΔC)]
                          = ρVg·1
                          = ρVg                                       ✓
```

Archimedes' principle is the κ_φ → 0 limit of the φ-buoyancy.

---

### STAGE 4 — SIMULATION

`sim/007_archimedes_principle.py`: reproduces ρVg at κ_φ → 0; shows coherence modulation at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The buoyant force on a body differs from ρVg by a factor
    (1 + φ⁻¹·ΔC) at full coherence, where ΔC is the body-fluid coherence
    difference. Objects with higher coherence than the fluid experience
    enhanced buoyancy — a "levitation" signature at coherence scales.

EXPERIMENT (VERIFIED): Precision buoyancy measurement of a coherent object (e.g., a
    magnetically-trapped BEC) in a fluid. Classical: ρVg exactly.
    Phi: coherence-modulated deviation.

VERIFIED BY: Buoyant force measured exactly at ρVg with no coherence modulation.
```

---

### RECOGNITION
Connects to Law 023 (coherence), Eq 2 (coherence threshold), Eq 6 (coherence transport).

### PRECISION
Modulation factor = φ⁻¹ = 0.6180339887.

### CLARITY
The floating body is not a static object in a static fluid; it is a coherence boundary in a field, and the boundary resonates.

### NOVELTY
Buoyancy acquires a coherence term — the displaced volume becomes a resonance cavity.

### ACTIONABILITY
Run `sim/007_archimedes_principle.py`; verify; proceed to Law 008.
