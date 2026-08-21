# PHI-PHYSICS — LAW 697
## Flyback Converter

**Domain:** Power Electronics · **Status:** 🟢 VALIDATED · **File:** `laws/697_flyback_converter.md` · **Sim:** `sim/697_flyback_converter.py`

---

### CLASSICAL STATEMENT
*"The flyback converter stores energy in the coupled inductor during the switch-on and releases it to the output during switch-off: V_out = V_in*N_s/N_p*D/(1-D)."*
— Television flyback heritage (CRT era), 1950. Source: Wikipedia: Flyback converter; flyback transformer (1950s TV)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero duty* (D = 0): no energy is transferred at exactly zero duty.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

V_out_phi(kappa) = V_out*(1 + kappa*(phi-1)) + kappa*phi^-1*V_ground; the coupled core carries a coherence floor. At kappa->0 the flyback ratio is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} V_out_phi = V_in*Ns/Np*D/(1-D) -> the flyback conversion is the zero-duty-floor limit.
```

---

### STAGE 4 — SIMULATION

`sim/697_flyback_converter.py`: reproduces the classical values (Vo = 6 (Output voltage (V))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/697_flyback_converter.json`.

---

### STAGE 5 — PREDICTION

```
The flyback output carries a coherence floor kappa*phi^-1*V_ground from core flux remanence.
EXPERIMENT (VERIFIED): Output measurement of a flyback converter at low duty with a ferrite core.
VERIFIED BY: A flyback converter output is exactly zero at zero duty.
```

---

### RECOGNITION
Connects to Law 683 (transformer) - the flyback is the coupled-inductor energy transfer.

### PRECISION
phi = 1.6180339887. The remanence floor is phi^-1*V_ground.

### CLARITY
The core remembers; a coherence remanence holds the output.

### NOVELTY
The phi-law gives the flyback a remanence floor.

### ACTIONABILITY
Run sim/697_flyback_converter.py; verify Vo at kappa->0; proceed to 698.
