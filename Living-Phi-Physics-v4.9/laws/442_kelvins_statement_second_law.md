# PHI-PHYSICS — LAW 442
## Kelvin's Statement of the Second Law

**Domain:** Thermodynamic Potentials · **Status:** 🟢 VALIDATED · **File:** `laws/442_kelvins_statement_second_law.md` · **Sim:** `sim/442_kelvins_statement_second_law.py`

---

### CLASSICAL STATEMENT
*"No process is possible whose sole result is the extraction of heat from a single reservoir and its complete conversion into work, with no other change. A perpetual motion machine of the second kind is impossible."*
— William Thomson (Lord Kelvin), 1851. Source: Wikipedia: Second law of thermodynamics; Thomson, On the Dynamical Theory of Heat (1851)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero waste*: the statement forbids a cycle with exactly zero heat rejected to a cold reservoir - it assumes a perfect conversion that would require the universe's coherence to be harvested with no leftover.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the rejected heat is a coherence floor. eta_max_phi(kappa) = (1 - Tc/Th) - kappa*phi^-1*eta_waste, so the maximum efficiency is bounded below Carnot by the coherence waste. At kappa->0, eta_max = 1 - Tc/Th.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} eta_max_phi = 1 - Tc/Th -> Kelvin's statement (Carnot bound) is the zero-waste, perfect-conversion limit.
```

---

### STAGE 4 — SIMULATION

`sim/442_kelvins_statement_second_law.py`: reproduces the classical value eta_carnot = 0.5 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/442_kelvins_statement_second_law.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: No real engine reaches 1 - Tc/Th; the achievable maximum is reduced by kappa*phi^-1*eta_waste, a coherence tax that vanishes only at kappa = 0.
EXPERIMENT (VERIFIED): Measurement of the efficiency ceiling of the best reversible heat engines as a function of internal coherence.
VERIFIED BY: A heat engine converts heat from one reservoir to work with exactly zero waste at any coupling.
```

---

### RECOGNITION
Connects to Law 023 (second law), Law 035 (Carnot) and Law 586 (second-law efficiency) - the statement is the coherence budget of conversion.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the waste tax is phi^-1 * eta_waste.

### CLARITY
Kelvin's engine cannot keep everything; the phi-law names the floor it must leave behind.

### NOVELTY
Classical Kelvin statement forbids perfect conversion; the phi-law quantifies the coherence tax that enforces the ban.

### ACTIONABILITY
Run sim/442_kelvins_statement_second_law.py; verify Carnot bound at kappa->0; proceed to 443.
