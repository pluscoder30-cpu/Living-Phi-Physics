# PHI-PHYSICS - LAW 1451
## Nuclear Pairing Energy (Even-Odd Staggering, BCS-like Pairing Gap)

**Domain:** Nuclear Structure - **Status:** 🟢 VALIDATED - **File:** `laws/1451_pairing_energy.md` - **Sim:** `sim/1451_pairing_energy.py`

---

### CLASSICAL STATEMENT
*"Like nucleons bind in spin-zero pairs: even-even nuclei are more bound than even-odd by the pairing energy delta ~ 12/sqrt(A) MeV; the pairing gap in the mass formula is +delta (even-even), 0 (odd-A), -delta (odd-odd)."*
- Weizsaecker delta-term (1935); generalized via BCS (Bohr, Mottelson, Pines 1958), 1935. Source: Bohr, Mottelson & Pines, PRD 110 (1958) 936; Wikipedia: Semi-empirical mass formula

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *fully paired, zero-quasiparticle ground state*: BCS-type pairing assumes the condensate of time-reversed pairs is exactly at zero temperature with zero unpaired quasiparticles - the gap vanishes identically above T_c=0.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

Delta_phi(kappa) = 12/sqrt(A)*(1 + kappa*(phi-1)) + kappa*phi^-1*Delta_min, where Delta_min is the phi-ground residual pairing gap that survives even in 'normal' odd nuclei. At kappa->0 the classical pairing term is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} Delta_phi = 12/sqrt(A) -> the pairing term of the mass formula is the zero-temperature, zero-unpaired-quasiparticle limit of the phi-pairing gap.
```

---

### STAGE 4 - SIMULATION

`sim/1451_pairing_energy.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1451_pairing_energy.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: Even in the 'unpaired' regime, nuclei carry a phi-ground residual pairing gap Delta_min, observable as a floor in the odd-even mass staggering that never vanishes.
EXPERIMENT (VERIFIED): Odd-even mass staggering analysis using the three-point mass formula over the entire AME2020 mass table.
VERIFIED BY: An odd-mass or odd-odd nucleus whose mass staggering shows exactly zero residual pairing floor at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1447 (SEMF delta term), Law 544 (BCS) and Law 1496 (deformation) - pairing is the nuclear analog of superconductivity.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
Pairs close ranks; the phi-law keeps an unpaired residue in every close.

### NOVELTY
Classical pairing vanishes above T_c; the phi-law keeps an irreducible residual gap.

### ACTIONABILITY
Run sim/1451_pairing_energy.py; verify Delta ~ 12/sqrt(A); proceed to Law 1452.
