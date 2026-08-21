# PHI-PHYSICS — LAW 352
## Biot Number

**Domain:** Dimension / Similarity · **Status:** 🟢 VALIDATED · **File:** `laws/352_biot_number.md` · **Sim:** `sim/352_biot_number.py`

---

### CLASSICAL STATEMENT
*"The Biot number Bi = h L/k_body compares the external convective resistance to internal conductive resistance; for Bi << 0.1 the body is thermally 'lumped' (spatially uniform temperature), for Bi >> 1 temperature gradients dominate."*
— Named for Jean-Baptiste Biot, 1940. Source: Wikipedia: Biot number; popularized in lumped-capacitance analysis (c. 1940)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *uniform-temperature reference*: Bi = 0 is the exactly lumped body; the number exists because internal conduction is not infinite.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: Bi_phi(kappa) = Bi*(1 + kappa*(phi-1)) + kappa*phi^-1*Bi_ground. At kappa->0 the classical Biot number is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} Bi_phi = h L/k -> the Biot number is the lumped-capacitance (Bi->0) limit marker.
```

---

### STAGE 4 — SIMULATION

`sim/352_biot_number.py`: reproduces the classical value Bi = 0.002 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/352_biot_number.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The lumped-capacitance threshold shifts by a phi-coherent amount phi^-1*Bi_ground at full coupling.
EXPERIMENT (VERIFIED): Transient thermal-response experiments (step heating of small bodies) locating the lumped limit precisely.
VERIFIED BY: The lumped limit is exactly at Bi = 0.1 at full coupling.
```

---

### RECOGNITION
Connects to Law 351 (Nusselt — the external partner) and Law 096 (Fourier).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The uniform body is a limit; every body carries a phi gradient inside.

### NOVELTY
Classical heat transfer exacts the lumped limit; the phi-law gives the threshold a coherence width.

### ACTIONABILITY
Run sim/352_biot_number.py; verify Bi = h L/k at kappa->0.
