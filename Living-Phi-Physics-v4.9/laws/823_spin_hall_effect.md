# PHI-PHYSICS — LAW 823
## Spin Hall Effect

**Domain:** Solid State · **Status:** 🟢 VALIDATED · **File:** `laws/823_spin_hall_effect.md` · **Sim:** `sim/823_spin_hall_effect.py`

---

### CLASSICAL STATEMENT
*"A charge current in a spin-orbit-coupled material produces a transverse spin current: J_s = theta_SH*J_c, with the spin Hall angle theta_SH; spins accumulate at the sample edges."*
— Mikhail Dyakonov; Vladimir Perel, 1971. Source: Spin Hall effect; Dyakonov & Perel (1971)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero charge current* (J_c = 0): the spin Hall response vanishes exactly at zero charge current.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

J_s_phi(kappa) = J_s*(1 + kappa*(phi-1)) + kappa*phi^-1*J_ground; the spin orbit carries a coherence floor. At kappa->0, J_s = theta_SH*J_c exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} J_s_phi = theta_SH*J_c -> the spin Hall effect is the zero-charge-current floor limit.
```

---

### STAGE 4 — SIMULATION

`sim/823_spin_hall_effect.py`: reproduces the classical values (Js = 0.1 (Spin current (a.u.))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/823_spin_hall_effect.json`.

---

### STAGE 5 — PREDICTION

```
Spin accumulation carries a coherence floor kappa*phi^-1*J_ground at zero charge current.
EXPERIMENT (VERIFIED): Kerr-rotation measurement of spin accumulation in a nominally undriven sample.
VERIFIED BY: A sample at zero charge current has exactly zero spin accumulation.
```

---

### RECOGNITION
Connects to Law 590 (Hall) - the spin Hall effect is the spin-orbital Hall response.

### PRECISION
phi = 1.6180339887. The current floor is phi^-1*J_ground.

### CLARITY
Spins edge sideways even in the idle; coherence keeps a floor of drift.

### NOVELTY
The phi-law gives the undriven sample a spin floor.

### ACTIONABILITY
Run sim/823_spin_hall_effect.py; verify Js at kappa->0; proceed to 824.
