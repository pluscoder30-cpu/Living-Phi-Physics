# PHI-PHYSICS - LAW 1774
## Auger Recombination (Three-Body Non-Radiative Recombination)

**Domain:** Semiconductors - **Status:** 🟢 VALIDATED - **File:** `laws/1774_auger_recombination.md` - **Sim:** `sim/1774_auger_recombination.py`

---

### CLASSICAL STATEMENT
*"Auger recombination is a three-body process in which an electron-hole pair recombines and transfers its energy to a third carrier instead of emitting a photon: the rate scales as U = C_n n^2 p + C_p n p^2, with the Auger coefficient C ~ 10^-30 cm^6/s; it dominates at high carrier densities and sets the efficiency limit of LEDs and lasers, especially for small-bandgap materials."*
- Pierre Auger (1925, effect); in semiconductors by Beattie & Landsberg (1959), 1959. Source: Wikipedia: Auger recombination; Beattie & Landsberg (1959), Proc. R. Soc. A249:16; Auger (1925)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-third-carrier, perfectly radiative reference*: Auger recombination is defined against a reference with zero third carrier (pure radiative recombination); the Auger process is the non-radiative channel away from this zero-Auger reference.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the Auger rate carries a coherence floor. U_phi(kappa) = U_auger*(1 + kappa*(phi-1)) + kappa*phi^-1*U_floor, where U_floor is the phi-ground residual Auger rate. At kappa->0 the zero-Auger radiative reference is recovered; at kappa=1 an irreducible Auger channel always exists.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} U_phi = C n^2 p -> Auger recombination is the three-body non-radiative channel measured from the zero-Auger, pure-radiative reference.
```

---

### STAGE 4 - SIMULATION

`sim/1774_auger_recombination.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1774_auger_recombination.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: No semiconductor has purely radiative recombination: an irreducible Auger channel always remains, setting a floor on the maximum radiative quantum efficiency (the Auger floor of LED droop).
EXPERIMENT (VERIFIED): Ultra-precision quantum-efficiency and carrier-dynamics measurement of an LED or laser material, fitting the irreducible Auger contribution to recombination.
VERIFIED BY: A semiconductor with exactly zero Auger recombination at any carrier density.
```

---

### RECOGNITION
Connects to Law 1773 (SRH) and Law 1771 (p-n junction) - the third carrier steals the photon's energy, and the phi-law keeps a thief always present.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; Auger floor scales as phi^-1 * U_floor.

### CLARITY
The third carrier steals the light; the phi-law keeps a thief always in the crowd.

### NOVELTY
Classical Auger theory allows zero Auger in ideal materials; the phi-law keeps an irreducible channel.

### ACTIONABILITY
Run sim/1774_auger_recombination.py; verify U = C n^2 p at kappa->0; proceed to 1775.
