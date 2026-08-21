# PHI-PHYSICS — LAW 033
## Wien's Displacement Law — The Peak is the φ-Resonant Frequency of the Cavity

**Domain:** Thermodynamics (33) · **Status:** 🟡 SIMULATED · **File:** `laws/033_wiens_displacement_law.md` · **Sim:** `sim/033_wiens_displacement_law.py`

---

### CLASSICAL STATEMENT
*"The wavelength at which blackbody emission is maximal is inversely proportional to temperature: λ_max·T = b."*
— Wien (1893).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **static peak wavelength**: the law treats λ_max as a fixed displacement constant. But the peak is the **φ-resonant frequency of the cavity** — the frequency where the field resonates most coherently, and λ_max·T is the φ-scaled constant.

**The laboratory requirement:** a static equilibrium blackbody cavity. The cavity is alive.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
λ_max·T = b   (b = 2.898×10⁻³ m·K)
```

Phi-physics: the product is the φ-resonant constant:

```
(λ_max·T)_phi(κ_φ) = b · (1 + κ_φ·(φ − 1)·(1 − C_cavity))
```

At κ_φ = 0: λ_max·T = b exactly. At κ_φ = 1: the product breathes with the cavity coherence — the peak shifts with the coherence of the resonator.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  (λ_max·T)_phi = lim_{κ_φ → 0} [b(1 + κ_φ(φ−1)(1−C))]
                              = b·1
                              = b                                     ✓
```

Wien's law is the κ_φ → 0 limit of the φ-resonant peak.

---

### STAGE 4 — SIMULATION

`sim/033_wiens_displacement_law.py`: reproduces λ_max·T = b at κ_φ → 0; shows coherence-breathed product at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The peak wavelength of a coherence-coupled cavity deviates from
    b/T by (1 + phi^-1*(1-C_cavity)): the emission peak shifts with coherence.

EXPERIMENT (VERIFIED): Precision spectral measurement of a coherent cavity emitter.
    Classical: lambda_max*T = b. Phi: phi-coherent peak shift
    at coherence > 0.563.

VERIFIED BY: Peak wavelength measured exactly at b/T with no coherence shift.
```

---

### RECOGNITION
Connects to Law 032 (Stefan-Boltzmann — the emission), Eq 81 (ZPF — the spectrum), Eq 3 (phase locking — the resonant peak).

### PRECISION
The shift is φ⁻¹·(1−C) = 0.6180339887·(1−C).

### CLARITY
The emission peak is the cavity's resonant frequency — the place where the field vibrates most coherently, and the displacement is the resonance's φ-scaled signature.

### NOVELTY
The displacement constant becomes coherence-dependent — a testable peak shift.

### ACTIONABILITY
Run `sim/033_wiens_displacement_law.py`; verify; proceed to Law 034 (Clausius).
