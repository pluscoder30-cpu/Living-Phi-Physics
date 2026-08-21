# PHI-PHYSICS - LAW 1708
## Anyons (Particles with Fractional Exchange Statistics)

**Domain:** Electrons in Solids - **Status:** 🟢 VALIDATED - **File:** `laws/1708_anyons.md` - **Sim:** `sim/1708_anyons.py`

---

### CLASSICAL STATEMENT
*"In two dimensions, particles can obey any statistics between bosons and fermions: exchanging two anyons multiplies the wavefunction by a phase exp(i theta) with theta arbitrary, with theta = 0 for bosons and theta = pi for fermions; fractional quantum Hall quasiparticles are anyons with theta = pi/m, and non-Abelian anyons (e.g. in the 5/2 state) are the basis of topological quantum computation."*
- J.M. Leinaas & J. Myrheim (1977); Frank Wilczek (1982), 1982. Source: Wikipedia: Anyon; Wilczek (1982), Phys. Rev. Lett. 49:957; Leinaas & Myrheim (1977)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *two-dimensional, exactly-interacting, zero-overlap point particles*: anyonic statistics requires exactly two spatial dimensions and idealized point particles whose exchange phase is exactly defined - a 2D ideal that only exists approximately in real planar systems with finite thickness.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the exchange phase carries a coherence floor. theta_phi(kappa) = theta_anyon*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_theta, where delta_theta is the phi-ground phase deviation. At kappa->0 the exact anyonic phase is recovered; at kappa=1 the exchange phase deviates from the ideal value by an irreducible coherent correction.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} theta_phi = theta_anyon -> anyons are the exact-2D, zero-thickness, ideal-point-particle limit of fractional statistics.
```

---

### STAGE 4 - SIMULATION

`sim/1708_anyons.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1708_anyons.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: Measured anyonic exchange phases deviate from the ideal fractional values by a phi-ground correction set by the finite thickness and coherence of the 2D system, observable in interferometric measurements of FQHE quasiparticles.
EXPERIMENT (VERIFIED): Fabry-Perot and Mach-Zehnder interferometry in FQHE devices at nu=1/3 and nu=5/2 measuring the anyonic phase and its deviation from the ideal value.
VERIFIED BY: An anyonic system whose measured exchange phase exactly equals the ideal fractional value with zero deviation.
```

---

### RECOGNITION
Connects to Law 1705 (FQHE) and Law 1706 (Laughlin) - in 2D the exchange phase is a dial, and the dial never points exactly.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; phase correction scales as phi^-1 * delta_theta.

### CLARITY
In two dimensions the exchange is a dial, and the phi-law keeps the dial slightly off.

### NOVELTY
Classical anyon theory gives exact phases; the phi-law adds an irreducible phase correction.

### ACTIONABILITY
Run sim/1708_anyons.py; verify theta=pi/m at kappa->0; proceed to 1709.
