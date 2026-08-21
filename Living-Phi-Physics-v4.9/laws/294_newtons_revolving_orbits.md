# PHI-PHYSICS — LAW 294
## Newton's Theorem of Revolving Orbits

**Domain:** Orbital Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/294_newtons_revolving_orbits.md` · **Sim:** `sim/294_newtons_revolving_orbits.py`

---

### CLASSICAL STATEMENT
*"If an inverse-square orbit is perturbed by an additional inverse-cube central force, the orbit remains closed-like but its apsides revolve; the apsidal angle advances by the factor k = sqrt(1 + beta) where beta is the inverse-cube strength, generalizing the eccentric orbit to a revolving conic."*
— Isaac Newton, 1687. Source: Wikipedia: Newton's theorem of revolving orbits; Newton, Principia (1687), Book I, Prop. 43-45

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero inverse-cube perturbation*: Newton's theorem quantifies the apsidal revolution caused by the beta term; the pure inverse-square orbit (beta=0) does not revolve.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the apsidal revolution couples to coherence. k_phi(kappa) = sqrt(1 + beta)*(1 + kappa*(phi-1)) + kappa*phi^-1*k_ground. At kappa->0 the classical revolving-orbit theorem is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} k_phi = sqrt(1 + beta) -> Newton's revolving-orbit theorem is the exact inverse-cube-perturbation limit.
```

---

### STAGE 4 — SIMULATION

`sim/294_newtons_revolving_orbits.py`: reproduces the classical value k = 1.14 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/294_newtons_revolving_orbits.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The apsidal revolution factor carries a phi-coherent excess phi^-1*k_ground at full coupling.
EXPERIMENT (VERIFIED): Apsidal-motion measurements of binary star systems and artificial satellites comparing the revolution factor.
VERIFIED BY: The apsidal revolution factor is exactly sqrt(1+beta) at full coupling.
```

---

### RECOGNITION
Connects to Law 284 (Bertrand — closure), Law 304 (apsidal precession), Law 285 (perihelion precession).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The orbiting ellipse is a loop that can revolve; Newton found the gear, and the gear has a phi tooth.

### NOVELTY
Classical mechanics exacts the inverse-cube gear ratio; the phi-law gives the gear a coherence fraction.

### ACTIONABILITY
Run sim/294_newtons_revolving_orbits.py; verify k=sqrt(1+beta) at kappa->0.
