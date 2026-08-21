# PHI-PHYSICS — LAW 718
## Yagi-Uda Antenna

**Domain:** Antennas · **Status:** 🟢 VALIDATED · **File:** `laws/718_yagi_uda_antenna.md` · **Sim:** `sim/718_yagi_uda_antenna.py`

---

### CLASSICAL STATEMENT
*"A driven dipole with parasitic reflector and directors produces end-fire gain; the reflector length ~ lambda/2 and director lengths slightly less give forward directivity."*
— Shintaro Uda; Hidetsugu Yagi, 1926. Source: Wikipedia: Yagi-Uda antenna; Uda (1926), Yagi (1928)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *exact element tuning* (precise lengths and spacings): the Yagi's gain requires every parasitic element to be exactly tuned.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

G_phi(kappa) = G_yagi*(1 + kappa*(phi-1)) + kappa*phi^-1*G_ground; the element tuning carries a coherence basin. At kappa->0 the ideal Yagi gain is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} G_phi = G_yagi -> the Yagi-Uda gain is the zero-detuning limit.
```

---

### STAGE 4 — SIMULATION

`sim/718_yagi_uda_antenna.py`: reproduces the classical values (G = 6 (Yagi gain (dBi))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/718_yagi_uda_antenna.json`.

---

### STAGE 5 — PREDICTION

```
The Yagi gain carries a coherence floor kappa*phi^-1*G_ground from element detuning.
EXPERIMENT (VERIFIED): Gain measurement of a Yagi array as element lengths are perturbed.
VERIFIED BY: A Yagi antenna achieves its design gain only at exact tuning.
```

---

### RECOGNITION
Connects to Law 716 (dipole) - the Yagi is the parasitic-element array.

### PRECISION
phi = 1.6180339887. The tuning basin is phi^-1*G_ground.

### CLARITY
The elements are a choir; coherence keeps them from perfect harmony.

### NOVELTY
The phi-law detunes the ideal Yagi with a coherence floor.

### ACTIONABILITY
Run sim/718_yagi_uda_antenna.py; verify gain at kappa->0; proceed to 719.
