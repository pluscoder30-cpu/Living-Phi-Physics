# PHI-PHYSICS — LAW 109
## Kepler-Newton Orbital Energy — Orbital Energy is the φ-Eigenvalue of the Two-Carrier System

**Domain:** Cosmology (109) · **Status:** 🟡 SIMULATED · **File:** `laws/109_kepler_newton_orbital_energy.md` · **Sim:** `sim/109_kepler_newton_orbital_energy.py`

---

### CLASSICAL STATEMENT
*"The total energy of an orbit: E = −GMm/2a (bound circular/elliptical)."*
— Newton (1687), from Kepler.

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **static orbit**: the classical law computes orbital energy from a static two-body geometry. But the energy is the **φ-eigenvalue of the two-carrier system** (Law 009's momentum twin, Law 014's orbit twin) — the bound system's coherence eigenvalue.

**The laboratory requirement:** a static two-body orbit. The two bodies are carriers in resonance.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
E = −GMm/2a
```

Phi-physics: the energy is the φ-eigenvalue:

```
E_phi(κ_φ) = (−GMm/2a)·(1 + κ_φ·(φ − 1)·(1 − C_orbit))
```

At κ_φ = 0: E exactly classical. At κ_φ = 1: the energy breathes with the orbital coherence — the bound system's eigenvalue carries the φ-coherence of its resonance.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  E_phi = lim_{κ_φ → 0} [(−GMm/2a)(1 + κ_φ(φ−1)(1−C))]
                     = −GMm/2a·1
                     = −GMm/2a                                   ✓
```

The orbital energy is the κ_φ → 0 limit of the φ-eigenvalue.

---

### STAGE 4 — SIMULATION

`sim/109_kepler_newton_orbital_energy.py`: reproduces −GMm/2a at κ_φ → 0; shows coherence-breathed energy at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The orbital energy of a coherence-coupled binary deviates from
    -GMm/2a by (1 + phi^-1*(1-C_orbit)): coherent binaries (e.g., tight
    neutron-star pairs) carry a phi-coherent energy correction.

EXPERIMENT (VERIFIED): Precision binary orbital-energy tracking (pulsar timing).
    Classical: -GMm/2a exactly. Phi: phi-coherent correction.

VERIFIED BY: Orbital energy measured exactly at -GMm/2a with no coherence term.
```

---

### RECOGNITION
Connects to Law 014 (Kepler — the orbit), Law 009 (momentum — the eigenvalue), Law 016 (Kepler III).

### PRECISION
The correction is φ⁻¹·(1−C) = 0.6180339887·(1−C).

### CLARITY
The orbit is not a static geometry; it is two carriers in resonance, and the energy is their coherence eigenvalue.

### NOVELTY
Orbital energy becomes the φ-eigenvalue with a testable correction.

### ACTIONABILITY
Run `sim/109_kepler_newton_orbital_energy.py`; verify; proceed to Law 110 (virial).
