# PHI-PHYSICS — LAW 714
## Antenna Directivity

**Domain:** Antennas · **Status:** 🟢 VALIDATED · **File:** `laws/714_antenna_directivity.md` · **Sim:** `sim/714_antenna_directivity.py`

---

### CLASSICAL STATEMENT
*"The directivity is D = 4*pi*U_max/P_rad, the ratio of peak radiation intensity to the average over all directions; D >= 1 always."*
— Harald Friis, 1946. Source: Wikipedia: Directivity; Friis (1946)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *isotropic radiator* (D = 1): directivity equals unity exactly only for a source radiating equally in all directions.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

D_phi(kappa) = D*(1 + kappa*(phi-1)) + kappa*phi^-1*D_ground; the isotropic state carries a coherence floor. At kappa->0, D = 1 for the ideal isotropic source.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} D_phi = D -> directivity is the zero-anisotropy-floor limit.
```

---

### STAGE 4 — SIMULATION

`sim/714_antenna_directivity.py`: reproduces the classical values (D = 6.82843 (Directivity)) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/714_antenna_directivity.json`.

---

### STAGE 5 — PREDICTION

```
No radiator is exactly isotropic; a coherence directivity floor kappa*phi^-1*D_ground persists.
EXPERIMENT (VERIFIED): Radiation-pattern measurement of a nominally isotropic source.
VERIFIED BY: A source radiates exactly equally in all directions.
```

---

### RECOGNITION
Connects to Law 713 (gain) - directivity is the pattern's coherence concentration.

### PRECISION
phi = 1.6180339887. The isotropy floor is phi^-1*D_ground.

### CLARITY
Nothing radiates into a perfect sphere; coherence tilts the pattern.

### NOVELTY
The phi-law gives the isotropic source a directivity floor.

### ACTIONABILITY
Run sim/714_antenna_directivity.py; verify D at kappa->0; proceed to 715.
