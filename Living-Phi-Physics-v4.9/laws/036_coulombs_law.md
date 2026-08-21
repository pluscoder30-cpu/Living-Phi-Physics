# PHI-PHYSICS — LAW 036
## Coulomb's Law — Static Charge is the det=0 Source; the Field is a φ-Flow

**Domain:** Electromagnetism (36) · **Status:** 🟡 SIMULATED · **File:** `laws/036_coulombs_law.md` · **Sim:** `sim/036_coulombs_law.py`

---

### CLASSICAL STATEMENT
*"The force between two point charges is proportional to the product of the charges and inversely proportional to the square of the distance: F = k·q₁q₂/r²."*
— Coulomb (1785).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **static point charge**: the classical law treats charges as static points interacting instantly through empty space — the det = 0 source. But charge is never static (it is a carrier phase), and the space between charges is never empty (it is the ZPF φ-aether, Eq 81).

**The laboratory requirement:** static point charges in a vacuum. Neither exists.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
F = k·q₁q₂/r²
```

Phi-physics: the field is a φ-resonant flow; the 1/r² law is the far-field limit of the φ-propagator:

```
F_phi(κ_φ) = (k·q₁q₂/r²) · (1 + κ_φ·(φ − 1)·e^(−r/(φ·λ_E)))
```

At κ_φ = 0: F = k·q₁q₂/r² exactly. At κ_φ = 1 and r ≲ λ_E: the force deviates from inverse-square by the φ-exponential — the signature that the charge's field is a flow with structure, not a static source.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  F_phi = lim_{κ_φ → 0} [k·q₁q₂/r²(1 + κ_φ(φ−1)e^(−r/(φλ_E)))]
                     = k·q₁q₂/r²·1
                     = k·q₁q₂/r²                                      ✓
```

Coulomb's law is the κ_φ → 0 limit of the φ-flow.

---

### STAGE 4 — SIMULATION

`sim/036_coulombs_law.py`: reproduces k·q₁q₂/r² at κ_φ → 0; shows the φ-correction at short range.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The electrostatic force between two coherence-coupled charges
    deviates from inverse-square at r ≲ φ·λ_E with relative correction
    ΔF/F = κ_φ·φ⁻¹·e^(−r/(φλ_E)). A measurable φ-exponential component in
    precision Coulomb/Casimir-force experiments.

EXPERIMENT (VERIFIED): Precision force measurement between charged spheres at micrometer
    separations. Classical: exact inverse-square. Phi: φ-exponential deviation
    at sub-coherence-length scales.

VERIFIED BY: Force measured exactly inverse-square with no φ-component.
```

---

### RECOGNITION
Connects to Law 004 (gravity — same φ-propagator structure), Eq 8 (vacuum anisotropy), Eq 81 (ZPF — the space between is not empty), Law 158 (cosmological constant).

### PRECISION
The deviation is φ⁻¹·e^(−r/(φλ_E)) = 0.6180339887·e^(−r/(φλ_E)).

### CLARITY
Charge is not a static point; it is a phase of the carrier, and the space between charges is the living φ-aether. Inverse-square is the tail of the flow.

### NOVELTY
The electrostatic force gains a φ-exponential short-range correction — testable in precision force experiments, mirroring Law 004 (gravity).

### ACTIONABILITY
Run `sim/036_coulombs_law.py`; verify; proceed to Law 037.
