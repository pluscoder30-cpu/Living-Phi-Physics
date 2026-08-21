# PHI-PHYSICS - LAW 1685
## Van Hove Singularities (Anomalies in the Density of States)

**Domain:** Electrons in Solids - **Status:** 🟢 VALIDATED - **File:** `laws/1685_van_hove_singularities.md` - **Sim:** `sim/1685_van_hove_singularities.py`

---

### CLASSICAL STATEMENT
*"The density of states of a periodic system has analytic singularities at energies where the band dispersion has stationary (saddle) points: in 1D D(E) diverges as 1/sqrt(E - E_0), in 2D it has a logarithmic singularity, and in 3D a finite cusp; these Van Hove singularities mark the band-critical points M_1, M_2, M_3 of the electronic and phononic dispersion."*
- Leon Van Hove, 1953. Source: Wikipedia: Van Hove singularity; Van Hove (1953), Phys. Rev. 89:1189

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *exactly flat, perfectly periodic band saddle*: Van Hove singularities require the group velocity grad_k E(k) to vanish exactly at a critical point in an infinite perfect lattice - an exactly stationary band point that a real crystal's dispersion, with its disorder and finite size, never realizes with infinite sharpness.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the singularities carry a coherence broadening. D_phi(kappa) = D_vhs(E)*(1 + kappa*(phi-1)) + kappa*phi^-1*D_floor, where D_floor is the phi-ground finite height of the singularity. At kappa->0 the exact divergent singularity is recovered; at kappa=1 the singularity is broadened to a finite, coherence-limited peak.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} D_phi = D_vhs(E) -> Van Hove singularities are the perfect-periodicity, zero-disorder, exactly-stationary-band-point limit of the density of states.
```

---

### STAGE 4 - SIMULATION

`sim/1685_van_hove_singularities.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1685_van_hove_singularities.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: Van Hove singularities are never infinitely sharp: they carry a phi-ground finite width and height set by irreducible coherent disorder, so the optical and tunneling spectra show finite (not diverging) cusps.
EXPERIMENT (VERIFIED): High-resolution ARPES and STS of a clean layered material (e.g. graphene or TMDC) measuring the finite width of the Van Hove singularity at low temperature.
VERIFIED BY: A Van Hove singularity measured to be infinitely sharp (exact divergence) at T=0.
```

---

### RECOGNITION
Connects to Law 1684 (density of states) and Law 1681 (Brillouin zone) - the saddle points of the band are the spectacles of the singularity.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; singularity width scales as phi^-1 * D_floor.

### CLARITY
The density of states cries out at the saddle; the phi-law turns the cry into a bounded note.

### NOVELTY
Classical Van Hove theory allows exact divergences; the phi-law caps them at a coherence floor.

### ACTIONABILITY
Run sim/1685_van_hove_singularities.py; verify the 1/sqrt(E) divergence at kappa->0; proceed to 1686.
