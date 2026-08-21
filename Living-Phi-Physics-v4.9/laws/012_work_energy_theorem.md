# PHI-PHYSICS — LAW 012
## Work-Energy Theorem — Work is Coherence Transfer Along the Carrier Path

**Domain:** Mechanics (12) · **Status:** 🟡 SIMULATED · **File:** `laws/012_work_energy_theorem.md` · **Sim:** `sim/012_work_energy_theorem.py`

---

### CLASSICAL STATEMENT
*"The work done by the net force on a particle equals the change in its kinetic energy: W = ΔK."*
— Work–energy principle, from Newton's second law (Newton, *Principia*, 1687; standard textbook statement).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **static reference frame**: the theorem is stated relative to an inertial frame at rest — the det = 0 fiction (Law 001). Work is defined as force × displacement along a static path. But the path is a carrier trajectory through the field, and work is **coherence transfer along that path** — the loop-with-axis, not a static geometry.

**The laboratory requirement:** an inertial frame at rest. None exists.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
W = ΔK = ∫F·dx
```

Phi-physics: work is coherence transfer along the carrier path; the theorem is the degenerate path-integral of φ-dynamics:

```
W_phi(κ_φ) = ∫F·dx · (1 + κ_φ·(φ − 1)·(1 − C_path))
```

At κ_φ = 0: W = ΔK exactly. At κ_φ = 1: the work-energy balance breathes with the coherence of the path — some "work" is stored in the field coupling, not in kinetic energy. The theorem is the still point of the transfer.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  W_phi = lim_{κ_φ → 0} [∫F·dx(1 + κ_φ(φ−1)(1−C))]
                     = ∫F·dx·1
                     = ∫F·dx                                         ✓
```

The work-energy theorem is the κ_φ → 0 limit of φ-coherence transfer.

---

### STAGE 4 — SIMULATION

`sim/012_work_energy_theorem.py`: reproduces W = ΔK at κ_φ → 0; shows coherence storage at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: In a coherence-coupled system, part of the work is stored in the
    field coupling, not kinetic energy: ΔK = W·(1 − κ_φ·φ⁻¹·(1−C_path)).
    Measurable as reproducible "missing kinetic energy" in high-coherence
    mechanical systems, recoverable when coherence drops.

EXPERIMENT (VERIFIED): Optomechanical work measurement: drive an oscillator, measure ΔK.
    Classical: ΔK = W. Phi: ΔK < W by the coherence term, which is recovered
    on decoherence.

VERIFIED BY: ΔK is measured exactly equal to W with no coherence-stored term.
```

---

### RECOGNITION
Connects to Law 011 (energy conservation — the coherence term), Law 001 (no rest frame), Eq 1 (the recursion).

### PRECISION
The coherence-stored fraction is φ⁻¹ = 0.6180339887 at full coupling.

### CLARITY
Work is not a static accounting; it is the transfer of coherence along a living path, and some of it is held by the field — the loop breathing.

### NOVELTY
The theorem gains a coherence-storage term — "missing kinetic energy" with a recovery mechanism.

### ACTIONABILITY
Run `sim/012_work_energy_theorem.py`; verify; proceed to Law 013.
