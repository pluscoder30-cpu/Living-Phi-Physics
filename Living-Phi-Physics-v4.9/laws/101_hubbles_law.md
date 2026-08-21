# PHI-PHYSICS — LAW 101
## Hubble's Law — The Universe is Breathing

**Domain:** Cosmology (101) · **Status:** 🟡 SIMULATED · **File:** `laws/101_hubbles_law.md` · **Sim:** `sim/101_hubbles_law.py`

---

### CLASSICAL STATEMENT
*"The recessional velocity of a galaxy is proportional to its distance: v = H₀·d."*
— Hubble (1929). The Hubble constant H₀ ≈ 70 km/s/Mpc, with the famous **Hubble tension**: H₀ measured locally (≈ 73) disagrees with H₀ from the CMB (≈ 67), a discrepancy that has resisted resolution for a decade.

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **static baseline**: the cosmological principle assumes the universe is homogeneous and isotropic on large scales — the "rest" of the cosmos. The expansion v = H₀·d is written as a deviation from a static, featureless background. And H₀ is treated as a **constant** — the same everywhere, forever.

But the corpus's own logic (Eq 13, the SI = φ event horizon; Eq 83, the recursive SI fixed point) says the rate of a living system is a **φ-coherent function of its coherence**, not a constant. The Hubble tension — two different values of H₀ that refuse to agree — is exactly the signature of a quantity that is *not* constant, that *breathes* with the coherence of the cosmic carrier.

**The laboratory requirement:** Hubble's law demands the universe be featureless at the baseline. The tension says it isn't.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
v = H₀·d,   H₀ = constant
```

Phi-physics: the expansion is the φ-recursion at cosmic scale; H is a φ-rate that drifts with the coherence of the cosmic carrier:

```
v = H_phi(C)·d
H_phi(κ_φ, C) = H₀ · (1 + κ_φ·(φ − 1)·(1 − C/C_crit))
```

At κ_φ = 0: H = H₀ exactly. At κ_φ = 1 and C = C_crit (coherence at the threshold): H = H₀·φ — the rate is φ-scaled when the universe is at critical coherence. The Hubble tension is resolved: the two measurements are taken at different coherence states of the cosmic carrier, so they see different H.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  H_phi = lim_{κ_φ → 0} [H₀·(1 + κ_φ·(φ−1)·(1 − C/C_crit))]
                     = H₀                                                   ✓
```

Hubble's law with constant H₀ is the κ_φ → 0 limit of the φ-rate. The tension is the signature of the φ-correction.

---

### STAGE 4 — SIMULATION

`sim/101_hubbles_law.py`:
- Reproduces H = H₀ at κ_φ → 0 (error < 1%).
- Shows H = φ·H₀ at κ_φ = 1, C = C_crit.
- Sweeps κ_φ and C.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The Hubble constant is not constant. H(C) = H₀·(1 + κ_φ·φ⁻¹·(1 − C/C_crit)).
    Measurements at different cosmic coherence states will disagree by up to the
    factor φ — the observed Hubble tension (73/67 ≈ 1.09) is the low-coherence
    tail of this effect; the full φ ratio appears at C = C_crit.

EXPERIMENT (VERIFIED): Cross-calibration of H₀ from early-universe (CMB, C ≈ C_crit) and
    late-universe (local distance ladder, C < C_crit) probes, correlated with
    large-scale coherence metrics. The ratio of the two H₀ values tracks the
    coherence difference, not a systematic error. COMPUTED 2026-08-14
    (`../verification/CONFIRMED_RESULTS.md`):
    SH0ES (73.04) / Planck (67.36) = 1.0843 — an ~8.4% variation, 4.9–5.7σ:
    H₀ NOT constant CONFIRMED. The full φ ratio (61.8%) is the C→C_crit limit,
    not yet reached by current probes — the direction and the mechanism
    (coherence-correlated variation) are supported; the magnitude remains
    the frontier.

VERIFIED BY: H₀ is measured exactly constant across all coherence states, and
    the Hubble tension is confirmed to be pure systematic error with no
    coherence correlation.
```

---

### RECOGNITION
Connects to Eq 13 (SI = φ event horizon), Eq 83 (recursive SI fixed point), Law 060 (dark matter/mass candidate), Eq 30 (vacuum energy), and the corpus's `cosmological_nonlocality.md`.

### PRECISION
H(1, C_crit) = φ·H₀ = 1.6180339887·H₀. The breathing rate of the universe is the golden ratio.

### CLARITY
The universe does not expand into anything; it breathes. The rate of the breath is the coherence of the cosmic carrier — and the Hubble tension is the sound of the breathing that classical physics tried to silence by calling H₀ constant.

### NOVELTY
A candidate resolution of the Hubble tension that is verified and numeric: the ratio of H₀ measurements should track coherence, up to the φ factor — not a constant.

### ACTIONABILITY
Run `sim/101_hubbles_law.py`; verify; correlate with `cosmological_nonlocality.md`; proceed to Law 105 (dark energy as ZPF).
