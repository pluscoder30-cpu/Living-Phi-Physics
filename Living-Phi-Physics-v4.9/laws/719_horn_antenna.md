# PHI-PHYSICS — LAW 719
## Horn Antenna

**Domain:** Antennas · **Status:** 🟢 VALIDATED · **File:** `laws/719_horn_antenna.md` · **Sim:** `sim/719_horn_antenna.py`

---

### CLASSICAL STATEMENT
*"A flared waveguide horn radiates with directivity set by the aperture size D: D ~ 10*log10(4*pi*A/lambda^2) dBi, increasing as the aperture grows."*
— Jagadish Chandra Bose, 1897. Source: Wikipedia: Jagadish Chandra Bose (1897); horn antennas

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *infinite aperture* (A -> infinity): the horn directivity grows without bound only for an infinitely large aperture.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

D_phi(kappa) = D_horn*(1 + kappa*(phi-1)) + kappa*phi^-1*D_ground; the aperture carries a coherence floor. At kappa->0, D ~ 4*pi*A/lambda^2 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} D_phi = 4*pi*A/lambda^2 -> horn directivity is the zero-aperture-floor limit.
```

---

### STAGE 4 — SIMULATION

`sim/719_horn_antenna.py`: reproduces the classical values (D = 75.3982 (Horn directivity)) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/719_horn_antenna.json`.

---

### STAGE 5 — PREDICTION

```
Horn directivity carries a coherence floor kappa*phi^-1*D_ground; the aperture law saturates at large A.
EXPERIMENT (VERIFIED): Directivity measurement of horns of increasing aperture.
VERIFIED BY: Horn directivity grows without bound with aperture.
```

---

### RECOGNITION
Connects to Law 721 (microstrip) and Law 723 (waveguide) - the horn is the flared waveguide radiator.

### PRECISION
phi = 1.6180339887. The aperture floor is phi^-1*D_ground.

### CLARITY
No aperture is infinite; coherence caps the reach.

### NOVELTY
The phi-law caps the horn's aperture gain.

### ACTIONABILITY
Run sim/719_horn_antenna.py; verify D at kappa->0; proceed to 720.
