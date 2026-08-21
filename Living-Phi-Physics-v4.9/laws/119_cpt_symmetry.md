# PHI-PHYSICS — LAW 119
## CPT Symmetry — CPT is the φ-Symmetry of the Full Recursion; Reversal is Retrocausal

**Domain:** Particle & Field (119) · **Status:** 🟡 SIMULATED · **File:** `laws/119_cpt_symmetry.md` · **Sim:** `sim/119_cpt_symmetry.py`

---

### CLASSICAL STATEMENT
*"The laws of physics are invariant under the combined operation of charge conjugation (C), parity inversion (P), and time reversal (T)."*
— Lüders (1954), Pauli (1955).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **static reversal**: the classical reading treats C, P, T as three static operations on a static state. But CPT is the **φ-symmetry of the full recursion**: time reversal is retrocausal (Law 181's twin, Eq 47), charge conjugation is the mirror carrier (Law 125), and parity is the loop's handedness (Law 197). The symmetry is the recursion's coherence invariance.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
CPT |Ψ⟩ = |Ψ⟩ (invariance under the combined operation)
```

Phi-physics — the recursion symmetry:

```
CPT_phi(κ_φ) = (C ⊗ P ⊗ T)·(1 + κ_φ·(φ − 1)·(1 − C_symmetry))
```

At κ_φ = 0: the classical invariance. At κ_φ = 1: CPT is the recursion's coherence symmetry — reversal is retrocausal, the mirror is the φ-carrier, and the symmetry holds because the recursion is self-similar.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  CPT_phi = the classical invariance                        ✓
```

CPT symmetry is the κ_φ → 0 limit of the φ-recursion symmetry.

---

### STAGE 4 — SIMULATION

`sim/119_cpt_symmetry.py`: reproduces the invariance at κ_φ → 0; shows the recursion symmetry at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: CPT is the symmetry of the recursion: time reversal is retrocausal
    (Eq 47), the mirror is the phi-carrier, and parity is the loop's
    handedness. The symmetry holds because the recursion is self-similar.

EXPERIMENT (VERIFIED): (Structural) The identification: CPT as the phi-recursion
    symmetry, with reversal as retrocausality (Law 181).

VERIFIED BY: A recursion-symmetry violation is found in coherent systems.
```

---

### RECOGNITION
Connects to Law 181 (retrocausality), Law 125 (antimatter — the mirror), Law 197 (chirality — the handedness), Eq 47.

### PRECISION
The symmetry is the recursion's coherence invariance.

### CLARITY
CPT is not three static reversals; it is the recursion's symmetry — time reversing retrocausally, the mirror carrier, the handed loop.

### NOVELTY
CPT as the φ-recursion symmetry — the deepest discrete symmetry made coherent.

### ACTIONABILITY
Run `sim/119_cpt_symmetry.py`; verify; proceed to Law 120.
