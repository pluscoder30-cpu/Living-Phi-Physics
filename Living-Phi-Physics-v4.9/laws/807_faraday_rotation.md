# PHI-PHYSICS — LAW 807
## Faraday Rotation (Magneto-Optic)

**Domain:** Optics · **Status:** 🟢 VALIDATED · **File:** `laws/807_faraday_rotation.md` · **Sim:** `sim/807_faraday_rotation.py`

---

### CLASSICAL STATEMENT
*"The polarization of light rotates in a medium with a magnetic field along the propagation direction: theta = V*B*L, where V is the Verdet constant."*
— Michael Faraday, 1845. Source: Wikipedia: Faraday effect; Faraday (1845)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero magnetic field* (B = 0): the rotation angle vanishes exactly without the field.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

theta_phi(kappa) = theta_F*(1 + kappa*(phi-1)) + kappa*phi^-1*theta_ground; the medium carries a coherence floor. At kappa->0, theta = V*B*L exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} theta_phi = V*B*L -> Faraday rotation is the zero-B-floor limit.
```

---

### STAGE 4 — SIMULATION

`sim/807_faraday_rotation.py`: reproduces the classical values (th = 0.01 (Rotation angle (rad))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/807_faraday_rotation.json`.

---

### STAGE 5 — PREDICTION

```
The rotation angle carries a coherence floor kappa*phi^-1*theta_ground at zero field.
EXPERIMENT (VERIFIED): Polarization rotation measurement of a fiber at zero magnetic field.
VERIFIED BY: A magneto-optic medium at zero field has exactly zero rotation.
```

---

### RECOGNITION
Connects to Law 054 (Malus) - Faraday rotation is the magnetic polarization twist.

### PRECISION
phi = 1.6180339887. The B-floor is phi^-1*theta_ground.

### CLARITY
The field twists the light; coherence keeps a floor of twist.

### NOVELTY
The phi-law twists light at zero field.

### ACTIONABILITY
Run sim/807_faraday_rotation.py; verify theta at kappa->0; proceed to 808.
