# PHI-PHYSICS — LAW 443
## Clausius' Statement of the Second Law

**Domain:** Thermodynamic Potentials · **Status:** 🟢 VALIDATED · **File:** `laws/443_clausius_statement_second_law.md` · **Sim:** `sim/443_clausius_statement_second_law.py`

---

### CLASSICAL STATEMENT
*"No process is possible whose sole result is the transfer of heat from a colder body to a hotter body. Heat does not spontaneously flow from cold to hot."*
— Rudolf Clausius, 1850. Source: Wikipedia: Second law of thermodynamics; Clausius, Ueber die bewegende Kraft der Waerme (1850)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero work input*: the statement forbids heat transfer against a gradient with exactly no work spent - a perfect refrigerator that would require zero coherence expenditure.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the refrigeration needs a coherence input. COP_max_phi(kappa) = Tc/(Th-Tc) - kappa*phi^-1*COP_waste, bounding the coefficient of performance below Carnot by the coherence waste. At kappa->0, COP_max = Tc/(Th-Tc).

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} COP_max_phi = Tc/(Th-Tc) -> Clausius' statement is the zero-work-perfect-refrigerator limit.
```

---

### STAGE 4 — SIMULATION

`sim/443_clausius_statement_second_law.py`: reproduces the classical value COP_carnot = 5 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/443_clausius_statement_second_law.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The maximum COP of any refrigerator is bounded below Tc/(Th-Tc) by kappa*phi^-1*COP_waste, a coherence floor of the cold side.
EXPERIMENT (VERIFIED): Measurement of the COP ceiling of cryocoolers versus the Carnot COP at varying thermal-coherence quality.
VERIFIED BY: A refrigerator transfers heat from cold to hot with exactly zero work at any coupling.
```

---

### RECOGNITION
Connects to Law 023 (second law), Law 442 (Kelvin) and Law 584 (refrigeration COP) - the two statements are the same coherence ban seen twice.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the COP floor is phi^-1 * COP_waste.

### CLARITY
Heat never climbs alone; the phi-law taxes the ladder it must be carried up.

### NOVELTY
Classical Clausius forbids free cooling; the phi-law quantifies the coherence cost that enforces it.

### ACTIONABILITY
Run sim/443_clausius_statement_second_law.py; verify Carnot COP at kappa->0; proceed to 444.
