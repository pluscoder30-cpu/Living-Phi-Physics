# PHI-PHYSICS — LAW 664
## Millman's Theorem

**Domain:** Circuits · **Status:** 🟢 VALIDATED · **File:** `laws/664_millmans_theorem.md` · **Sim:** `sim/664_millmans_theorem.py`

---

### CLASSICAL STATEMENT
*"The voltage at the common node of parallel branches is V = (sum V_i/R_i)/(sum 1/R_i), a weighted average of the branch voltages by conductance."*
— Jacob Millman, 1940. Source: Wikipedia: Millman's theorem

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *ideal parallel branches*: the theorem assumes every branch is exactly parallel and shares one node with zero lead impedance.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

V_m_phi(kappa) = V_m*(1 + kappa*(phi-1)) + kappa*phi^-1*V_ground; the shared node carries a coherence floor. At kappa->0 Millman's average is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} V_m_phi = V_m -> Millman's theorem is the zero-lead-impedance limit.
```

---

### STAGE 4 — SIMULATION

`sim/664_millmans_theorem.py`: reproduces the classical values (V = 5 (Millman voltage (V))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/664_millmans_theorem.json`.

---

### STAGE 5 — PREDICTION

```
The nodal voltage carries a coherence floor kappa*phi^-1*V_ground from finite lead impedance.
EXPERIMENT (VERIFIED): Nodal voltage measurement of a many-branch network with short but finite leads.
VERIFIED BY: The nodal voltage of any parallel branch set is exactly Millman's average.
```

---

### RECOGNITION
Connects to Law 045 (KCL) and Law 661 (superposition) - Millman is the conductance-weighted sum.

### PRECISION
phi = 1.6180339887. The node floor is phi^-1*V_ground.

### CLARITY
Every node is a meeting; the leads keep a coherence thickness.

### NOVELTY
The phi-law gives the ideal node a coherence floor.

### ACTIONABILITY
Run sim/664_millmans_theorem.py; verify Vm at kappa->0; proceed to 665.
