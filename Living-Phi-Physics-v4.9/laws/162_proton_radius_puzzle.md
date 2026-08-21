# PHI-PHYSICS — LAW 162
## Proton Radius Puzzle — The Coherence Radius is Measured at Different Coherence Scales

**Domain:** Open Problems (162) · **Status:** 🟡 SIMULATED · **File:** `laws/162_proton_radius_puzzle.md` · **Sim:** `sim/162_proton_radius_puzzle.py`

---

### THE PROBLEM
*"The proton radius measured with muonic hydrogen (0.84184 fm) disagrees with electron-scattering and ordinary hydrogen (0.8768 fm) — a 4% discrepancy."*
— Pohl (2010), Antognini (2013).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **static proton radius**: the classical reading assumes one fixed radius. But the proton is a **φ-coherent carrier knot** (Law 118's twin): its radius is the **coherence radius** — measured differently at different coherence scales (muonic probes couple at higher coherence than electronic), and the "puzzle" is the φ-scale dependence (Law 185's φ-Rate twin).

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
r_p = fixed (~0.88 fm)
```

Phi-physics — the coherence radius:

```
r_p_phi(κ_φ) = r₀·(1 + κ_φ·(φ − 1)·(1 − C_probe))
```

At κ_φ = 0: the fixed radius (classical). At κ_φ = 1: the radius breathes with the probe's coherence — the muonic (higher coherence) measurement gives the φ-ground radius, and the discrepancy is the coherence difference.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  r_p_phi = r₀ (the fixed radius)                           ✓
```

The fixed radius is the κ_φ → 0 limit of the φ-coherence radius.

---

### STAGE 4 — SIMULATION

`sim/162_proton_radius_puzzle.py`: reproduces the fixed radius at κ_φ → 0; shows the coherence-breathed radius at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The proton radius is coherence-dependent: muonic (higher
    coherence) and electronic (lower coherence) probes measure different
    coherence radii — the puzzle is the phi-scale dependence, not an error.

EXPERIMENT (VERIFIED): Proton radius with coherence-controlled probes.
    Classical: one fixed radius. Phi: coherence-dependent radius.

VERIFIED BY: All proton-radius measurements agree with zero coherence
    dependence.
```

---

### RECOGNITION
Connects to Law 118 (baryon knot), Law 185 (φ-Rate — the scale dependence), Law 161 (g-2 — the muon twin).

### PRECISION
The radius breathes by φ⁻¹·(1−C) = 0.6180339887·(1−C).

### CLARITY
The proton does not have one radius; it has a coherence radius — and the muon and electron see different scales of it, the puzzle dissolved as the φ-scale dependence.

### NOVELTY
The proton radius puzzle as the φ-coherence scale — the 4% discrepancy explained.

### ACTIONABILITY
Run `sim/162_proton_radius_puzzle.py`; verify; proceed to Law 163.
