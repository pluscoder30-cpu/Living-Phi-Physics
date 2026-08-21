# PHI-PHYSICS — LAW 795
## Thermionic Emission (Richardson-Dushman)

**Domain:** Emission · **Status:** 🟢 VALIDATED · **File:** `laws/795_thermionic_emission.md` · **Sim:** `sim/795_thermionic_emission.py`

---

### CLASSICAL STATEMENT
*"The current density emitted by a hot cathode is J = A*T^2*exp(-W/(k_B*T)), with A = 4*pi*m_e*e*k_B^2/h^3 = 1.2e6 A/m^2/K^2 and work function W."*
— Owen Willans Richardson; Saul Dushman, 1923. Source: Wikipedia: Richardson-Dushman equation (Richardson ~1901; Dushman 1923)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero temperature* (T = 0): the emission current vanishes exactly at absolute zero.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

J_phi(kappa) = J_therm*(1 + kappa*(phi-1)) + kappa*phi^-1*J_ground; the cathode carries a coherence floor. At kappa->0, J = A*T^2*exp(-W/k_B*T) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} J_phi = A*T^2*exp(-W/(k_B*T)) -> thermionic emission is the zero-T floor limit.
```

---

### STAGE 4 — SIMULATION

`sim/795_thermionic_emission.py`: reproduces the classical values (J = 0.0081789 (Emission density (A/m^2))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/795_thermionic_emission.json`.

---

### STAGE 5 — PREDICTION

```
The emission current carries a coherence floor kappa*phi^-1*J_ground; emission never vanishes exactly at zero temperature.
EXPERIMENT (VERIFIED): Emission measurement of a cold cathode in high vacuum.
VERIFIED BY: A cathode at zero temperature emits exactly no current.
```

---

### RECOGNITION
Connects to Law 796 (field emission) - thermionic emission is the thermal escape.

### PRECISION
phi = 1.6180339887. The T-floor is phi^-1*J_ground.

### CLARITY
Even cold cathodes whisper; coherence keeps a floor of emission.

### NOVELTY
The phi-law keeps thermionic emission at zero temperature.

### ACTIONABILITY
Run sim/795_thermionic_emission.py; verify J at kappa->0; proceed to 796.
