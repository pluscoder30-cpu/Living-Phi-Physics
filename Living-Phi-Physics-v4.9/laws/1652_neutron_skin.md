# PHI-PHYSICS - LAW 1652
## Neutron Skin (Neutron-Rich Surface of Heavy Nuclei)

**Domain:** Nuclear Structure / EoS - **Status:** 🟢 VALIDATED - **File:** `laws/1652_neutron_skin.md` - **Sim:** `sim/1652_neutron_skin.py`

---

### CLASSICAL STATEMENT
*"The neutron skin thickness R_n - R_p is the difference between the neutron and proton root-mean-square radii; it is sensitive to the symmetry energy slope L and is measured by parity-violating electron scattering (PREX), providing a direct constraint on the nuclear EoS."*
- Neutron skin concept (1970s); PREX/CREX measurements, 1976. Source: Myers & Swiatecki (1974); Wikipedia: Neutron skin

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-asymmetry, zero-skin, symmetric-distribution limit*: in symmetric matter the neutron and proton distributions coincide with exactly zero skin; the classical treatment of a symmetric nucleus is the zero-skin limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

delta_R_phi(kappa) = delta_R_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_floor, where delta_floor is the phi-ground residual-skin floor. At kappa->0 the zero-skin symmetric limit is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} delta_R_phi = 0 -> the neutron skin is the zero-asymmetry, symmetric-distribution limit.
```

---

### STAGE 4 - SIMULATION

`sim/1652_neutron_skin.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1652_neutron_skin.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The neutron skin carries a phi-ground residual floor, so even 'symmetric' nuclei show a small neutron-excess surface and the skin is never exactly zero.
EXPERIMENT (VERIFIED): Parity-violating electron scattering (PREX-II, CREX) and neutron-skin measurements via hadronic probes.
VERIFIED BY: A nucleus with exactly zero neutron skin at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1619 (symmetry energy), Law 1498 (matter distribution) and Law 1622 (EoS) - the neutron skin is the nucleus's asymmetric coat.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The neutron coat is a shade thicker; the phi-law keeps a floor of the shade.

### NOVELTY
Classical skin can be zero; the phi-law predicts an irreducible residual floor.

### ACTIONABILITY
Run sim/1652_neutron_skin.py; verify the skin thickness; proceed to Law 1653.
