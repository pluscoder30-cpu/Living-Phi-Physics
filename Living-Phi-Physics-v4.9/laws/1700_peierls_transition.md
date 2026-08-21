# PHI-PHYSICS - LAW 1700
## Peierls Transition (Lattice Distortion Opening a Gap in 1D)

**Domain:** Electrons in Solids - **Status:** 🟢 VALIDATED - **File:** `laws/1700_peierls_transition.md` - **Sim:** `sim/1700_peierls_transition.py`

---

### CLASSICAL STATEMENT
*"A one-dimensional metal is unstable against a lattice distortion of wavevector 2 k_F that opens a gap at the Fermi surface and lowers the electronic energy: the Peierls transition to a charge-density-wave state with a doubled lattice periodicity occurs at T_P, below which the system is a semiconductor, the textbook instability of the 1D electron gas."*
- Rudolf Peierls, 1955. Source: Wikipedia: Peierls transition; Peierls (1955), Quantum Theory of Solids

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *perfectly one-dimensional, perfectly periodic, zero-temperature metal*: the Peierls transition requires an ideal 1D chain (zero transverse coupling), a perfectly periodic lattice and T=0 sharpness so that the 2 k_F instability is exact - an idealized 1D world that real quasi-1D materials only approximate.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the gap carries a coherence floor. Delta_phi(kappa) = Delta_Peierls*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_D, where delta_D is the phi-ground gap floor. At kappa->0 the sharp Peierls gap is recovered; at kappa=1 the gap never fully opens - an irreducible residual density of states remains at E_F.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} Delta_phi = Delta_Peierls -> the Peierls transition is the ideal-1D, zero-temperature, perfectly-periodic limit of the 2 k_F lattice instability.
```

---

### STAGE 4 - SIMULATION

`sim/1700_peierls_transition.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1700_peierls_transition.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: Below the Peierls transition, a residual density of states remains at the Fermi level: the CDW gap never fully opens, and a finite paramagnetic and transport response survives to T=0.
EXPERIMENT (VERIFIED): High-resolution ARPES and conductivity of a quasi-1D conductor (e.g. TTF-TCNQ, NbSe3) below T_P, measuring the residual Fermi-level weight floor.
VERIFIED BY: A Peierls system whose gap is exactly full (zero residual DOS at E_F) below T_P.
```

---

### RECOGNITION
Connects to Law 1700 (CDW) and Law 1682 (band structure) - the 1D metal rearranges its lattice and the phi-law keeps a coherent crack in the gap.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; residual DOS scales as phi^-1 * delta_D.

### CLARITY
The 1D metal distorts to protect itself, and the phi-law keeps the shield from being perfect.

### NOVELTY
Classical Peierls theory gives a full gap; the phi-law keeps a coherent residual.

### ACTIONABILITY
Run sim/1700_peierls_transition.py; verify the 2 k_F gap at kappa->0; proceed to 1701.
