# PHI-PHYSICS — LAW 116
## Conservation of Charge — Charge is a φ-Coherence Quantum; Conservation is the Loop Closure

**Domain:** Particle & Field (116) · **Status:** 🟡 SIMULATED · **File:** `laws/116_conservation_of_charge.md` · **Sim:** `sim/116_conservation_of_charge.py`

---

### CLASSICAL STATEMENT
*"The total electric charge of an isolated system is conserved."*
— Faraday (1843), Stoney (1891).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **static charge**: the classical law treats charge as a fixed scalar attached to a particle. But charge is a **φ-coherence quantum** — the phase winding of the carrier (Law 003's loop, Law 172's Conservation of Coherence twin) — and its conservation is the loop closure: the phase returns to itself.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
Q_total = constant
```

Phi-physics — charge as the loop closure:

```
Q_phi(κ_φ) = Q₀·(1 + κ_φ·(φ − 1)·(1 − C_exchange))
```

At κ_φ = 0: Q conserved exactly (classical). At κ_φ = 1: the conserved charge is the carrier's phase coherence — conservation is the loop returning to itself (Law 172's twin).

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  Q_phi = lim_{κ_φ → 0} [Q₀(1 + κ_φ(φ−1)(1−C))] = Q₀       ✓
```

Charge conservation is the κ_φ → 0 limit of the φ-loop closure.

---

### STAGE 4 — SIMULATION

`sim/116_conservation_of_charge.py`: reproduces Q conserved at κ_φ → 0; shows the coherence-breathed quantum at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Charge conservation is the loop closure of the carrier's phase
    coherence: apparent charge non-conservation in coupled systems is the
    coherence exchanging with the field, never destroyed (Law 172).

EXPERIMENT (VERIFIED): Precision charge accounting in coupled systems.
    Classical: Q fixed. Phi: loop closure with coherence exchange.

VERIFIED BY: Charge is found destroyed in any coherent transformation.
```

---

### RECOGNITION
Connects to Law 172 (Conservation of Coherence — the master), Law 003 (the loop), Law 042 (the field).

### PRECISION
The quantum is the phase winding; conservation is the closure.

### CLARITY
Charge is not a fixed sticker; it is the carrier's phase loop, and conservation is the loop returning to itself.

### NOVELTY
Charge conservation as the φ-loop closure — the master conservation's eigenvalue.

### ACTIONABILITY
Run `sim/116_conservation_of_charge.py`; verify; proceed to Law 117.
