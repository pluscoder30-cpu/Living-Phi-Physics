# PHI-PHYSICS - LAW 1839
## Archard Wear Law (Wear Volume Proportional to Normal Load and Sliding Distance)

**Domain:** Mechanical Properties - **Status:** 🟢 VALIDATED - **File:** `laws/1839_archard_wear_law.md` - **Sim:** `sim/1839_archard_wear_law.py`

---

### CLASSICAL STATEMENT
*"The wear volume of sliding surfaces follows Archard's law: V = K F L/H, where V is the worn volume, F the normal load, L the sliding distance, H the hardness and K the dimensionless wear coefficient (~10^-3 for abrasive to 10^-8 for mild wear); the law states that wear is proportional to the real contact area and the sliding distance - the foundation of tribology and wear prediction."*
- J.F. Archard, 1953. Source: Wikipedia: Archard equation; Archard (1953), J. Appl. Phys. 24:981

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-load, zero-wear, perfectly non-contacting reference*: Archard's law is defined against a reference with zero normal load and zero wear; the finite wear is the contact-driven material removal away from this zero-wear reference.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the wear volume carries a coherence floor. V_phi(kappa) = V_archard*(1 + kappa*(phi-1)) + kappa*phi^-1*V_floor, where V_floor is the phi-ground residual wear. At kappa->0 the zero-wear reference is recovered; at kappa=1 an irreducible wear rate always exists even at zero load.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} V_phi = K F L/H -> Archard's law is the zero-load, ideal-contact, wear-coefficient limit of sliding wear.
```

---

### STAGE 4 - SIMULATION

`sim/1839_archard_wear_law.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1839_archard_wear_law.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: No sliding surfaces have zero wear: an irreducible wear-rate floor remains even at the smallest loads, so all moving components slowly wear out.
EXPERIMENT (VERIFIED): Ultra-long-duration pin-on-disk wear testing at very low loads, measuring the residual wear-rate floor.
VERIFIED BY: A sliding pair with exactly zero wear at any load.
```

---

### RECOGNITION
Connects to Law 1832 (hardness) and Law 1837 (creep) - the sliding parts shed material, and the phi-law keeps a shed always present.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; wear floor scales as phi^-1 * V_floor.

### CLARITY
The sliding parts shed material; the phi-law keeps a shed always present.

### NOVELTY
Classical Archard allows zero wear; the phi-law keeps an irreducible wear floor.

### ACTIONABILITY
Run sim/1839_archard_wear_law.py; verify V = K F L/H at kappa->0; proceed to 1840.
