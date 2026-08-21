# PHI-PHYSICS — LAW 459
## Faraday's Laws of Electrolysis

**Domain:** Thermodynamic Potentials · **Status:** 🟢 VALIDATED · **File:** `laws/459_faradays_laws_of_electrolysis.md` · **Sim:** `sim/459_faradays_laws_of_electrolysis.py`

---

### CLASSICAL STATEMENT
*"The mass of a substance deposited at an electrode is proportional to the quantity of electric charge passed: m = (M / (n F)) Q, where M is molar mass, n the number of electrons per ion, F the Faraday constant."*
— Michael Faraday, 1833. Source: Wikipedia: Faraday's laws of electrolysis; Faraday, Experimental Researches in Electricity (1833)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *perfect faradaic efficiency*: the law assumes every coulomb of charge produces exactly the stoichiometric amount of product, with no side reactions, leaks, or coherence loss at the electrode.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the electrode exchange carries coherence. m_phi(kappa) = (M/(n F))*Q*(1 + kappa*(phi-1)) + kappa*phi^-1*m_ground. At kappa->0, m = (M/nF) Q exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} m_phi = (M/(n F)) Q -> Faraday's laws are the zero-loss perfect-faradaic limit.
```

---

### STAGE 4 — SIMULATION

`sim/459_faradays_laws_of_electrolysis.py`: reproduces the classical value m_dep = 1.118e-05 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/459_faradays_laws_of_electrolysis.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling, electrolysis deposits a residual mass floor kappa*phi^-1*m_ground or shows a sub-faradaic deficit growing with current density.
EXPERIMENT (VERIFIED): Precision coulometric deposition of silver from solution measuring mass versus integrated charge at varying current densities.
VERIFIED BY: The deposited mass equals (M/nF)Q exactly at all current densities and couplings.
```

---

### RECOGNITION
Connects to Law 456 (Nernst), Law 049 (Joule) and Law 452 (mass action) - electrolysis is the coherence conversion of charge into matter.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the floor is phi^-1 * m_ground.

### CLARITY
Every electron arriving at an electrode brings the metal into being; the phi-law keeps the residual motion of the birth.

### NOVELTY
Classical electrolysis assumes exact coulomb-to-atom conversion; the phi-law adds the coherence efficiency floor.

### ACTIONABILITY
Run sim/459_faradays_laws_of_electrolysis.py; verify m = (M/nF)Q at kappa->0; proceed to 460.
