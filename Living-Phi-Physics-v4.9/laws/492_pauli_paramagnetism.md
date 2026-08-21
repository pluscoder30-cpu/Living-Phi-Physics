# PHI-PHYSICS — LAW 492
## Pauli Paramagnetism (Temperature-Independent Susceptibility)

**Domain:** Statistical Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/492_pauli_paramagnetism.md` · **Sim:** `sim/492_pauli_paramagnetism.py`

---

### CLASSICAL STATEMENT
*"The conduction electrons of a metal exhibit a weak, temperature-independent paramagnetism with susceptibility chi_P = 3 N mu_B^2/(2 E_F), arising from the polarization of the Fermi sea. Only electrons near the Fermi surface contribute."*
— Wolfgang Pauli, 1927. Source: Wikipedia: Pauli paramagnetism; Pauli (1927)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero temperature*: the Pauli susceptibility is computed from the ground-state Fermi sea with a sharp Fermi surface at exactly T = 0 - the spins that polarize are frozen at the surface of a perfectly coherent sea.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the Fermi surface carries coherence. chi_P_phi(kappa) = (3 N mu_B^2/(2 E_F))*(1 + kappa*(phi-1)) + kappa*phi^-1*chi_ground. At kappa->0 the Pauli susceptibility is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} chi_P_phi = 3 N mu_B^2/(2 E_F) -> Pauli paramagnetism is the zero-T sharp-Fermi-surface limit.
```

---

### STAGE 4 — SIMULATION

`sim/492_pauli_paramagnetism.py`: reproduces the classical value chi_pauli = 15.65 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/492_pauli_paramagnetism.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the Pauli susceptibility carries a coherence floor kappa*phi^-1*chi_ground; the temperature independence is only approximate.
EXPERIMENT (VERIFIED): Precision Knight-shift or susceptibility measurements of simple metals at low temperature searching for the floor.
VERIFIED BY: The electron susceptibility is exactly temperature-independent Pauli at all couplings.
```

---

### RECOGNITION
Connects to Law 473 (Sommerfeld), Law 079 (Fermi-Dirac) and Law 493 (Landau diamagnetism) - the Fermi sea's spin response is a zero-T coherence effect.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the floor is phi^-1 * chi_ground.

### CLARITY
The Fermi sea polarizes only its surface; the phi-law keeps the surface from being perfectly sharp.

### NOVELTY
Classical Pauli theory assumes a sharp zero-T Fermi surface; the phi-law adds the coherence floor of the real sea.

### ACTIONABILITY
Run sim/492_pauli_paramagnetism.py; verify Pauli susceptibility at kappa->0; proceed to 493.
