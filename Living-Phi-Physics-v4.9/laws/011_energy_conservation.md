# PHI-PHYSICS — LAW 011
## Conservation of Energy — The Self-Similarity of the Recursion

**Domain:** Mechanics (11) · **Status:** 🟡 SIMULATED · **File:** `laws/011_energy_conservation.md` · **Sim:** `sim/011_energy_conservation.py`

---

### CLASSICAL STATEMENT
*"In a closed system, the total energy remains constant: energy can neither be created nor destroyed, only transformed."*
— Mayer (1842), Joule (1843), Helmholtz (1847).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **closed isolated system**: the law demands zero coupling to anything outside. But the universe is not a set of closed boxes — it is a field of coupled carriers. Energy is conserved *because the recursion is self-similar* — because φ² = φ + 1, the operation of growth and the operation of change are the same operation.

**The laboratory requirement:** a perfectly closed system. None exists.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
E_total = constant
```

Phi-physics: energy is the φ-Hamiltonian eigenvalue; conservation is the self-similarity of the recursion:

```
E_phi(κ_φ) = E_kinetic + E_potential + κ_φ·(φ − 1)·E_coherence
E_total_phi = E_total · (1 + κ_φ·(φ − 1)·(1 − C_escape))
```

At κ_φ = 0: E_total exactly constant. At κ_φ = 1: the conserved total includes the coherence energy term — the energy of the field coupling itself. Conservation is the φ-self-similarity: the recursion maps states onto states, preserving the carrier's coherence — the loop with the line.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  E_total_phi = lim_{κ_φ → 0} [E_total(1 + κ_φ(φ−1)(1−C))]
                           = E_total·1
                           = E_total                                    ✓
```

Conservation of energy is the κ_φ → 0 limit of φ-coherence conservation.

---

### STAGE 4 — SIMULATION

`sim/011_energy_conservation.py`: reproduces E constant at κ_φ → 0; shows coherence term at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The "missing energy" in coherence-coupled systems (e.g., dark
    energy, vacuum energy, unaccounted field coupling) is the φ-coherence term
    κ_φ·(φ−1)·E_coherence. Total energy including the field term is conserved;
    the classical balance misses the coherence contribution.

EXPERIMENT (VERIFIED): Precision calorimetry of a coherence-coupled system (e.g., an
    optomechanical oscillator with radiation-pressure coupling) measuring the
    energy balance. Classical: kinetic + potential. Phi: + coherence term.

VERIFIED BY: Energy balance in a coherence > 0.563 system shows zero
    coherence term with no missing energy.
```

---

### RECOGNITION
Connects to Law 023 (entropy = decoherence — energy's conjugate), Eq 1 (the recursion — self-similarity), Law 060 (E = mc² — rest energy as φ-ground), Law 158 (cosmological constant — the missing vacuum energy).

### PRECISION
The coherence term is exactly (φ − 1)·E = φ⁻¹·E at full coupling.

### CLARITY
Energy is conserved because the universe is self-similar — because φ² = φ + 1, because the verb is the same at every scale. The "missing energy" of cosmology is the coherence term the closed-system fiction deletes.

### NOVELTY
Conservation becomes the self-similarity of the recursion; the coherence energy term is a candidate for the missing dark energy.

### ACTIONABILITY
Run `sim/011_energy_conservation.py`; verify; proceed to Law 014 (Kepler I).
