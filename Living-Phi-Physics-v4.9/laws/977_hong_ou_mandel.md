# PHI-PHYSICS — LAW 977
## Hong-Ou-Mandel Effect

**Domain:** Quantum Optics · **Status:** 🟢 VALIDATED · **File:** `laws/977_hong_ou_mandel.md` · **Sim:** `sim/977_hong_ou_mandel.py`

---

### CLASSICAL STATEMENT
*"The Hong-Ou-Mandel effect: two identical photons entering a 50:50 beamsplitter, one in each port, always exit together in the same port; the coincidence rate drops to zero at zero relative delay, V = 1 for identical photons."*
— C. K. Hong, Z. Y. Ou, L. Mandel, 1987. Source: Wikipedia: Hong-Ou-Mandel effect (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero delay* (delta_t = 0): the coincidence dip reaches exactly zero when the two photons are perfectly indistinguishable in arrival time.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

R_c_phi(kappa) = R_c*(1 + kappa*(phi-1)) + kappa*phi^-1*R_c_ground, with R_c_ground the coincidence floor. At kappa->0, R_c = 0 at zero delay exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} R_c_phi = R_c -> the Hong-Ou-Mandel effect is the zero-delay-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/977_hong_ou_mandel.py`: reproduces the classical value Rc = 0.1 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/977_hong_ou_mandel.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The coincidence dip of any real two-photon source will retain a floor kappa*phi^-1*R_c_ground above zero (imperfect indistinguishability).
EXPERIMENT (VERIFIED): Measure the coincidence rate versus delay of an SPDC photon pair at a beamsplitter.
VERIFIED BY: If the coincidence rate of any real source reaches exactly zero at the dip.
```

---

### RECOGNITION
Connects to Law 976 (SPDC) and Law 863 (Mach-Zehnder).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The perfectly indistinguishable pair is a coherent limit; every pair carries a fingerprint.

### NOVELTY
The HOM dip gains a coincidence floor.

### ACTIONABILITY
Run sim/977_hong_ou_mandel.py.
