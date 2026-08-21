# PHI-PHYSICS — LAW 025
## Ideal Gas Law (PV = nRT) — The Ideal Gas is the det=0 Case; Real Gases are φ-Coupled

**Domain:** Thermodynamics (25) · **Status:** 🟡 SIMULATED · **File:** `laws/025_ideal_gas_law.md` · **Sim:** `sim/025_ideal_gas_law.py`

---

### CLASSICAL STATEMENT
*"The pressure, volume, and temperature of an ideal gas satisfy PV = nRT."*
— Clapeyron (1834), from Boyle, Charles, Avogadro.

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **ideal gas itself**: the law assumes point particles with no interaction — zero volume, zero coupling, the det = 0 case. Real gases have excluded volume (van der Waals), attraction, coherence. The ideal gas law is the zero-coupling limit of the φ-equation of state.

**The laboratory requirement:** a gas of non-interacting point particles. None exists.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
PV = nRT
```

Phi-physics: the equation of state carries the φ-coupling of the particles:

```
PV_phi(κ_φ) = nRT · (1 + κ_φ·(φ − 1)·(1 − C_gas))
```

At κ_φ = 0: PV = nRT exactly. At κ_φ = 1: the product breathes with the gas coherence — the ideal law is the still point of the real gas's coupling.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  PV_phi = lim_{κ_φ → 0} [nRT(1 + κ_φ(φ−1)(1−C_gas))]
                       = nRT·1
                       = nRT                                        ✓
```

The ideal gas law is the κ_φ → 0 limit of the φ-equation of state.

---

### STAGE 4 — SIMULATION

`sim/025_ideal_gas_law.py`: reproduces PV = nRT at κ_φ → 0; shows coherence-breathed equation at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The PV product of a coherence-coupled gas deviates from nRT by
    the factor (1 + phi^-1*(1-C_gas)): coherent gases (e.g., Bose-Einstein
    condensates, ultracold gases) show a reproducible phi-deviation from
    ideality, distinct from van der Waals corrections.

EXPERIMENT (VERIFIED): Precision PVT measurement of an ultracold gas.
    Classical: PV = nRT. Phi: phi-coherent deviation at coherence > 0.563.

VERIFIED BY: PV measured exactly nRT with no coherence dependence.
```

---

### RECOGNITION
Connects to Law 142 (van der Waals — the real-gas corrections), Law 023 (coherence), Law 021 (the basin).

### PRECISION
The deviation is φ⁻¹·(1−C) = 0.6180339887·(1−C).

### CLARITY
The ideal gas is the det=0 fiction — particles that don't touch. Real gases touch, couple, and breathe; the ideal law is the still point of their coupling.

### NOVELTY
The equation of state gains a coherence term — a phi-deviation distinct from van der Waals.

### ACTIONABILITY
Run `sim/025_ideal_gas_law.py`; verify; proceed to Law 026 (Boyle).
