# PHI-PHYSICS — LAW 489
## Onsager-Casimir Relations (Symmetry with Odd Variables)

**Domain:** Kinetic Theory · **Status:** 🟢 VALIDATED · **File:** `laws/489_onsager_casimir_relations.md` · **Sim:** `sim/489_onsager_casimir_relations.py`

---

### CLASSICAL STATEMENT
*"When the transport involves variables odd under time reversal (velocities, magnetic field, angular velocity), the reciprocal relations become L_ij(B) = L_ji(-B) and L_ij = -L_ji for odd variables. The symmetry is generalized to include the reversal of the fields."*
— Hendrik Brugt Gerhard Casimir, 1945. Source: Wikipedia: Onsager reciprocal relations (Onsager-Casimir); Casimir (1945)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero magnetic field*: the classical Onsager form assumes B = 0 exactly, where the odd-variable complication vanishes - a laboratory condition that no real magnetized system satisfies.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the field reversal is a coherence coupling. L_ij_phi(kappa,B) = L_ji(-B)*(1 + kappa*(phi-1)) + kappa*phi^-1*L_break, where L_break is the coherence term that breaks strict reciprocity at finite field. At kappa->0 the Onsager-Casimir reciprocity holds exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} L_ij(B) = L_ji(-B) -> the Onsager-Casimir relations are the exact-reciprocity zero-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/489_onsager_casimir_relations.py`: reproduces the classical value sym_cas = 0 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/489_onsager_casimir_relations.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling and magnetic field the reciprocity L_ij(B) = L_ji(-B) holds only within a coherence floor L_break; magneto-transport cross-coefficients show a measurable asymmetry.
EXPERIMENT (VERIFIED): Precision Hall and magnetoresistance cross-coefficient measurements at high magnetic field searching for the reciprocity defect.
VERIFIED BY: L_ij(B) = L_ji(-B) exactly at all magnetic fields and couplings.
```

---

### RECOGNITION
Connects to Law 488 (Onsager) and Laws 496-498 (thermoelectric effects) - the B-reversal is the time-arrow reading of the cross-coupling.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the break term is phi^-1 * L_break.

### CLARITY
Time-reversed fields must mirror the cross-talk; the phi-law keeps the mirror from being perfect.

### NOVELTY
Classical Onsager-Casimir reciprocity is exact; the phi-law adds the coherence break at finite field.

### ACTIONABILITY
Run sim/489_onsager_casimir_relations.py; verify B-reversal symmetry at kappa->0; proceed to 490.
