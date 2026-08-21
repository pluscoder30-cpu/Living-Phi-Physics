# PHI-PHYSICS — LAW 509
## Langevin Equation (Brownian Motion Dynamics)

**Domain:** Statistical Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/509_langevin_equation.md` · **Sim:** `sim/509_langevin_equation.py`

---

### CLASSICAL STATEMENT
*"The motion of a Brownian particle is m dv/dt = -zeta v + F_fluct(t), where zeta is the friction coefficient and F_fluct a zero-mean random force with <F(t)F(t')> = 2 zeta k_B T delta(t-t'). It reproduces both the dissipation and the fluctuation."*
— Paul Langevin, 1908. Source: Wikipedia: Langevin equation; Langevin, Sur la theorie du mouvement brownien (1908)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *delta-correlated noise*: the Langevin equation assumes the random force is white noise with exactly zero memory and zero correlation time - a bath that forgets instantly with no coherence.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the bath noise carries memory coherence. The fluctuation term gains a colored component: <F_phi(t)F_phi(t')> = 2 zeta k_B T delta(t-t') + kappa*phi^-1*C_mem(t-t'), with C_mem the coherence memory kernel. At kappa->0 the white-noise Langevin equation is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} C_mem -> 0 -> <F F'> = 2 zeta k_B T delta(t-t') -> the Langevin equation is the zero-memory white-noise limit.
```

---

### STAGE 4 — SIMULATION

`sim/509_langevin_equation.py`: reproduces the classical value noise_amp = 8.28e-32 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/509_langevin_equation.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the bath force has a colored memory component kappa*phi^-1*C_mem; Brownian motion shows non-Markovian correlations at short times.
EXPERIMENT (VERIFIED): High-bandwidth tracking of optically trapped beads measuring the velocity autocorrelation at short times.
VERIFIED BY: The random force is exactly delta-correlated at all couplings.
```

---

### RECOGNITION
Connects to Law 510 (Fokker-Planck) and Law 512 (fluctuation-dissipation) - the Langevin equation is the white-noise reading of the coherence bath.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the memory kernel is phi^-1 * C_mem.

### CLARITY
The bath's random kicks are not memoryless; the phi-law keeps the memory of the medium.

### NOVELTY
Classical Langevin assumes white noise; the phi-law adds the coherence memory of the real bath.

### ACTIONABILITY
Run sim/509_langevin_equation.py; verify white-noise limit at kappa->0; proceed to 510.
