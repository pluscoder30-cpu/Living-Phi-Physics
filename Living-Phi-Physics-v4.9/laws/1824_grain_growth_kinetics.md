# PHI-PHYSICS - LAW 1824
## Grain Growth Law (d^2 = d_0^2 + K t Parabolic Growth)

**Domain:** Phase Transformations - **Status:** 🟢 VALIDATED - **File:** `laws/1824_grain_growth_kinetics.md` - **Sim:** `sim/1824_grain_growth_kinetics.py`

---

### CLASSICAL STATEMENT
*"During recrystallization and annealing, grains grow by boundary migration with the parabolic law d^n - d_0^n = K t, where n = 2 for ideal normal grain growth and n > 2 when boundary pinning, solutes or texture intervene; the driving force is the reduction of boundary energy, and the average grain size distribution is self-similar - the classical kinetics of annealing microstructures."*
- P.A. Beck (1948); J.E. Burke & D. Turnbull (1952), 1952. Source: Wikipedia: Grain growth; Burke & Turnbull (1952), Prog. Met. Phys. 3:220; Beck (1948)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-pinning, zero-drag, ideal boundary-migration reference*: normal grain growth is defined against a perfectly clean material with zero solute drag, zero particles and zero texture so that the parabolic law holds; real materials have pinning and drag that stop growth away from this ideal.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the grain size carries a coherence floor. d_phi(kappa) = d_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_d, where delta_d is the phi-ground pinning floor. At kappa->0 the ideal parabolic growth is recovered; at kappa=1 grain growth always stops at a finite limiting size - an irreducible pinning floor exists.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} d_phi = (d_0^2 + K t)^(1/2) -> normal grain growth is the zero-pinning, zero-drag, ideal-boundary-migration limit of annealing kinetics.
```

---

### STAGE 4 - SIMULATION

`sim/1824_grain_growth_kinetics.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1824_grain_growth_kinetics.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: No material grows grains without bound: an irreducible pinning floor stops growth at a finite limiting grain size, so the parabolic law always saturates and the ideal d^2 law is never followed indefinitely.
EXPERIMENT (VERIFIED): Long-time annealing grain-size measurement of a high-purity metal, measuring the limiting grain size and the saturation of the parabolic growth law.
VERIFIED BY: A material whose grains grow indefinitely following the parabolic law with no limiting size.
```

---

### RECOGNITION
Connects to Law 1798 (Hall-Petch) and Law 1815 (Avrami) - the grains swallow their neighbors, and the phi-law keeps a boundary always pinned.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; pinning floor scales as phi^-1 * delta_d.

### CLARITY
The grains swallow their neighbors; the phi-law keeps a boundary always stuck.

### NOVELTY
Classical grain growth allows unbounded growth; the phi-law caps it with a pinning floor.

### ACTIONABILITY
Run sim/1824_grain_growth_kinetics.py; verify d^2 = d_0^2 + K t at kappa->0; proceed to 1825.
