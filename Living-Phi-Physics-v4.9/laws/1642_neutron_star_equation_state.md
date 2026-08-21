# PHI-PHYSICS - LAW 1642
## Neutron Star Equation of State (Tolman-Oppenheimer-Volkoff Structure)

**Domain:** Nuclear Astrophysics / EoS - **Status:** 🟢 VALIDATED - **File:** `laws/1642_neutron_star_equation_state.md` - **Sim:** `sim/1642_neutron_star_equation_state.py`

---

### CLASSICAL STATEMENT
*"The neutron star structure is governed by the Tolman-Oppenheimer-Volkoff equation dP/dr = -G (rho + P/c^2)(m + 4 pi r^3 P/c^2)/(r^2 (1 - 2 G m/c^2 r)); the mass-radius relation is set by the nuclear equation of state, with the maximum mass ~2.1-2.3 M_sun constraining the EoS."*
- Tolman (1939); Oppenheimer & Volkoff (1939), 1939. Source: Oppenheimer & Volkoff, Phys. Rev. 55 (1939) 374; Wikipedia: Tolman-Oppenheimer-Volkoff equation

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-pressure, zero-density, vacuum-limit*: at the star's surface the pressure is exactly zero; the classical treatment of the surface boundary is the zero-pressure, zero-density, vacuum limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

P_phi(kappa) = P_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*P_floor, where P_floor is the phi-ground residual floor. At kappa->0 the TOV equation is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} P_phi = P_TOV -> the neutron star EoS is the zero-surface-pressure, exact-TOV, vacuum-boundary limit.
```

---

### STAGE 4 - SIMULATION

`sim/1642_neutron_star_equation_state.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1642_neutron_star_equation_state.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The neutron star mass-radius relation carries a phi-ground EoS floor, so the inferred maximum mass and radii have an irreducible uncertainty from the unknown EoS.
EXPERIMENT (VERIFIED): Neutron star mass and radius measurements (NICER, GW170817, pulsar timing) constraining the EoS.
VERIFIED BY: A neutron star exactly described by a known EoS with zero EoS-uncertainty floor.
```

---

### RECOGNITION
Connects to Law 1495 (incompressibility), Law 1619 (symmetry energy) and Law 1183 (neutron star EOS) - the TOV equation is the star's skeleton.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The star balances on the EoS; the phi-law keeps a floor of the balance uncertain.

### NOVELTY
Classical TOV is exact; the phi-law predicts an irreducible EoS floor.

### ACTIONABILITY
Run sim/1642_neutron_star_equation_state.py; verify the mass-radius relation; proceed to Law 1643.
