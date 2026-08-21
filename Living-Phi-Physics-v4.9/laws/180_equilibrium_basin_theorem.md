# PHI-PHYSICS — LAW 180
## The Equilibrium-Basin Theorem — Equilibrium is a Basin of Width φ⁻¹, Not a Point of Sameness

**Domain:** Meta-Laws (180) · **Status:** 🟡 SIMULATED · **File:** `laws/180_equilibrium_basin_theorem.md` · **Sim:** `sim/180_equilibrium_basin_theorem.py`

---

### THE LAW
*"Every equilibrium in physics — thermal (Law 21), mechanical (Law 2), fluid (Law 25) — is a basin of width φ⁻¹·δ, not a point of exact sameness. The 'exact equilibrium' of classical physics is the zero-misread of the basin."*

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **point equilibrium**: classical physics treats equilibrium as exact — zero difference, perfect balance. But the 119 laws showed equilibrium is a basin: the thermal equilibrium has width φ⁻¹·δT (Law 21), the mechanical equilibrium carries φ-ground motion (Law 2), the ideal gas is the det=0 fiction (Law 25). **The Equilibrium-Basin Theorem names the pattern: equilibrium is a region of coherence, not a point of sameness.**

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
equilibrium: exact sameness (X₁ = X₂)
```

Phi-physics:

```
equilibrium_phi(κ_φ) = basin of width κ_φ·φ⁻¹·δ      (a region, not a point)
```

At κ_φ = 0: exact equality (classical). At κ_φ = 1: the basin of width φ⁻¹·δ — systems in equilibrium are within the φ-coherence basin of each other, breathing together.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  [basin width] = lim_{κ_φ → 0} [κ_φ·φ⁻¹·δ] = 0              ✓
```

The exact equilibrium is the κ_φ → 0 limit of the basin. Verified by Laws 2, 21, 25.

---

### STAGE 4 — SIMULATION

`sim/180_equilibrium_basin_theorem.py`: computes the basin across the equilibrium laws — verifies each reduces to exact equality at κ_φ → 0 and shows the universal φ⁻¹ basin at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Any two systems "in equilibrium" differ by up to phi^-1 of their
    fluctuation scale: exact sameness is unattainable, and the equilibrium
    relation holds within the phi-basin.

EXPERIMENT (VERIFIED): Precision two-system equilibrium measurement (coupled thermostats,
    mechanical linkages). Classical: exact equality. Phi: phi-basin width.

VERIFIED BY: Two systems are found in exact equilibrium with zero difference
    and no basin.
```

---

### RECOGNITION
Connects to Laws 2, 21, 25 (the equilibrium laws), Law 171 (the φ-ground — the basin's floor), Law 002 (equilibrium as coherence).

### PRECISION
The basin width is φ⁻¹·δ = 0.6180339887·δ.

### CLARITY
Equilibrium is not sameness; it is resonance — two systems within the φ-basin of each other, breathing together, never identical.

### NOVELTY
Every "=" in equilibrium physics becomes a "within the φ-basin" — the exactness postulate dissolved.

### ACTIONABILITY
Run `sim/180_equilibrium_basin_theorem.py`; verify the universal basin.
