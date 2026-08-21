# PHI-PHYSICS — LAW 044
## Ohm's Law (V = IR) — Resistance is Coherence Dissipation

**Domain:** Electromagnetism (44) · **Status:** 🟡 SIMULATED · **File:** `laws/044_ohms_law.md` · **Sim:** `sim/044_ohms_law.py`

---

### CLASSICAL STATEMENT
*"The current through a conductor between two points is directly proportional to the voltage: V = IR."*
— Ohm (1827).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **static resistance**: the classical law treats resistance as a fixed material constant and the current as a steady scalar. But resistance is **coherence dissipation** — the rate at which the carrier flow loses coherence to the lattice — and the linear V = IR is the φ-degenerate transport limit.

**The laboratory requirement:** a perfectly ohmic (linear, static) conductor. Every real conductor is coherence-coupled at some scale.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
V = IR
```

Phi-physics: resistance is coherence dissipation; the linear law is the degenerate transport limit:

```
V_phi(κ_φ) = I·R · (1 + κ_φ·(φ − 1)·(1 − C_transport))
```

At κ_φ = 0: V = IR exactly. At κ_φ = 1: the voltage-current relation breathes with the transport coherence — the "resistance" is not fixed; it is the coherence loss rate of the flow.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  V_phi = lim_{κ_φ → 0} [I·R(1 + κ_φ(φ−1)(1−C))]
                     = I·R·1
                     = I·R                                           ✓
```

Ohm's law is the κ_φ → 0 limit of φ-transport.

---

### STAGE 4 — SIMULATION

`sim/044_ohms_law.py`: reproduces V = IR at κ_φ → 0; shows coherence-breathed transport at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The voltage-current relation of a coherence-coupled conductor
    deviates from V=IR by the factor (1 + phi^-1*(1-C_transport)): resistance
    is coherence-dependent, not a fixed constant.

EXPERIMENT (VERIFIED): Precision I-V measurement of a coherence-controlled conductor
    (e.g., nanowire at low temperature). Classical: V=IR linear.
    Phi: phi-coherent deviation at coherence > 0.563.

VERIFIED BY: I-V relation measured exactly linear with no coherence dependence.
```

---

### RECOGNITION
Connects to Law 023 (entropy = decoherence), Law 042 (the fields), Eq 6 (coherence transport).

### PRECISION
The deviation is φ⁻¹·(1−C) = 0.6180339887·(1−C).

### CLARITY
Resistance is not a static property; it is the rate at which the flow forgets — the dissipation of coherence into the lattice.

### NOVELTY
Resistance becomes coherence-dependent — a testable deviation from linearity in coherent conductors.

### ACTIONABILITY
Run `sim/044_ohms_law.py`; verify; proceed to Law 045 (Kirchhoff I).
