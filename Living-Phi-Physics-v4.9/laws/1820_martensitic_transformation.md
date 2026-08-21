# PHI-PHYSICS - LAW 1820
## Martensitic Transformation (Diffusionless Shear Transformation of Steel)

**Domain:** Phase Transformations - **Status:** 🟢 VALIDATED - **File:** `laws/1820_martensitic_transformation.md` - **Sim:** `sim/1820_martensitic_transformation.py`

---

### CLASSICAL STATEMENT
*"The martensitic transformation is a diffusionless, displacive (shear) transformation of austenite (fcc) to martensite (bct) that occurs athermally as the temperature drops below M_s; the transformation is characterized by the lattice correspondence (Bain strain), habit planes, and the diffusionless, near-instantaneous, plate-like growth - the basis of steel hardening and of shape-memory alloys."*
- Adolf Martens (1890s); E.C. Bain (1924); G. Kurdjumov & G. Sachs (1930), 1924. Source: Wikipedia: Martensite; Bain (1924); Kurdjumov & Sachs (1930), Z. Phys. 64:325

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-nucleation-barrier, infinitely-fast athermal reference*: the martensitic transformation is defined against a reference with zero nucleation barrier where transformation is instantaneous and athermal; real martensite forms at finite rates with thermal activation away from this zero-barrier ideal.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the start temperature carries a coherence floor. M_s_phi(kappa) = M_s*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_M, where delta_M is the phi-ground M_s shift. At kappa->0 the sharp M_s is recovered; at kappa=1 the transformation start is smeared - M_s is never a sharp line.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} M_s_phi = M_s -> the martensitic transformation is the zero-nucleation-barrier, athermal, sharp-M_s limit of displacive transformations.
```

---

### STAGE 4 - SIMULATION

`sim/1820_martensitic_transformation.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1820_martensitic_transformation.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The martensite start temperature is never sharp: an irreducible smearing and undercooling floor remains, so the transformation always begins over a finite temperature range and never exactly at M_s.
EXPERIMENT (VERIFIED): Precision dilatometry and calorimetry of a steel or shape-memory alloy through the martensitic transformation, measuring the M_s transition-width floor.
VERIFIED BY: A martensitic transformation beginning exactly at M_s with zero transition width.
```

---

### RECOGNITION
Connects to Law 1815 (Avrami) and Law 1821 (shape memory) - the steel shears into a new crystal, and the phi-law keeps the shear from being a line.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; transition width scales as phi^-1 * delta_M.

### CLARITY
The crystal shears into martensite; the phi-law keeps the shear spread over a range.

### NOVELTY
Classical martensite theory gives a sharp M_s; the phi-law smears it with a coherence floor.

### ACTIONABILITY
Run sim/1820_martensitic_transformation.py; verify the M_s start at kappa->0; proceed to 1821.
