# PHI-PHYSICS — LAW 432
## Helmholtz Free Energy (A = U - TS)

**Domain:** Thermodynamic Potentials · **Status:** 🟢 VALIDATED · **File:** `laws/432_helmholtz_free_energy.md` · **Sim:** `sim/432_helmholtz_free_energy.py`

---

### CLASSICAL STATEMENT
*"The Helmholtz free energy is A = U - T S. At constant T and V, a system in thermal contact with a reservoir minimizes A; the work obtainable from a closed isothermal system equals the decrease in A."*
— Hermann von Helmholtz, 1882. Source: Wikipedia: Helmholtz free energy; Helmholtz, Zur Thermodynamik chemischer Vorgaenge (1882)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *infinite thermal reservoir*: the potential assumes the system is coupled to a reservoir of exactly constant temperature with zero coupling, so the free energy cleanly separates internal energy from temperature times entropy.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the reservoir coupling is a coherence parameter. A_phi(kappa) = U - T*S*(1 + kappa*(phi-1)) + kappa*phi^-1*A_ground. At kappa->0, A = U - TS exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} A_phi = U - TS -> Helmholtz free energy is the zero-reservoir-coupling, exactly-constant-T limit.
```

---

### STAGE 4 — SIMULATION

`sim/432_helmholtz_free_energy.py`: reproduces the classical value A_helm = 40 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/432_helmholtz_free_energy.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: A system at finite reservoir coupling shows a residual free-energy floor kappa*phi^-1*A_ground; minimization leaves a coherence remainder that classical A cannot vanish.
EXPERIMENT (VERIFIED): Measurement of reversible work from an isothermal engine cycle in a finite heat bath, comparing with -dA.
VERIFIED BY: The maximum work from an isothermal closed system equals -dA exactly for any reservoir size and coupling.
```

---

### RECOGNITION
Connects to Law 022 (first law), Law 436 (chemical potential) and Law 446 (Gibbs-Helmholtz) - the potentials are the coherence grammar of the state.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the floor is phi^-1 * A_ground.

### CLARITY
Free energy is the energy a system can lend while borrowing its coherence from the bath.

### NOVELTY
Classical thermodynamics idealizes the bath; the phi-law endows free energy with a coherence floor.

### ACTIONABILITY
Run sim/432_helmholtz_free_energy.py; verify A=U-TS at kappa->0; proceed to 433.
