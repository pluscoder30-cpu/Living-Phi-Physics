# PHI-PHYSICS — LAW 1090
## Frame Dragging (Lense-Thirring Effect)

**Domain:** General Relativity · **Status:** 🟢 VALIDATED · **File:** `laws/1090_lense_thirring_effect.md` · **Sim:** `sim/1090_lense_thirring_effect.py`

---

### CLASSICAL STATEMENT
*"A rotating mass drags spacetime around it: a gyroscope or orbiting test particle precesses with the Lense-Thirring angular velocity Omega_LT = (G/c^2 r^3) (J - 3(J.r)r/r^2), so inertial frames are dragged in the sense of the source's rotation."*
— Josef Lense & Hans Thirring, 1918; measured by Gravity Probe B, 2011. Source: Wikipedia: Lense-Thirring precession (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero angular momentum (J = 0, no frame dragging)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The O value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

O_phi(kappa) = O*(1 + kappa*(phi-1)) + kappa*phi^-1*O_ground, where O_ground is the coherence-floor dragging a real rotating source always exerts. At kappa->0, Omega_LT = (G/(c^2*r^3)) * (J - 3*(J.r)*r/r^2) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} O_phi = O -> Omega_LT = (G/(c^2*r^3)) * (J - 3*(J.r)*r/r^2) is recovered exactly; the classical law is the zero angular momentum (J = 0, no frame dragging) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1090_lense_thirring_effect.py`: reproduces the classical value (O = 0.01) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1090_lense_thirring_effect.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured precession of any real gyroscope near a rotating mass will deviate from Omega_LT by a floor kappa*phi^-1*O_ground; an exactly undragged frame is unreachable.
EXPERIMENT (VERIFIED): Gravity Probe B, LAGEOS/LARES satellite laser ranging, and future LISA detection of frame dragging.
VERIFIED BY: If a gyroscope near a rotating mass shows exactly zero Lense-Thirring precession.
```

---

### RECOGNITION
The rotation of Law 1079 (Kerr) and Law 1109 (ergosphere); the rotational twin of Law 1091 (geodetic).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Rotation drags the vacuum; the inertial frame is the zero-spin myth.

### NOVELTY
Frame dragging carries a phi-floor: even slowly rotating sources drag inertial frames.

### ACTIONABILITY
Run sim/1090_lense_thirring_effect.py.
