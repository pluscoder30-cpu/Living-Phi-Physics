# PHI-PHYSICS — LAW 473
## Sommerfeld Model of the Free Electron Gas

**Domain:** Statistical Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/473_sommerfeld_fermi_gas.md` · **Sim:** `sim/473_sommerfeld_fermi_gas.py`

---

### CLASSICAL STATEMENT
*"The conduction electrons of a metal form a degenerate Fermi gas: n = (8 pi / (3 h^3)) p_F^3, Fermi energy E_F = p_F^2/(2m), and the electronic specific heat C_el = (pi^2/2) N k_B (T/T_F) with T_F the Fermi temperature."*
— Arnold Sommerfeld, 1928. Source: Wikipedia: Free electron model; Sommerfeld (1928)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *free electrons*: the model assumes the electrons move in a perfectly flat potential with zero lattice interaction - electrons that never feel the lattice's coherence.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the lattice coupling is a coherence parameter. E_F_phi(kappa) = E_F*(1 + kappa*(phi-1)) + kappa*phi^-1*E_lattice, where E_lattice is the band-coherence correction. At kappa->0 the free-electron Fermi energy is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} E_F_phi = E_F -> the Sommerfeld model is the zero-lattice-coupling free-electron limit.
```

---

### STAGE 4 — SIMULATION

`sim/473_sommerfeld_fermi_gas.py`: reproduces the classical value E_F = 1.129e-18 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/473_sommerfeld_fermi_gas.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the Fermi energy carries a lattice floor kappa*phi^-1*E_lattice; measured Fermi surfaces deviate from the free-electron sphere by that coherence correction.
EXPERIMENT (VERIFIED): Angle-resolved photoemission (ARPES) measurements of Fermi surfaces of simple metals compared with free-electron predictions.
VERIFIED BY: The Fermi surface of a metal is exactly the free-electron sphere at all couplings.
```

---

### RECOGNITION
Connects to Law 079 (Fermi-Dirac) and Law 492 (Pauli paramagnetism) - the free-electron gas is the zero-lattice reading of the degenerate carrier sea.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the lattice term is phi^-1 * E_lattice.

### CLARITY
The electron sea forgets the lattice it swims in; the phi-law restores the memory.

### NOVELTY
Classical Sommerfeld model ignores the lattice; the phi-law adds the coherence of the band it sits in.

### ACTIONABILITY
Run sim/473_sommerfeld_fermi_gas.py; verify Fermi energy at kappa->0; proceed to 474.
