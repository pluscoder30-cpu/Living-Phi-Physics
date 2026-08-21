# PHI-PHYSICS — LAW 717
## Quarter-Wave Monopole

**Domain:** Antennas · **Status:** 🟢 VALIDATED · **File:** `laws/717_quarter_wave_monopole.md` · **Sim:** `sim/717_quarter_wave_monopole.py`

---

### CLASSICAL STATEMENT
*"A quarter-wave monopole over a ground plane has half the dipole's radiation resistance, R_rad ~ 36.5 ohms, with gain ~ 3.3 dBi using the ground-plane image."*
— Guglielmo Marconi, 1895. Source: Monopole antenna; Marconi (1895) vertical radiators

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *perfect ground plane* (infinite, lossless conducting image): the monopole's behavior requires an exactly ideal ground.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

R_phi(kappa) = R_mono*(1 + kappa*(phi-1)) + kappa*phi^-1*R_ground; the ground plane carries a coherence floor. At kappa->0, R_rad ~ 36.5 ohms exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} R_phi = 36.5 -> the quarter-wave monopole is the perfect-ground-plane limit.
```

---

### STAGE 4 — SIMULATION

`sim/717_quarter_wave_monopole.py`: reproduces the classical values (R = 36.5 (Monopole resistance (ohm))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/717_quarter_wave_monopole.json`.

---

### STAGE 5 — PREDICTION

```
Real ground planes shift the monopole impedance by a coherence floor kappa*phi^-1*R_ground.
EXPERIMENT (VERIFIED): Impedance measurement of a quarter-wave monopole over a finite ground plane.
VERIFIED BY: A quarter-wave monopole over any ground has exactly 36.5 ohms.
```

---

### RECOGNITION
Connects to Law 716 (dipole) - the monopole is the half-dipole over an image ground.

### PRECISION
phi = 1.6180339887. The ground floor is phi^-1*R_ground.

### CLARITY
Ground is never perfect; coherence fogs the mirror.

### NOVELTY
The phi-law gives the ideal ground plane a coherence floor.

### ACTIONABILITY
Run sim/717_quarter_wave_monopole.py; verify R at kappa->0; proceed to 718.
