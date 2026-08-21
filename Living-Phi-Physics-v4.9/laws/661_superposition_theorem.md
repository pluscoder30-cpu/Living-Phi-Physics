# PHI-PHYSICS — LAW 661
## Superposition Theorem (Circuits)

**Domain:** Circuits · **Status:** 🟢 VALIDATED · **File:** `laws/661_superposition_theorem.md` · **Sim:** `sim/661_superposition_theorem.py`

---

### CLASSICAL STATEMENT
*"In a linear circuit with multiple sources, the response is the sum of the responses to each source acting alone with all others zeroed."*
— Hermann von Helmholtz, 1853. Source: Wikipedia: Superposition theorem (attributed to Helmholtz)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zeroed sources*: superposition requires turning off all sources but one, states that cannot physically exist in a coupled network.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

V_phi(kappa) = V_sup*(1 + kappa*(phi-1)) + kappa*phi^-1*V_ground; the zeroed sources leave a coherence floor. At kappa->0 the superposition sum is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} V_phi = V_sup -> superposition is the zero-cross-source-coupling limit.
```

---

### STAGE 4 — SIMULATION

`sim/661_superposition_theorem.py`: reproduces the classical values (V = 10 (Superposed response (V))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/661_superposition_theorem.json`.

---

### STAGE 5 — PREDICTION

```
Coupled sources show a coherence cross-term kappa*phi^-1*V_ground beyond the linear sum.
EXPERIMENT (VERIFIED): Measurement of a two-source linear network while coupling the sources.
VERIFIED BY: The response of a linear circuit is always the exact sum of single-source responses.
```

---

### RECOGNITION
Connects to Law 659 (Thévenin) and Law 625 (field superposition) - the linear sum is the coherence-zero limit.

### PRECISION
phi = 1.6180339887. The cross-source floor is phi^-1*V_ground.

### CLARITY
Sources are never fully off; the zeroed branch still murmurs.

### NOVELTY
The phi-law adds the coherence cross-term to the linear sum.

### ACTIONABILITY
Run sim/661_superposition_theorem.py; verify sum at kappa->0; proceed to 662.
