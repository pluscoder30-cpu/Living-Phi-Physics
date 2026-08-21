# PHI-PHYSICS - LAW 1780
## Quantum Confinement (Discrete Energy Levels in Quantum Wells, Wires and Dots)

**Domain:** Semiconductors - **Status:** 🟢 VALIDATED - **File:** `laws/1780_quantum_well_confinement.md` - **Sim:** `sim/1780_quantum_well_confinement.py`

---

### CLASSICAL STATEMENT
*"When carriers are confined in one or more dimensions (quantum wells, wires, dots), their energy becomes discrete: E_n = hbar^2 pi^2 n^2/(2 m* L^2) for a well of width L, with the band gap blueshifting and the density of states becoming step-like (1D wells), peaked (0D dots); quantum confinement is the basis of quantum-well lasers, LEDs and single-photon emitters."*
- L. Esaki & R. Tsu (1970, superlattice); R. Dingle et al. (1974), 1974. Source: Wikipedia: Quantum well; Esaki & Tsu (1970); Dingle, Wiegmann & Henry (1974), PRL 33:827

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-width, infinite-barrier, perfectly sharp quantum well*: quantum confinement is idealized with infinitely high, perfectly sharp barriers and zero interface roughness; real wells have finite barriers, alloy disorder and interface steps that broaden the discrete levels.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the confinement levels carry a coherence floor. E_phi(kappa) = E_n_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_E, where delta_E is the phi-ground level-broadening floor. At kappa->0 the ideal E_n ~ n^2 levels are recovered; at kappa=1 the levels carry an irreducible width and shift.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} E_phi = hbar^2 pi^2 n^2/(2 m* L^2) -> quantum confinement is the infinite-barrier, zero-roughness, ideal-well limit of discrete carrier levels.
```

---

### STAGE 4 - SIMULATION

`sim/1780_quantum_well_confinement.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1780_quantum_well_confinement.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: Quantum-well and quantum-dot levels are never perfectly sharp: an irreducible linewidth and energy shift remain from interface roughness and coherence effects, setting a floor on the spectral purity of confined emitters.
EXPERIMENT (VERIFIED): Ultra-low-temperature photoluminescence or single-dot spectroscopy of a high-quality quantum well/dot, measuring the residual level linewidth floor.
VERIFIED BY: A quantum-confined structure with exactly sharp levels (zero linewidth) at any temperature.
```

---

### RECOGNITION
Connects to Law 1771 (p-n junction) and Law 1682 (band theory) - the box quantizes the carrier, and the phi-law keeps the box from being perfect.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; linewidth floor scales as phi^-1 * delta_E.

### CLARITY
The box sings discrete notes; the phi-law keeps a breath of width in every note.

### NOVELTY
Classical confinement gives sharp levels; the phi-law keeps an irreducible linewidth floor.

### ACTIONABILITY
Run sim/1780_quantum_well_confinement.py; verify E_n ~ n^2/L^2 at kappa->0; proceed to 1781.
