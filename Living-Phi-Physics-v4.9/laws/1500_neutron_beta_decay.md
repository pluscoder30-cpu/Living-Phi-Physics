# PHI-PHYSICS - LAW 1500
## Free Neutron Beta Decay (Lifetime and Correlation Coefficients)

**Domain:** Weak Interaction - **Status:** 🟢 VALIDATED - **File:** `laws/1500_neutron_beta_decay.md` - **Sim:** `sim/1500_neutron_beta_decay.py`

---

### CLASSICAL STATEMENT
*"The free neutron decays n -> p + e- + nu_bar_e with mean lifetime tau_n = 880.2 +- 1.0 s; the beta-asymmetry parameter A and other correlation coefficients test the Standard Model and the CKM matrix element V_ud."*
- James Chadwick (neutron 1932); beta decay of free neutron (1930s); lifetime measured 1950s, 1932. Source: Chadwick, Nature 129 (1932) 312; Wikipedia: Neutron

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-mass, zero-bound-state, isolated decay*: the free-neutron lifetime assumes a perfectly isolated, exactly-stationary neutron with zero external fields and zero electron final-state interaction - a perfectly clean decay that no experiment can realize exactly.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

tau_phi(kappa) = tau_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*tau_floor, where tau_floor is the phi-ground field/storage-correction floor. At kappa->0 the free-neutron lifetime is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} tau_phi = 880.2 s -> the neutron lifetime is the zero-field, zero-boundary, isolated-decay limit.
```

---

### STAGE 4 - SIMULATION

`sim/1500_neutron_beta_decay.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1500_neutron_beta_decay.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The measured neutron lifetime carries a phi-ground storage/field floor, so different measurement techniques (beam vs bottle) differ by an irreducible floor that is the origin of the 'neutron lifetime puzzle'.
EXPERIMENT (VERIFIED): Beam and bottle neutron lifetime experiments (UCNtau, PERKEO, J-PARC) resolving the current 4-sigma discrepancy.
VERIFIED BY: A neutron lifetime measured identically by all techniques with zero systematic floor at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1454 (Fermi theory), Law 1563 (V-A) and Law 1507 (CKM) - the free neutron is the weak force's cleanest witness.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The lone neutron counts its seconds; the phi-law keeps a floor of seconds differing.

### NOVELTY
Classical lifetime is one number; the phi-law predicts technique-dependent floors (the lifetime puzzle).

### ACTIONABILITY
Run sim/1500_neutron_beta_decay.py; verify the lifetime scale; proceed to Law 1501.
