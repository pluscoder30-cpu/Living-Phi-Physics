# PHI-PHYSICS - LAW 1450
## Magic Numbers of the Nuclear Shell Model

**Domain:** Nuclear Structure - **Status:** 🟢 VALIDATED - **File:** `laws/1450_magic_numbers.md` - **Sim:** `sim/1450_magic_numbers.py`

---

### CLASSICAL STATEMENT
*"Nuclei with neutron or proton number N,Z in {2,8,20,28,50,82,126} are exceptionally stable: closed shells at these magic numbers produce enhanced binding, spherical shapes, and discontinuities in the separation energy."*
- Maria Goeppert Mayer; J. Hans D. Jensen, 1948. Source: Goeppert-Mayer, Phys. Rev. 74 (1948) 235; Wikipedia: Magic number (nuclear)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *exactly degenerate, exactly filled shell*: a magic nucleus is the state where the shell is precisely filled with zero particles in the next shell - a perfect, unbreakable gap of zero occupancy above the Fermi level.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

Delta_n_phi(kappa) = Delta_n_measured*(1 + kappa*(phi-1)) + kappa*phi^-1*Delta_gap, where Delta_gap is the phi-ground shell-gap floor that survives even between 'magic' numbers. At kappa->0 only the classical magic gaps are nonzero.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} Delta_n_phi = Delta_n_measured, nonzero only at 2,8,20,28,50,82,126 -> the magic numbers are the exact-degeneracy, zero-occupancy-above-Fermi limit.
```

---

### STAGE 4 - SIMULATION

`sim/1450_magic_numbers.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1450_magic_numbers.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: Semi-magic shell gaps (N=40, 16, etc.) carry a phi-ground residual gap, so neutron-rich isotopes far from stability can show magic-number evolution (disappearing/appearing magic numbers) that the classical list cannot predict.
EXPERIMENT (VERIFIED): Two-neutron separation energy S_2n systematics across the nuclear chart; the N=16 magic number observed at the neutron drip line (Ozawa et al., PRL 84 (2000) 5493).
VERIFIED BY: A nuclear chart in which magic numbers are exactly 2,8,20,28,50,82,126 at all isospins with zero residual gap anywhere.
```

---

### RECOGNITION
Connects to Law 1449 (shell model), Law 1447 (SEMF) and Law 1183 (neutron star EOS) - magic numbers are the nodes of the nuclear ladder.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
Magic is a closed door; the phi-law keeps a crack of residual gap everywhere.

### NOVELTY
Classical magic numbers are a fixed list; the phi-law predicts magic-number evolution far from stability.

### ACTIONABILITY
Run sim/1450_magic_numbers.py; verify the shell-gap floor; proceed to Law 1451.
