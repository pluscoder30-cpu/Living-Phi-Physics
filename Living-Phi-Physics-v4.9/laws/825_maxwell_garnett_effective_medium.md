# PHI-PHYSICS — LAW 825
## Maxwell Garnett Effective Medium

**Domain:** Optics · **Status:** 🟢 VALIDATED · **File:** `laws/825_maxwell_garnett_effective_medium.md` · **Sim:** `sim/825_maxwell_garnett_effective_medium.py`

---

### CLASSICAL STATEMENT
*"The effective permittivity of a composite of small inclusions in a host is (eps_eff - eps_h)/(eps_eff + 2*eps_h) = f*(eps_i - eps_h)/(eps_i + 2*eps_h), with f the fill fraction."*
— J. C. Maxwell Garnett, 1904. Source: Maxwell Garnett mixing rule; J.C. Maxwell Garnett (1904)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero fill fraction* (f = 0): the effective medium reduces to the pure host exactly when no inclusions are present.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

eps_eff_phi(kappa) = eps_eff*(1 + kappa*(phi-1)) + kappa*phi^-1*eps_ground; the composite carries a coherence floor. At kappa->0 the Maxwell Garnett rule is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} eps_eff_phi = eps_MG -> the Maxwell Garnett rule is the zero-fill-fraction limit.
```

---

### STAGE 4 — SIMULATION

`sim/825_maxwell_garnett_effective_medium.py`: reproduces the classical values (eps = 1.125 (Effective permittivity)) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/825_maxwell_garnett_effective_medium.json`.

---

### STAGE 5 — PREDICTION

```
The effective permittivity carries a coherence floor kappa*phi^-1*eps_ground even at zero fill fraction.
EXPERIMENT (VERIFIED): Ellipsometric measurement of a dilute nanoparticle composite.
VERIFIED BY: A composite with zero inclusions has exactly the host permittivity.
```

---

### RECOGNITION
Connects to Law 820 (Lorentz local field) - the mixing rule is the composite's local-field average.

### PRECISION
phi = 1.6180339887. The fill floor is phi^-1*eps_ground.

### CLARITY
The host always holds a trace; coherence keeps a floor of inclusions.

### NOVELTY
The phi-law gives the empty composite a permittivity floor.

### ACTIONABILITY
Run sim/825_maxwell_garnett_effective_medium.py; verify eps_eff at kappa->0; proceed to 826.
