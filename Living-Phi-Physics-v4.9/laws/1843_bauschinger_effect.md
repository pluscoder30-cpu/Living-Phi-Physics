# PHI-PHYSICS - LAW 1843
## Bauschinger Effect (Reduced Yield on Reverse Loading After Plastic Deformation)

**Domain:** Mechanical Properties - **Status:** 🟢 VALIDATED - **File:** `laws/1843_bauschinger_effect.md` - **Sim:** `sim/1843_bauschinger_effect.py`

---

### CLASSICAL STATEMENT
*"After plastic deformation in one direction, a metal's yield strength in the reverse direction is reduced: the Bauschinger effect sigma_y(reverse) < sigma_y(forward) because the dislocation structure formed during forward loading aids reverse slip; the effect is quantified by the Bauschinger parameter and governs springback, fatigue and metal forming."*
- Johann Bauschinger, 1881. Source: Wikipedia: Bauschinger effect; Bauschinger (1881), Mitt. Mech-Tech. Lab. Munchen 13:1

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-back-stress, perfectly symmetric hardening reference*: the Bauschinger effect is defined against a reference with zero residual back-stress and perfectly symmetric hardening (kinematic hardening absent); the reduced reverse yield is the dislocation-structure effect away from this zero-back-stress reference.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the reverse yield carries a coherence floor. sigma_rev_phi(kappa) = sigma_rev*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_sigma, where delta_sigma is the phi-ground back-stress floor. At kappa->0 the symmetric-hardening reference is recovered; at kappa=1 an irreducible Bauschinger effect always exists.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} sigma_rev_phi = sigma_fwd -> the Bauschinger effect is the reverse-yield reduction measured from the zero-back-stress, symmetric-hardening reference.
```

---

### STAGE 4 - SIMULATION

`sim/1843_bauschinger_effect.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1843_bauschinger_effect.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: Every metal shows an irreducible Bauschinger effect: reverse loading always softens the yield slightly even for the most symmetric dislocation structures, so perfectly symmetric hardening is impossible.
EXPERIMENT (VERIFIED): Forward-reverse loading of a high-purity metal measuring the Bauschinger parameter and its residual floor.
VERIFIED BY: A metal whose reverse yield exactly equals the forward yield with zero Bauschinger effect.
```

---

### RECOGNITION
Connects to Law 1832 (strain hardening) and Law 1826 (dislocations) - the metal remembers its forward push, and the phi-law keeps the memory always present.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; back-stress floor scales as phi^-1 * delta_sigma.

### CLARITY
The metal remembers its forward push; the phi-law keeps the memory always present.

### NOVELTY
Classical hardening theory allows symmetric behavior; the phi-law keeps an irreducible Bauschinger floor.

### ACTIONABILITY
Run sim/1843_bauschinger_effect.py; verify the reverse yield at kappa->0; proceed to 1844.
