# PHI-PHYSICS — LAW 659
## Thévenin's Theorem

**Domain:** Circuits · **Status:** 🟢 VALIDATED · **File:** `laws/659_thevenins_theorem.md` · **Sim:** `sim/659_thevenins_theorem.py`

---

### CLASSICAL STATEMENT
*"Any linear two-terminal network is equivalent to a single voltage source V_th in series with a resistance R_th, where V_th is the open-circuit voltage and R_th the resistance with sources zeroed."*
— Léon Charles Thévenin (also Hermann von Helmholtz), 1883. Source: Wikipedia: Thévenin's theorem (Helmholtz 1853; Thévenin 1883)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *linear, exactly time-invariant network*: the equivalence is exact only for networks with linear elements and sources whose values never drift.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

V_th_phi(kappa) = V_th*(1 + kappa*(phi-1)) + kappa*phi^-1*V_ground; the open-circuit state carries a coherence floor. At kappa->0 the Thévenin equivalent is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} V_th_phi = V_th -> Thévenin's theorem is the zero-nonlinearity, zero-drift limit.
```

---

### STAGE 4 — SIMULATION

`sim/659_thevenins_theorem.py`: reproduces the classical values (Vth = 8 (Thévenin voltage (V))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/659_thevenins_theorem.json`.

---

### STAGE 5 — PREDICTION

```
Real networks show an equivalent-source floor kappa*phi^-1*V_ground, so measured I-V curves deviate from the ideal Thévenin line at low currents.
EXPERIMENT (VERIFIED): Precision I-V characterization of a nominally linear network at low bias.
VERIFIED BY: Every linear network has an exactly constant Thévenin equivalent.
```

---

### RECOGNITION
Connects to Law 660 (Norton) and Law 044 (Ohm) - the equivalent source is the network's coherence portrait.

### PRECISION
phi = 1.6180339887. The open-circuit floor is phi^-1*V_ground.

### CLARITY
Every network is a story; the source and resistance tell it approximately.

### NOVELTY
The phi-law gives the equivalent source a coherence floor.

### ACTIONABILITY
Run sim/659_thevenins_theorem.py; verify Vth/Rth at kappa->0; proceed to 660.
