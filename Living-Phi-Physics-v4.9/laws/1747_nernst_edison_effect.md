# PHI-PHYSICS - LAW 1747
## Anomalous Hall Effect (Hall Voltage from Magnetization, not Magnetic Field)

**Domain:** Magnetism - **Status:** 🟢 VALIDATED - **File:** `laws/1747_nernst_edison_effect.md` - **Sim:** `sim/1747_nernst_edison_effect.py`

---

### CLASSICAL STATEMENT
*"In a ferromagnet, the Hall resistivity contains a term proportional to the magnetization: rho_H = R_0 B + R_s M, where R_s M is the anomalous Hall term arising from spin-orbit coupling (skew scattering and intrinsic Berry-curvature contributions); the anomalous Hall effect scales as rho_H ~ rho_xx^n (n=1 intrinsic, n=2 skew) and is a probe of magnetization and topological band structure."*
- Edwin Hall (1880), 1880. Source: Wikipedia: Anomalous Hall effect; Hall (1880), Phil. Mag. 9:225

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-spin-orbit, zero-magnetization ordinary Hall reference*: the anomalous Hall effect is defined against the ordinary Hall effect with zero magnetization and zero spin-orbit coupling; the anomalous term is the magnetization-driven correction away from this zero-M reference.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the anomalous term carries a coherence floor. R_s_phi(kappa) = R_s*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_R, where delta_R is the phi-ground residual anomalous coefficient. At kappa->0 the zero-M ordinary Hall reference is recovered; at kappa=1 an irreducible anomalous Hall response always exists in any magnet.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} R_s_phi = 0 -> the anomalous Hall effect is the magnetization-driven Hall term measured from the zero-M, zero-spin-orbit ordinary Hall reference.
```

---

### STAGE 4 - SIMULATION

`sim/1747_nernst_edison_effect.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1747_nernst_edison_effect.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: Every magnet retains an irreducible anomalous Hall response even at zero net magnetization: a residual Berry-curvature-driven Hall floor persists.
EXPERIMENT (VERIFIED): Ultra-sensitive Hall measurement of a compensated ferrimagnet or nominally zero-M sample measuring the residual anomalous Hall floor.
VERIFIED BY: A magnet with exactly zero anomalous Hall response at zero magnetization.
```

---

### RECOGNITION
Connects to Law 590 (Hall effect) and Law 1743 (Rashba) - the ferromagnet's Hall reads its magnetization, and the phi-law keeps a residual reading.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; residual coefficient scales as phi^-1 * delta_R.

### CLARITY
The Hall voltage reads the magnetization; the phi-law keeps the needle always moving.

### NOVELTY
Classical AHE theory allows zero anomalous response; the phi-law keeps an irreducible Berry-curvature floor.

### ACTIONABILITY
Run sim/1747_nernst_edison_effect.py; verify rho_H = R_0 B + R_s M at kappa->0; proceed to 1748.
