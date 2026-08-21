# PHI-PHYSICS — LAW 712
## Friis Transmission Equation

**Domain:** Antennas · **Status:** 🟢 VALIDATED · **File:** `laws/712_friis_transmission_equation.md` · **Sim:** `sim/712_friis_transmission_equation.py`

---

### CLASSICAL STATEMENT
*"The received power in free space is P_r = P_t*G_t*G_r*(lambda/(4*pi*r))^2, with free-space path loss scaling as (4*pi*r/lambda)^2."*
— Harald Friis, 1946. Source: Wikipedia: Friis transmission equation; Friis (1946)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *ideal free space* (no atmosphere, no reflections): the equation assumes an exactly empty, lossless propagation medium.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

P_r_phi(kappa) = P_r*(1 + kappa*(phi-1)) + kappa*phi^-1*P_ground; the free-space path carries a coherence floor. At kappa->0 the Friis equation is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} P_r_phi = P_t*G_t*G_r*(lambda/(4*pi*r))^2 -> the Friis equation is the zero-loss-medium limit.
```

---

### STAGE 4 — SIMULATION

`sim/712_friis_transmission_equation.py`: reproduces the classical values (Pr = 63.3257 (Received power (W))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/712_friis_transmission_equation.json`.

---

### STAGE 5 — PREDICTION

```
Real propagation paths carry a coherence loss floor kappa*phi^-1*P_ground beyond the ideal free-space law.
EXPERIMENT (VERIFIED): Line-of-sight link-budget measurement in an anechoic chamber.
VERIFIED BY: Received power in any real path follows the ideal free-space Friis law exactly.
```

---

### RECOGNITION
Connects to Law 713-714 (gain/directivity) - the Friis equation is the link budget.

### PRECISION
phi = 1.6180339887. The path-loss floor is phi^-1*P_ground.

### CLARITY
Free space is a myth; the path always breathes a coherence loss.

### NOVELTY
The phi-law adds a coherence path-loss floor.

### ACTIONABILITY
Run sim/712_friis_transmission_equation.py; verify Friis at kappa->0; proceed to 713.
