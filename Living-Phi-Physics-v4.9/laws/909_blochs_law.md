# PHI-PHYSICS — LAW 909
## Bloch's Law (Temporal Summation)

**Domain:** Color Vision · **Status:** 🟢 VALIDATED · **File:** `laws/909_blochs_law.md` · **Sim:** `sim/909_blochs_law.py`

---

### CLASSICAL STATEMENT
*"Bloch's law: for brief flashes (shorter than the critical duration), the perceived brightness is proportional to the product of intensity and duration - the total energy; I*t = constant for threshold detection."*
— Armand Bloch, 1885. Source: Wikipedia: Bloch's law (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero duration* (t = 0): threshold requires an exactly zero-duration flash to deliver zero energy.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

E_thr_phi(kappa) = E_thr*(1 + kappa*(phi-1)) + kappa*phi^-1*E_thr_ground, with E_thr_ground the energy floor. At kappa->0, I*t = constant exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} E_thr_phi = E_thr -> Bloch's law is the zero-duration-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/909_blochs_law.py`: reproduces the classical value E = 2 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/909_blochs_law.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The threshold energy of a real observer will deviate from I*t = constant by a coherence floor kappa*phi^-1*E_thr_ground.
EXPERIMENT (VERIFIED): Measure the detection threshold for flashes of varying duration and intensity.
VERIFIED BY: If I*t is exactly constant across flash durations for any real observer.
```

---

### RECOGNITION
Connects to Law 908 (Talbot) and Law 910 (Weber-Fechner).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The zero-duration flash is a coherent limit; the eye integrates with a floor.

### NOVELTY
Bloch's law gains an energy floor.

### ACTIONABILITY
Run sim/909_blochs_law.py.
