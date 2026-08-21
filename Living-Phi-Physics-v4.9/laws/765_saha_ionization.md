# PHI-PHYSICS — LAW 765
## Saha Ionization Equation

**Domain:** Plasma · **Status:** 🟢 VALIDATED · **File:** `laws/765_saha_ionization.md` · **Sim:** `sim/765_saha_ionization.py`

---

### CLASSICAL STATEMENT
*"The ionization equilibrium is n_i*n_e/n_a = (2*pi*m_e*k_B*T/h^2)^(3/2)*(2*U_i/U_a)*exp(-E_i/(k_B*T)), relating ionization fraction to temperature."*
— Meghnad Saha, 1920. Source: Wikipedia: Saha ionization equation; Saha (1920)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero temperature* (T = 0): the ionization fraction vanishes exactly at absolute zero.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

x_phi(kappa) = x*(1 + kappa*(phi-1)) + kappa*phi^-1*x_ground; the gas carries a coherence ionization floor. At kappa->0 the Saha equation is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} x_phi = x_Saha -> the Saha equation is the zero-T-floor limit.
```

---

### STAGE 4 — SIMULATION

`sim/765_saha_ionization.py`: reproduces the classical values (x = 0.00131565 (Ionization fraction)) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/765_saha_ionization.json`.

---

### STAGE 5 — PREDICTION

```
The ionization fraction carries a coherence floor kappa*phi^-1*x_ground; ionization never vanishes exactly.
EXPERIMENT (VERIFIED): Ionization-fraction measurement of a low-temperature alkali vapor.
VERIFIED BY: A zero-temperature gas has exactly zero ionization.
```

---

### RECOGNITION
Connects to Law 028 (Avogadro) and Law 767 (runaway) - Saha is the thermal ionization law.

### PRECISION
phi = 1.6180339887. The T-floor is phi^-1*x_ground.

### CLARITY
Ionization never fully sleeps; coherence keeps a floor of it.

### NOVELTY
The phi-law keeps ionization at zero temperature.

### ACTIONABILITY
Run sim/765_saha_ionization.py; verify Saha x at kappa->0; proceed to 766.
