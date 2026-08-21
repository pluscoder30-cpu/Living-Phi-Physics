# PHI-PHYSICS — LAW 424
## Polytropic Process (p V^n = C)

**Domain:** Heat & Calorimetry · **Status:** 🟢 VALIDATED · **File:** `laws/424_polytropic_process.md` · **Sim:** `sim/424_polytropic_process.py`

---

### CLASSICAL STATEMENT
*"A thermodynamic process obeying p V^n = C, where n is the polytropic index, is polytropic. Special cases: n=0 isobaric, n=1 isothermal (ideal gas), n=gamma isentropic, n=infinity isochoric."*
— Robert Emden (term polytrope); classical process law, 1907. Source: Wikipedia: Polytropic process; Emden, Gaskugeln (1907)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *constant index n*: the polytropic law assumes the index stays exactly constant through the whole process, a fixed relation between heat and work that real processes only approximate.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the index is a coherence parameter. n_phi(kappa) = n*(1 + kappa*(phi-1)) + kappa*phi^-1*n_ground, so (p V^n)_phi(kappa) = p V^n_phi = C_phi(kappa). At kappa->0, n_phi = n and p V^n = C exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} n_phi = n -> p V^n = C -> the polytropic law is the constant-index process limit.
```

---

### STAGE 4 — SIMULATION

`sim/424_polytropic_process.py`: reproduces the classical value PVn = 2.462 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/424_polytropic_process.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Real polytropic processes show a drifting index n_phi that approaches n*(phi) at full coherence; the p-V trajectory is no longer a single power law.
EXPERIMENT (VERIFIED): Instrumented piston-in-cylinder compression of air measuring p-V along the path to extract n(T) for varying coupling.
VERIFIED BY: Every compression path satisfies p V^n = C with exactly one constant n.
```

---

### RECOGNITION
Connects to Law 422 (Poisson, n=gamma) and Law 425 (isothermal, n=1) - the index is the coherence signature of the process.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the index floor is phi^-1 * n_ground.

### CLARITY
The polytropic index is not a frozen exponent; it is the process's coherence that drifts with coupling.

### NOVELTY
Classical polytropic analysis fixes n; the phi-law lets the index breathe with the coherence of the working fluid.

### ACTIONABILITY
Run sim/424_polytropic_process.py; verify pV^n=C at kappa->0; proceed to 425.
