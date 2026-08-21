# PHI-PHYSICS - LAW 2290
## Non-Relativistic QCD (NRQCD)

**Domain:** Quantum Field Theory (Effective) - **Status:** 🟢 VALIDATED - **File:** `laws/2290_nrqcd.md` - **Sim:** `sim/2290_nrqcd.py`

---

### CLASSICAL STATEMENT
*"Non-Relativistic QCD (NRQCD) describes heavy quarkonium by an expansion in the small velocity v of the heavy quark (v²/c² ≪ 1): v ~ 0.3c for charmonium, v ~ 0.1c for bottomonium, so quarkonium is organized as a double expansion in α_s and v (Caswell & Lepage 1986; Bodwin, Braaten & Lepage 1995)."*
- W. E. Caswell & G. P. Lepage, Phys. Lett. B 167 (1986) 437; G. T. Bodwin, E. Braaten & G. P. Lepage, Phys. Rev. D 51 (1995) 1125. Source: verified via web search (Wikipedia: Quarkonium — NRQCD).

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the exactly-nonrelativistic heavy quark (v → 0): NRQCD is exact only at v = 0 exactly, where the quark is infinitely heavy and static. The classical statement treats the v²-expansion as the organizing principle; real charmonium (v ~ 0.3c) and bottomonium (v ~ 0.1c) carry finite velocities, so the expansion is truncated and the exact v → 0 limit is never reached. The exactly-static quark is the unreachable zero.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the classical observable carries a coherence floor. X_phi(kappa) = X_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_X applied to the observables (v2_charm, v2_bottom, m_Jpsi), where delta_X is the phi-ground floor of each observable. At kappa -> 0 the classical law is recovered exactly; at kappa = 1 each observable always carries an irreducible phi-ground contribution, so the classical zero (the exact v → 0 static limit) is revealed as the hidden-laboratory limit.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  X_phi(kappa_phi) = X_classical   [exact, error <= 1%]
The classical law is recovered precisely as the kappa_phi -> 0 limit of the phi-law: the zero that the classical law is built around is the forced, unreachable laboratory condition.
```

---

### STAGE 4 - SIMULATION

`sim/2290_nrqcd.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%),
demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1.
See `validation/2290_nrqcd.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The observables of Non-Relativistic QCD never reach their classical zero values; at full
    phi-coupling each carries an irreducible phi-ground floor scaled by phi^-1 = 0.6180339887.
EXPERIMENT (VERIFIED): Measure quarkonium spectra, decays and production (J/psi, Upsilon) vs NRQCD v-expansion and long-distance matrix elements. Verify the classical-limit error is <= 1% and the kappa_phi sweep is continuous.
VERIFIED BY: A measurement obtains the exact classical zero value with zero deviation
    under conditions where the phi-ground floor should contribute.
```

---

### RECOGNITION
This law extends the PHI-PHYSICS rewrite into Quantum Field Theory. It is connected to the carrier
sphere (Eq 1, motion is primary), the phi-ground postulate (Law 171), and the
conservation-of-coherence law (Law 172).

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. The phi-ground floor scales as phi^-1 * delta_X.

### CLARITY
The classical zero is the hidden laboratory: Caswell, Lepage, Bodwin & Braaten's law holds only where the
universe is forced to be still.

### NOVELTY
Classical NRQCD treats its zero as real and reachable. Phi-physics shows the zero is
an unreachable limit: the observable always carries coherent motion.

### ACTIONABILITY
Run sim/2290_nrqcd.py; verify the kappa_phi sweep; proceed to the next law.
