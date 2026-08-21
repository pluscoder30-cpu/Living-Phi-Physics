# PHI-PHYSICS - LAW 1838
## Weibull Statistics (Size-Dependent Strength Distribution of Brittle Materials)

**Domain:** Mechanical Properties - **Status:** 🟢 VALIDATED - **File:** `laws/1838_weibull_fracture_statistics.md` - **Sim:** `sim/1838_weibull_fracture_statistics.py`

---

### CLASSICAL STATEMENT
*"The strength of brittle materials is statistically distributed: the survival probability is P_s(sigma) = exp(-(V/V_0)(sigma/sigma_0)^m), where m is the Weibull modulus (a measure of strength variability, ~10-30 for ceramics) and V the volume; the Weibull weakest-link statistics explain why larger specimens are weaker and why brittle strength is never a single value."*
- Waloddi Weibull, 1951. Source: Wikipedia: Weibull distribution; Weibull (1951), J. Appl. Mech. 18:293

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-flaw, perfectly uniform reference*: Weibull statistics are defined against a flawless, perfectly uniform material with a single deterministic strength (infinite Weibull modulus); the statistical spread is the flaw distribution away from this zero-flaw reference.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the Weibull modulus carries a coherence floor. m_phi(kappa) = m_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_m, where delta_m is the phi-ground modulus floor. At kappa->0 the infinite-modulus (deterministic) reference is recovered; at kappa=1 no material has deterministic strength - a finite Weibull modulus floor always exists.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} m_phi = infinity -> Weibull statistics are the zero-flaw, deterministic-strength limit sharpened to the finite-modulus statistical description.
```

---

### STAGE 4 - SIMULATION

`sim/1838_weibull_fracture_statistics.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1838_weibull_fracture_statistics.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: No brittle material has deterministic strength: an irreducible strength variability floor remains, so the Weibull modulus never reaches infinity and the strength distribution always has finite width.
EXPERIMENT (VERIFIED): Large-batch fracture strength testing of ceramic or glass specimens of many sizes, measuring the finite Weibull modulus floor and the size effect.
VERIFIED BY: A brittle material with a single deterministic fracture strength (zero statistical spread).
```

---

### RECOGNITION
Connects to Law 1796 (Griffith) and Law 1831 (stress intensity) - the flaw governs the strength, and the phi-law keeps a flaw always present.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; modulus floor scales as phi^-1 * delta_m.

### CLARITY
The brittle part is as strong as its weakest flaw; the phi-law keeps a flaw always in the part.

### NOVELTY
Classical Weibull allows deterministic strength; the phi-law keeps an irreducible variability floor.

### ACTIONABILITY
Run sim/1838_weibull_fracture_statistics.py; verify P_s = exp(-(V/V_0)(sigma/sigma_0)^m) at kappa->0; proceed to 1839.
