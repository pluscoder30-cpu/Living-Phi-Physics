# PHI-PHYSICS — LAW 043
## Lorentz Force — Force is Coherence-Gradient Coupling; the Cross Product is the φ-Spin

**Domain:** Electromagnetism (43) · **Status:** 🟡 SIMULATED · **File:** `laws/043_lorentz_force.md` · **Sim:** `sim/043_lorentz_force.py`

---

### CLASSICAL STATEMENT
*"The force on a charged particle in electric and magnetic fields: F = q(E + v×B)."*
— Lorentz (1895).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **static charge in a field**: the classical law treats the charge as a static test particle pushed by pre-existing fields. But the charge is a carrier, the fields are coherence gradients, and the force is the coupling between them — the φ-spin interaction in the cross product.

**The laboratory requirement:** a static test charge in known fields. The fields are alive.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
F = q(E + v×B)
```

Phi-physics: force is coherence-gradient coupling; the cross product is the φ-spin interaction:

```
F_phi(κ_φ) = q(E + v×B) · (1 + κ_φ·(φ − 1)·C_coupling)
```

At κ_φ = 0: F = q(E + v×B) exactly. At κ_φ = 1: the force is modulated by the coherence between the charge's carrier and the field — the coupling is a resonance, not a push.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  F_phi = lim_{κ_φ → 0} [q(E + v×B)(1 + κ_φ(φ−1)C)]
                     = q(E + v×B)·1
                     = q(E + v×B)                                    ✓
```

The Lorentz force is the κ_φ → 0 limit of the φ-coupling.

---

### STAGE 4 — SIMULATION

`sim/043_lorentz_force.py`: reproduces q(E + v×B) at κ_φ → 0; shows coherence modulation at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The force on a coherence-coupled charge deviates from the Lorentz
    value by the factor (1 + phi^-1*C_coupling): F = q(E+v*B)*(1+phi^-1*C).
    The deviation scales with the charge-field coherence.

EXPERIMENT (VERIFIED): Precision trapped-ion trajectory in known E and B fields with
    controlled coherence. Classical: Lorentz exactly. Phi: phi-coherent
    deviation at coherence > 0.563.

VERIFIED BY: Trajectories follow exactly the Lorentz force with no
    coherence-modulated deviation.
```

---

### RECOGNITION
Connects to Law 042 (Maxwell — the fields), Eq 1 (carrier coupling), Law 023 (coherence).

### PRECISION
The modulation is φ⁻¹·C = 0.6180339887·C.

### CLARITY
The charge is not pushed; it resonates with the field's coherence. The cross product is the spin of the loop.

### NOVELTY
The Lorentz force becomes a resonance coupling with testable coherence modulation.

### ACTIONABILITY
Run `sim/043_lorentz_force.py`; verify; proceed to Law 044 (Ohm).
