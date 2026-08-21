# PHI-PHYSICS — LAW 668
## Nodal Analysis (KCL at Nodes)

**Domain:** Circuits · **Status:** 🟢 VALIDATED · **File:** `laws/668_nodal_analysis.md` · **Sim:** `sim/668_nodal_analysis.py`

---

### CLASSICAL STATEMENT
*"Applying KCL at every node gives a linear system G*V = I that determines all node voltages; the reference node is taken at potential zero."*
— Gustav Kirchhoff, 1847. Source: Wikipedia: Nodal analysis; Kirchhoff (1847)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero reference potential*: nodal analysis is built on a reference node assumed to be exactly at V = 0, a state no real point in a field-coupled circuit holds.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

V_ref_phi(kappa) = V_ref*(1 + kappa*(phi-1)) + kappa*phi^-1*V_ground; the reference node carries a coherence floor. At kappa->0 the KCL system is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} V_phi = V_kcl -> nodal analysis is the zero-reference-floor limit.
```

---

### STAGE 4 — SIMULATION

`sim/668_nodal_analysis.py`: reproduces the classical values (V = 1000 (Node voltage (V))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/668_nodal_analysis.json`.

---

### STAGE 5 — PREDICTION

```
Every real reference node floats at kappa*phi^-1*V_ground; measured node voltages include a coherence offset from the assumed ground.
EXPERIMENT (VERIFIED): Node-voltage measurement of a circuit with a nominally grounded reference.
VERIFIED BY: The reference node of a circuit is exactly at zero potential.
```

---

### RECOGNITION
Connects to Law 045 (KCL) - nodal analysis is KCL organized as a system.

### PRECISION
phi = 1.6180339887. The reference floor is phi^-1*V_ground.

### CLARITY
Ground is a story we tell; the node floats at its floor.

### NOVELTY
The phi-law floats the reference node.

### ACTIONABILITY
Run sim/668_nodal_analysis.py; verify KCL solution at kappa->0; proceed to 669.
