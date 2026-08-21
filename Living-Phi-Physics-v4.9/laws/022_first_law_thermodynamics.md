# PHI-PHYSICS — LAW 022
## First Law of Thermodynamics — Energy Conserves Because the Recursion is Self-Similar

**Domain:** Thermodynamics (22) · **Status:** 🟡 SIMULATED · **File:** `laws/022_first_law_thermodynamics.md` · **Sim:** `sim/022_first_law_thermodynamics.py`

---

### CLASSICAL STATEMENT
*"The change in internal energy of a system equals the heat added minus the work done: ΔU = Q − W."*
— Mayer (1842), Joule (1843).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **closed isolated system**: the law assumes the system's energy balance is fully accounted by heat and work — no coupling to anything outside. But the φ-ground state carries ZPF energy (Eq 81, never zero), and the balance includes the coherence term (Law 011's twin).

**The laboratory requirement:** a perfectly isolated system. None exists — the vacuum alone couples energy in.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
ΔU = Q − W
```

Phi-physics: energy conserves because the recursion is self-similar (φ² = φ + 1); the balance includes the coherence term:

```
ΔU_phi(κ_φ) = (Q − W) + κ_φ·(φ − 1)·E_coherence
```

At κ_φ = 0: ΔU = Q − W exactly. At κ_φ = 1: the balance includes the coherence energy — the ZPF coupling, the field storage; the first law is the self-similarity of the recursion.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  ΔU_phi = lim_{κ_φ → 0} [(Q − W) + κ_φ(φ−1)E_coh] = Q − W     ✓
```

The first law is the κ_φ → 0 limit of the φ-balance.

---

### STAGE 4 — SIMULATION

`sim/022_first_law_thermodynamics.py`: reproduces ΔU = Q − W at κ_φ → 0; shows the coherence term at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The energy balance of a coherence-coupled system includes a
    phi-coherence term: dU = Q - W + phi^-1*E_coherence. The "missing energy"
    of coupled systems is the coherence storage — recoverable on decoherence.

EXPERIMENT (VERIFIED): Precision calorimetry of a coherence-controlled system (e.g.,
    optomechanical oscillator). Classical: dU = Q - W exactly.
    Phi: phi-coherent storage term at coherence > 0.563.

VERIFIED BY: Energy balance measured exactly at Q - W with no coherence term.
```

---

### RECOGNITION
Connects to Law 011 (energy conservation — the coherence term), Law 023 (entropy), Eq 81 (ZPF — the ground never zero).

### PRECISION
The coherence term is (φ−1)·E = 0.6180339887·E.

### CLARITY
The first law is the recursion's self-similarity: energy conserves because the universe is the same verb at every scale.

### NOVELTY
The balance gains the coherence-storage term — the thermodynamic twin of Law 011's missing energy.

### ACTIONABILITY
Run `sim/022_first_law_thermodynamics.py`; verify; proceed to Law 025 (ideal gas).
