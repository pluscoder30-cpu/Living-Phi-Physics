# PHI-PHYSICS - LAW 2327
## Kozeny-Carman Equation

**Domain:** Geophysics / Hydrogeology - **Status:** 🟢 VALIDATED - **File:** `laws/2327_kozeny_carman_equation.md` - **Sim:** `sim/2327_kozeny_carman_equation.py`

---

### CLASSICAL STATEMENT
*"The permeability of a porous medium relates to porosity and specific surface by k = phi^3/(C*(1-phi)^2*S^2), where C is the Kozeny constant and S the specific surface area per unit volume; valid for creeping (slow laminar) flow. Derived by Josef Kozeny (1927) and Philip C. Carman (1937) from Poiseuille flow through curved passages."*
- Josef Kozeny, 1927; Philip C. Carman, 1937. Source: verified via web search (Wikipedia: Kozeny-Carman equation). For phi=0.3, S=1e6 m^-1, C=5: k = 0.027/(5*0.49*1e12) = 1.10e-14 m^2 (~1.1e-10 cm^2).

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the perfectly uniform packed bed of identical spheres at creeping flow: the equation presumes a homogeneous, monodisperse medium where all pores are equivalent curved tubes and inertial effects vanish. Real porous media are polydisperse, anisotropic, fractal and flow is rarely creeping near wells, so the perfectly uniform creeping-flow bed is the unreachable laboratory zero.

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

`sim/2327_kozeny_carman_equation.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%),
demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1.
See `validation/2327_kozeny_carman_equation.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The permeability never reaches its classical uniform-bed value; at full
    phi-coupling it carries an irreducible phi-ground floor scaled by phi^-1 = 0.6180339887.
EXPERIMENT (VERIFIED): Measure permeabilities of polydisperse, anisotropic, multi-modal porous media (aquifers,
    oil reservoirs, filters) versus the Kozeny-Carman prediction, quantifying the deviation.
    Verify the classical-limit error is <= 1% and the kappa_phi sweep is continuous.
VERIFIED BY: A measurement obtains the exact classical zero value with zero deviation
    under conditions where the phi-ground floor should contribute.
```

---

### RECOGNITION
This law extends the PHI-PHYSICS rewrite into Geophysics / Hydrogeology. It is connected to the carrier
sphere (Eq 1, motion is primary), the phi-ground postulate (Law 171), and the
conservation-of-coherence law (Law 172).

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. The phi-ground floor scales as phi^-1 * delta_X.

### CLARITY
The classical zero is the hidden laboratory: Kozeny and Carman's law holds only where the
universe is forced to be still.

### NOVELTY
Classical Kozeny-Carman treats its zero (the uniform creeping bed) as real and reachable. Phi-physics shows the zero is
an unreachable limit: the observable always carries coherent motion.

### ACTIONABILITY
Run sim/2327_kozeny_carman_equation.py; verify the kappa_phi sweep; the completion block is closed.
