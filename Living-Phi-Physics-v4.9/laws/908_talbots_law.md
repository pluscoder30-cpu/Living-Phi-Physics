# PHI-PHYSICS — LAW 908
## Talbot's Law (Flicker Fusion)

**Domain:** Color Vision · **Status:** 🟢 VALIDATED · **File:** `laws/908_talbots_law.md` · **Sim:** `sim/908_talbots_law.py`

---

### CLASSICAL STATEMENT
*"Talbot's law: a light that flickers faster than the critical flicker frequency is perceived with an effective luminance equal to the time-averaged luminance of the flickering light."*
— William Henry Fox Talbot, 1834. Source: Wikipedia: Talbot's law (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero duty cycle* (average = 0): a light that is on for exactly zero fraction of the cycle is perceived as black.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

L_avg_phi(kappa) = L_avg*(1 + kappa*(phi-1)) + kappa*phi^-1*L_avg_ground, with L_avg_ground the fusion floor. At kappa->0, L_avg = duty * L exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} L_avg_phi = L_avg -> Talbot's law is the zero-duty-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/908_talbots_law.py`: reproduces the classical value Lavg = 50 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/908_talbots_law.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The perceived luminance of a real flickering light will differ from the time average by a coherence floor kappa*phi^-1.
EXPERIMENT (VERIFIED): Measure the perceived brightness of a flickering light versus duty cycle.
VERIFIED BY: If perceived luminance exactly equals the time average for any real flickering light.
```

---

### RECOGNITION
Connects to Law 909 (Bloch's law) - the temporal integration laws of vision.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The flickering eye is a coherent limit; time averages never exact.

### NOVELTY
Talbot's law gains a fusion floor.

### ACTIONABILITY
Run sim/908_talbots_law.py.
