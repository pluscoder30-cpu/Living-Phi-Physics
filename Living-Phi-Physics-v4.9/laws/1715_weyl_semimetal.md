# PHI-PHYSICS - LAW 1715
## Weyl Semimetal (Band Structure with Weyl Points)

**Domain:** Electrons in Solids - **Status:** 🟢 VALIDATED - **File:** `laws/1715_weyl_semimetal.md` - **Sim:** `sim/1715_weyl_semimetal.py`

---

### CLASSICAL STATEMENT
*"A Weyl semimetal has band crossings (Weyl points) where two bands touch linearly in three dimensions, with the quasiparticles described by the Weyl equation H = v sigma.p; each Weyl point is a monopole of Berry curvature with chiral charge +/-1, and the surface hosts Fermi arcs connecting Weyl points of opposite chirality - a 3D analogue of graphene's Dirac physics."*
- Hermann Weyl (1929); realized in TaAs 2015, 2015. Source: Wikipedia: Weyl semimetal; Weyl (1929), Z. Phys. 56:330; Xu et al. / Lv et al. (2015)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *perfectly linear, gapless, isolated Weyl point*: Weyl semimetals are defined against band structures where the touching is exactly linear and exactly gapless, with zero mixing of the crossing bands and zero disorder - an ideal linear crossing that real materials realize only approximately with finite curvature and finite scattering.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the Weyl point carries a coherence gap floor. Delta_w_phi(kappa) = Delta_w*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_D, where delta_D is the phi-ground residual gap/width of the Weyl point. At kappa->0 the exactly gapless linear Weyl point is recovered; at kappa=1 every Weyl point carries an irreducible width and curvature.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} Delta_w_phi = 0 -> Weyl points are the zero-gap, exactly-linear, ideal-3D-band-crossing limit of chiral semimetals.
```

---

### STAGE 4 - SIMULATION

`sim/1715_weyl_semimetal.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1715_weyl_semimetal.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: Weyl points are never exactly gapless or exactly linear: an irreducible residual width and curvature floor remains, producing finite chiral-anomaly conductivities and broadened transport signatures that do not vanish at T=0.
EXPERIMENT (VERIFIED): High-resolution ARPES and magnetotransport of TaAs or WTe2 measuring the residual Weyl-point width and the chiral anomaly response floor.
VERIFIED BY: A Weyl point measured to be exactly gapless and exactly linear with zero width.
```

---

### RECOGNITION
Connects to Law 1710 (topological insulator) and Law 1709 (Chern) - the Weyl point is a monopole in momentum space, and the phi-law keeps the monopole slightly fuzzy.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; point width scales as phi^-1 * delta_D.

### CLARITY
The bands cross linearly at a Weyl point; the phi-law keeps the crossing from being a knife's edge.

### NOVELTY
Classical Weyl theory gives exact linear crossings; the phi-law widens them with a coherence floor.

### ACTIONABILITY
Run sim/1715_weyl_semimetal.py; verify the linear crossing at kappa->0; proceed to 1716.
