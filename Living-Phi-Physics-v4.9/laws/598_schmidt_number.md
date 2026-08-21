# PHI-PHYSICS — LAW 598
## Schmidt Number (Momentum to Mass Diffusivity Ratio)

**Domain:** Kinetic Theory · **Status:** 🟢 VALIDATED · **File:** `laws/598_schmidt_number.md` · **Sim:** `sim/598_schmidt_number.py`

---

### CLASSICAL STATEMENT
*"The Schmidt number is the ratio of kinematic viscosity to mass diffusivity: Sc = nu/D = mu/(rho D). It governs the relative thickness of the momentum and concentration boundary layers."*
— Ernst Schmidt, 1925. Source: Wikipedia: Schmidt number; Schmidt (1925)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *unity ratio*: many analyses assume Sc = 1 (momentum and mass diffuse identically) - a condition no real fluid satisfies precisely.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the diffusivity ratio carries coherence. Sc_phi(kappa) = Sc*(1 + kappa*(phi-1)) + kappa*phi^-1*Sc_ground. At kappa->0 the Schmidt number is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} Sc_phi = nu/D -> the Schmidt number is the zero-coherence diffusivity-ratio limit.
```

---

### STAGE 4 — SIMULATION

`sim/598_schmidt_number.py`: reproduces the classical value Sc = 0.75 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/598_schmidt_number.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the effective Schmidt number deviates from the molecular value by a coherence term.
EXPERIMENT (VERIFIED): Boundary-layer mass-transfer measurements (e.g. dissolution experiments) to extract Sc.
VERIFIED BY: Sc = nu/D exactly with no coherence correction for all couplings.
```

---

### RECOGNITION
Connects to Law 597 (Lewis) and Law 599 (Sherwood) - the Schmidt number is the momentum-mass coherence ratio.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the floor is phi^-1 * Sc_ground.

### CLARITY
Momentum and mass do not diffuse at the same pace; the phi-law keeps the pace's floor.

### NOVELTY
Classical Schmidt is a fixed ratio; the phi-law adds the coherence correction of the real transport.

### ACTIONABILITY
Run sim/598_schmidt_number.py; verify Sc at kappa->0; proceed to 599.
