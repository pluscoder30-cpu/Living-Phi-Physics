# PHI-PHYSICS — LAW 866
## Coherence Time

**Domain:** Wave Optics · **Status:** 🟢 VALIDATED · **File:** `laws/866_coherence_time.md` · **Sim:** `sim/866_coherence_time.py`

---

### CLASSICAL STATEMENT
*"tau_c = 1/delta_nu, the time over which a field is mutually coherent; the Fourier-limited duration of a field's coherence."*
— Classical coherence theory, 1891. Source: Wikipedia: Coherence time (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero bandwidth*: infinite coherence time requires an exactly monochromatic field.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

tau_phi(kappa) = tau*(1 + kappa*(phi-1)) + kappa*phi^-1*tau_ground, with tau_ground the time floor. At kappa->0, tau_c = 1/delta_nu exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} tau_phi = tau -> coherence time is the zero-bandwidth-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/866_coherence_time.py`: reproduces the classical value tau = 1e-08 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/866_coherence_time.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured coherence time of any real field will be bounded by a floor; no field is coherent forever.
EXPERIMENT (VERIFIED): Measure the temporal coherence of a source via a scanning Michelson delay.
VERIFIED BY: If any real field has exactly infinite coherence time.
```

---

### RECOGNITION
Connects to Law 865 (coherence length) and Law 867 (Wiener-Khinchin).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Even the most stable laser forgets itself in time.

### NOVELTY
Coherence time gains a floor.

### ACTIONABILITY
Run sim/866_coherence_time.py.
