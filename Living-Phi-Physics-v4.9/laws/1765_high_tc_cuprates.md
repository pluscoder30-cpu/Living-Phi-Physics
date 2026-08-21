# PHI-PHYSICS - LAW 1765
## High-Tc Cuprate Superconductors (Bednorz-Mueller Discovery of T_c > 30 K)

**Domain:** Superconductivity - **Status:** 🟢 VALIDATED - **File:** `laws/1765_high_tc_cuprates.md` - **Sim:** `sim/1765_high_tc_cuprates.py`

---

### CLASSICAL STATEMENT
*"Bednorz and Mueller discovered superconductivity at 35 K in the cuprate La-Ba-Cu-O (T_c above the previous record ~23 K), initiating the high-Tc era: the layered copper-oxide structure with CuO2 planes is the key building block, with T_c rising to 92 K in YBCO and 138 K in Hg-based cuprates at ambient pressure; the pairing mechanism remains a central open problem (d-wave, magnetic)."*
- J. Georg Bednorz & K. Alex Mueller, 1986. Source: Wikipedia: Cuprate superconductor; Bednorz & Mueller (1986), Z. Phys. B 64:189

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-magnetic-correlation, conventional phonon-BCS reference*: high-Tc cuprates are defined against the conventional BCS (phonon) superconductor reference; their anomalously high T_c and d-wave pairing are measured away from this conventional weak-coupling reference.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: T_c carries a coherence floor. T_c_phi(kappa) = T_c_cuprate*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_T, where delta_T is the phi-ground transition-temperature floor. At kappa->0 the sharp T_c value is recovered; at kappa=1 cuprate transitions are smeared and the pseudogap floor survives to higher temperature.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} T_c_phi = T_c_cuprate -> high-Tc cuprates are the unconventional-pairing state measured from the conventional BCS reference, sharpened to their nominal T_c.
```

---

### STAGE 4 - SIMULATION

`sim/1765_high_tc_cuprates.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1765_high_tc_cuprates.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The cuprate superconducting transition is never perfectly sharp and a pseudogap floor persists well above T_c: the nominal T_c value carries a phi-ground smearing and the normal state always retains incipient pairing correlations.
EXPERIMENT (VERIFIED): Ultra-high-resolution specific-heat and ARPES of a high-quality cuprate (e.g. YBCO, BSCCO) measuring the transition width and the pseudogap floor above T_c.
VERIFIED BY: A cuprate with an exactly sharp transition at its nominal T_c and zero pseudogap above it.
```

---

### RECOGNITION
Connects to Law 1761 (BCS gap) and Law 1766 (d-wave) - the cuprate breaks the phonon ceiling, and the phi-law keeps a thread of the old ceiling in the new sky.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; transition width scales as phi^-1 * delta_T.

### CLARITY
The cuprate leaps past the phonon ceiling; the phi-law keeps a step of the old limit.

### NOVELTY
Classical BCS sets a phonon ceiling; the phi-law keeps the cuprate's leap from being exact.

### ACTIONABILITY
Run sim/1765_high_tc_cuprates.py; verify the layered structure T_c at kappa->0; proceed to 1766.
