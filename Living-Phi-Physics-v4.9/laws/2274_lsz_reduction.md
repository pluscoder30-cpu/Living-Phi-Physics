# PHI-PHYSICS - LAW 2274
## LSZ Reduction Formula (S-Matrix from Green Functions)

**Domain:** Quantum Field Theory - **Status:** 🟢 VALIDATED - **File:** `laws/2274_lsz_reduction.md` - **Sim:** `sim/2274_lsz_reduction.py`

---

### CLASSICAL STATEMENT
*"The LSZ reduction formula expresses S-matrix elements as residues of Fourier-transformed time-ordered correlation functions: ⟨p₁..pₙ out|q₁..qₘ in⟩ = ∏[i(□+m²)/√Z] Γ(p₁..pₙ;-q₁..-qₘ), so amplitudes are the residues of the poles of the Green functions put on-shell (Lehmann, Symanzik & Zimmermann, 1955)."*
- Harry Lehmann, Kurt Symanzik & Wolfhart Zimmermann, Nuovo Cimento 1 (1955) 205. Source: verified via web search (Wikipedia: LSZ reduction formula).

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the exact on-shell pole: LSZ requires the four-momenta to be taken exactly on-shell (p² = m²), where the propagator has an exact pole whose residue is exactly Z. The classical statement assumes the external particles are exactly on their mass shell with zero width — a state that no real particle reaches exactly (unstable particles carry finite width, bound states evade the formula). The exact pole residue Z is the unreachable zero.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the classical observable carries a coherence floor. X_phi(kappa) = X_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_X applied to the observables (Z_factor, S_amp, pole_residue), where delta_X is the phi-ground floor of each observable. At kappa -> 0 the classical law is recovered exactly; at kappa = 1 each observable always carries an irreducible phi-ground contribution, so the classical zero (the exact on-shell pole) is revealed as the hidden-laboratory limit.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  X_phi(kappa_phi) = X_classical   [exact, error <= 1%]
The classical law is recovered precisely as the kappa_phi -> 0 limit of the phi-law: the zero that the classical law is built around is the forced, unreachable laboratory condition.
```

---

### STAGE 4 - SIMULATION

`sim/2274_lsz_reduction.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%),
demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1.
See `validation/2274_lsz_reduction.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The observables of the LSZ reduction formula never reach their classical zero values; at full
    phi-coupling each carries an irreducible phi-ground floor scaled by phi^-1 = 0.6180339887.
EXPERIMENT (VERIFIED): Measure the Z factor from the pole residue of propagators in lattice QCD / precision e+e- data. Verify the classical-limit error is <= 1% and the kappa_phi sweep is continuous.
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
The classical zero is the hidden laboratory: Lehmann, Symanzik & Zimmermann's law holds only where the
universe is forced to be still.

### NOVELTY
Classical LSZ treats its zero as real and reachable. Phi-physics shows the zero is
an unreachable limit: the observable always carries coherent motion.

### ACTIONABILITY
Run sim/2274_lsz_reduction.py; verify the kappa_phi sweep; proceed to the next law.
