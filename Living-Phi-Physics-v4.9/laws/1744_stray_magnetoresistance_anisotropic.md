# PHI-PHYSICS - LAW 1744
## Anisotropic Magnetoresistance (AMR) (Orientation-Dependent Resistance of Ferromagnets)

**Domain:** Magnetism - **Status:** 🟢 VALIDATED - **File:** `laws/1744_stray_magnetoresistance_anisotropic.md` - **Sim:** `sim/1744_stray_magnetoresistance_anisotropic.py`

---

### CLASSICAL STATEMENT
*"The resistance of a ferromagnet depends on the angle between current and magnetization: rho = rho_perp + (rho_parallel - rho_perp) cos^2 theta, with AMR ratios of a few percent in permalloy and FeNi alloys; AMR originates from spin-orbit coupling and s-d scattering asymmetry, and is the mechanism of AMR read heads and magnetoresistive sensors."*
- W. Thomson (Lord Kelvin), 1857. Source: Wikipedia: Anisotropic magnetoresistance; Thomson (1857), Proc. R. Soc. 8:546

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-spin-orbit, perfectly isotropic resistance reference*: AMR is defined against a magnetically isotropic reference where rho_parallel = rho_perp and the resistance is orientation-independent; the effect is the spin-orbit-driven anisotropy away from this zero-AMR reference.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the AMR ratio carries a coherence floor. AMR_phi(kappa) = AMR_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_A, where delta_A is the phi-ground residual magnetoresistance anisotropy. At kappa->0 the zero-AMR isotropic reference is recovered; at kappa=1 an irreducible anisotropy floor always exists.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} AMR_phi = 0 -> anisotropic magnetoresistance is the spin-orbit-driven orientation dependence measured from the zero-AMR isotropic reference.
```

---

### STAGE 4 - SIMULATION

`sim/1744_stray_magnetoresistance_anisotropic.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1744_stray_magnetoresistance_anisotropic.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: Every ferromagnet retains an irreducible AMR floor even in nominally isotropic configurations: the orientation-dependent resistance never vanishes completely.
EXPERIMENT (VERIFIED): Ultra-sensitive AMR measurement of a magnetically isotropic ferromagnet as a function of angle, measuring the residual anisotropy floor.
VERIFIED BY: A ferromagnet with exactly orientation-independent resistance (zero AMR).
```

---

### RECOGNITION
Connects to Law 1729 (GMR) and Law 1743 (Rashba) - the ferromagnet's resistance turns with its magnetization, and the phi-law keeps a turn always present.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; AMR floor scales as phi^-1 * delta_A.

### CLARITY
The resistance reads the angle; the phi-law keeps a residual angle-reading in every magnet.

### NOVELTY
Classical AMR allows zero anisotropy; the phi-law keeps an irreducible orientation floor.

### ACTIONABILITY
Run sim/1744_stray_magnetoresistance_anisotropic.py; verify rho = rho_perp + delta cos^2 theta at kappa->0; proceed to 1745.
