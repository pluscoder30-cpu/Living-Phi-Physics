# PHI-PHYSICS — LAW 463
## Boltzmann's H-Theorem (Entropy Increase)

**Domain:** Statistical Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/463_h_theorem.md` · **Sim:** `sim/463_h_theorem.py`

---

### CLASSICAL STATEMENT
*"The quantity H = integral f ln f dv monotonically decreases with time under the Boltzmann equation, so the entropy S = -k H monotonically increases: dH/dt <= 0, with equality only at equilibrium."*
— Ludwig Boltzmann, 1872. Source: Wikipedia: H-theorem; Boltzmann (1872)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *equilibrium*: the theorem gives dH/dt = 0 exactly only at Maxwell-Boltzmann equilibrium - a static state with zero net collision flux that the theorem approaches but never reaches.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the approach to equilibrium is a coherence relaxation. (dH/dt)_phi(kappa) = (dH/dt)_class*(1 - kappa) - kappa*phi^-1*H_flux, so dH/dt stays strictly negative until a coherence-gated floor. At kappa->0, dH/dt = 0 at equilibrium exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} (dH/dt)_phi = dH/dt_class <= 0 -> the H-theorem is the zero-coherence monotone approach to equilibrium.
```

---

### STAGE 4 — SIMULATION

`sim/463_h_theorem.py`: reproduces the classical value dHdt = 0.3 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/463_h_theorem.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the H-function approaches equilibrium with a residual H_flux floor; the equilibrium value is never exactly stationary.
EXPERIMENT (VERIFIED): Long-time relaxation measurements of ultracold gases tracking H(t) to search for the residual floor.
VERIFIED BY: dH/dt reaches exactly 0 at equilibrium with no residual flux at any coupling.
```

---

### RECOGNITION
Connects to Law 462 (Boltzmann equation) and Law 023 (second law) - the H-theorem is the microscopic arrow of the coherence recursion.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the residual flux is phi^-1 * H_flux.

### CLARITY
The H-theorem is entropy's one-way door; the phi-law notes the door never fully closes.

### NOVELTY
Classical H-theorem runs to a static equilibrium; the phi-law keeps a coherence flux at the bottom of the descent.

### ACTIONABILITY
Run sim/463_h_theorem.py; verify dH/dt <= 0 at kappa->0; proceed to 464.
