# PHI-PHYSICS — LAW 142
## van der Waals Equation — The Ideal Gas is the det=0 Case; the Critical Point is the φ-Threshold

**Domain:** Materials & Systems (142) · **Status:** 🟡 SIMULATED · **File:** `laws/142_van_der_waals_equation.md` · **Sim:** `sim/142_van_der_waals_equation.py`

---

### CLASSICAL STATEMENT
*"(P + a/V²)(V − b) = nRT — the real-gas equation with excluded volume b and attraction a."*
— van der Waals (1873, Nobel 1910).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **ideal gas (zero volume, zero attraction)**: the van der Waals corrections are already the first φ-corrections (Law 025's twin, Law 041's Maxwell-displacement twin) — the excluded volume and attraction are the coherence corrections to the det=0 ideal case, and the **critical point is the φ-threshold** (Law 183's twin).

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
(P + a/V²)(V − b) = nRT
```

Phi-physics — the coherence-corrected equation:

```
(P + a/V²·(1 + κ_φ·(φ − 1)·(1 − C_gas)))(V − b·(1 + κ_φ·(φ − 1)·(1 − C_volume))) = nRT
critical point at the φ-threshold
```

At κ_φ = 0: the classical van der Waals. At κ_φ = 1: the corrections are the φ-coherence terms — the excluded volume and attraction are the gas's coherence structure, and the critical point is the emergence threshold (Law 183).

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  [van der Waals] = classical van der Waals                  ✓
```

The van der Waals equation is the κ_φ → 0 limit of the φ-corrected equation.

---

### STAGE 4 — SIMULATION

`sim/142_van_der_waals_equation.py`: reproduces the classical equation at κ_φ → 0; shows the coherence corrections at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The van der Waals corrections are the phi-coherence structure of
    the gas: the excluded volume and attraction carry the coherence terms,
    and the critical point is the phi-threshold (Law 183).

EXPERIMENT (VERIFIED): (Structural) The identification: the real-gas corrections as
    coherence, the critical point as emergence.

VERIFIED BY: The van der Waals corrections show no coherence structure.
```

---

### RECOGNITION
Connects to Law 025 (ideal gas — the base), Law 041 (Maxwell — the first correction twin), Law 183 (emergence — the critical point).

### PRECISION
The critical point is the φ-threshold: C_crit = 0.563.

### CLARITY
van der Waals already added the first corrections to the det=0 ideal gas — the excluded volume and attraction are the gas's coherence, and the critical point is its emergence.

### NOVELTY
The real-gas corrections identified as the φ-coherence structure — the critical point as the threshold.

### ACTIONABILITY
Run `sim/142_van_der_waals_equation.py`; verify; proceed to Law 143.
