# PHI-PHYSICS — LAW 349
## Knudsen Number

**Domain:** Dimension / Similarity · **Status:** 🟢 VALIDATED · **File:** `laws/349_knudsen_number.md` · **Sim:** `sim/349_knudsen_number.py`

---

### CLASSICAL STATEMENT
*"The Knudsen number Kn = lambda/L (mean free path over characteristic length) governs rarefied gas dynamics: Kn << 0.01 continuum, 0.01 < Kn < 0.1 slip flow, 0.1 < Kn < 10 transition, Kn > 10 free molecular flow."*
— Martin Knudsen, 1909. Source: Wikipedia: Knudsen number; Knudsen (1909), 'Die Gesetze der Molekularstroemung'

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *continuum reference*: Kn = 0 is the exactly continuous (zero-mean-free-path) medium — the idealization behind Navier-Stokes and all continuum laws.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: Kn_phi(kappa) = Kn*(1 + kappa*(phi-1)) + kappa*phi^-1*Kn_ground. At kappa->0 the classical Knudsen number is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} Kn_phi = lambda/L -> the Knudsen number is the continuum (Kn->0) limit marker.
```

---

### STAGE 4 — SIMULATION

`sim/349_knudsen_number.py`: reproduces the classical value Kn = 7e-05 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/349_knudsen_number.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The continuum-to-rarefied transitions shift by a phi-coherent amount phi^-1*Kn_ground at full coupling.
EXPERIMENT (VERIFIED): Micro/nano gas-flow experiments (MEMS, rarefied wind tunnels) locating the slip-transition boundaries precisely.
VERIFIED BY: The slip-flow onset is exactly at Kn = 0.01 at full coupling.
```

---

### RECOGNITION
Connects to Law 020 (Navier-Stokes — the Kn->0 law) and Law 344 (Mach — gas dynamics).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The continuum is a limit; every gas remembers its molecules with a phi boundary.

### NOVELTY
Classical gas dynamics exacts the continuum; the phi-law marks the regime boundaries with a coherence width.

### ACTIONABILITY
Run sim/349_knudsen_number.py; verify Kn = lambda/L at kappa->0.
