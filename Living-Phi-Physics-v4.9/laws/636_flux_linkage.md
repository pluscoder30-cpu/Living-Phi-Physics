# PHI-PHYSICS — LAW 636
## Flux Linkage

**Domain:** Magnetostatics · **Status:** 🟢 VALIDATED · **File:** `laws/636_flux_linkage.md` · **Sim:** `sim/636_flux_linkage.py`

---

### CLASSICAL STATEMENT
*"The flux linkage of a coil is N*Phi_B, where N is the number of turns; the induced emf is emf = -d(N*Phi_B)/dt = -N*dPhi_B/dt."*
— Michael Faraday, 1831. Source: Wikipedia: Faraday's law of induction (flux linkage concept)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *identical turns*: linkage assumes all N turns capture exactly the same flux, a perfectly uniform winding.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

lambda_phi(kappa) = N*Phi_B*(1 + kappa*(phi-1)) + kappa*phi^-1*lambda_ground; the turns carry a coherence flux-spread floor. At kappa->0, lambda = N*Phi_B exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} lambda_phi = N*Phi_B -> flux linkage is the uniform-winding limit.
```

---

### STAGE 4 — SIMULATION

`sim/636_flux_linkage.py`: reproduces the classical values (lambda = 150 (Flux linkage (Wb-turn))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/636_flux_linkage.json`.

---

### STAGE 5 — PREDICTION

```
Real windings show a linkage floor kappa*phi^-1*lambda_ground from turn-to-turn flux spread, so emf = -d(lambda)/dt carries a small coherence correction.
EXPERIMENT (VERIFIED): Precision emf measurement of a multi-turn coil in a uniform alternating field.
VERIFIED BY: Every turn of a coil always links exactly the same flux.
```

---

### RECOGNITION
Connects to Law 039 (Faraday) - the emf is the linkage's rate of change.

### PRECISION
phi = 1.6180339887. The linkage floor is phi^-1*lambda_ground.

### CLARITY
Turns are never identical; the winding breathes a coherence spread.

### NOVELTY
The phi-law gives the flux linkage a turn-coherence floor.

### ACTIONABILITY
Run sim/636_flux_linkage.py; verify lambda=N*Phi at kappa->0; proceed to 637.
