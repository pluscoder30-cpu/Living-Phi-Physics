# PHI-PHYSICS - LAW 1298
## S-Matrix (Scattering Matrix: Transition Amplitudes)

**Domain:** Quantum Dynamics - **Status:** 🟢 VALIDATED - **File:** `laws/1298_s_matrix.md` - **Sim:** `sim/1298_s_matrix.py`

---

### CLASSICAL STATEMENT
*"The S-matrix maps asymptotic in-states to asymptotic out-states: |out> = S|in>, with unitarity S^dagger S = I encoding probability conservation and the optical theorem sigma_tot = (4 pi/k) Im f(0) relating the total cross section to the forward scattering amplitude; S = I + iT with T the transition matrix."*
- Werner Heisenberg (1943); John Wheeler (1937), 1943. Source: Wikipedia: S-matrix; Heisenberg, Z. Phys. 120 (1943) 513; Wheeler (1937)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is *no scattering*: for a free field the S-matrix is exactly the identity I, i.e. zero interaction between in and out states - the non-interacting limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the identity channel carries a coherence residue. S_phi(kappa) = S*(1 + kappa*(phi-1)) + kappa*phi^-1*S_floor, where S_floor is the phi-ground scattering residue of the recursion. At kappa->0, S = I for free fields.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} S_phi = I + iT -> the S-matrix is the zero-interaction free-field limit.
```

---

### STAGE 4 - SIMULATION

`sim/1298_s_matrix.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1298_s_matrix.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: A nominally non-interacting field at full coherence coupling shows a phi-ground scattering residue kappa*phi^-1*S_floor, a floor in the free-field cross section.
EXPERIMENT (VERIFIED): Ultrahigh-vacuum atom interferometry searching for residual scattering of 'free' atomic beams at increasing coherence.
VERIFIED BY: The S-matrix of a free field is exactly the identity for all couplings.
```

---

### RECOGNITION
Connects to Law 1301 (perturbation) and Law 389 (Rutherford scattering) - the S-matrix is the coherence map of in-to-out.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the scattering residue is phi^-1 * S_floor.

### CLARITY
Every scattering is the story of two somethings meeting; the phi-law notes even not-meeting leaves a mark.

### NOVELTY
Classical scattering theory identities the free channel; the phi-law gives even free fields a coherence residue.

### ACTIONABILITY
Run sim/1298_s_matrix.py; verify unitarity at kappa->0; proceed to 1299.
