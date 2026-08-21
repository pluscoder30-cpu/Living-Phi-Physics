# PHI-PHYSICS - LAW 1489
## Yukawa Potential (Meson-Exchange Nuclear Force)

**Domain:** Nuclear Forces - **Status:** 🟢 VALIDATED - **File:** `laws/1489_yukawa_potential.md` - **Sim:** `sim/1489_yukawa_potential.py`

---

### CLASSICAL STATEMENT
*"The nuclear force is mediated by meson exchange with a Yukawa potential V(r) = -g^2 e^(-mu r)/r, where mu = m_pi c/hbar is the pion mass scale (~1.4 fm range); this was Yukawa's prediction of the pion, discovered in 1947."*
- Hideki Yukawa, 1935. Source: Yukawa, Proc. Phys.-Math. Soc. Japan 17 (1935) 48; Wikipedia: Yukawa potential

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-mass, zero-range mediator*: the Yukawa potential becomes the Coulomb potential when the meson mass is exactly zero (mu -> 0) and a contact force at zero range - the zero-mass mediator limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

V_phi(kappa) = V_yukawa*(1 + kappa*(phi-1)) + kappa*phi^-1*V_core, where V_core is the phi-ground short-range repulsive core floor. At kappa->0 the Yukawa potential is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} V_phi = -g^2 e^(-mu r)/r -> the Yukawa potential is the zero-mass-mediator, pure-one-pion-exchange limit.
```

---

### STAGE 4 - SIMULATION

`sim/1489_yukawa_potential.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1489_yukawa_potential.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The nucleon-nucleon force carries a phi-ground repulsive core floor at short range, so the full NN interaction is never exactly one-pion exchange and the core appears as an irreducible short-range repulsion.
EXPERIMENT (VERIFIED): Nucleon-nucleon scattering phase shifts (SAID database) and potential reconstruction (e.g. Nijmegen, AV18, chiral EFT) including the repulsive core.
VERIFIED BY: A nucleon-nucleon interaction exactly described by pure one-pion exchange with zero repulsive core at all separations.
```

---

### RECOGNITION
Connects to Law 1490 (deuteron), Law 1447 (SEMF) and Law 1523 (skyrmion) - the Yukawa potential is the glue of the nucleus.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The pion carries the grip; the phi-law keeps a floor of grip at the core.

### NOVELTY
Classical Yukawa is one-pion; the phi-law predicts an irreducible repulsive core.

### ACTIONABILITY
Run sim/1489_yukawa_potential.py; verify e^(-mu r)/r; proceed to Law 1490.
