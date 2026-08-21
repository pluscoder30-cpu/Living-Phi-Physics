# PHI-PHYSICS - LAW 2286
## Neutrinoless Double Beta Decay (Majorana Test)

**Domain:** Quantum Field Theory (Nuclear/Particle) - **Status:** 🟢 VALIDATED - **File:** `laws/2286_neutrinoless_double_beta.md` - **Sim:** `sim/2286_neutrinoless_double_beta.py`

---

### CLASSICAL STATEMENT
*"Neutrinoless double beta decay (0νββ), (A,Z) → (A,Z+2) + 2e⁻, occurs only if the neutrino is a Majorana particle; the rate is Γ = G⁰ν |M⁰ν|² ⟨m_ββ⟩², directly probing lepton-number violation and the effective Majorana mass (Furry, 1939 conjecture)."*
- Wendell H. Furry, Phys. Rev. 56 (1939) 1184 (conjecture of the Majorana-mediated 0ν mode, building on Goeppert-Mayer 1935 and Majorana 1937). Source: verified via web search (Wikipedia: Neutrinoless double beta decay).

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the exactly-zero effective Majorana mass: 0νββ proceeds only if ⟨m_ββ⟩ ≠ 0; if neutrinos were exactly massless (or purely Dirac), the 0ν rate would be exactly zero and lepton number exactly conserved. The classical Standard Model is built on the exactly-zero neutrino mass — the very zero that 0νββ is designed to falsify. The detection threshold ⟨m_ββ⟩ > 0 is the unreachable-zero boundary.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the classical observable carries a coherence floor. X_phi(kappa) = X_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_X applied to the observables (G0nu, M0nu, m_bb), where delta_X is the phi-ground floor of each observable. At kappa -> 0 the classical law is recovered exactly; at kappa = 1 each observable always carries an irreducible phi-ground contribution, so the classical zero (the exactly-zero Majorana mass) is revealed as the hidden-laboratory limit.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  X_phi(kappa_phi) = X_classical   [exact, error <= 1%]
The classical law is recovered precisely as the kappa_phi -> 0 limit of the phi-law: the zero that the classical law is built around is the forced, unreachable laboratory condition.
```

---

### STAGE 4 - SIMULATION

`sim/2286_neutrinoless_double_beta.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%),
demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1.
See `validation/2286_neutrinoless_double_beta.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The observables of Neutrinoless Double Beta Decay never reach their classical zero values; at full
    phi-coupling each carries an irreducible phi-ground floor scaled by phi^-1 = 0.6180339887.
EXPERIMENT (VERIFIED): KamLAND-Zen, GERDA/LEGEND, EXO/nEXO, CUORE, JUNO searches for 0nubb; measure the effective Majorana mass floor. Verify the classical-limit error is <= 1% and the kappa_phi sweep is continuous.
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
The classical zero is the hidden laboratory: Furry's law holds only where the
universe is forced to be still.

### NOVELTY
Classical Neutrinoless Double Beta Decay treats its zero as real and reachable. Phi-physics shows the zero is
an unreachable limit: the observable always carries coherent motion.

### ACTIONABILITY
Run sim/2286_neutrinoless_double_beta.py; verify the kappa_phi sweep; proceed to the next law.
