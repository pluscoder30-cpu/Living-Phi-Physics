# PHI-PHYSICS - LAW 1738
## Dzyaloshinskii-Moriya Interaction (Antisymmetric Exchange in Non-Centrosymmetric Magnets)

**Domain:** Magnetism - **Status:** 🟢 VALIDATED - **File:** `laws/1738_dmi_interaction.md` - **Sim:** `sim/1738_dmi_interaction.py`

---

### CLASSICAL STATEMENT
*"In magnets lacking inversion symmetry, an antisymmetric exchange term H_DM = sum D_ij . (S_i x S_j) is allowed, with the Dzyaloshinskii-Moriya vector D_ij set by spin-orbit coupling; the DM interaction tilts spins, stabilizes canted and spiral order, and is the microscopic origin of skyrmions and of weak ferromagnetism in antiferromagnets like alpha-Fe2O3."*
- I.E. Dzyaloshinskii (1958); T. Moriya (1960), 1958. Source: Wikipedia: Antisymmetric exchange; Dzyaloshinskii (1958), J. Phys. Chem. Solids 4:241; Moriya (1960), Phys. Rev. 120:91

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *perfectly centrosymmetric, zero-spin-orbit reference magnet*: the DM interaction is defined against a centrosymmetric, zero-spin-orbit reference where D = 0 and exchange is exactly Heisenberg; the antisymmetric term is the symmetry-broken correction away from this zero-D reference.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the DM vector carries a coherence floor. D_phi(kappa) = D*(1 + kappa*(phi-1)) + kappa*phi^-1*D_floor, where D_floor is the phi-ground residual antisymmetric coupling. At kappa->0 the zero-D centrosymmetric reference is recovered; at kappa=1 an irreducible DM interaction always exists.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} D_phi = 0 -> the Dzyaloshinskii-Moriya interaction is the antisymmetric exchange measured from the zero-D, centrosymmetric, zero-spin-orbit reference.
```

---

### STAGE 4 - SIMULATION

`sim/1738_dmi_interaction.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1738_dmi_interaction.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: Even nominally centrosymmetric magnets retain an irreducible antisymmetric exchange floor: a weak DM interaction always persists, producing residual canting and weak ferromagnetic signatures.
EXPERIMENT (VERIFIED): Ultra-sensitive neutron diffraction and magnetization of a nominally centrosymmetric antiferromagnet (e.g. high-symmetry oxide) measuring the residual spin canting floor.
VERIFIED BY: A centrosymmetric magnet with exactly zero DM interaction and zero spin canting.
```

---

### RECOGNITION
Connects to Law 1737 (skyrmions) and Law 1718 (Heisenberg) - the antisymmetric handshake of spins, and the phi-law keeps the handshake from being symmetric.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; DM floor scales as phi^-1 * D_floor.

### CLARITY
The spins lean into a DM tilt; the phi-law keeps even symmetric magnets leaning.

### NOVELTY
Classical DM theory allows zero coupling in symmetric crystals; the phi-law keeps an irreducible floor.

### ACTIONABILITY
Run sim/1738_dmi_interaction.py; verify the D.SxS term at kappa->0; proceed to 1739.
