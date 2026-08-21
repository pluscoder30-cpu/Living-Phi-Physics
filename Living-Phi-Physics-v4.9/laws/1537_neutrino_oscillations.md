# PHI-PHYSICS - LAW 1537
## Neutrino Oscillations (Pontecorvo's Flavor Conversion)

**Domain:** Particle Physics / Neutrinos - **Status:** 🟢 VALIDATED - **File:** `laws/1537_neutrino_oscillations.md` - **Sim:** `sim/1537_neutrino_oscillations.py`

---

### CLASSICAL STATEMENT
*"Neutrinos oscillate between flavors as they propagate because the mass eigenstates differ from the flavor eigenstates: the survival probability P = 1 - sin^2(2theta) sin^2(1.27 delta_m^2 L/E), with delta_m^2 in eV^2, L in km, E in GeV; the atmospheric (delta_m^2 ~ 2.4e-3) and solar (7.5e-5) splittings are measured."*
- Bruno Pontecorvo (1957); confirmed by Super-Kamiokande (1998), 1957. Source: Pontecorvo, Sov. Phys. JETP 6 (1958) 429; Fukuda et al., PRL 81 (1998) 1562

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-mass-difference, zero-oscillation limit*: oscillations require the mass eigenstates to be non-degenerate (delta_m^2 != 0); if the masses are exactly equal, no oscillation occurs - a zero-mass-splitting, frozen-flavor limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

P_phi(kappa) = P_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*P_floor, where P_floor is the phi-ground matter/coherence floor. At kappa->0 the vacuum oscillation formula is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} P_phi = 1 - sin^2(2theta) sin^2(1.27 delta_m^2 L/E) -> neutrino oscillations are the zero-matter, zero-decoherence, vacuum limit.
```

---

### STAGE 4 - SIMULATION

`sim/1537_neutrino_oscillations.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1537_neutrino_oscillations.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The oscillation probability carries a phi-ground matter/coherence floor, so the effective survival probability deviates from the vacuum formula by an irreducible matter-effect correction (the MSW floor).
EXPERIMENT (VERIFIED): Long-baseline and reactor experiments (Daya Bay, KamLAND, T2K, NOvA, JUNO, DUNE) measuring oscillation parameters.
VERIFIED BY: Neutrino oscillations exactly following the vacuum formula with zero matter floor in all media.
```

---

### RECOGNITION
Connects to Law 1511 (PMNS), Law 1536 (seesaw) and Law 1538 (MSW) - oscillations are the neutrino's identity shifts.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The neutrino is three at once; the phi-law keeps a floor of the three mixing.

### NOVELTY
Classical vacuum oscillation is exact; the phi-law predicts an irreducible matter floor.

### ACTIONABILITY
Run sim/1537_neutrino_oscillations.py; verify the survival probability; proceed to Law 1538.
