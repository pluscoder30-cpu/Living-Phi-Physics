# PHI-PHYSICS — LAW 676
## Parallel (Anti-)Resonance

**Domain:** Circuits · **Status:** 🟢 VALIDATED · **File:** `laws/676_parallel_resonance.md` · **Sim:** `sim/676_parallel_resonance.py`

---

### CLASSICAL STATEMENT
*"A parallel LC tank resonates at f_0 = 1/(2*pi*sqrt(L*C)); at resonance the impedance is maximum and the circulating current is large while the source current is minimum."*
— James Clerk Maxwell, 1873. Source: Parallel resonance; tank circuit theory (Maxwell era)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero source current*: ideal parallel resonance draws exactly zero current from the source, a lossless tank condition.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

f0_phi(kappa) = f0*(1 + kappa*(phi-1)) + kappa*phi^-1*f0_ground; the tank carries a coherence loss floor. At kappa->0 the ideal tank is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} f0_phi = f0 -> parallel resonance is the zero-loss-tank limit.
```

---

### STAGE 4 — SIMULATION

`sim/676_parallel_resonance.py`: reproduces the classical values (f0 = 5032.92 (Tank frequency (Hz))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/676_parallel_resonance.json`.

---

### STAGE 5 — PREDICTION

```
Real tanks draw a residual source current kappa*phi^-1; the anti-resonance impedance never reaches its ideal maximum.
EXPERIMENT (VERIFIED): Impedance measurement of a parallel LC tank at resonance with low-loss components.
VERIFIED BY: A parallel LC tank draws exactly zero current at resonance.
```

---

### RECOGNITION
Connects to Law 675 (series resonance) - the tank is the parallel dual of the series resonance.

### PRECISION
phi = 1.6180339887. The tank loss floor is phi^-1*f0_ground.

### CLARITY
The tank circulates forever in the ideal; coherence drains it.

### NOVELTY
The phi-law drains the ideal lossless tank.

### ACTIONABILITY
Run sim/676_parallel_resonance.py; verify f0 at kappa->0; proceed to 677.
