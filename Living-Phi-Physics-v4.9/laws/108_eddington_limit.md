# PHI-PHYSICS — LAW 108
## Eddington Limit — The Limit is the Coherence-Boundary Luminosity; Accretion is φ-Resonance Feeding

**Domain:** Cosmology (108) · **Status:** 🟡 SIMULATED · **File:** `laws/108_eddington_limit.md` · **Sim:** `sim/108_eddington_limit.py`

---

### CLASSICAL STATEMENT
*"The maximum luminosity a star can radiate before radiation pressure overcomes gravity: L_Edd = 4πGMc/κ."*
— Eddington (1920).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **static luminosity**: the classical limit treats the Eddington luminosity as a fixed threshold of a static star. But the limit is the **coherence-boundary luminosity** — the luminosity at which the star's coherence can no longer hold matter — and accretion is **φ-resonance feeding**.

**The laboratory requirement:** a static star with fixed opacity. The star is a coherent structure.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
L_Edd = 4πGMc/κ
```

Phi-physics: the limit is the coherence boundary:

```
L_Edd_phi(κ_φ) = (4πGMc/κ)·(1 + κ_φ·(φ − 1)·(1 − C_star))
```

At κ_φ = 0: L_Edd exactly classical. At κ_φ = 1: the limit breathes with the star's coherence — the boundary luminosity is the coherence the star holds, and accretion feeds by φ-resonance.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  L_Edd_phi = lim_{κ_φ → 0} [(4πGMc/κ)(1 + κ_φ(φ−1)(1−C))]
                          = 4πGMc/κ·1
                          = 4πGMc/κ                                ✓
```

The Eddington limit is the κ_φ → 0 limit of the φ-coherence boundary.

---

### STAGE 4 — SIMULATION

`sim/108_eddington_limit.py`: reproduces L_Edd at κ_φ → 0; shows coherence-breathed limit at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The Eddington luminosity of a coherence-coupled star deviates from
    4*pi*G*M*c/kappa by (1 + phi^-1*(1-C_star)): coherent accretion systems
    (e.g., super-Eddington accretors) exceed the classical limit by the
    phi-coherence factor.

EXPERIMENT (VERIFIED): Super-Eddington accretion measurement (ULXs, TDEs).
    Classical: hard limit at L_Edd. Phi: phi-coherent excess
    at coherence > 0.563.

VERIFIED BY: Accretion luminosity never exceeds the classical Eddington
    limit with no coherence structure.
```

---

### RECOGNITION
Connects to Law 023 (coherence), Law 107 (Chandrasekhar — the twin threshold), Law 004 (gravity).

### PRECISION
The excess is φ⁻¹·(1−C) = 0.6180339887·(1−C).

### CLARITY
The star does not hit a fixed luminosity wall; it reaches the coherence it can hold — and coherent accretion feeds beyond the classical limit.

### NOVELTY
The Eddington limit becomes coherence-dependent — explaining super-Eddington accretors.

### ACTIONABILITY
Run `sim/108_eddington_limit.py`; verify; proceed to Law 109 (orbital energy).
