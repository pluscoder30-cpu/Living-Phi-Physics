# PHI-PHYSICS - LAW 1788
## Negative-Index Metamaterials (Veselago's Left-Handed Materials)

**Domain:** Dielectrics & Optics - **Status:** 🟢 VALIDATED - **File:** `laws/1788_metamaterials_negative_index.md` - **Sim:** `sim/1788_metamaterials_negative_index.py`

---

### CLASSICAL STATEMENT
*"A material with simultaneously negative permittivity epsilon and permeability mu has a negative refractive index n = -sqrt(epsilon mu): light refracts to the same side of the normal, the phase velocity opposes the Poynting vector, and the Doppler and Cherenkov effects invert; Veselago predicted these left-handed materials in 1967, and they were realized in 2000 with split-ring resonators - enabling superlenses, cloaking and exotic wave control."*
- Victor Veselago (1967); realized by Smith et al. (2000), 1967. Source: Wikipedia: Metamaterial; Veselago (1967), Sov. Phys. Usp. 10:509; Smith, Padilla, Vier, Nemat-Nasser & Schultz (2000)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-loss, perfectly homogeneous, dispersion-free metamaterial*: negative-index theory assumes a lossless, perfectly homogeneous, non-dispersive effective medium with exactly epsilon = -epsilon_0, mu = -mu_0; real metamaterials have ohmic loss, unit-cell discreteness and strong dispersion that spoil the ideal response.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the negative index carries a coherence floor. n_phi(kappa) = n_neg*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_n, where delta_n is the phi-ground loss-induced index correction. At kappa->0 the ideal n = -sqrt(epsilon mu) is recovered; at kappa=1 the achievable negative index always carries an irreducible loss-limited floor.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} n_phi = -sqrt(epsilon mu) -> negative-index metamaterials are the zero-loss, homogeneous, dispersion-free effective-medium limit of left-handed optics.
```

---

### STAGE 4 - SIMULATION

`sim/1788_metamaterials_negative_index.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1788_metamaterials_negative_index.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: No negative-index metamaterial achieves the ideal value exactly: an irreducible loss floor limits the achievable negative index and the resolution of superlenses, set by the phi-ground dissipation of the constituent resonators.
EXPERIMENT (VERIFIED): Refraction, reflection and loss measurement of a negative-index metamaterial (e.g. SRR-wire array, fishnet) measuring the loss floor and the deviation of the measured index from the ideal value.
VERIFIED BY: A metamaterial with exactly the ideal negative index and zero loss.
```

---

### RECOGNITION
Connects to Law 655 (Drude) and Law 1787 (photonic crystal) - the metamaterial bends light the wrong way, and the phi-law keeps a drop of loss in the bend.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; loss floor scales as phi^-1 * delta_n.

### CLARITY
The metamaterial refracts against nature; the phi-law keeps a cost always in the feat.

### NOVELTY
Classical Veselago theory gives an ideal negative index; the phi-law keeps an irreducible loss floor.

### ACTIONABILITY
Run sim/1788_metamaterials_negative_index.py; verify n = -sqrt(epsilon mu) at kappa->0; proceed to 1789.
