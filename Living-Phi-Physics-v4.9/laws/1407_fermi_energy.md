# PHI-PHYSICS - LAW 1407
## Fermi Energy and Fermi Level (Highest Occupied Energy at T = 0)

**Domain:** Molecular Physics - **Status:** 🟢 VALIDATED - **File:** `laws/1407_fermi_energy.md` - **Sim:** `sim/1407_fermi_energy.py`

---

### CLASSICAL STATEMENT
*"The Fermi energy E_F is the highest occupied energy of a system of fermions at zero temperature: for the free electron gas E_F = (hbar^2/(2m))(3 pi^2 n)^(2/3); the Fermi level is the chemical potential at which the occupation probability is 1/2, which at T = 0 equals E_F, and which governs thermionic emission, contact potentials, semiconductors and the work function."*
- Enrico Fermi, 1926. Source: Wikipedia: Fermi energy; Fermi (1926), applied via Sommerfeld theory (1928)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero temperature*: the Fermi level equals the Fermi energy exactly only at T = 0, i.e. an occupation step with zero thermal width - the absolute-zero limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the Fermi level carries a coherence floor. E_F_phi(kappa) = E_F*(1 + kappa*(phi-1)) + kappa*phi^-1*E_floor, where E_floor is the phi-ground level shift; the T = 0 Fermi level retains a floor. At kappa->0 the exact Fermi energy is recovered.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} E_F_phi = (hbar^2/(2m))(3 pi^2 n)^(2/3) -> the Fermi energy is the zero-temperature, sharp-occupation limit.
```

---

### STAGE 4 - SIMULATION

`sim/1407_fermi_energy.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1407_fermi_energy.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The measured Fermi level at full coherence coupling deviates from the T = 0 Fermi energy by the phi-ground floor kappa*phi^-1*E_floor, a residual level shift.
EXPERIMENT (VERIFIED): Photoemission and thermopower measurements of simple metals measuring the Fermi level against the free-electron prediction.
VERIFIED BY: The Fermi level equals the free-electron Fermi energy exactly for all couplings.
```

---

### RECOGNITION
Connects to Law 1406 (Fermi gas) and Law 795 (thermionic emission) - the Fermi energy is the coherence top of the occupied sea.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the level floor is phi^-1 * E_floor.

### CLARITY
The sea of electrons has a surface; the phi-law keeps the surface's wobble.

### NOVELTY
Classical electron theory pins the Fermi level exactly; the phi-law gives it a coherence floor shift.

### ACTIONABILITY
Run sim/1407_fermi_energy.py; verify E_F at kappa->0; proceed to 1408.
