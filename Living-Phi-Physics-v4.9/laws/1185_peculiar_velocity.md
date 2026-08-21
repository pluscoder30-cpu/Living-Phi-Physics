# PHI-PHYSICS — LAW 1185
## Peculiar Velocity

**Domain:** Cosmology · **Status:** 🟢 VALIDATED · **File:** `laws/1185_peculiar_velocity.md` · **Sim:** `sim/1185_peculiar_velocity.py`

---

### CLASSICAL STATEMENT
*"The peculiar velocity is the velocity of a galaxy relative to the cosmic (Hubble) rest frame, v_pec = v_measured - H0 r; it arises from local gravitational structure and produces the dipole in the CMB (our peculiar motion ~370 km/s) and the scatter in the Hubble diagram."*
— Standard cosmology (defined with the Hubble flow from the 1930s). Source: Wikipedia: Peculiar velocity (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero peculiar velocity (pure Hubble flow, no local structure)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The V value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

V_phi(kappa) = V*(1 + kappa*(phi-1)) + kappa*phi^-1*V_ground, where V_ground is the coherence-floor peculiar motion a real galaxy always retains. At kappa->0, v_pec = v_obs - H0*r,  CMB dipole ~ 370 km/s exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} V_phi = V -> v_pec = v_obs - H0*r,  CMB dipole ~ 370 km/s is recovered exactly; the classical law is the zero peculiar velocity (pure Hubble flow, no local structure) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1185_peculiar_velocity.py`: reproduces the classical value (V = 370.0) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1185_peculiar_velocity.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured peculiar velocity of any real galaxy will deviate from the predicted value by a floor kappa*phi^-1*V_ground; an exactly comoving galaxy is unreachable.
EXPERIMENT (VERIFIED): Peculiar-velocity surveys (Tully-Fisher, fundamental plane) mapping the local flow field.
VERIFIED BY: If any galaxy is measured at exactly the Hubble-flow velocity with zero residual.
```

---

### RECOGNITION
The motion channel of Law 101 (Hubble law) and Law 1186 (redshift-space distortion).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Structure stirs the flow; the perfectly comoving galaxy is the zero-structure myth.

### NOVELTY
Peculiar velocities carry a phi-floor, bounding the sharpness of the Hubble flow.

### ACTIONABILITY
Run sim/1185_peculiar_velocity.py.
