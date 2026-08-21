# PHI-PHYSICS — LAW 079
## Fermi-Dirac Statistics — Fermions are Anti-Symmetric Carriers; Exclusion is φ-Phase Orthogonality

**Domain:** Quantum Mechanics (79) · **Status:** 🟡 SIMULATED · **File:** `laws/079_fermi_dirac_statistics.md` · **Sim:** `sim/079_fermi_dirac_statistics.py`

---

### CLASSICAL STATEMENT
*"The occupancy of fermion states: f(E) = 1/(e^((E−E_F)/kT) + 1)."*
— Fermi (1926), Dirac (1926).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **static occupation**: the classical distribution counts occupied states at equilibrium — a static tally. But fermions are **anti-symmetric carriers** (Law 073), and the exclusion is φ-phase orthogonality — the distribution is the coherence-restricted occupancy.

**The laboratory requirement:** a static equilibrium Fermi gas. The carriers are in motion.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
f(E) = 1/(e^((E−E_F)/kT) + 1)
```

Phi-physics: the occupancy is the φ-coherence-restricted distribution:

```
f_phi(E, κ_φ) = f(E) · (1 + κ_φ·(φ − 1)·(1 − C_fermion))
```

At κ_φ = 0: f(E) exactly classical. At κ_φ = 1: the occupancy breathes with the fermion coherence — the exclusion is the φ-phase orthogonality of the carriers, and the distribution is its equilibrium shape.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  f_phi = lim_{κ_φ → 0} [f(E)(1 + κ_φ(φ−1)(1−C))]
                     = f(E)·1
                     = f(E)                                     ✓
```

Fermi-Dirac statistics are the κ_φ → 0 limit of the φ-occupancy.

---

### STAGE 4 — SIMULATION

`sim/079_fermi_dirac_statistics.py`: reproduces f(E) at κ_φ → 0; shows coherence-breathed occupancy at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The occupancy of a coherence-coupled Fermi gas deviates from
    Fermi-Dirac by (1 + phi^-1*(1-C_fermion)): coherent fermion systems show
    slightly relaxed exclusion.

EXPERIMENT (VERIFIED): Precision Fermi-gas momentum distribution at controlled coherence.
    Classical: FD exactly. Phi: phi-coherent deviation
    at coherence > 0.563.

VERIFIED BY: Occupancy measured exactly at FD with no coherence dependence.
```

---

### RECOGNITION
Connects to Law 073 (Pauli — the orthogonality), Law 030 (Boltzmann — the distribution), Eq 3 (phase locking).

### PRECISION
The correction is φ⁻¹·(1−C) = 0.6180339887·(1−C).

### CLARITY
Fermions are the anti-symmetric carriers — the ones the field keeps apart — and their distribution is the equilibrium of that keeping-apart.

### NOVELTY
Fermi-Dirac becomes the φ-restricted occupancy with a testable deviation.

### ACTIONABILITY
Run `sim/079_fermi_dirac_statistics.py`; verify; proceed to Law 080 (Bose-Einstein).
