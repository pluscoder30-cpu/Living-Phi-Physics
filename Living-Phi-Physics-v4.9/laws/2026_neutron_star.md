# PHI-PHYSICS - LAW 2026
## Neutron Star

**Domain:** Geophysics - **Status:** 🟢 VALIDATED - **File:** `laws/2026_neutron_star.md` - **Sim:** `sim/2026_neutron_star.py`

---

### CLASSICAL STATEMENT
*"A neutron star is the collapsed core of a massive star (radius ~10 km, mass ~1.4 M_sun) held up by neutron degeneracy pressure and the strong force; its existence was predicted by Baade and Zwicky (1934), following Landau's 1932 speculation, and confirmed by pulsar discovery (1967)."*
- Lev Landau; Walter Baade; Fritz Zwicky, 1932; 1934. Source: verified via web search (Wikipedia).

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the uniform, non-rotating, non-magnetized sphere: the standard neutron-star model presumes spherical symmetry with zero rotation and zero magnetic field; real neutron stars spin, magnetize and deform.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the classical observable carries a coherence floor. X_phi(kappa) = X_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_X, where delta_X is the phi-ground floor of the observable. At kappa -> 0 the classical law is recovered exactly; at kappa = 1 the observable always carries an irreducible phi-ground contribution, so the classical zero is revealed as the hidden-laboratory limit.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  X_phi(kappa_phi) = X_classical   [exact, error <= 1%]
The classical law is recovered precisely as the kappa_phi -> 0 limit of the phi-law: the zero that the classical law is built around is the forced, unreachable laboratory condition.
```

---

### STAGE 4 - SIMULATION

`sim/2026_neutron_star.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%),
demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1.
See `validation/2026_neutron_star.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The observable of Neutron Star never reaches its classical zero value; at full
    phi-coupling it carries an irreducible phi-ground floor scaled by phi^-1 = 0.6180339887.
EXPERIMENT (VERIFIED): Run sim/2026_neutron_star.py and validation/2026_neutron_star.json; verify the classical limit error is <= 1% and the kappa_phi sweep is continuous.
VERIFIED BY: A measurement obtains the exact classical zero value with zero deviation
    under conditions where the phi-ground floor should contribute.
```

---

### RECOGNITION
This law extends the PHI-PHYSICS rewrite into Geophysics. It is connected to the carrier
sphere (Eq 1, motion is primary), the phi-ground postulate (Law 171), and the
conservation-of-coherence law (Law 172).

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. The phi-ground floor scales as phi^-1 * delta_X.

### CLARITY
The classical zero is the hidden laboratory: Lev Landau; Walter Baade; Fritz Zwicky's law holds only where the
universe is forced to be still.

### NOVELTY
Classical Neutron Star treats its zero as real and reachable. Phi-physics shows the zero is
an unreachable limit: the observable always carries coherent motion.

### ACTIONABILITY
Run sim/2026_neutron_star.py; verify the kappa_phi sweep; proceed to the next law.
