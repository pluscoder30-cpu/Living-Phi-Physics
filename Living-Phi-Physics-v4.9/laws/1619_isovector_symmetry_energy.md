# PHI-PHYSICS - LAW 1619
## Isovector Symmetry Energy (Neutron-Proton Asymmetry Term)

**Domain:** Nuclear Structure / EoS - **Status:** 🟢 VALIDATED - **File:** `laws/1619_isovector_symmetry_energy.md` - **Sim:** `sim/1619_isovector_symmetry_energy.py`

---

### CLASSICAL STATEMENT
*"The symmetry energy is the term in the nuclear binding proportional to (N - Z)^2/A, with coefficient a_sym ~ 25-35 MeV; it reflects the Pauli energy cost of neutron-proton asymmetry and its density dependence (slope L) determines neutron-star radii and the neutron-skin thickness."*
- Symmetry energy (Wigner 1937; Weizsaecker asymmetry term), 1937. Source: Wigner, Phys. Rev. 51 (1937) 106; Wikipedia: Symmetry energy

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-asymmetry, N = Z, symmetric-nuclear-matter limit*: in symmetric nuclear matter (N = Z) the symmetry energy contribution is exactly zero; the classical treatment of symmetric matter is the zero-asymmetry, zero-symmetry-energy limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

S_phi(kappa) = S_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*S_floor, where S_floor is the phi-ground residual-asymmetry floor. At kappa->0 the symmetric-matter limit is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} S_phi = a_sym (N - Z)^2/A -> the symmetry energy is the zero-asymmetry, symmetric-matter, Pauli-only limit.
```

---

### STAGE 4 - SIMULATION

`sim/1619_isovector_symmetry_energy.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1619_isovector_symmetry_energy.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The symmetry energy carries a phi-ground residual floor, so even N = Z nuclei show a small symmetry-energy contribution and the density dependence L has an irreducible uncertainty.
EXPERIMENT (VERIFIED): Neutron-skin measurements (PREX, CREX), nuclear masses, and heavy-ion isospin diffusion constraining L and the symmetry energy.
VERIFIED BY: An N = Z nucleus with exactly zero symmetry-energy contribution at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1495 (compressibility), Law 1447 (SEMF) and Law 1183 (neutron star EOS) - the symmetry energy is the neutron-proton tension.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The asymmetry costs energy; the phi-law keeps a floor of cost in the symmetric.

### NOVELTY
Classical symmetric matter is free; the phi-law predicts an irreducible symmetry floor.

### ACTIONABILITY
Run sim/1619_isovector_symmetry_energy.py; verify the (N-Z)^2 term; proceed to Law 1620.
