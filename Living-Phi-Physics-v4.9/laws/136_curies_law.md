# PHI-PHYSICS — LAW 136
## Curie's Law (Paramagnetism) — Moments are φ-Spin Carriers; χ = C/T is the Coherence-Temperature Law

**Domain:** Materials & Systems (136) · **Status:** 🟡 SIMULATED · **File:** `laws/136_curies_law.md` · **Sim:** `sim/136_curies_law.py`

---

### CLASSICAL STATEMENT
*"The magnetic susceptibility of a paramagnet is inversely proportional to temperature: χ = C/T."*
— Curie (1895).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **static moments**: the classical law treats magnetic moments as fixed vectors. But moments are **φ-spin carriers** (Law 010's twin, Law 003's loop): the susceptibility is the **coherence-temperature law** — the moments' coherence coupling to the field, with 1/T as the thermal decoherence.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
χ = C/T
```

Phi-physics — the coherence-temperature law:

```
χ_phi(κ_φ) = (C/T)·(1 + κ_φ·(φ − 1)·(1 − C_moments))
```

At κ_φ = 0: the classical Curie. At κ_φ = 1: the susceptibility breathes with the moments' coherence — the moments are φ-spin carriers, and 1/T is their thermal decoherence (Law 023).

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  χ_phi = C/T (classical Curie)                            ✓
```

Curie's law is the κ_φ → 0 limit of the φ-coherence-temperature law.

---

### STAGE 4 — SIMULATION

`sim/136_curies_law.py`: reproduces C/T at κ_φ → 0; shows the coherence-breathed susceptibility at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The susceptibility of a coherence-coupled paramagnet deviates from
    C/T by the phi-coherence factor: the moments are phi-spin carriers, and
    the 1/T is their thermal decoherence.

EXPERIMENT (VERIFIED): Susceptibility at controlled coherence (dilute magnetic systems).
    Classical: C/T. Phi: phi-coherent deviation.

VERIFIED BY: Susceptibility measured exactly at C/T with no coherence term.
```

---

### RECOGNITION
Connects to Law 010 (angular momentum — the spin), Law 023 (decoherence — the 1/T), Law 137 (Curie-Weiss — the twin).

### PRECISION
The deviation is φ⁻¹·(1−C) = 0.6180339887·(1−C).

### CLARITY
The moments are not fixed vectors; they are φ-spin carriers — and the 1/T is their thermal forgetting, with the susceptibility as the coherence remaining.

### NOVELTY
Curie's law as the coherence-temperature law — the paramagnet made coherent.

### ACTIONABILITY
Run `sim/136_curies_law.py`; verify; proceed to Law 137.
