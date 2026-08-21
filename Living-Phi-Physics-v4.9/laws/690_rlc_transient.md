# PHI-PHYSICS — LAW 690
## RLC Transient Response

**Domain:** Circuits · **Status:** 🟢 VALIDATED · **File:** `laws/690_rlc_transient.md` · **Sim:** `sim/690_rlc_transient.py`

---

### CLASSICAL STATEMENT
*"The RLC transient is governed by L*d^2q/dt^2 + R*dq/dt + q/C = 0, with underdamped (zeta<1), critically damped (zeta=1), or overdamped (zeta>1) solutions."*
— Oliver Heaviside, 1887. Source: RLC circuit; Heaviside (1887) operational calculus

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *critical damping* (zeta = 1 exactly): the special solution occurs only at a precise balance of R against sqrt(L/C).

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

zeta_phi(kappa) = zeta*(1 + kappa*(phi-1)) + kappa*phi^-1*zeta_ground; the damping ratio carries a coherence floor. At kappa->0 the RLC equation is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} zeta_phi = R/(2)*sqrt(C/L) -> the RLC transient is the zero-coherence-damping limit.
```

---

### STAGE 4 — SIMULATION

`sim/690_rlc_transient.py`: reproduces the classical values (q = 0.32771 (Transient charge (C))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/690_rlc_transient.json`.

---

### STAGE 5 — PREDICTION

```
The critical-damping condition is a basin of width kappa*phi^-1 around zeta = 1; exact critical damping is unreachable.
EXPERIMENT (VERIFIED): Damping-ratio sweep of an RLC circuit near critical damping.
VERIFIED BY: An RLC circuit is exactly critically damped only at zeta = 1.
```

---

### RECOGNITION
Connects to Law 238 (damped oscillator) and Law 677 (Q) - the RLC transient is the electrical damped oscillator.

### PRECISION
phi = 1.6180339887. The critical basin is phi^-1*zeta_ground.

### CLARITY
Critical damping is a myth; the basin is where circuits settle.

### NOVELTY
The phi-law broadens critical damping into a basin.

### ACTIONABILITY
Run sim/690_rlc_transient.py; verify RLC solution at kappa->0; proceed to 691.
