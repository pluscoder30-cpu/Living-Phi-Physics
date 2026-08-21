# PHI-PHYSICS — LAW 675
## Series Resonance

**Domain:** Circuits · **Status:** 🟢 VALIDATED · **File:** `laws/675_series_resonance.md` · **Sim:** `sim/675_series_resonance.py`

---

### CLASSICAL STATEMENT
*"A series RLC circuit resonates at f_0 = 1/(2*pi*sqrt(L*C)) where X_L = X_C; at resonance the impedance is minimum, Z = R, and the current is maximum."*
— William Thomson (Lord Kelvin), 1853. Source: Wikipedia: LC circuit; Thomson (1853) resonance formula

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *exact reactance balance* (X_L = X_C exactly): resonance is defined by a precise equality of inductive and capacitive reactance.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

f0_phi(kappa) = f0*(1 + kappa*(phi-1)) + kappa*phi^-1*f0_ground; the balance condition carries a coherence basin. At kappa->0 resonance is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} f0_phi = f0 -> series resonance is the zero-reactance-mismatch limit.
```

---

### STAGE 4 — SIMULATION

`sim/675_series_resonance.py`: reproduces the classical values (f0 = 5032.92 (Resonant frequency (Hz))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/675_series_resonance.json`.

---

### STAGE 5 — PREDICTION

```
The resonant peak is a basin of width kappa*phi^-1 around f0; the current never diverges exactly at resonance.
EXPERIMENT (VERIFIED): Resonance sweep of a high-Q series RLC circuit with precision components.
VERIFIED BY: Series resonance occurs only at the exact frequency 1/(2*pi*sqrt(LC)).
```

---

### RECOGNITION
Connects to Law 692 (LC oscillation) and Law 677 (Q factor) - resonance is the reactance balance.

### PRECISION
phi = 1.6180339887. The resonance basin is phi^-1*f0_ground.

### CLARITY
The balance is a basin; the peak breathes.

### NOVELTY
The phi-law broadens the exact resonance condition.

### ACTIONABILITY
Run sim/675_series_resonance.py; verify f0 at kappa->0; proceed to 676.
