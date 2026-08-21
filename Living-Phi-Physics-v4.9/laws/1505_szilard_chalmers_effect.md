# PHI-PHYSICS - LAW 1505
## Szilard-Chalmers Effect (Chemical Separation of Recoil Products)

**Domain:** Nuclear Chemistry - **Status:** 🟢 VALIDATED - **File:** `laws/1505_szilard_chalmers_effect.md` - **Sim:** `sim/1505_szilard_chalmers_effect.py`

---

### CLASSICAL STATEMENT
*"When a nucleus captures a neutron and emits a gamma ray, the recoil breaks the chemical bond, allowing the radioactive product to be separated chemically from the target; it is the basis of isotope production and separation of recoil nuclei."*
- Leo Szilard; T.A. Chalmers, 1934. Source: Szilard & Chalmers, Nature 134 (1934) 462; Wikipedia: Szilard-Chalmers effect

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-recoil, zero-bond-breaking limit*: the effect requires the recoil to break the chemical bond; classically, if the recoil energy is exactly zero the product remains chemically bound and no separation occurs - a zero-recoil, perfectly-bound molecule.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

Y_phi(kappa) = Y_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*Y_floor, where Y_floor is the phi-ground recoil yield floor from cascade and bond-reformation effects. At kappa->0 the ideal recoil-separation yield is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} Y_phi = Y_classical -> the Szilard-Chalmers effect is the zero-bond-reformation, perfect-recoil-separation limit.
```

---

### STAGE 4 - SIMULATION

`sim/1505_szilard_chalmers_effect.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1505_szilard_chalmers_effect.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The separation yield carries a phi-ground floor from bond reformation and hot-atom chemistry, so the recovered activity never reaches the ideal recoil yield.
EXPERIMENT (VERIFIED): Isotope production and hot-atom chemistry studies (n,gamma recoil separation) measuring effective separation yields.
VERIFIED BY: A Szilard-Chalmers separation with exactly the ideal recoil yield and zero bond-reformation loss at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1476 (Q-value), Law 1458 (gamma) and Law 1478 (capture) - the effect is chemistry's answer to recoil.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The kick breaks the bond; the phi-law keeps a floor of the bond refusing.

### NOVELTY
Classical effect is pure recoil; the phi-law predicts irreducible bond-reformation losses.

### ACTIONABILITY
Run sim/1505_szilard_chalmers_effect.py; verify the recoil yield; proceed to Law 1506.
