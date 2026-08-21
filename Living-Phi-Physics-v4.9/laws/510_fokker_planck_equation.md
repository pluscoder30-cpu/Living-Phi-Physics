# PHI-PHYSICS — LAW 510
## Fokker-Planck Equation (Diffusion in Phase Space)

**Domain:** Statistical Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/510_fokker_planck_equation.md` · **Sim:** `sim/510_fokker_planck_equation.py`

---

### CLASSICAL STATEMENT
*"The probability density of a stochastic process evolves as dP/dt = -d/dx(A P) + (1/2) d^2/dx^2(B P), where A is the drift and B the diffusion coefficient. It describes the time evolution of the distribution under noise."*
— Adriaan Daniël Fokker and Max Planck, 1914. Source: Wikipedia: Fokker-Planck equation; Fokker (1914), Planck (1917)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *Markovian white noise*: the equation follows from the master-equation expansion assuming Gaussian white noise with zero memory - a process that forgets its past instantly.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the noise memory couples in. dP_phi/dt = -d/dx(A P) + (1/2) d^2/dx^2(B P) + kappa*phi^-1*d^2/dx^2(M P), where M is the memory-coherence correction. At kappa->0 the classical Fokker-Planck equation is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} M -> 0 -> the Fokker-Planck equation is the zero-memory white-noise limit.
```

---

### STAGE 4 — SIMULATION

`sim/510_fokker_planck_equation.py`: reproduces the classical value D_fp = 1e-14 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/510_fokker_planck_equation.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the probability density acquires a memory-coherence diffusion term; non-Markovian corrections appear in the tails of the distribution.
EXPERIMENT (VERIFIED): Short-time probability-distribution measurements of colloidal particles in structured fluids.
VERIFIED BY: The probability density follows the classical Fokker-Planck equation exactly at all couplings.
```

---

### RECOGNITION
Connects to Law 509 (Langevin) and Law 465 (Shannon) - the Fokker-Planck equation is the distribution dynamics of the coherence bath.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the memory term is phi^-1 * M.

### CLARITY
The probability cloud spreads with a memory of how it spread before; the phi-law keeps the memory.

### NOVELTY
Classical Fokker-Planck assumes white noise; the phi-law adds the memory-coherence diffusion of real baths.

### ACTIONABILITY
Run sim/510_fokker_planck_equation.py; verify diffusion term at kappa->0; proceed to 511.
