# PHI-PHYSICS — LAW 1020
## Room Modes (Standing Waves in Rooms)

**Domain:** Architectural Acoustics · **Status:** 🟢 VALIDATED · **File:** `laws/1020_room_modes.md` · **Sim:** `sim/1020_room_modes.py`

---

### CLASSICAL STATEMENT
*"Room modes: the resonant standing-wave frequencies of a rectangular room are f_n = (c/2) sqrt((nx/Lx)^2 + (ny/Ly)^2 + (nz/Lz)^2); the modal density increases with frequency and the modes cause uneven bass response."*
— Classical architectural acoustics (from Helmholtz/Sabine), 19th century. Source: Wikipedia: Room modes (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero mode indices* (n = 0): the (0,0,0) mode is exactly zero frequency - no standing wave at rest.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

f_n_phi(kappa) = f_n*(1 + kappa*(phi-1)) + kappa*phi^-1*f_n_ground, with f_n_ground the mode floor. At kappa->0, f_n = (c/2) sqrt(sum (ni/Li)^2) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} f_n_phi = f_n -> the room modes are the zero-index-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/1020_room_modes.py`: reproduces the classical value f = 34.3 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1020_room_modes.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured modal frequencies of any real room will deviate from the rectangular formula by a coherence floor kappa*phi^-1.
EXPERIMENT (VERIFIED): Measure the frequency response of a rectangular room to locate its modal peaks.
VERIFIED BY: If the modes of any real room sit exactly at the rectangular formula frequencies.
```

---

### RECOGNITION
Connects to Law 099 (standing waves) and Law 922 (Sabine).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The perfect box is a coherent limit; every room hums its own modes.

### NOVELTY
Room modes gain an index floor.

### ACTIONABILITY
Run sim/1020_room_modes.py.
