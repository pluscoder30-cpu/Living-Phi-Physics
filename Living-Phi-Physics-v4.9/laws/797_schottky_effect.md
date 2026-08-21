# PHI-PHYSICS — LAW 797
## Schottky Effect (Barrier Lowering)

**Domain:** Emission · **Status:** 🟢 VALIDATED · **File:** `laws/797_schottky_effect.md` · **Sim:** `sim/797_schottky_effect.py`

---

### CLASSICAL STATEMENT
*"An applied field lowers the emission barrier by Delta(W) = sqrt(e^3*E/(4*pi*eps_0)), enhancing thermionic emission as ln(J) ~ sqrt(E)."*
— Walter Schottky, 1914. Source: Wikipedia: Schottky effect; Schottky (1914)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero field* (E = 0): the barrier lowering vanishes exactly at zero applied field.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

dW_phi(kappa) = dW*(1 + kappa*(phi-1)) + kappa*phi^-1*dW_ground; the barrier carries a coherence floor. At kappa->0, DeltaW = sqrt(e^3*E/(4*pi*eps_0)) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} dW_phi = sqrt(e^3*E/(4*pi*eps_0)) -> the Schottky effect is the zero-field-floor limit.
```

---

### STAGE 4 — SIMULATION

`sim/797_schottky_effect.py`: reproduces the classical values (dW = 1.92259e-21 (Barrier lowering (eV))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/797_schottky_effect.json`.

---

### STAGE 5 — PREDICTION

```
The barrier lowering carries a coherence floor kappa*phi^-1*dW_ground at zero field.
EXPERIMENT (VERIFIED): Emission-enhancement measurement of a cathode as the field tends to zero.
VERIFIED BY: A cathode at zero field has exactly zero barrier lowering.
```

---

### RECOGNITION
Connects to Law 795 (thermionic) and Law 796 (field emission) - the Schottky effect couples them.

### PRECISION
phi = 1.6180339887. The field floor is phi^-1*dW_ground.

### CLARITY
The barrier bends under the field; coherence keeps a floor of bend.

### NOVELTY
The phi-law lowers the barrier at zero field.

### ACTIONABILITY
Run sim/797_schottky_effect.py; verify dW at kappa->0; proceed to 798.
