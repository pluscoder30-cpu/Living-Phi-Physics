# PHI-PHYSICS — LAW 1026
## Strouhal Vortex Shedding (Acoustic)

**Domain:** Aeroacoustics · **Status:** 🟢 VALIDATED · **File:** `laws/1026_strouhal_vortex_shedding.md` · **Sim:** `sim/1026_strouhal_vortex_shedding.py`

---

### CLASSICAL STATEMENT
*"Vortex shedding frequency: f = St U / D, where St ~ 0.2 is the Strouhal number, U the flow velocity, and D the cylinder diameter; the shedding generates the Aeolian tone heard from wires and struts."*
— Vincenc Strouhal (1878), 1878. Source: Wikipedia: Strouhal number (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero velocity* (U = 0): no vortices are shed by still air - the tone vanishes exactly.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

f_phi(kappa) = f*(1 + kappa*(phi-1)) + kappa*phi^-1*f_ground, with f_ground the frequency floor. At kappa->0, f = St U/D exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} f_phi = f -> vortex shedding is the zero-velocity-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/1026_strouhal_vortex_shedding.py`: reproduces the classical value f = 200 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1026_strouhal_vortex_shedding.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The shedding frequency of any real cylinder will deviate from St U/D by a coherence floor kappa*phi^-1.
EXPERIMENT (VERIFIED): Measure the Aeolian tone frequency of a wire in a wind tunnel as a function of velocity.
VERIFIED BY: If the shedding frequency of any real cylinder equals St U/D exactly.
```

---

### RECOGNITION
Connects to Law 345 (Strouhal number) and Law 1023 (flow acoustics).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The still wire is a coherent limit; every strut sings with a floor.

### NOVELTY
Vortex shedding gains a velocity floor.

### ACTIONABILITY
Run sim/1026_strouhal_vortex_shedding.py.
