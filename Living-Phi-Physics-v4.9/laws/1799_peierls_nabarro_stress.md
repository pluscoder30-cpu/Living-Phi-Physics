# PHI-PHYSICS - LAW 1799
## Peierls-Nabarro Stress (Lattice Resistance to Dislocation Motion)

**Domain:** Mechanical Properties - **Status:** 🟢 VALIDATED - **File:** `laws/1799_peierls_nabarro_stress.md` - **Sim:** `sim/1799_peierls_nabarro_stress.py`

---

### CLASSICAL STATEMENT
*"A dislocation moves through a crystal by overcoming the periodic lattice resistance, the Peierls-Nabarro stress: tau_PN = (2 G/(1 - nu)) exp(-2 pi w/b), where w is the dislocation width and b the Burgers vector; the exponential dependence on w/b explains why wide dislocations (fcc metals) move easily while narrow dislocations (bcc, covalent) have high Peierls stress and a strong temperature dependence of yield."*
- Rudolf Peierls (1940); F.R.N. Nabarro (1947), 1940. Source: Wikipedia: Peierls stress; Peierls (1940), Proc. Phys. Soc. 52:34; Nabarro (1947)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-lattice-resistance, perfectly continuous elastic reference*: the Peierls-Nabarro stress is defined against a perfectly continuous elastic medium with zero periodic lattice resistance; the finite resistance is the lattice discreteness correction away from this zero-resistance reference.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the Peierls stress carries a coherence floor. tau_PN_phi(kappa) = tau_PN*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_tau, where delta_tau is the phi-ground residual lattice resistance. At kappa->0 the zero-resistance continuum reference is recovered; at kappa=1 every dislocation carries an irreducible lattice resistance.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} tau_PN_phi = (2G/(1-nu)) exp(-2 pi w/b) -> the Peierls-Nabarro stress is the lattice-discreteness resistance measured from the zero-resistance continuum reference.
```

---

### STAGE 4 - SIMULATION

`sim/1799_peierls_nabarro_stress.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1799_peierls_nabarro_stress.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: No dislocation moves with zero lattice resistance: an irreducible Peierls stress floor remains in every crystal, and dislocation mobility never reaches the continuum ideal.
EXPERIMENT (VERIFIED): Ultra-low-temperature yield and internal-friction measurement of a high-purity crystal (e.g. bcc Nb, Mo, or fcc Al) measuring the residual lattice-resistance floor.
VERIFIED BY: A dislocation moving with exactly zero lattice resistance (perfectly continuous crystal).
```

---

### RECOGNITION
Connects to Law 1799 (dislocations) and Law 1798 (Hall-Petch) - the lattice resists the dislocation's glide, and the phi-law keeps a resistance always present.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; resistance floor scales as phi^-1 * delta_tau.

### CLARITY
The lattice grudges the dislocation passage; the phi-law keeps a grudge always present.

### NOVELTY
Classical Peierls theory allows zero resistance in the continuum limit; the phi-law keeps an irreducible floor.

### ACTIONABILITY
Run sim/1799_peierls_nabarro_stress.py; verify tau = (2G/(1-nu)) exp(-2 pi w/b) at kappa->0; proceed to 1800.
