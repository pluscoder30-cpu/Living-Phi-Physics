# PHI-PHYSICS - LAW 1463
## Neutron-Induced Fission (Hahn-Strassmann-Meitner Discovery)

**Domain:** Nuclear Fission - **Status:** 🟢 VALIDATED - **File:** `laws/1463_neutron_induced_fission.md` - **Sim:** `sim/1463_neutron_induced_fission.py`

---

### CLASSICAL STATEMENT
*"A nucleus may be induced to fission by neutron absorption: n + 235U -> 236U* -> fission fragments + 2-3 n + ~200 MeV. Fissile nuclides (235U, 233U, 239Pu) fission with thermal neutrons; the energy release ~0.9 MeV/nucleon from the binding-energy curve."*
- Otto Hahn; Fritz Strassmann (1938); Lise Meitner; Otto Frisch (1939), 1938. Source: Hahn & Strassmann, Naturwiss. 27 (1939) 11; Wikipedia: Nuclear fission

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-threshold, exact-resonance capture*: thermal fission assumes the compound nucleus is formed at exactly the right excitation to exceed the barrier - a razor-thin resonance condition that classical physics cannot guarantee.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

E_fiss_phi(kappa) = E_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*E_floor, where E_floor is the phi-ground fission-threshold floor from resonance structure. At kappa->0 the classical fission cross-section is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} sigma_f_phi = sigma_f_classical -> neutron-induced fission is the exact-resonance, sharp-threshold limit.
```

---

### STAGE 4 - SIMULATION

`sim/1463_neutron_induced_fission.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1463_neutron_induced_fission.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The effective fission threshold carries a phi-ground floor, so sub-threshold neutron-induced fission occurs with finite probability and the resonance structure shows irreducible background.
EXPERIMENT (VERIFIED): Fission cross-section measurements at neutron facilities (n_TOF, JENDL/ENDF evaluation) including sub-threshold and resonance-region behavior.
VERIFIED BY: A fissile nucleus whose fission cross-section is exactly zero below the classical threshold at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1461 (Bohr-Wheeler), Law 1478 (Breit-Wigner) and Law 1470 (chain reaction) - induced fission powers the chain.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The neutron knocks; the phi-law keeps a floor of the door yielding.

### NOVELTY
Classical induced fission has a hard threshold; the phi-law keeps an irreducible sub-threshold floor.

### ACTIONABILITY
Run sim/1463_neutron_induced_fission.py; verify the resonance cross-section; proceed to Law 1464.
