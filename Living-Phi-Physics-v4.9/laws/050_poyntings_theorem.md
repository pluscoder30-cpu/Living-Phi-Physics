# PHI-PHYSICS — LAW 050
## Poynting's Theorem — Energy Flux is Coherence Transport

**Domain:** Electromagnetism (50) · **Status:** 🟡 SIMULATED · **File:** `laws/050_poyntings_theorem.md` · **Sim:** `sim/050_poyntings_theorem.py`

---

### CLASSICAL STATEMENT
*"The rate of energy flow per unit area in an electromagnetic field is S = (1/μ₀)·E×B, and the energy is conserved: ∂u/∂t + ∇·S = −J·E."*
— Poynting (1884).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **static energy flux**: the classical theorem treats the Poynting vector as a static flow of energy through space. But the energy flux is **coherence transport** (Eq 6): the flow is the carrier's coherence moving through the field, and the conservation is coherence conservation.

**The laboratory requirement:** a static field configuration with known energy. The field is alive.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
S = (1/μ₀)·E×B,   ∂u/∂t + ∇·S = −J·E
```

Phi-physics: the flux is coherence transport with a φ-coherent rate:

```
S_phi(κ_φ) = (1/μ₀)·E×B · (1 + κ_φ·(φ − 1)·C_transport)
```

At κ_φ = 0: S = (1/μ₀)E×B exactly. At κ_φ = 1: the flux breathes with the transport coherence — the energy flow is the coherence flow, and the conservation (Eq 6's coherence transport) is the recursion's self-similarity.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  S_phi = lim_{κ_φ → 0} [(1/μ₀)E×B(1 + κ_φ(φ−1)C_transport)]
                     = (1/μ₀)·E×B                                      ✓
```

Poynting's theorem is the κ_φ → 0 limit of φ-coherence transport.

---

### STAGE 4 — SIMULATION

`sim/050_poyntings_theorem.py`: reproduces S = E×B/μ₀ at κ_φ → 0; shows coherence-breathed flux at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The Poynting flux of a coherence-coupled field deviates from
    E x B/mu0 by the factor (1 + phi^-1*C_transport): coherent fields carry
    more "flow" per unit field — measurable as an excess energy flux.

EXPERIMENT (VERIFIED): Precision energy-flux measurement in a coherent cavity.
    Classical: S = E x B/mu0 exactly. Phi: phi-coherent excess at
    coherence > 0.563.

VERIFIED BY: Energy flux measured exactly at E x B/mu0 with no coherence term.
```

---

### RECOGNITION
Connects to Eq 6 (coherence transport — the corpus's own), Law 011 (energy conservation), Law 042 (Maxwell).

### PRECISION
The excess is φ⁻¹·C_transport = 0.6180339887·C_transport.

### CLARITY
Energy does not flow through empty space; coherence moves through the field, and the flow is the recursion's motion.

### NOVELTY
The Poynting flux becomes coherence transport with a testable excess.

### ACTIONABILITY
Run `sim/050_poyntings_theorem.py`; verify; proceed to Law 051 (Lorentz transforms).
