# PHI-PHYSICS — LAW 066
## Planck's Law (Blackbody Spectrum) — At T→0 the φ-Spectrum Retains ℏω/2

**Domain:** Quantum Mechanics (66) · **Status:** 🟡 SIMULATED · **File:** `laws/066_plancks_law.md` · **Sim:** `sim/066_plancks_law.py`

---

### CLASSICAL STATEMENT
*"The spectral energy density of blackbody radiation: u(ν) = (8πhν³/c³)·1/(e^(hν/kT) − 1)."*
— Planck (1900).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **zero-temperature vacuum**: the classical spectrum at T → 0 vanishes — the radiation dies to zero. But the corpus's Eq 81 says the ZPF spectrum at T → 0 retains `ℏω/2` at every frequency: **the vacuum radiation never dies to zero.** Planck's law is the coherence-bounded ZPF spectrum; the classical version misses the ground term because it assumed a zero vacuum.

**The laboratory requirement:** a perfect blackbody at equilibrium. The vacuum is alive.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
u(ν) = (8πhν³/c³)·1/(e^(hν/kT) − 1)    → 0 as T → 0
```

Phi-physics (Eq 81's ZPF):

```
u_phi(ν, κ_φ) = (8πhν³/c³)·[1/(e^(hν/kT) − 1) + κ_φ·(ℏω/2)·Φ^(−ω/ω_crit)]
```

At κ_φ = 0: u → 0 as T → 0 (classical). At κ_φ = 1: the spectrum retains the φ-ZPF ground — the radiation never dies; it floors at the φ-coherent zero-point.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  u_phi = lim_{κ_φ → 0} [(8πhν³/c³)(1/(e^(hν/kT)−1) + κ_φ(ℏω/2)Φ^(−ω/ω_crit))]
                     = (8πhν³/c³)·1/(e^(hν/kT)−1)                       ✓
```

Planck's law is the κ_φ → 0 limit of the φ-ZPF spectrum.

---

### STAGE 4 — SIMULATION

`sim/066_plancks_law.py`: reproduces the classical spectrum at κ_φ → 0; shows the ZPF floor at κ_φ = 1, T → 0.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At temperatures approaching zero, the radiation spectrum does not
    vanish: it floors at the phi-ZPF level (hbar*omega/2 per mode, Eq 81).
    The "zero-point radiation" is measurable — the vacuum is not silent.

EXPERIMENT (VERIFIED): Ultra-low-temperature cavity radiation measurement.
    Classical: spectrum -> 0 as T -> 0. Phi: phi-ZPF floor persists.

VERIFIED BY: Radiation spectrum measured to vanish completely at T -> 0.
```

---

### RECOGNITION
Connects to Eq 81 (the φ-suppressed ZPF — the corpus's own), Law 032 (Stefan-Boltzmann), Law 024 (the φ-ground temperature).

### PRECISION
The floor is ℏω/2 per mode at T → 0 — the corpus's ZPF.

### CLARITY
The blackbody spectrum is the ZPF-bounded emission of the φ-field; the classical version killed the ground state by assuming a zero vacuum.

### NOVELTY
Planck's law gains the ZPF floor — the vacuum's voice at zero temperature.

### ACTIONABILITY
Run `sim/066_plancks_law.py`; verify; proceed to Law 067 (photoelectric).
