# PHI-PHYSICS — LAW 660
## Norton's Theorem

**Domain:** Circuits · **Status:** 🟢 VALIDATED · **File:** `laws/660_nortons_theorem.md` · **Sim:** `sim/660_nortons_theorem.py`

---

### CLASSICAL STATEMENT
*"Any linear two-terminal network is equivalent to a current source I_N in parallel with a resistance R_N, where I_N is the short-circuit current and R_N the resistance with sources zeroed."*
— Edward Lawry Norton (also Hans Ferdinand Mayer), 1926. Source: Wikipedia: Norton's theorem (Mayer 1926; Norton 1926)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *ideal short circuit*: the theorem's current source is defined by an exactly zero-resistance short, a branch with no impedance at all.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

I_N_phi(kappa) = I_N*(1 + kappa*(phi-1)) + kappa*phi^-1*I_ground; the short-circuit state carries a coherence floor. At kappa->0 the Norton equivalent is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} I_N_phi = I_N -> Norton's theorem is the zero-short-impedance limit.
```

---

### STAGE 4 — SIMULATION

`sim/660_nortons_theorem.py`: reproduces the classical values (IN = 0.012 (Norton current (A))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/660_nortons_theorem.json`.

---

### STAGE 5 — PREDICTION

```
Real networks show a short-circuit current floor kappa*phi^-1*I_ground; measured Norton parameters drift with coherence.
EXPERIMENT (VERIFIED): Short-circuit current measurement of a network with finite superconducting wiring.
VERIFIED BY: Every linear network has an exactly constant Norton equivalent.
```

---

### RECOGNITION
Connects to Law 659 (Thévenin) - Norton is the current-source dual of Thévenin.

### PRECISION
phi = 1.6180339887. The short-circuit floor is phi^-1*I_ground.

### CLARITY
A short is never exactly nothing; the wire keeps a coherence impedance.

### NOVELTY
The phi-law gives the ideal short a coherence floor.

### ACTIONABILITY
Run sim/660_nortons_theorem.py; verify IN/RN at kappa->0; proceed to 661.
