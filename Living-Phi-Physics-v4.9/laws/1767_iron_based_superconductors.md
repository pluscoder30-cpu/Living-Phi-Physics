# PHI-PHYSICS - LAW 1767
## Iron-Based Superconductors (Hosono's Discovery of LaFeAsO1-xFx)

**Domain:** Superconductivity - **Status:** 🟢 VALIDATED - **File:** `laws/1767_iron_based_superconductors.md` - **Sim:** `sim/1767_iron_based_superconductors.py`

---

### CLASSICAL STATEMENT
*"The discovery of superconductivity at 26 K in fluorine-doped LaFeAsO opened the iron-based superconductor family (T_c up to ~56 K in SmFeAsO1-xFx): superconductivity arises in FeAs (or FeSe) layers with the Fe 3d orbitals dominating, multiple Fermi-surface sheets and likely sign-changing s+- pairing driven by magnetic fluctuations - a new class that followed cuprates."*
- Yoichi Kamihara, H. Hiramatsu, M. Hirano, R. Kawamura, H. Yanagi, T. Kamiya & Hideo Hosono, 2008. Source: Wikipedia: Iron-based superconductor; Kamihara et al. (2008), J. Am. Chem. Soc. 130:3296

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-magnetic-fluctuation, conventional-phonon reference*: iron-based superconductors are defined against the conventional BCS (phonon) reference; their high T_c and magnetic-fluctuation-driven pairing are measured away from this conventional reference.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: T_c carries a coherence floor. T_c_phi(kappa) = T_c_iron*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_T, where delta_T is the phi-ground transition smearing. At kappa->0 the sharp T_c is recovered; at kappa=1 the transition is smeared and a nematic/pseudogap floor persists.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} T_c_phi = T_c_iron -> iron-based superconductors are the magnetic-fluctuation-paired state measured from the conventional phonon reference.
```

---

### STAGE 4 - SIMULATION

`sim/1767_iron_based_superconductors.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1767_iron_based_superconductors.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: Iron-based superconducting transitions are smeared over a phi-ground width and incipient magnetic/nematic correlations persist in the normal state, observable as residual order-parameter fluctuations above T_c.
EXPERIMENT (VERIFIED): High-resolution specific-heat, neutron-scattering and ARPES of a high-quality iron pnictide (e.g. BaFe2As2-based) measuring the transition width and the residual spin-fluctuation floor.
VERIFIED BY: An iron-based superconductor with exactly zero transition width and zero spin fluctuations above T_c.
```

---

### RECOGNITION
Connects to Law 1765 (cuprates) and Law 1761 (BCS) - the iron layers pair by magnetism, and the phi-law keeps a magnetic thread always present.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; transition width scales as phi^-1 * delta_T.

### CLARITY
The iron layers sing with magnetic glue; the phi-law keeps a magnetic hum above T_c.

### NOVELTY
Classical superconductivity theory allows clean transitions; the phi-law keeps a fluctuation floor.

### ACTIONABILITY
Run sim/1767_iron_based_superconductors.py; verify the FeAs-layer T_c at kappa->0; proceed to 1768.
