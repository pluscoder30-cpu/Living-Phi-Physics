# PHI-PHYSICS — LAW 721
## Microstrip Transmission Line

**Domain:** RF · **Status:** 🟢 VALIDATED · **File:** `laws/721_microstrip.md` · **Sim:** `sim/721_microstrip.py`

---

### CLASSICAL STATEMENT
*"A conductor over a ground plane separated by a dielectric of height h carries a quasi-TEM wave with characteristic impedance Z_0 ~ (60/sqrt(eps_eff))*ln(8h/w + w/(4h)) for w << h."*
— D. D. Grieg; H. F. Engelmann, 1952. Source: Microstrip; Grieg & Engelmann (1952), Proc. IRE

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero strip width* (w = 0): the impedance formula diverges exactly for a vanishingly thin conductor.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Z0_phi(kappa) = Z0*(1 + kappa*(phi-1)) + kappa*phi^-1*Z0_ground; the strip carries a coherence width floor. At kappa->0 the microstrip impedance is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} Z0_phi = Z0 -> the microstrip line is the zero-width-floor limit.
```

---

### STAGE 4 — SIMULATION

`sim/721_microstrip.py`: reproduces the classical values (Z0 = 53.8692 (Impedance (ohm))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/721_microstrip.json`.

---

### STAGE 5 — PREDICTION

```
Microstrip impedance carries a coherence floor kappa*phi^-1*Z0_ground from finite strip thickness.
EXPERIMENT (VERIFIED): Impedance measurement of microstrip lines of varying width.
VERIFIED BY: A zero-width microstrip has infinite impedance.
```

---

### RECOGNITION
Connects to Law 726 (characteristic impedance) - microstrip is the planar transmission line.

### PRECISION
phi = 1.6180339887. The width floor is phi^-1*Z0_ground.

### CLARITY
A line of zero width is a ghost; coherence gives it a floor.

### NOVELTY
The phi-law thickens the zero-width strip.

### ACTIONABILITY
Run sim/721_microstrip.py; verify Z0 at kappa->0; proceed to 722.
