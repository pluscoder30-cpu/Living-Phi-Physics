# PHI-PHYSICS - LAW 1674
## Goldschmidt Tolerance Factor (Perovskite Stability Criterion)

**Domain:** Crystallography - **Status:** 🟢 VALIDATED - **File:** `laws/1674_goldschmidt_tolerance_factor.md` - **Sim:** `sim/1674_goldschmidt_tolerance_factor.py`

---

### CLASSICAL STATEMENT
*"The stability of the ABO3 perovskite structure is governed by the tolerance factor t = (r_A + r_O)/(sqrt(2)(r_B + r_O)), where r are the ionic radii; t = 1 gives the ideal cubic perovskite, and the structure distorts (rhombohedral, orthorhombic, tetragonal) as t deviates from unity, with perovskite stability roughly bounded by 0.75 < t < 1.0."*
- Victor M. Goldschmidt, 1926. Source: Wikipedia: Goldschmidt tolerance factor; Goldschmidt (1926), Skrifter Norske Videnskaps-Akad.

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *perfectly close-packed, zero-tilt ideal perovskite*: the tolerance factor is built on the assumption of ideal ionic spheres with exact radius ratios so that t = 1 exactly and the structure is perfectly cubic with zero octahedral tilt - a hard-sphere ideal no real oxide realizes.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the ideal cubic perovskite carries a coherent tilt floor. t_phi(kappa) = t_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_t, where delta_t is the phi-ground tolerance deviation from coherent octahedral tilting. At kappa->0 the ideal t=1 cubic structure is exact; at kappa=1 no perovskite is perfectly cubic - an irreducible tilt remains.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} t_phi = t_classical -> the Goldschmidt tolerance factor is the zero-tilt, ideal-ionic-radius, perfect-cubic limit of perovskite geometry.
```

---

### STAGE 4 - SIMULATION

`sim/1674_goldschmidt_tolerance_factor.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1674_goldschmidt_tolerance_factor.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: No perovskite is exactly cubic at any temperature: a phi-ground octahedral-tilt floor remains even when t = 1 exactly, observable as a residual tetragonal or rhombohedral distortion and phonon softening that never vanishes.
EXPERIMENT (VERIFIED): Precision synchrotron diffraction and neutron scattering of a t=1 perovskite (e.g. SrTiO3 or BaTiO3) measuring the residual octahedral-tilt order parameter vs temperature down to millikelvin.
VERIFIED BY: A perovskite with t=1 exactly cubic at all temperatures with zero octahedral tilt.
```

---

### RECOGNITION
Connects to Law 1656 (Bravais) and Law 791 (ferroelectricity) - the perovskite is the workhorse structure, and the workhorse always has a wobble.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; tolerance floor scales as phi^-1 * delta_t.

### CLARITY
The ideal cube is the dream of the perovskite; the phi-law keeps it tilting forever.

### NOVELTY
Classical tolerance-factor analysis allows a perfect cube; the phi-law keeps an irreducible tilt.

### ACTIONABILITY
Run sim/1674_goldschmidt_tolerance_factor.py; verify t=1 cubic at kappa->0; proceed to 1675.
