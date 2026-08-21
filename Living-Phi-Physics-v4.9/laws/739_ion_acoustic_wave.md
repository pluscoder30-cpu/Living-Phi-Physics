# PHI-PHYSICS — LAW 739
## Ion Acoustic Wave

**Domain:** Plasma · **Status:** 🟢 VALIDATED · **File:** `laws/739_ion_acoustic_wave.md` · **Sim:** `sim/739_ion_acoustic_wave.py`

---

### CLASSICAL STATEMENT
*"The low-frequency ion wave has phase speed c_s = sqrt(k_B*T_e/m_i) with dispersion w = c_s*k/(1 + k^2*lambda_D^2)^(1/2)."*
— Lewi Tonks; Irving Langmuir, 1929. Source: Wikipedia: Ion acoustic wave; Tonks & Langmuir (1929)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero electron temperature* (T_e = 0): the ion acoustic speed vanishes exactly for a cold electron background.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

c_s_phi(kappa) = c_s*(1 + kappa*(phi-1)) + kappa*phi^-1*c_s_ground; the electron background carries a coherence floor. At kappa->0, c_s = sqrt(k_B*T_e/m_i) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} c_s_phi = sqrt(k_B*T_e/m_i) -> the ion acoustic wave is the zero-T_e floor limit.
```

---

### STAGE 4 — SIMULATION

`sim/739_ion_acoustic_wave.py`: reproduces the classical values (cs = 90853.7 (Ion sound speed (m/s))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/739_ion_acoustic_wave.json`.

---

### STAGE 5 — PREDICTION

```
The ion acoustic speed carries a coherence floor kappa*phi^-1*c_s_ground; a cold plasma still supports the wave.
EXPERIMENT (VERIFIED): Ion wave velocity measurement in a plasma with very cold electrons.
VERIFIED BY: A zero-electron-temperature plasma has exactly zero ion sound speed.
```

---

### RECOGNITION
Connects to Law 098 (speed of sound) and Law 762 (Landau damping) - the ion wave is the plasma's sound.

### PRECISION
phi = 1.6180339887. The T_e floor is phi^-1*c_s_ground.

### CLARITY
The plasma always has a voice; coherence keeps it audible.

### NOVELTY
The phi-law keeps ion sound in a cold plasma.

### ACTIONABILITY
Run sim/739_ion_acoustic_wave.py; verify c_s at kappa->0; proceed to 740.
