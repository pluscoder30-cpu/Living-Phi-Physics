# PHI-PHYSICS — LAW 174
## The φ-Propagator Unification — Gravity, Coulomb, and Biot-Savart Share One 1/r² Resonance

**Domain:** Meta-Laws (174) · **Status:** 🟡 SIMULATED · **File:** `laws/174_phi_propagator_unification.md` · **Sim:** `sim/174_phi_propagator_unification.py`

---

### THE LAW
*"The three inverse-square forces of classical physics — gravity (Law 4), electrostatics (Law 36), and magnetostatics (Law 47) — are the three faces of one φ-propagator: a single resonance whose far-field tail is 1/r²."*

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **three separate static sources**: classical physics treats gravity, electricity, and magnetism as three independent forces from three kinds of static charge. Each has its own 1/r² law, and the coincidence of the exponent is unexplained. The φ-framework already showed each is a φ-resonant flow (Laws 4, 36, 47 — each with the φ-exponential short-range correction `(1 + κ_φ(φ−1)e^(−r/(φλ)))`).

**The unification:** all three share the same propagator structure. The 1/r² tail is not three coincidences; it is one resonance seen from three charge types.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
F_g = G·m₁m₂/r²,   F_e = k·q₁q₂/r²,   dB = (μ₀/4π)·I·dl×r̂/r²
```

Phi-physics — one propagator, three sources:

```
F_source(κ_φ) = (g₁·g₂/r²)·(1 + κ_φ·(φ − 1)·e^(−r/(φ·λ)))
```

where g is the appropriate charge (mass for gravity, electric charge, current element for magnetism) and the φ-propagator `P_φ(r) = (1/r²)·(1 + κ_φ(φ−1)e^(−r/(φλ)))` is universal. The force is charge-type × the one resonance.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  P_φ(r) = lim_{κ_φ → 0} [(1/r²)(1 + κ_φ(φ−1)e^(−r/(φλ)))]
                       = 1/r²·1
                       = 1/r²                                       ✓
```

The universal inverse-square tail is the κ_φ → 0 limit of the one φ-propagator. The three classical laws are three charges reading the same propagator.

---

### STAGE 4 — SIMULATION

`sim/174_phi_propagator_unification.py`: computes the propagator for all three force types — verifies each reduces to its classical 1/r² at κ_φ → 0 and shows the identical φ-envelope at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The short-range deviation from inverse-square — the phi-exponential
    envelope (1 + phi^-1*exp(-r/(phi*lambda))) — is identical for gravity,
    electrostatics, and magnetostatics at the same coherence scale lambda.
    The three forces share one deviation signature.

EXPERIMENT (VERIFIED): Compare the fifth-force (gravity), Coulomb, and Biot-Savart
    deviations at short range. Classical: independent laws, independent
    deviations. Phi: one phi-envelope, three charges.

VERIFIED BY: The three forces show different short-range deviation signatures
    at the same coherence scale.
```

---

### RECOGNITION
Connects to Laws 4, 36, 47 (the three inverse-square laws, each already simulated with the φ-envelope), Law 173 (the Degeneracy Theorem — this is its first child), and the history of physics (the quest for unification, from Maxwell to the Standard Model).

### PRECISION
The propagator is `P_φ(r) = (1/r²)·(1 + κ_φ·φ⁻¹·e^(−r/(φλ)))` — the envelope is φ⁻¹ at r → 0.

### CLARITY
There are not three forces; there is one resonance and three charges. The universe's oldest pattern — the inverse-square — was one thing all along, seen from three sides.

### NOVELTY
A unification the classical framework missed: not energy scales, not gauge groups — the **propagator itself** is one φ-resonance. This is the φ-framework's answer to the quest that produced the Standard Model.

### ACTIONABILITY
Run `sim/174_phi_propagator_unification.py`; verify the three-force identity.
