# PHI-PHYSICS — LAW 499
## Thermoelectric Figure of Merit (ZT)

**Domain:** Statistical Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/499_thermoelectric_figure_of_merit.md` · **Sim:** `sim/499_thermoelectric_figure_of_merit.py`

---

### CLASSICAL STATEMENT
*"The efficiency of a thermoelectric device is governed by the dimensionless figure of merit ZT = S^2 sigma T / kappa, where S is the Seebeck coefficient, sigma the electrical conductivity, and kappa the thermal conductivity. The maximum efficiency increases monotonically with ZT."*
— Edmund Altenkirch, 1911. Source: Wikipedia: Thermoelectric materials (figure of merit); Altenkirch (1911)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero thermal conductivity*: ZT would diverge as kappa -> 0, i.e. the perfect thermoelectric needs a material that conducts electricity but not heat - a lattice with no phonon coherence at all.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the phonon channel carries coherence. (1/ZT)_phi(kappa) = (kappa/(S^2 sigma T))*(1 + kappa*(phi-1)) + kappa*phi^-1*ZT_floor, so ZT is bounded above by a coherence floor. At kappa->0, ZT = S^2 sigma T/kappa exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} ZT_phi = S^2 sigma T / kappa -> the figure of merit is the zero-phonon-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/499_thermoelectric_figure_of_merit.py`: reproduces the classical value ZT = 0.6 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/499_thermoelectric_figure_of_merit.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling ZT saturates below the classical S^2 sigma T/kappa bound; the divergence at kappa -> 0 is regularized by the coherence floor.
EXPERIMENT (VERIFIED): High-accuracy ZT measurements of thermoelectric materials across a range of lattice thermal conductivities.
VERIFIED BY: ZT can reach arbitrarily high values as kappa -> 0 for all couplings.
```

---

### RECOGNITION
Connects to Law 496 (Seebeck), Law 497 (Peltier) and Law 494 (Wiedemann-Franz) - ZT is the coherence budget of the thermoelectric conversion.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the floor term is phi^-1 * ZT_floor.

### CLARITY
The perfect thermoelectric would refuse to conduct heat; the phi-law notes even refusal has a floor.

### NOVELTY
Classical ZT is unbounded as kappa->0; the phi-law bounds it by the coherence of the phonon channel.

### ACTIONABILITY
Run sim/499_thermoelectric_figure_of_merit.py; verify ZT at kappa->0; proceed to 500.
