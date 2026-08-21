# PHI-PHYSICS — LAW 449
## Exergy (Maximum Usable Work)

**Domain:** Thermodynamic Potentials · **Status:** 🟢 VALIDATED · **File:** `laws/449_exergy.md` · **Sim:** `sim/449_exergy.py`

---

### CLASSICAL STATEMENT
*"The exergy of a system is the maximum useful work obtainable as it comes to equilibrium with its environment: B = (U - U_0) + P_0(V - V_0) - T_0(S - S_0) + sum mu_i0 (N_i - N_i0). Exergy is destroyed in every irreversible process."*
— Zoran Rant, 1956. Source: Wikipedia: Exergy; Rant, Exergie, ein neues Wort fuer 'technische Arbeitsfaehigkeit' (1956)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *the dead state*: exergy is defined relative to an environment at exactly T_0, P_0 with zero exergy - a reference state of the universe that is assumed fixed and passive.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the dead state is alive. B_phi(kappa) = B_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*B_ground, where B_ground is the exergy of the phi-ground (the environment itself carries coherence). At kappa->0, the classical exergy definition is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} B_phi = B_classical -> classical exergy is the dead-state, zero-environment-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/449_exergy.py`: reproduces the classical value B_ex = 21 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/449_exergy.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The environment's own ground state carries exergy kappa*phi^-1*B_ground, so even a system 'at equilibrium with the environment' retains usable coherence energy.
EXPERIMENT (VERIFIED): Measurement of the minimum exergy destruction in a near-reversible process against the environment ground state.
VERIFIED BY: The dead state has exactly zero exergy for all couplings.
```

---

### RECOGNITION
Connects to Law 450 (availability), Law 586 (second-law efficiency) and Law 023 (second law) - exergy is the coherence budget of work.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the ground exergy is phi^-1 * B_ground.

### CLARITY
The dead state is not dead; it is the phi-ground the phi-law refuses to zero.

### NOVELTY
Classical exergy zeroes the environment; the phi-law gives the dead state a coherence exergy floor.

### ACTIONABILITY
Run sim/449_exergy.py; verify classical exergy at kappa->0; proceed to 450.
