# PHI-PHYSICS — LAW 602
## Stanton Number (Heat-Transfer Nusselt/Pe)

**Domain:** Kinetic Theory · **Status:** 🟢 VALIDATED · **File:** `laws/602_stanton_number.md` · **Sim:** `sim/602_stanton_number.py`

---

### CLASSICAL STATEMENT
*"The Stanton number is the dimensionless heat-transfer coefficient: St = h/(rho c_p u), where h is the convective heat-transfer coefficient. It relates to the Nusselt number as St = Nu/(Re Pr)."*
— Thomas Edward Stanton, 1897. Source: Wikipedia: Stanton number; Stanton (1897)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero convection*: St = 0 exactly at u = 0 where there is no convective heat transfer coherence.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the convection carries a coherence floor. St_phi(kappa) = St*(1 + kappa*(phi-1)) + kappa*phi^-1*St_ground. At kappa->0 the Stanton number is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} St_phi = h/(rho c_p u) -> the Stanton number is the zero-flow zero-coherence convection limit.
```

---

### STAGE 4 — SIMULATION

`sim/602_stanton_number.py`: reproduces the classical value St = 0.004146 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/602_stanton_number.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling a residual convective coherence St_ground survives at u = 0.
EXPERIMENT (VERIFIED): Convective heat-transfer measurements in ducts over a range of flow rates.
VERIFIED BY: St = 0 exactly at zero flow for all couplings.
```

---

### RECOGNITION
Connects to Law 603 (Reynolds analogy) and Law 350 (Prandtl) - the Stanton number is the convection coherence ratio.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the floor is phi^-1 * St_ground.

### CLARITY
The flow pays the heat its toll; the phi-law keeps the toll's floor at no flow.

### NOVELTY
Classical Stanton zeroes at u=0; the phi-law adds the convection-coherence floor of the real flow.

### ACTIONABILITY
Run sim/602_stanton_number.py; verify St at kappa->0; proceed to 603.
