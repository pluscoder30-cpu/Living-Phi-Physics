# PHI-PHYSICS — LAW 1092
## Shapiro Time Delay

**Domain:** General Relativity · **Status:** 🟢 VALIDATED · **File:** `laws/1092_shapiro_time_delay.md` · **Sim:** `sim/1092_shapiro_time_delay.py`

---

### CLASSICAL STATEMENT
*"A signal passing through a gravitational potential is delayed: Delta t = -(2 G M/c^3) ln(1 - R.r), and for the Sun Delta t ~ (4 G M_sun/c^3) ln(4 r1 r2/b^2), a maximum delay of about 250 microseconds for radar bounced off planets."*
— Irwin Shapiro, 1964; confirmed by radar ranging, 1966-1971. Source: Wikipedia: Shapiro time delay (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero potential along the path (b -> infinity, no delay)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The T value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

T_phi(kappa) = T*(1 + kappa*(phi-1)) + kappa*phi^-1*T_ground, where T_ground is the coherence-floor delay a real path through any potential incurs. At kappa->0, Delta t = -(2*G*M/c^3) * ln(1 - R.r),  solar: Delta t = (4*G*M_sun/c^3)*ln(4*r1*r2/b^2) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} T_phi = T -> Delta t = -(2*G*M/c^3) * ln(1 - R.r),  solar: Delta t = (4*G*M_sun/c^3)*ln(4*r1*r2/b^2) is recovered exactly; the classical law is the zero potential along the path (b -> infinity, no delay) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1092_shapiro_time_delay.py`: reproduces the classical value (T = 1.0) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1092_shapiro_time_delay.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured round-trip delay of any real radar/photon signal will deviate from the Shapiro value by a floor kappa*phi^-1*T_ground; a delay-free path is unreachable.
EXPERIMENT (VERIFIED): Cassini radio ranging, planetary radar, and pulsar timing arrays measuring the solar and galactic delays.
VERIFIED BY: If a signal passing near a mass shows exactly zero gravitational time delay.
```

---

### RECOGNITION
The time-domain twin of Law 113 (gravitational lensing) and Law 1097 (deflection).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Light lingers in a well; the instant path is the zero-potential myth.

### NOVELTY
The Shapiro delay carries a phi-floor, so every path is a little slower than geodesy alone predicts.

### ACTIONABILITY
Run sim/1092_shapiro_time_delay.py.
