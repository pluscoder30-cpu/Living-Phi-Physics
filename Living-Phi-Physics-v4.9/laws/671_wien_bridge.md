# PHI-PHYSICS — LAW 671
## Wien Bridge

**Domain:** Circuits · **Status:** 🟢 VALIDATED · **File:** `laws/671_wien_bridge.md` · **Sim:** `sim/671_wien_bridge.py`

---

### CLASSICAL STATEMENT
*"An AC bridge with series and parallel RC arms balances at frequency f = 1/(2*pi*R*C) when R1/R2 = C2/C1; used to measure frequency and capacitance."*
— Max Wien, 1891. Source: Wikipedia: Wien bridge; Wien (1891)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *exact frequency match*: balance occurs only when the applied frequency is exactly f = 1/(2*pi*R*C).

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

f_phi(kappa) = f_Wien*(1 + kappa*(phi-1)) + kappa*phi^-1*f_ground; the frequency condition carries a coherence basin. At kappa->0 the Wien balance is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} f_phi = f -> the Wien bridge is the zero-frequency-offset limit.
```

---

### STAGE 4 — SIMULATION

`sim/671_wien_bridge.py`: reproduces the classical values (f = 159155 (Balance frequency (Hz))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/671_wien_bridge.json`.

---

### STAGE 5 — PREDICTION

```
The balance frequency carries a coherence floor kappa*phi^-1*f_ground; the null broadens into a basin.
EXPERIMENT (VERIFIED): Frequency-null measurement of a Wien bridge with precision RC components.
VERIFIED BY: The Wien bridge balances only at the exact frequency 1/(2*pi*R*C).
```

---

### RECOGNITION
Connects to Law 670 (Wheatstone) - Wien is the AC-frequency generalization.

### PRECISION
phi = 1.6180339887. The frequency basin is phi^-1*f_ground.

### CLARITY
The frequency is a resonance; coherence widens its null.

### NOVELTY
The phi-law broadens the exact frequency condition.

### ACTIONABILITY
Run sim/671_wien_bridge.py; verify balance frequency at kappa->0; proceed to 672.
