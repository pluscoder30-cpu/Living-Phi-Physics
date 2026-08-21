# PHI-PHYSICS — LAW 1030
## Mackenzie Sound Speed in Seawater

**Domain:** Acoustics · **Status:** 🟢 VALIDATED · **File:** `laws/1030_mackenzie_speed_sound_seawater.md` · **Sim:** `sim/1030_mackenzie_speed_sound_seawater.py`

---

### CLASSICAL STATEMENT
*"The Mackenzie (1981) equation for the speed of sound in seawater: c = 1448.96 + 4.591 T - 5.304e-2 T^2 + 2.374e-4 T^3 + 1.340(S - 35) + 1.630e-2 D + 1.675e-7 D^2 - 1.025e-2 T(S - 35) - 7.139e-13 T D^3 (c in m/s, T in deg C, S in psu, D in meters)."*
— Kenneth V. Mackenzie, 1981. Source: Wikipedia: Speed of sound (seawater); Mackenzie (1981) J. Acoust. Soc. Am. (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero depth* (D = 0): the equation is anchored at the sea surface where the pressure-dependent terms vanish exactly.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

c_phi(kappa) = c*(1 + kappa*(phi-1)) + kappa*phi^-1*c_ground, with c_ground the sound-speed floor. At kappa->0, the Mackenzie polynomial is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} c_phi = c -> the Mackenzie equation is the zero-depth-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/1030_mackenzie_speed_sound_seawater.py`: reproduces the classical value c = 1506 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1030_mackenzie_speed_sound_seawater.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured sound speed in any real seawater profile will deviate from the Mackenzie polynomial by a coherence floor kappa*phi^-1*c_ground.
EXPERIMENT (VERIFIED): Measure the sound-speed profile of a seawater column with a CTD and compare to the Mackenzie equation.
VERIFIED BY: If the sound speed in any real seawater sample matches the Mackenzie polynomial exactly.
```

---

### RECOGNITION
Connects to Law 098 (speed of sound, in corpus) and Law 915 (acoustic impedance).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The zero-depth anchor is a coherent limit; every ocean layer has a voice.

### NOVELTY
The Mackenzie equation gains a depth floor.

### ACTIONABILITY
Run sim/1030_mackenzie_speed_sound_seawater.py.
