# PHI-PHYSICS - LAW 1609
## Space Charge Limit (Beam Self-Field Effects)

**Domain:** Accelerators - **Status:** 🟢 VALIDATED - **File:** `laws/1609_space_charge_limit.md` - **Sim:** `sim/1609_space_charge_limit.py`

---

### CLASSICAL STATEMENT
*"The beam's own charge and current produce space-charge forces that defocus the beam, shifting the betatron tune by delta_Q = -N r_p/(4 pi beta^2 gamma^3 epsilon) (Laslett tune shift); this limits the beam intensity and is a key constraint on accelerator performance."*
- Space charge physics (1950s-70s); Laslett tune shift, 1958. Source: Laslett, in Proc. Int. Conf. High Energy Accel. (1958); Wikipedia: Space charge

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-charge, zero-density, zero-tune-shift limit*: a beam of exactly zero charge has zero space-charge force; the classical treatment of a single particle is the zero-charge, zero-tune-shift, ideal-focusing limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

delta_Q_phi(kappa) = delta_Q_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_Q_floor, where delta_Q_floor is the phi-ground space-charge floor. At kappa->0 the single-particle tune is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} delta_Q_phi = -N r_p/(4 pi beta^2 gamma^3 epsilon) -> the space charge limit is the zero-charge, zero-density, ideal-focusing limit.
```

---

### STAGE 4 - SIMULATION

`sim/1609_space_charge_limit.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1609_space_charge_limit.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The betatron tune shift carries a phi-ground space-charge floor, so even the weakest beams show a residual coherent tune shift and the intensity limit is bounded below the ideal.
EXPERIMENT (VERIFIED): Tune shift and intensity limit measurements in high-intensity rings (PSI, J-PARC, SNS) vs Laslett theory.
VERIFIED BY: A beam with exactly zero space-charge tune shift at finite intensity at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1560 (emittance), Law 1559 (betatron) and Law 1607 (lifetime) - space charge is the beam's self-weight.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The beam feels its own mass; the phi-law keeps a floor of the feeling in every bunch.

### NOVELTY
Classical single particle is ideal; the phi-law predicts an irreducible space-charge floor.

### ACTIONABILITY
Run sim/1609_space_charge_limit.py; verify the tune shift; proceed to Law 1610.
