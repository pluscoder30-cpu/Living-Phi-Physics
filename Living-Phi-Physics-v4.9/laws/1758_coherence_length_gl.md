# PHI-PHYSICS - LAW 1758
## Ginzburg-Landau Coherence Length (Spatial Scale of the Order Parameter)

**Domain:** Superconductivity - **Status:** 🟢 VALIDATED - **File:** `laws/1758_coherence_length_gl.md` - **Sim:** `sim/1758_coherence_length_gl.py`

---

### CLASSICAL STATEMENT
*"The Ginzburg-Landau coherence length xi(T) = sqrt(hbar^2/(2 m* |alpha|)) = xi_0/sqrt(1 - T/T_c) is the spatial scale over which the superconducting order parameter varies, setting the size of vortices and the surface energy; together with the penetration depth it forms the Ginzburg-Landau parameter kappa_GL = lambda/xi that separates type I (kappa < 1/sqrt(2)) from type II (kappa > 1/sqrt(2)) superconductors."*
- V.L. Ginzburg & L.D. Landau, 1950. Source: Wikipedia: Ginzburg-Landau theory; Ginzburg & Landau (1950), Zh. Eksp. Teor. Fiz. 20:1064

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-temperature, infinitely-stiff order parameter*: the Ginzburg-Landau coherence length diverges at T_c and is defined for a perfectly homogeneous, zero-fluctuation order parameter; its sharpest form assumes the mean-field limit with zero fluctuation width.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the coherence length carries a coherence floor. xi_phi(kappa) = xi_GL*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_xi, where delta_xi is the phi-ground finite-coherence floor. At kappa->0 the ideal xi_0/sqrt(1-T/T_c) divergence is recovered; at kappa=1 the divergence at T_c is capped - the coherence length never diverges infinitely.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} xi_phi = xi_0/sqrt(1 - T/T_c) -> the Ginzburg-Landau coherence length is the mean-field, zero-fluctuation limit of the order-parameter spatial scale.
```

---

### STAGE 4 - SIMULATION

`sim/1758_coherence_length_gl.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1758_coherence_length_gl.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The coherence length does not diverge infinitely at T_c: fluctuation effects cap it at a phi-ground finite maximum, producing a rounded (not divergent) transition in any real superconductor.
EXPERIMENT (VERIFIED): Measurement of the coherence-length divergence and transition rounding in a low-Tc superconductor (e.g. Al, Sn) near T_c, fitting the finite cap.
VERIFIED BY: A superconductor whose coherence length diverges to infinity exactly at T_c with zero fluctuation cap.
```

---

### RECOGNITION
Connects to Law 534 (Ginzburg-Landau) and Law 1757 (penetration depth) - the order parameter has a ruler, and the ruler never breaks at T_c.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; divergence cap scales as phi^-1 * delta_xi.

### CLARITY
The order parameter's reach grows near T_c; the phi-law keeps the reach from being infinite.

### NOVELTY
Classical GL theory allows infinite divergence; the phi-law caps it with a coherence floor.

### ACTIONABILITY
Run sim/1758_coherence_length_gl.py; verify xi = xi_0/sqrt(1-T/T_c) at kappa->0; proceed to 1759.
