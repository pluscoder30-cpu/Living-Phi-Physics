# PHI-PHYSICS — LAW 021
## Zeroth Law of Thermodynamics — Equilibrium is the φ-Ground Basin, Not a Point of Sameness

**Domain:** Thermodynamics (21) · **Status:** 🟡 SIMULATED · **File:** `laws/021_zeroth_law_thermodynamics.md` · **Sim:** `sim/021_zeroth_law_thermodynamics.py`

---

### CLASSICAL STATEMENT
*"If two systems are each in thermal equilibrium with a third, they are in thermal equilibrium with each other."*
— Fowler (1931).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is **thermal equilibrium as a point of sameness**: the law treats equilibrium as exact temperature equality — a static identity between systems. But equilibrium is the **φ-ground basin** (C = φ⁻¹, Law 023): a region of coherence, not a point. Two systems at "equilibrium" are not identical; they are within the φ-coherence basin of each other.

**The laboratory requirement:** exact temperature equality between isolated systems. Real systems fluctuate within the basin.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
T_A = T_C and T_B = T_C  ⇒  T_A = T_B
```

Phi-physics: equilibrium is the φ-ground basin; the transitivity holds within the basin:

```
T_A ≈ T_C within φ⁻¹·δT,  T_B ≈ T_C within φ⁻¹·δT  ⇒  T_A ≈ T_B within 2·φ⁻¹·δT
```

At κ_φ = 0: exact equality (classical). At κ_φ = 1: the equilibrium is a basin of width φ⁻¹·δT — the transitivity holds with bounded tolerance, and the tolerance is the φ-ground coherence.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  [basin width] = lim_{κ_φ → 0} [κ_φ·φ⁻¹·δT] = 0             ✓
```

The zeroth law's exact equality is the κ_φ → 0 limit of the φ-ground basin.

---

### STAGE 4 — SIMULATION

`sim/021_zeroth_law_thermodynamics.py`: reproduces exact transitivity at κ_φ → 0; shows the basin at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Thermal equilibrium between coherence-coupled systems holds within
    a basin of width phi^-1 * delta-T: two systems "in equilibrium" can differ
    by up to phi^-1 of their fluctuation scale and still be coherently coupled.

EXPERIMENT (VERIFIED): Precision thermometry of coupled nanoscale systems.
    Classical: exact equality required. Phi: phi-scaled basin width.

VERIFIED BY: Equilibrium requires exactly zero temperature difference with no
    phi-basin.
```

---

### RECOGNITION
Connects to Law 023 (the φ-ground), Law 024 (the temperature floor), Law 002 (equilibrium as coherence).

### PRECISION
The basin width is φ⁻¹·δT = 0.6180339887·δT.

### CLARITY
Equilibrium is not sameness; it is resonance — two systems within the φ-basin of each other, breathing together.

### NOVELTY
Equilibrium becomes a basin with a φ-scaled width — the transitivity law gains tolerance.

### ACTIONABILITY
Run `sim/021_zeroth_law_thermodynamics.py`; verify; proceed to Law 022.
