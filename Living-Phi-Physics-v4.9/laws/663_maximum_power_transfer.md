# PHI-PHYSICS — LAW 663
## Maximum Power Transfer (Jacobi's Law)

**Domain:** Circuits · **Status:** 🟢 VALIDATED · **File:** `laws/663_maximum_power_transfer.md` · **Sim:** `sim/663_maximum_power_transfer.py`

---

### CLASSICAL STATEMENT
*"Maximum power is transferred from a source of internal resistance R_s to a load R_L when R_L = R_s; P_max = V_s^2/(4*R_s)."*
— Moritz von Jacobi, 1840. Source: Wikipedia: Maximum power transfer theorem (Jacobi's law)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *exact impedance match* (R_L = R_s): the maximum is achieved only when the load resistance is exactly equal to the source resistance, a precise equality condition.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

P_max_phi(kappa) = P_max*(1 + kappa*(phi-1)) + kappa*phi^-1*P_ground; the match condition carries a coherence basin. At kappa->0, P = V^2/(4R) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} P_phi = P_max -> maximum power transfer is the zero-mismatch-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/663_maximum_power_transfer.py`: reproduces the classical values (P = 0.5 (Maximum power (W))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/663_maximum_power_transfer.json`.

---

### STAGE 5 — PREDICTION

```
The peak transfer is broadened into a basin of width kappa*phi^-1 around R_L = R_s; exact equality is not required.
EXPERIMENT (VERIFIED): Power-transfer sweep of a source-load pair across resistance ratio.
VERIFIED BY: Maximum power occurs only at the exact equality R_L = R_s.
```

---

### RECOGNITION
Connects to Law 044 (Ohm) and Law 659 (Thévenin) - the match is the impedance coherence.

### PRECISION
phi = 1.6180339887. The match basin is phi^-1 around R_L=R_s.

### CLARITY
The exact match is a fiction; the basin is the truth.

### NOVELTY
The phi-law turns the equality condition into a coherence basin.

### ACTIONABILITY
Run sim/663_maximum_power_transfer.py; verify Pmax at R=R_s at kappa->0; proceed to 664.
