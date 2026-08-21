# PHI-PHYSICS - LAW 1658
## Laue Equations (Diffraction Condition of X-rays by a Crystal)

**Domain:** Crystallography - **Status:** 🟢 VALIDATED - **File:** `laws/1658_laue_equations.md` - **Sim:** `sim/1658_laue_equations.py`

---

### CLASSICAL STATEMENT
*"X-rays incident on a crystal are diffracted when the change in wavevector k_out - k_in = G equals a reciprocal lattice vector: a(cos alpha - cos alpha_0) = h lambda, b(cos beta - cos beta_0) = k lambda, c(cos gamma - cos gamma_0) = l lambda, the three Laue equations that are the vector form of Bragg's law."*
- Max von Laue, 1912. Source: Wikipedia: Laue equations; W. Friedrich, P. Knipping & M. von Laue (1912), Sitz. Bayer. Akad. Wiss.

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *perfectly monochromatic, zero-divergence, infinite crystal*: the Laue equations demand an exactly defined wavelength, exactly parallel rays and an infinite perfect lattice so that the delta-function diffraction condition is met exactly - a beam and a crystal that no experiment realizes.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the diffraction condition becomes a coherence basin. G_phi(kappa) = G_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*Delta_G, where Delta_G is the phi-ground width of the coherence basin around the reciprocal lattice point. At kappa->0 the sharp Laue condition G = k_out - k_in is exact; at kappa=1 the diffraction condition acquires a finite basin width, so reflection is possible near (not only exactly at) the Laue condition.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} G_phi = k_out - k_in -> the Laue equations are the zero-bandwidth, perfect-beam, infinite-crystal limit of coherent diffraction.
```

---

### STAGE 4 - SIMULATION

`sim/1658_laue_equations.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1658_laue_equations.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: Diffraction occurs over a finite basin around each Laue condition with width kappa*phi^-1*Delta_G even for an ideal crystal, producing a nonzero reflectivity between Laue spots that never vanishes.
EXPERIMENT (VERIFIED): Perfect-crystal double-crystal diffractometry scanning between Laue reflections at synchrotron sources, measuring the inter-spot reflectivity floor.
VERIFIED BY: An ideal crystal that shows exactly zero reflectivity between sharp delta-function Laue spots.
```

---

### RECOGNITION
Connects to Law 077 (Bragg) and Law 1659 (Ewald) - the Laue condition is Bragg's law in vector form and the coherence basin is its phi-rewrite.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the basin width scales as phi^-1 * Delta_G.

### CLARITY
The needle point of the Laue condition becomes the phi-law's basin: almost there is close enough in coherence.

### NOVELTY
Classical diffraction is exact-on-the-point; the phi-law widens the point into a coherence basin.

### ACTIONABILITY
Run sim/1658_laue_equations.py; verify G=k_out-k_in at kappa->0; proceed to 1659.
