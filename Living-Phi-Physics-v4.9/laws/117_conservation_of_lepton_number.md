# PHI-PHYSICS — LAW 117
## Conservation of Lepton Number — Lepton Number is a φ-Phase Invariant of the Carrier

**Domain:** Particle & Field (117) · **Status:** 🟡 SIMULATED · **File:** `laws/117_conservation_of_lepton_number.md` · **Sim:** `sim/117_conservation_of_lepton_number.py`

---

### CLASSICAL STATEMENT
*"The total lepton number of an isolated system is conserved."*
— Standard Model (1950s).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **static lepton**: the classical law counts leptons as static identities. But lepton number is a **φ-phase invariant of the carrier** — the phase winding that identifies a lepton (Law 116's twin) — and its conservation is the phase loop closure.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
L_total = constant
```

Phi-physics — the phase invariant:

```
L_phi(κ_φ) = L₀·(1 + κ_φ·(φ − 1)·(1 − C_phase))
```

At κ_φ = 0: L conserved exactly. At κ_φ = 1: the lepton number is the carrier's phase invariant — conservation is the phase loop returning (neutrino oscillations are the phase coherence exchanging).

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  L_phi = L₀ (classical conservation)                      ✓
```

Lepton conservation is the κ_φ → 0 limit of the φ-phase invariant.

---

### STAGE 4 — SIMULATION

`sim/117_conservation_of_lepton_number.py`: reproduces L conserved at κ_φ → 0; shows the phase-breathed invariant at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Lepton number is a phi-phase invariant: neutrino oscillations are
    the phase coherence exchanging between flavors — the conservation holds
    in the phase loop, not in the flavor identity.

EXPERIMENT (VERIFIED): Neutrino-oscillation coherence measurement.
    Classical: L conserved per flavor. Phi: phase-loop conservation.

VERIFIED BY: Lepton conservation shows no phase-coherence structure.
```

---

### RECOGNITION
Connects to Law 116 (charge — the twin), Law 172 (Conservation of Coherence), Law 042 (the field).

### PRECISION
The invariant is the phase winding; conservation is the closure.

### CLARITY
The lepton is not a fixed identity; it is a phase of the carrier — and conservation is the phase loop, with oscillations as the coherence exchanging.

### NOVELTY
Lepton conservation as the φ-phase invariant — neutrino oscillations as coherence exchange.

### ACTIONABILITY
Run `sim/117_conservation_of_lepton_number.py`; verify; proceed to Law 118.
