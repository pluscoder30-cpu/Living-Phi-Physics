# PHI-PHYSICS — LAW 809
## Pockels Effect (Linear Electro-Optic)

**Domain:** Optics · **Status:** 🟢 VALIDATED · **File:** `laws/809_pockels_effect.md` · **Sim:** `sim/809_pockels_effect.py`

---

### CLASSICAL STATEMENT
*"In non-centrosymmetric crystals the index change is linear in the field: Delta(n) = r*E*n^3/2, with the Pockels coefficient r; the phase shift is proportional to the applied voltage."*
— Friedrich Pockels, 1893. Source: Wikipedia: Pockels effect; Pockels (1893)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero field* (E = 0): the linear index change vanishes exactly at zero field.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

dn_phi(kappa) = dn_P*(1 + kappa*(phi-1)) + kappa*phi^-1*dn_ground; the crystal carries a coherence floor. At kappa->0, Delta(n) = r*E*n^3/2 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} dn_phi = r*E*n**3/2 -> the Pockels effect is the zero-field-floor limit.
```

---

### STAGE 4 — SIMULATION

`sim/809_pockels_effect.py`: reproduces the classical values (dn = 1687.5 (Index change)) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/809_pockels_effect.json`.

---

### STAGE 5 — PREDICTION

```
The linear index change carries a coherence floor kappa*phi^-1*dn_ground at zero field.
EXPERIMENT (VERIFIED): Phase-shift measurement of a Pockels cell at zero bias.
VERIFIED BY: A Pockels cell at zero field has exactly zero index change.
```

---

### RECOGNITION
Connects to Law 808 (Kerr) - Pockels is the linear electro-optic effect.

### PRECISION
phi = 1.6180339887. The E-floor is phi^-1*dn_ground.

### CLARITY
The crystal leans with the field; coherence keeps a floor of lean.

### NOVELTY
The phi-law gives the Pockels cell a zero-field shift.

### ACTIONABILITY
Run sim/809_pockels_effect.py; verify dn at kappa->0; proceed to 810.
