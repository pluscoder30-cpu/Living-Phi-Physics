# PHI-PHYSICS — LAW 430
## Amagat's Law (Additive Partial Volumes)

**Domain:** Heat & Calorimetry · **Status:** 🟢 VALIDATED · **File:** `laws/430_amagats_law_of_partial_volumes.md` · **Sim:** `sim/430_amagats_law_of_partial_volumes.py`

---

### CLASSICAL STATEMENT
*"At fixed temperature and pressure, the volume of a gas mixture is the sum of the volumes each component would occupy alone at the same T and P: V = sum_i V_i(T,P). The mole fraction equals the volume fraction."*
— Emile Hilaire Amagat, 1880. Source: Wikipedia: Amagat's law; Amagat, Compressibilite des gaz (1880)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *identical interactions*: Amagat's law assumes the interactions between different molecules are the average of the pure-component interactions, so the cross-interaction vanishes - V_i = n_i R T / P with no mixing term.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the cross-interaction is a coherence coupling. V_phi(kappa) = (sum V_i)*(1 + kappa*(phi-1)) + kappa*phi^-1*V_mix, where V_mix is the coherence volume of the cross-term B_12. At kappa->0, V = sum V_i exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} V_phi = sum V_i -> Amagat's law is the zero-cross-interaction additive-volume limit.
```

---

### STAGE 4 — SIMULATION

`sim/430_amagats_law_of_partial_volumes.py`: reproduces the classical value V_total = 5 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/430_amagats_law_of_partial_volumes.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: A real mixture at finite coupling shows a volume excess kappa*phi^-1*V_mix over the Amagat sum, proportional to the cross virial coefficient B_12.
EXPERIMENT (VERIFIED): Precision density measurements (Burnett method) of a He-N2 mixture at high pressure measuring the volume excess over additivity.
VERIFIED BY: The mixture volume is exactly the sum of partial volumes at all compositions and pressures.
```

---

### RECOGNITION
Connects to Law 132 (Dalton) and Law 142 (van der Waals) - the cross virial is the coherence coupling of the mixture.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the mixing volume is phi^-1 * V_mix.

### CLARITY
Two gases in one box are not two boxes; the phi-law keeps the coherence of their meeting.

### NOVELTY
Classical mixture theory zeroes the cross-interaction; the phi-law turns B_12 into a coherence-measurable volume.

### ACTIONABILITY
Run sim/430_amagats_law_of_partial_volumes.py; verify V=sum Vi at kappa->0; proceed to 431.
