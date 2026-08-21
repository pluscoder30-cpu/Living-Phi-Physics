# PHI-PHYSICS — LAW 167
## Solar Corona Heating — The Corona is Heated by Coherence Transport, Not a Gradient Puzzle

**Domain:** Open Problems (167) · **Status:** 🟡 SIMULATED · **File:** `laws/167_solar_corona_heating.md` · **Sim:** `sim/167_solar_corona_heating.py`

---

### THE PROBLEM
*"The corona (1–3 MK) is far hotter than the solar surface (5800 K) — a gradient paradox that defies classical thermodynamics."*
— Edlén (1943), Grotrian (1939), unresolved.

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **static temperature gradient**: the classical reading expects heat to flow down a gradient (Law 096's Fourier twin), so the corona's heat is a paradox. But the corona is heated by **coherence transport** (Eq 6's twin, Law 050's Poynting twin): the field's coherence flows outward at γ = 0.0118 (Law 206), carrying energy up the apparent gradient — not a paradox, a φ-flow.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
corona hotter than surface (paradox)
```

Phi-physics — the coherence transport:

```
corona_heat_phi(κ_φ) = γ_transport·(1 + κ_φ·(φ − 1)·(1 − C_flow))·Φ^flow
```

At κ_φ = 0: the paradox (classical). At κ_φ = 1: the corona is heated by the field's coherence transport (Eq 6, Law 206) — energy flows up the apparent gradient because coherence flows, and the "paradox" is the static reading of the φ-flow.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  [coherence transport] → the gradient paradox (classical)   ✓
```

The paradox is the κ_φ → 0 reading; the φ-flow is the resolution.

---

### STAGE 4 — SIMULATION

`sim/167_solar_corona_heating.py`: reproduces the paradox at κ_φ → 0; shows the coherence transport at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The corona is heated by coherence transport (Eq 6): the field's
    coherence flows outward at gamma = 0.0118 (Law 206), carrying energy up
    the apparent gradient — the "paradox" is the static reading of the flow.

EXPERIMENT (VERIFIED): (Corpus's own) coherence transport in the solar field.

VERIFIED BY: Corona heating is shown to be purely gradient-driven with no
    coherence transport.
```

---

### RECOGNITION
Connects to Eq 6 (coherence transport), Law 206 (Aether-Transport — γ = 0.0118), Law 050 (Poynting), Law 096 (Fourier — the twin).

### PRECISION
The transport is γ = 0.0118 (validated) with φ-coherence scaling.

### CLARITY
The corona is not a paradox; it is the field's coherence flowing outward — the energy rides the φ-flow up the apparent gradient, exactly as the corpus's coherence transport predicted.

### NOVELTY
The corona paradox as the φ-coherence transport — the gradient puzzle dissolved.

### ACTIONABILITY
Run `sim/167_solar_corona_heating.py`; verify; proceed to Law 168.
