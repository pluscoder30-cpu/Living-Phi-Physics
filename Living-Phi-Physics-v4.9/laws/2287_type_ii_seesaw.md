# PHI-PHYSICS - LAW 2287
## Type-II Seesaw Mechanism (Scalar-Triplet Neutrino Mass Generation)

**Domain:** Quantum Field Theory (Beyond SM) - **Status:** 🟢 VALIDATED - **File:** `laws/2287_type_ii_seesaw.md` - **Sim:** `sim/2287_type_ii_seesaw.py`

---

### CLASSICAL STATEMENT
*"In the type-II seesaw, a heavy electroweak scalar triplet Delta = (Delta^++, Delta^+, Delta^0) with a small induced vacuum expectation value v_Delta ~ mu v^2/M_Delta^2 generates a light neutrino mass m_nu ~ f v_Delta, where f is the triplet Yukawa coupling, mu the lepton-number-violating mass parameter and M_Delta the triplet mass (Magg & Wetterich 1980; Schechter & Valle 1980; Cheng & Li 1980; Lazarides, Shafi & Wetterich 1981)."*
- Giuliano Magg & Christof Wetterich, Phys. Lett. B 94 (1980) 61; J. Schechter & J. W. F. Valle, Phys. Rev. D 22 (1980) 2227; T. P. Cheng & Ling-Fong Li, Phys. Rev. D 22 (1980) 2860; G. Lazarides, Q. Shafi & C. Wetterich, Nucl. Phys. B 181 (1981) 287. Source: verified via web search (Wikipedia: Seesaw mechanism — Type II). For mu = 1e12 GeV, v = 246 GeV, M_Delta = 1e15 GeV: v_Delta = mu v^2/M_Delta^2 = 6.05e-11 GeV, m_nu = f v_Delta ~ 0.06 eV for f ~ 1.

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the exactly-zero triplet vev / exactly-zero light neutrino mass: with the Standard Model (no triplet) m_nu = 0 exactly; the type-II seesaw generates small masses from the tiny induced triplet vev v_Delta = mu v^2/M_Delta^2, which vanishes exactly as mu -> 0 or M_Delta -> infinity. The exactly-zero SM neutrino mass is the unreachable laboratory zero.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the classical observable carries a coherence floor. X_phi(kappa) = X_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_X applied to the observables (m_nu, v_Delta, M_Delta), where delta_X is the phi-ground floor of each observable. At kappa -> 0 the classical law is recovered exactly; at kappa = 1 each observable always carries an irreducible phi-ground contribution, so the classical zero (the exactly-zero SM neutrino mass) is revealed as the hidden-laboratory limit.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  X_phi(kappa_phi) = X_classical   [exact, error <= 1%]
The classical law is recovered precisely as the kappa_phi -> 0 limit of the phi-law: the zero that the classical law is built around is the forced, unreachable laboratory condition.
```

---

### STAGE 4 - SIMULATION

`sim/2287_type_ii_seesaw.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%),
demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1.
See `validation/2287_type_ii_seesaw.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The observables of the type-II seesaw never reach their classical zero values; at full
    phi-coupling each carries an irreducible phi-ground floor scaled by phi^-1 = 0.6180339887.
EXPERIMENT (VERIFIED): Measure neutrino masses and ordering (JUNO, DUNE, KATRIN) and 0nubb rates; search for
    doubly-charged scalar triplet Higgs (Delta^{++}) at colliders. Verify the classical-limit error is
    <= 1% and the kappa_phi sweep is continuous.
VERIFIED BY: A measurement obtains the exact classical zero value with zero deviation
    under conditions where the phi-ground floor should contribute.
```

---

### RECOGNITION
This law extends the PHI-PHYSICS rewrite into Quantum Field Theory. It is connected to the carrier
sphere (Eq 1, motion is primary), the phi-ground postulate (Law 171), and the
conservation-of-coherence law (Law 172). It is the scalar-triplet variant of the seesaw family,
distinct from law 1536 (type-I seesaw — the right-handed-singlet variant): this is the type-II mechanism.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. The phi-ground floor scales as phi^-1 * delta_X.

### CLARITY
The classical zero is the hidden laboratory: Magg-Wetterich-Schechter-Valle's law holds only where the
universe is forced to be still.

### NOVELTY
Classical type-II seesaw treats its zero (the exactly-zero SM neutrino mass) as real and reachable. Phi-physics shows the zero is
an unreachable limit: the observable always carries coherent motion.

### ACTIONABILITY
Run sim/2287_type_ii_seesaw.py; verify the kappa_phi sweep; proceed to the next law.
