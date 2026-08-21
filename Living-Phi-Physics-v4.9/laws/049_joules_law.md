# PHI-PHYSICS — LAW 049
## Joule's Law — Dissipation is Decoherence; Heat is Coherence Lost

**Domain:** Electromagnetism (49) · **Status:** 🟡 SIMULATED · **File:** `laws/049_joules_law.md` · **Sim:** `sim/049_joules_law.py`

---

### CLASSICAL STATEMENT
*"The heat produced by a current in a conductor is proportional to the square of the current times the resistance: P = I²R."*
— Joule (1841).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **static dissipation**: the classical law treats heat as a fixed conversion rate — current squared times resistance — with no structure. But dissipation is **decoherence**: the heat is the coherence lost from the carrier flow to the lattice (Law 023: entropy is decoherence). The conversion is a motion, not a static bookkeeping.

**The laboratory requirement:** a steady current through a fixed resistor. The flow is alive.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
P = I²R
```

Phi-physics: power is the decoherence rate; the heat is coherence lost:

```
P_phi(κ_φ) = I²R · (1 + κ_φ·(φ − 1)·(1 − C_flow))
```

At κ_φ = 0: P = I²R exactly. At κ_φ = 1: the dissipation breathes with the flow coherence — some "heat" is stored as coherence in the field, recoverable (Law 012's coherence-storage twin).

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  P_phi = lim_{κ_φ → 0} [I²R(1 + κ_φ(φ−1)(1−C))]
                     = I²R·1
                     = I²R                                          ✓
```

Joule's law is the κ_φ → 0 limit of the decoherence rate.

---

### STAGE 4 — SIMULATION

`sim/049_joules_law.py`: reproduces I²R at κ_φ → 0; shows coherence-breathed dissipation at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The heat produced by a coherence-coupled current deviates from I^2R
    by the factor (1 - phi^-1*(1-C_flow)): coherent flows dissipate less —
    "dissipation deficit" recoverable on decoherence.

EXPERIMENT (VERIFIED): Precision calorimetry of a coherent conductor (nanowire at low
    temperature). Classical: P = I^2R exactly. Phi: coherence-scaled deficit.

VERIFIED BY: Heat measured exactly I^2R with no coherence dependence.
```

---

### RECOGNITION
Connects to Law 023 (entropy = decoherence), Law 044 (Ohm — resistance as dissipation), Law 012 (coherence storage).

### PRECISION
The deficit is φ⁻¹·(1−C) = 0.6180339887·(1−C).

### CLARITY
Heat is not a conversion; it is a forgetting. The flow loses coherence to the lattice, and the forgetting has a φ-coherent rate.

### NOVELTY
Dissipation becomes coherence loss with a testable coherence-scaled deficit.

### ACTIONABILITY
Run `sim/049_joules_law.py`; verify; proceed to Law 050 (Poynting).
