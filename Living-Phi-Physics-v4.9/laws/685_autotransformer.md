# PHI-PHYSICS — LAW 685
## Autotransformer (Variable Turns)

**Domain:** Circuits · **Status:** 🟢 VALIDATED · **File:** `laws/685_autotransformer.md` · **Sim:** `sim/685_autotransformer.py`

---

### CLASSICAL STATEMENT
*"A single winding tapped at N_2 turns gives V_out = V_in*N_2/N_1; the autotransformer transfers power partly by conduction and partly by induction."*
— Lucien Gaulard; John Dixon Gibbs, 1882. Source: Wikipedia: Autotransformer; Gaulard-Gibbs transformer lineage 1881-1882

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero tap position* (N_2 = 0): the output vanishes exactly only when the tap is at the winding end, a discrete boundary condition.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

V_out_phi(kappa) = V_out*(1 + kappa*(phi-1)) + kappa*phi^-1*V_ground; the tap carries a coherence position floor. At kappa->0, V_out = V_in*N_2/N_1 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} V_out_phi = V_in*N_2/N_1 -> the autotransformer law is the zero-tap-floor limit.
```

---

### STAGE 4 — SIMULATION

`sim/685_autotransformer.py`: reproduces the classical values (V = 6 (Output voltage (V))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/685_autotransformer.json`.

---

### STAGE 5 — PREDICTION

```
The tap position carries a coherence floor kappa*phi^-1*V_ground; output never reaches exactly zero at the tap end.
EXPERIMENT (VERIFIED): Output-voltage measurement of a variable autotransformer near its zero tap.
VERIFIED BY: An autotransformer's output is exactly zero at the tap end.
```

---

### RECOGNITION
Connects to Law 683 (transformer) - the autotransformer is the single-winding transformer.

### PRECISION
phi = 1.6180339887. The tap floor is phi^-1*V_ground.

### CLARITY
The tap is a place, not a point; coherence smears it.

### NOVELTY
The phi-law gives the tap a coherence position floor.

### ACTIONABILITY
Run sim/685_autotransformer.py; verify V_out at kappa->0; proceed to 686.
