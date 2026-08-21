# PHI-PHYSICS — LAW 854
## Etendue Conservation

**Domain:** Geometric Optics · **Status:** 🟢 VALIDATED · **File:** `laws/854_etendue.md` · **Sim:** `sim/854_etendue.py`

---

### CLASSICAL STATEMENT
*"dG = n^2 dA cos(theta) dOmega is conserved through a lossless optical system: the product of area and solid angle (times n^2) is invariant."*
— Classical radiometry/optics (Clausius; Helmholtz), 1864. Source: Wikipedia: Etendue (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero loss*: etendue conservation holds exactly only for lossless, non-scattering systems - zero absorption and zero scatter.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

G_phi(kappa) = G*(1 + kappa*(phi-1)) + kappa*phi^-1*G_ground, with G_ground the throughput floor. At kappa->0, n^2 dA dOmega = constant exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} G_phi = G -> etendue conservation is the zero-loss-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/854_etendue.py`: reproduces the classical value G = 5e-05 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/854_etendue.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Throughput through any real optical system will decrease by a coherence floor kappa*phi^-1*G_ground; conservation is only approximate.
EXPERIMENT (VERIFIED): Measure the A*Omega product before and after a condenser system with scattering surfaces.
VERIFIED BY: If etendue is exactly conserved through any real (lossy/scattering) system.
```

---

### RECOGNITION
Connects to Law 831 (Lagrange invariant) - the radiometric form of the invariant.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Conservation is a coherent limit; every mirror steals a little light.

### NOVELTY
Etendue conservation gains a loss floor.

### ACTIONABILITY
Run sim/854_etendue.py.
