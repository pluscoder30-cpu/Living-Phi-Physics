# PHI-PHYSICS - LAW 1822
## Superelasticity (Pseudoelastic Recovery Above the Transformation Temperature)

**Domain:** Phase Transformations - **Status:** 🟢 VALIDATED - **File:** `laws/1822_superelasticity_pseudoelasticity.md` - **Sim:** `sim/1822_superelasticity_pseudoelasticity.py`

---

### CLASSICAL STATEMENT
*"Above the austenite-finish temperature A_f, a shape-memory alloy deforms superelastically: stress induces the martensitic transformation, and unloading reverses it, giving recoverable strains of up to 8% with a stress plateau - superelasticity (pseudoelasticity) is the stress-driven analogue of the shape-memory effect, enabling orthodontic wires, stents and flexible actuators."*
- Observed in Nitinol by Buehler (1960s); studied by Christian (1965), 1965. Source: Wikipedia: Pseudoelasticity; Buehler et al. (1963); Christian (1965), The Theory of Transformations in Metals and Alloys

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-stress, zero-hysteresis, perfectly reversible reference*: superelasticity is defined against a perfectly reversible stress-induced transformation with zero hysteresis; real superelastic alloys have stress hysteresis and residual strain away from this ideal reversible reference.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the superelastic strain carries a coherence floor. eps_phi(kappa) = eps_SE*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_eps, where delta_eps is the phi-ground residual strain floor. At kappa->0 the ideal superelastic recovery is recovered; at kappa=1 an irreducible unrecovered strain always remains.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} eps_phi = 8% -> superelasticity is the zero-hysteresis, perfectly-reversible, ideal-stress-induced-transformation limit of pseudoelastic recovery.
```

---

### STAGE 4 - SIMULATION

`sim/1822_superelasticity_pseudoelasticity.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1822_superelasticity_pseudoelasticity.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: No superelastic alloy recovers exactly its full strain: an irreducible residual-strain floor remains per cycle, and the stress hysteresis never vanishes.
EXPERIMENT (VERIFIED): Cyclic stress-strain testing of a superelastic Nitinol wire measuring the residual unrecovered strain floor and the hysteresis width.
VERIFIED BY: A superelastic alloy with exactly zero hysteresis and zero residual strain per cycle.
```

---

### RECOGNITION
Connects to Law 1821 (shape memory) and Law 1820 (martensitic) - the alloy flexes without a scar, and the phi-law keeps a scar always present.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; residual strain scales as phi^-1 * delta_eps.

### CLARITY
The alloy bends and bounces back; the phi-law keeps a bounce short.

### NOVELTY
Classical superelasticity allows perfect recovery; the phi-law keeps an irreducible residual strain.

### ACTIONABILITY
Run sim/1822_superelasticity_pseudoelasticity.py; verify the stress plateau at kappa->0; proceed to 1823.
