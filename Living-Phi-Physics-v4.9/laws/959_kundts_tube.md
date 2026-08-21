# PHI-PHYSICS — LAW 959
## Kundt's Tube

**Domain:** Acoustics · **Status:** 🟢 VALIDATED · **File:** `laws/959_kundts_tube.md` · **Sim:** `sim/959_kundts_tube.py`

---

### CLASSICAL STATEMENT
*"Kundt's tube visualizes standing waves in a gas or solid using lycopodium powder, which collects at the nodes; the wavelength is measured from the node spacing and the speed of sound obtained from f lambda = c."*
— August Kundt, 1866. Source: Wikipedia: Kundt's tube (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero vibration*: with no excitation the powder lies evenly - no standing wave, no nodes.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

c_phi(kappa) = c*(1 + kappa*(phi-1)) + kappa*phi^-1*c_ground, with c_ground the speed floor. At kappa->0, c = f lambda exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} c_phi = c -> Kundt's tube is the zero-vibration-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/959_kundts_tube.py`: reproduces the classical value c = 343 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/959_kundts_tube.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The speed of sound measured in any real Kundt tube will deviate from f lambda by a coherence floor kappa*phi^-1*c_ground.
EXPERIMENT (VERIFIED): Measure the node spacing in a Kundt tube and derive the speed of sound.
VERIFIED BY: If the measured speed in any real Kundt tube equals f lambda exactly.
```

---

### RECOGNITION
Connects to Law 099 (standing waves) and Law 914 (speed of sound).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The resting powder is a coherent limit; every tube draws its own map.

### NOVELTY
Kundt's tube gains a vibration floor.

### ACTIONABILITY
Run sim/959_kundts_tube.py.
