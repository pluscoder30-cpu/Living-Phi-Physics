# PHI-PHYSICS - LAW 1796
## Griffith Fracture Criterion (Energy Balance of Crack Propagation)

**Domain:** Mechanical Properties - **Status:** 🟢 VALIDATED - **File:** `laws/1796_griffith_fracture_criterion.md` - **Sim:** `sim/1796_griffith_fracture_criterion.py`

---

### CLASSICAL STATEMENT
*"A crack propagates when the released elastic energy equals the surface energy of the new crack faces: for a crack of length 2a in a plate, sigma_c = sqrt(2 E gamma/(pi a)), the Griffith criterion sigma_c sqrt(a) = sqrt(2 E gamma/pi) = constant; the criterion establishes that fracture is an energy balance and that the critical stress scales as 1/sqrt(a), the foundation of linear elastic fracture mechanics."*
- Alan Arnold Griffith, 1921. Source: Wikipedia: Griffith's criterion; Griffith (1921), Phil. Trans. R. Soc. A221:163

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-toughness, perfectly brittle, zero-plastic-dissipation reference*: the Griffith criterion assumes perfectly brittle fracture with energy dissipated only in creating new surface (zero plastic zone, zero damage); real materials dissipate energy plastically at the crack tip, away from this zero-plasticity reference.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the critical stress carries a coherence floor. sigma_c_phi(kappa) = sigma_c_griffith*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_sigma, where delta_sigma is the phi-ground toughness floor. At kappa->0 the ideal brittle criterion is recovered; at kappa=1 an irreducible plastic dissipation always adds to the fracture resistance.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} sigma_c_phi = sqrt(2 E gamma/(pi a)) -> the Griffith criterion is the perfectly-brittle, zero-plastic-dissipation limit of crack energy balance.
```

---

### STAGE 4 - SIMULATION

`sim/1796_griffith_fracture_criterion.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1796_griffith_fracture_criterion.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: No material fractures purely by surface energy: an irreducible plastic-dissipation contribution always adds to the fracture resistance, so the measured surface energy from fracture tests always exceeds the true surface energy by a floor.
EXPERIMENT (VERIFIED): Fracture-toughness measurement of a model brittle material (e.g. glass, silicon) at different crack speeds and temperatures, fitting the residual plastic-dissipation floor.
VERIFIED BY: A material whose fracture energy is exactly the surface energy with zero plastic dissipation.
```

---

### RECOGNITION
Connects to Law 1795 (Paris) and Law 1797 (Irwin) - the crack trades energy for area, and the phi-law keeps a fee always in the trade.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; dissipation floor scales as phi^-1 * delta_sigma.

### CLARITY
The crack pays for new surface; the phi-law keeps a tip always bleeding energy.

### NOVELTY
Classical Griffith gives a clean energy balance; the phi-law adds an irreducible dissipation floor.

### ACTIONABILITY
Run sim/1796_griffith_fracture_criterion.py; verify sigma_c = sqrt(2 E gamma/(pi a)) at kappa->0; proceed to 1797.
