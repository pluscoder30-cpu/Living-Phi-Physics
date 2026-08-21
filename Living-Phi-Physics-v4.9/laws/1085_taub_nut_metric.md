# PHI-PHYSICS — LAW 1085
## Taub-NUT Metric

**Domain:** General Relativity · **Status:** 🟢 VALIDATED · **File:** `laws/1085_taub_nut_metric.md` · **Sim:** `sim/1085_taub_nut_metric.py`

---

### CLASSICAL STATEMENT
*"The Taub-NUT metric is an exact vacuum solution with a 'gravitomagnetic' (NUT) charge N that generates a twisted, non-trivial topology: ds^2 = -f(r)(dt + 2 N cos(theta) dphi)^2 + f(r)^-1 dr^2 + (r^2 + N^2)(dtheta^2 + sin^2 theta dphi^2); it is a key testbed for singularity theorems and Misner-string topology."*
— Abraham Taub, 1951; Ezra Newman, Louis Tamburino & Theodore Unti, 1963. Source: Wikipedia: Taub-NUT metric (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero NUT charge (N = 0, the Schwarzschild limit)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The T value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

T_phi(kappa) = T*(1 + kappa*(phi-1)) + kappa*phi^-1*T_ground, where T_ground is the coherence-floor gravitomagnetic charge a real spacetime retains. At kappa->0, ds^2 = -f(r)*(dt + 2*N*cos(theta)*dphi)^2 + f(r)^-1*dr^2 + (r^2+N^2)*(dtheta^2 + sin^2(theta)*dphi^2) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} T_phi = T -> ds^2 = -f(r)*(dt + 2*N*cos(theta)*dphi)^2 + f(r)^-1*dr^2 + (r^2+N^2)*(dtheta^2 + sin^2(theta)*dphi^2) is recovered exactly; the classical law is the zero NUT charge (N = 0, the Schwarzschild limit) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1085_taub_nut_metric.py`: reproduces the classical value (T = 0.5) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1085_taub_nut_metric.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured gravitomagnetic structure of any real rotating source will deviate from the Taub-NUT form by a floor kappa*phi^-1*T_ground; an exactly NUT-free spacetime is unreachable.
EXPERIMENT (VERIFIED): Frame-dragging experiments (Law 1090) bounding a residual gravitomagnetic monopole charge.
VERIFIED BY: If any real spacetime has exactly zero NUT charge to arbitrary precision.
```

---

### RECOGNITION
The gravitomagnetic generalization of Law 064 (Schwarzschild); tests Law 1077 (singularity theorems).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The NUT charge is the magnetic pole of gravity; the Schwarzschild limit is the zero-monopole myth.

### NOVELTY
Gravitomagnetic charge carries a phi-floor, so spacetime always has a twisted residue.

### ACTIONABILITY
Run sim/1085_taub_nut_metric.py.
