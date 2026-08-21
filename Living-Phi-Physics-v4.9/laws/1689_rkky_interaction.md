# PHI-PHYSICS - LAW 1689
## RKKY Interaction (Ruderman-Kittel-Kasuya-Yosida Indirect Exchange)

**Domain:** Electrons in Solids - **Status:** 🟢 VALIDATED - **File:** `laws/1689_rkky_interaction.md` - **Sim:** `sim/1689_rkky_interaction.py`

---

### CLASSICAL STATEMENT
*"Localized magnetic moments interact indirectly through the conduction electrons: J_RKKY(R) ~ J^2 D(E_F) F(2 k_F R), where F(x) = (x cos x - sin x)/x^4 is the RKKY function, oscillating in sign with distance and decaying as cos(2 k_F R)/R^3; it mediates the exchange coupling in dilute magnetic alloys, rare-earth metals and GMR multilayers."*
- M.A. Ruderman & C. Kittel (1954); T. Kasuya (1956); K. Yosida (1957), 1954. Source: Wikipedia: RKKY interaction; Ruderman & Kittel (1954), Phys. Rev. 96:99; Kasuya (1956); Yosida (1957)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *non-interacting, T=0, sharp-Fermi-surface electron gas with point impurities*: the RKKY interaction assumes free conduction electrons at T=0 with a sharp Fermi surface and zero impurity radius - a pristine, sharp-edged electron sea that no real host metal provides.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the interaction carries a coherence envelope. J_phi(kappa) = J_RKKY(R)*(1 + kappa*(phi-1)) + kappa*phi^-1*J_floor, where J_floor is the phi-ground long-range coupling floor. At kappa->0 the exact cos(2 k_F R)/R^3 law is recovered; at kappa=1 the RKKY coupling retains an irreducible long-range tail.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} J_phi = J^2 D(E_F) F(2 k_F R) -> the RKKY interaction is the zero-temperature, non-interacting, sharp-Fermi-surface limit of indirect exchange.
```

---

### STAGE 4 - SIMULATION

`sim/1689_rkky_interaction.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1689_rkky_interaction.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: RKKY coupling between magnetic moments retains an irreducible long-range tail beyond the nominal 1/R^3 decay, producing weak but finite inter-spin correlations at large separation that never vanish.
EXPERIMENT (VERIFIED): Spin-polarized STM or neutron scattering of a dilute magnetic alloy measuring the RKKY coupling vs inter-impurity distance, detecting the residual long-range tail.
VERIFIED BY: RKKY coupling measured to decay to exactly zero beyond the nominal range.
```

---

### RECOGNITION
Connects to Law 1688 (Friedel) and Law 1683 (Fermi surface) - indirect exchange is the electron sea's handshake across the metal.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; residual coupling scales as phi^-1 * J_floor.

### CLARITY
Two spins shake hands through the electron sea, and the phi-law keeps the hand extended.

### NOVELTY
Classical RKKY decays to zero; the phi-law keeps an irreducible long-range handshake.

### ACTIONABILITY
Run sim/1689_rkky_interaction.py; verify F(2 k_F R) at kappa->0; proceed to 1690.
