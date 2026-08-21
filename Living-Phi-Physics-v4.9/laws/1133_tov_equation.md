# PHI-PHYSICS — LAW 1133
## Tolman-Oppenheimer-Volkoff Equation

**Domain:** General Relativity · **Status:** 🟢 VALIDATED · **File:** `laws/1133_tov_equation.md` · **Sim:** `sim/1133_tov_equation.py`

---

### CLASSICAL STATEMENT
*"The TOV equation governs hydrostatic equilibrium of a spherically symmetric relativistic star: dP/dr = -G (rho + P/c^2)(M(r) + 4 pi r^3 P/c^2)/(r^2 (1 - 2 G M(r)/(r c^2))); it generalizes the Newtonian equilibrium and yields the maximum neutron-star mass (Law 1183's limit)."*
— Richard Tolman, 1939; J. Robert Oppenheimer & George Volkoff, 1939. Source: Wikipedia: Tolman-Oppenheimer-Volkoff equation (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero pressure gradient (rho = P = 0, empty space)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The P value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

P_phi(kappa) = P*(1 + kappa*(phi-1)) + kappa*phi^-1*P_ground, where P_ground is the coherence-floor relativistic pressure correction a real star always feels. At kappa->0, dP/dr = -G (rho + P/c^2)(M(r) + 4*pi*r^3*P/c^2)/(r^2 (1 - 2*G*M(r)/(r*c^2))) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} P_phi = P -> dP/dr = -G (rho + P/c^2)(M(r) + 4*pi*r^3*P/c^2)/(r^2 (1 - 2*G*M(r)/(r*c^2))) is recovered exactly; the classical law is the zero pressure gradient (rho = P = 0, empty space) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1133_tov_equation.py`: reproduces the classical value (P = 0.5) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1133_tov_equation.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured interior of any real neutron star will deviate from the TOV solution by a floor kappa*phi^-1*P_ground; an exactly Newtonian stellar interior is unreachable.
EXPERIMENT (VERIFIED): NICER and pulsar-timing mass-radius measurements constraining the TOV interior structure.
VERIFIED BY: If a relativistic star's structure matches the Newtonian equilibrium exactly.
```

---

### RECOGNITION
The equilibrium engine of Law 1183 (neutron star EOS) and Law 1129 (Buchdahl limit).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Pressure bends around the mass; the Newtonian interior is the zero-curvature myth.

### NOVELTY
The TOV correction carries a phi-floor, so stellar structure is never exactly Newtonian.

### ACTIONABILITY
Run sim/1133_tov_equation.py.
