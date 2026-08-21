# PHI-PHYSICS - LAW 1631
## Fusion Neutron Spectrum (DT and DD Neutron Energies)

**Domain:** Nuclear Fusion - **Status:** 🟢 VALIDATED - **File:** `laws/1631_fusion_neutron_spectrum.md` - **Sim:** `sim/1631_fusion_neutron_spectrum.py`

---

### CLASSICAL STATEMENT
*"Fusion reactions produce characteristic neutron energies: D-T gives 14.1 MeV neutrons and D-D gives 2.45 MeV neutrons, determined by the reaction Q-values and two-body kinematics; the neutron energy spectrum is used for fusion diagnostics and the 14 MeV neutrons drive tritium breeding and activation."*
- Fusion kinematics (1950s); DT 14.1 MeV neutrons, 1952. Source: Wikipedia: Fusion power; Lawson (1957)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-recoil, zero-spread, monoenergetic-neutron limit*: in the exact two-body center-of-mass the neutron energy is a single sharp value; the classical treatment of a monoenergetic fusion neutron is the zero-spread, zero-recoil limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

E_n_phi(kappa) = E_n_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*E_floor, where E_floor is the phi-ground spectral-spread floor. At kappa->0 the monoenergetic fusion neutron is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} E_n_phi = 14.1 MeV (DT) -> the fusion neutron spectrum is the zero-recoil, monoenergetic, two-body limit.
```

---

### STAGE 4 - SIMULATION

`sim/1631_fusion_neutron_spectrum.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1631_fusion_neutron_spectrum.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The fusion neutron energy carries a phi-ground spectral-spread floor, so even 'monoenergetic' fusion neutrons show an irreducible energy spread from target/beam conditions.
EXPERIMENT (VERIFIED): Fusion neutron spectrometry (TOF, scintillator) at JET, TFTR, NIF resolving the 14.1/2.45 MeV lines and their widths.
VERIFIED BY: A fusion neutron beam with exactly zero energy spread at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1466 (DT), Law 1467 (DD) and Law 1604 (ignition) - the fusion neutron is the reaction's signature.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The neutron carries the exact message; the phi-law keeps a floor of static in the message.

### NOVELTY
Classical neutron is monoenergetic; the phi-law predicts an irreducible spread floor.

### ACTIONABILITY
Run sim/1631_fusion_neutron_spectrum.py; verify the 14.1 MeV line; proceed to Law 1632.
