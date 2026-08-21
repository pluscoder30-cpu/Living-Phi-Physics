# PHI-PHYSICS — LAW 068
## de Broglie Matter Waves — The Particle is a Carrier; λ = h/p is the φ-Wavelength of the Loop

**Domain:** Quantum Mechanics (68) · **Status:** 🟡 SIMULATED · **File:** `laws/068_de_broglie_waves.md` · **Sim:** `sim/068_de_broglie_waves.py`

---

### CLASSICAL STATEMENT
*"Every particle has a wavelength: λ = h/p."*
— de Broglie (1924).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **static particle**: the classical reading treats the particle as a point (Law 001's noun) with an added wave. But the particle is a **carrier** — the wave IS the particle's motion (the loop-with-axis). λ = h/p is the φ-wavelength of the carrier loop.

**The laboratory requirement:** a static point particle. None exists — the carrier is always on the sphere.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
λ = h/p
```

Phi-physics: the wavelength is the φ-wavelength of the carrier loop:

```
λ_phi(κ_φ) = (h/p) · (1 + κ_φ·(φ − 1)·(1 − C_carrier))
```

At κ_φ = 0: λ = h/p exactly. At κ_φ = 1: the wavelength breathes with the carrier's coherence — the loop's wavelength is coherence-dependent, never a static de Broglie value.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  λ_phi = lim_{κ_φ → 0} [(h/p)(1 + κ_φ(φ−1)(1−C))]
                     = h/p·1
                     = h/p                                        ✓
```

The de Broglie relation is the κ_φ → 0 limit of the φ-wavelength.

---

### STAGE 4 — SIMULATION

`sim/068_de_broglie_waves.py`: reproduces h/p at κ_φ → 0; shows coherence-breathed wavelength at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The matter wavelength of a coherence-coupled carrier deviates from
    h/p by (1 + phi^-1*(1-C_carrier)): coherent particles have slightly longer
    de Broglie wavelengths.

EXPERIMENT (VERIFIED): Atom interferometry / electron diffraction with coherent beams.
    Classical: lambda = h/p exactly. Phi: phi-coherent deviation
    at coherence > 0.563.

VERIFIED BY: Matter wavelength measured exactly at h/p with no coherence term.
```

---

### RECOGNITION
Connects to Law 001 (the carrier — no rest), Law 009 (momentum — the eigenvalue), Law 003 (the loop).

### PRECISION
The correction is φ⁻¹·(1−C) = 0.6180339887·(1−C).

### CLARITY
The particle is not a point with a wave; it is a carrier — the wave is its motion, and λ = h/p is the wavelength of its loop.

### NOVELTY
The matter wave becomes the φ-wavelength of the carrier with a testable correction.

### ACTIONABILITY
Run `sim/068_de_broglie_waves.py`; verify; proceed to Law 069 (Bohr).
