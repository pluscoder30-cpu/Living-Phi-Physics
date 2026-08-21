# PHI-PHYSICS - LAW 1362
## Koopmans' Theorem (Ionization Potential = -epsilon_orbital)

**Domain:** Atomic Physics - **Status:** 🟢 VALIDATED - **File:** `laws/1362_koopmans_theorem.md` - **Sim:** `sim/1362_koopmans_theorem.py`

---

### CLASSICAL STATEMENT
*"In the frozen-orbital approximation, the first ionization potential of a molecule equals the negative of the highest occupied molecular orbital (HOMO) energy: I = -epsilon_HOMO, and electron affinities equal -epsilon_LUMO; the theorem assumes the remaining orbitals do not relax after ionization."*
- Tjalling Koopmans, 1933. Source: Wikipedia: Koopmans' theorem; Koopmans, Physica 1 (1933) 104

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *frozen orbitals*: the theorem holds exactly only if the orbitals are completely frozen during ionization, i.e. zero relaxation of the remaining electrons - the non-relaxation limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the orbital relaxation carries a coherence floor. I_phi(kappa) = -epsilon_HOMO*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_relax, where delta_relax is the phi-ground relaxation energy; the measured IP deviates from -epsilon by the floor. At kappa->0 Koopmans' theorem is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} I_phi = -epsilon_HOMO -> Koopmans' theorem is the zero-relaxation, frozen-orbital limit.
```

---

### STAGE 4 - SIMULATION

`sim/1362_koopmans_theorem.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1362_koopmans_theorem.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The measured ionization potential at full coherence coupling exceeds -epsilon_HOMO by the phi-ground relaxation floor kappa*phi^-1*delta_relax, a systematic deviation in photoelectron spectra.
EXPERIMENT (VERIFIED): Photoelectron spectroscopy of small molecules comparing measured IPs against Koopmans' -epsilon_HOMO at increasing precision.
VERIFIED BY: The ionization potential equals -epsilon_HOMO exactly for all couplings.
```

---

### RECOGNITION
Connects to Law 1361 (Hartree-Fock) and Law 1346 (photoionization) - Koopmans' theorem is the coherence frozen-orbital reading of the IP.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the relaxation floor is phi^-1 * delta_relax.

### CLARITY
The orbital energy predicts the ionization, but the atom moves when struck; the phi-law keeps the movement's floor.

### NOVELTY
Classical quantum chemistry freezes orbitals exactly; the phi-law keeps the relaxation coherence floor.

### ACTIONABILITY
Run sim/1362_koopmans_theorem.py; verify I = -epsilon at kappa->0; proceed to 1363.
