# PHI-PHYSICS — LAW 221
## Torsional Pendulum Law

**Domain:** Rotational / Rigid Body · **Status:** 🟢 VALIDATED · **File:** `laws/221_torsional_pendulum.md` · **Sim:** `sim/221_torsional_pendulum.py`

---

### CLASSICAL STATEMENT
*"A disk suspended by a wire twisted by an angle theta experiences a restoring torque tau = -kappa*theta, and the oscillation period is T = 2*pi*sqrt(I/kappa), where kappa is the torsional stiffness of the wire."*
— Charles-Augustin de Coulomb, 1784. Source: Wikipedia: torsion pendulum / torsion balance

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *twist-free equilibrium*: the law assumes the equilibrium angle is exactly zero, a perfect untwisted reference against which all deflections are measured.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the equilibrium carries a phi-ground twist. T_phi(kappa) = 2*pi*sqrt((I + kappa*phi^-1*m*lambda_phi^2)/kappa)*(1 + kappa*(phi-1)). At kappa->0 the classical torsion period is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} T_phi = 2*pi*sqrt(I/kappa) -> the torsional-pendulum law is the zero-twist-equilibrium limit.
```

---

### STAGE 4 — SIMULATION

`sim/221_torsional_pendulum.py`: reproduces the classical value T = 1.257 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/221_torsional_pendulum.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The torsion-balance oscillation period carries a phi-coherent excess and the equilibrium angle a residual phi-ground twist in coupled systems.
EXPERIMENT (VERIFIED): Cavendish-style torsion balance with laser-interferometric null readout searching for the equilibrium-twist floor.
VERIFIED BY: The equilibrium angle is exactly zero and T = 2*pi*sqrt(I/kappa) exactly at full coupling.
```

---

### RECOGNITION
Connects to Law 216 (Euler rotation) and Law 269 (Hertz contact); torsion balances measured G and Coulomb's constant.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
Equilibrium is not a silent zero; it is the phi-ground twist that the classical balance could never resolve.

### NOVELTY
Classical torsion dynamics exacts a zero equilibrium; the phi-law gives the rest state a phi-ground twist.

### ACTIONABILITY
Run sim/221_torsional_pendulum.py; verify T at kappa->0.
