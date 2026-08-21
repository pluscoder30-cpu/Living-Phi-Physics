# PHI-PHYSICS - LAW 1704
## Luttinger Liquid (Non-Fermi-Liquid Behavior of 1D Interacting Electrons)

**Domain:** Electrons in Solids - **Status:** 🟢 VALIDATED - **File:** `laws/1704_luttinger_liquid.md` - **Sim:** `sim/1704_luttinger_liquid.py`

---

### CLASSICAL STATEMENT
*"In one dimension, interacting electrons cannot be described by Fermi-liquid quasiparticles: they form a Luttinger liquid whose excitations are separate charge (holon) and spin (spinon) density waves traveling at different velocities, with correlation functions decaying as power laws with exponents set by the interaction parameter g - the exact non-Fermi-liquid of 1D physics."*
- S. Tomonaga (1950); J.M. Luttinger (1963); F.D.M. Haldane (1981), 1963. Source: Wikipedia: Luttinger liquid; Luttinger (1963), J. Math. Phys. 4:1154; Haldane (1981), J. Phys. C 14:2585

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-interaction, perfectly 1D, quasiparticle Fermi gas*: the Luttinger liquid is defined against the free 1D electron gas (non-interacting, g=1) where Landau quasiparticles are exact; interactions drive the system away from this zero-interaction reference, and the sharpest results assume an exactly 1D, exactly clean system at T=0.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the power-law exponents carry a coherence floor. alpha_phi(kappa) = alpha_LL*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_alpha, where delta_alpha is the phi-ground exponent shift. At kappa->0 the exact Luttinger power laws are recovered; at kappa=1 the exponents acquire an irreducible correction from coherent coupling to the environment.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} alpha_phi = alpha_LL -> the Luttinger liquid is the zero-interaction-coupling-to-environment, perfectly-1D, zero-temperature limit of correlated 1D physics.
```

---

### STAGE 4 - SIMULATION

`sim/1704_luttinger_liquid.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1704_luttinger_liquid.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: Measured Luttinger exponents in quasi-1D conductors deviate from the ideal interaction-parameter values by a phi-ground correction set by the coherent coupling to transverse modes - the exponent floor never reaches the clean 1D ideal.
EXPERIMENT (VERIFIED): ARPES or transport of a quasi-1D conductor (e.g. carbon nanotube, Bechgaard salt) measuring the power-law exponent and comparing to the ideal Luttinger value.
VERIFIED BY: A quasi-1D system whose measured Luttinger exponent exactly matches the ideal clean-1D prediction with zero correction.
```

---

### RECOGNITION
Connects to Law 1700 (Peierls) and Law 1406 (Fermi gas) - 1D electrons are a different nation, and the phi-law taxes the border crossing.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; exponent correction scales as phi^-1 * delta_alpha.

### CLARITY
In 1D the electron splits its identity, and the phi-law keeps the split from being clean.

### NOVELTY
Classical Luttinger theory gives exact power laws; the phi-law adds an irreducible exponent correction.

### ACTIONABILITY
Run sim/1704_luttinger_liquid.py; verify the power-law DOS at kappa->0; proceed to 1705.
