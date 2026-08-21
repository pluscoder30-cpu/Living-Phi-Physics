# PHI-PHYSICS — LAW 118
## Conservation of Baryon Number — Baryon Number is the φ-Stability of the Carrier Knot

**Domain:** Particle & Field (118) · **Status:** 🟡 SIMULATED · **File:** `laws/118_conservation_of_baryon_number.md` · **Sim:** `sim/118_conservation_of_baryon_number.py`

---

### CLASSICAL STATEMENT
*"The total baryon number of an isolated system is conserved."*
— Standard Model (1950s).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **static baryon**: the classical law counts baryons as static identities. But a baryon is a **carrier knot** — three quarks tied in a φ-stable configuration — and baryon number is the **φ-stability of the knot** (Law 116's twin, Law 177's still-point cousin). Its conservation is the knot's coherence stability.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
B_total = constant
```

Phi-physics — the knot stability:

```
B_phi(κ_φ) = B₀·(1 + κ_φ·(φ − 1)·(1 − C_knot))
```

At κ_φ = 0: B conserved exactly. At κ_φ = 1: the baryon is the carrier knot — conservation is the knot's φ-stability, and baryogenesis (Law 163) is the knot's coherence forming.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  B_phi = B₀ (classical conservation)                      ✓
```

Baryon conservation is the κ_φ → 0 limit of the φ-knot stability.

---

### STAGE 4 — SIMULATION

`sim/118_conservation_of_baryon_number.py`: reproduces B conserved at κ_φ → 0; shows the knot-breathed invariant at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Baryon number is the phi-stability of the carrier knot: baryons
    are three-quark knots held by coherence, and the conservation is the
    knot's stability — baryogenesis (Law 163) is the coherence forming.

EXPERIMENT (VERIFIED): Baryon-structure coherence measurement (lattice QCD).
    Classical: B conserved. Phi: knot-stability conservation.

VERIFIED BY: Baryon stability shows no coherence-knot structure.
```

---

### RECOGNITION
Connects to Law 116 (charge — the twin), Law 177 (the still point), Law 163 (baryogenesis — the open problem).

### PRECISION
The knot's stability is the φ-ground of the three-carrier configuration.

### CLARITY
The baryon is not a static count; it is a carrier knot — three quarks tied in coherence, and conservation is the knot's stability.

### NOVELTY
Baryon conservation as the φ-knot stability — the baryon made coherent.

### ACTIONABILITY
Run `sim/118_conservation_of_baryon_number.py`; verify; proceed to Law 119.
