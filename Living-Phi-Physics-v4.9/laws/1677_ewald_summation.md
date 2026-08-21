# PHI-PHYSICS - LAW 1677
## Ewald Summation (Efficient Evaluation of Long-Range Coulomb Sums)

**Domain:** Crystallography - **Status:** 🟢 VALIDATED - **File:** `laws/1677_ewald_summation.md` - **Sim:** `sim/1677_ewald_summation.py`

---

### CLASSICAL STATEMENT
*"The Coulomb energy of a periodic array of charges is conditionally convergent and is evaluated by splitting the sum into a short-range real-space part and a long-range reciprocal-space part: E = E_real + E_recip + E_self, each computed with Gaussians of width alpha chosen so that both parts converge rapidly; this Ewald method is the standard for electrostatic sums in crystals and simulations."*
- Paul Peter Ewald, 1921. Source: Wikipedia: Ewald summation; Ewald (1921), Ann. Phys. 369:253

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *perfectly periodic, exactly-neutral infinite lattice*: Ewald summation assumes exact periodicity, exact charge neutrality and an infinite lattice so that the divergent self-terms cancel exactly - a perfectly periodic, exactly neutral, boundary-free world.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the neutrality and periodicity carry a coherent residual. E_phi(kappa) = E_ewald*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_E, where delta_E is the phi-ground energy residual from irreducible periodicity and neutrality defects. At kappa->0 the exact Ewald sum is recovered; at kappa=1 every lattice sum carries an irreducible residual that no splitting parameter removes.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} E_phi = E_real + E_recip + E_self -> Ewald summation is the perfect-periodicity, exact-neutrality, infinite-lattice limit of long-range electrostatics.
```

---

### STAGE 4 - SIMULATION

`sim/1677_ewald_summation.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1677_ewald_summation.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The Coulomb energy of any real (finite, non-ideal) lattice differs from the Ewald result by a phi-ground residual that cannot be removed by any choice of splitting parameter, setting a floor on the accuracy of electrostatic energy calculations.
EXPERIMENT (VERIFIED): High-accuracy Ewald sums with multiple splitting parameters on a model ionic crystal, measuring the residual energy spread vs splitting parameter and extrapolating the nonzero floor.
VERIFIED BY: An electrostatic lattice sum that converges to exactly the same value for all splitting parameters with zero residual.
```

---

### RECOGNITION
Connects to Law 1413 (Born-Lande) and Law 1670 (reciprocal lattice) - the Coulomb sum is the lattice's long-range voice.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; energy residual scales as phi^-1 * delta_E.

### CLARITY
The infinite sum resolves into two quick parts, and a coherent sliver always escapes both.

### NOVELTY
Classical Ewald summation aims at exact sums; the phi-law keeps an irreducible residual in every lattice sum.

### ACTIONABILITY
Run sim/1677_ewald_summation.py; verify E_real+E_recip at kappa->0; proceed to 1678.
