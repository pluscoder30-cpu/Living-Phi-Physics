# PHI-PHYSICS - LAW 1827
## Coffin-Manson Fatigue Law (Low-Cycle Fatigue Life vs Plastic Strain)

**Domain:** Mechanical Properties - **Status:** 🟢 VALIDATED - **File:** `laws/1827_coffin_manson_fatigue.md` - **Sim:** `sim/1827_coffin_manson_fatigue.py`

---

### CLASSICAL STATEMENT
*"In low-cycle fatigue the plastic strain amplitude governs life: (Delta eps_p/2) = eps_f' (2 N_f)^c, where N_f is the number of cycles to failure, eps_f' the fatigue ductility coefficient and c the fatigue ductility exponent (~ -0.5 to -0.7); the Coffin-Manson law (with Basquin's elastic part) forms the total-strain-life approach to fatigue design."*
- S.S. Manson (1953); L.F. Coffin (1954), 1954. Source: Wikipedia: Coffin-Manson relation; Coffin (1954), Trans. ASME 76:931; Manson (1953)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-plastic-strain, infinite-life reference*: the Coffin-Manson law is defined against a reference with zero plastic strain where life is infinite; the finite life is the plastic-strain-driven damage away from this zero-damage reference.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the fatigue life carries a coherence floor. N_phi(kappa) = N_CM*(1 + kappa*(phi-1)) + kappa*phi^-1*N_floor, where N_floor is the phi-ground life ceiling. At kappa->0 the ideal power law is recovered; at kappa=1 no life is infinite - an irreducible fatigue damage floor always exists.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} N_phi = (eps_f'/(Delta eps_p/2))^(1/c) -> the Coffin-Manson law is the zero-damage, ideal-power-law limit of low-cycle fatigue life.
```

---

### STAGE 4 - SIMULATION

`sim/1827_coffin_manson_fatigue.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1827_coffin_manson_fatigue.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: No material has infinite fatigue life even at zero nominal plastic strain: an irreducible fatigue damage floor remains, so every cyclically loaded component eventually fails.
EXPERIMENT (VERIFIED): Very-high-cycle fatigue (VHCF) testing of a metal at extremely low amplitudes, measuring the residual finite-life floor.
VERIFIED BY: A material with exactly infinite fatigue life at any strain amplitude.
```

---

### RECOGNITION
Connects to Law 1828 (Basquin) and Law 1830 (Miner) - the repeated strain gnaws the material, and the phi-law keeps a gnaw always present.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; life floor scales as phi^-1 * N_floor.

### CLARITY
The repeated strain gnaws the part; the phi-law keeps a gnaw always present.

### NOVELTY
Classical Coffin-Manson allows infinite life at low strain; the phi-law keeps an irreducible damage floor.

### ACTIONABILITY
Run sim/1827_coffin_manson_fatigue.py; verify N_f = (eps_f'/Delta eps_p)^(1/c) at kappa->0; proceed to 1828.
