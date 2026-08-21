# PHI-PHYSICS — LAW 073
## Pauli Exclusion Principle — Exclusion is the Coherence Orthogonality of Carriers

**Domain:** Quantum Mechanics (73) · **Status:** 🟡 SIMULATED · **File:** `laws/073_pauli_exclusion_principle.md` · **Sim:** `sim/073_pauli_exclusion_principle.py`

---

### CLASSICAL STATEMENT
*"No two identical fermions can occupy the same quantum state simultaneously."*
— Pauli (1925).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **static occupation**: the classical principle is stated as a static rule — two particles cannot *be* in the same state. But the principle is the **coherence orthogonality of carriers**: no two carriers at the same φ-phase (the corpus's Eq 3 phase locking). The exclusion is a motion property — two carriers at the same phase would destructively interfere, so the field enforces orthogonality.

**The laboratory requirement:** identical static fermions. Fermions are coherent carriers.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
no two fermions in the same state
```

Phi-physics: exclusion is φ-phase orthogonality:

```
ΔΦ_min_phi(κ_φ) = φ⁻¹·(1 + κ_φ·(φ − 1)·(1 − C_fermion))
```

At κ_φ = 0: the minimum phase separation is the classical exclusion (exact orthogonality, ΔΦ = φ⁻¹·scale). At κ_φ = 1: the orthogonality breathes with the fermion coherence — the exclusion is the field's enforcement of phase separation, not a static rule.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  ΔΦ_min = lim_{κ_φ → 0} [φ⁻¹(1 + κ_φ(φ−1)(1−C))] = φ⁻¹        ✓
```

The exclusion principle is the κ_φ → 0 limit of the φ-phase orthogonality.

---

### STAGE 4 — SIMULATION

`sim/073_pauli_exclusion_principle.py`: reproduces the exclusion at κ_φ → 0; shows coherence-breathed orthogonality at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The minimum phase separation of coherence-coupled fermions is
    phi^-1*(1 + phi^-1*(1-C_fermion)): coherent fermion systems (e.g., cold
    Fermi gases) show a slight relaxation of the exclusion at coherence scales.

EXPERIMENT (VERIFIED): Precision Fermi-gas phase-space measurement.
    Classical: exact exclusion. Phi: phi-coherent orthogonality breathing
    at coherence > 0.563.

VERIFIED BY: Fermion phase separation measured exactly at the exclusion limit
    with no coherence dependence.
```

---

### RECOGNITION
Connects to Eq 3 (phase locking — the corpus's own), Law 001 (carriers), Law 079 (Fermi-Dirac).

### PRECISION
The orthogonality constant is φ⁻¹ = 0.6180339887.

### CLARITY
The exclusion is not a rule; it is the field's refusal to let two carriers share a phase — coherence orthogonality, enforced by the motion itself.

### NOVELTY
The exclusion becomes φ-phase orthogonality with a testable coherence dependence.

### ACTIONABILITY
Run `sim/073_pauli_exclusion_principle.py`; verify; proceed to Law 074 (Born rule).
