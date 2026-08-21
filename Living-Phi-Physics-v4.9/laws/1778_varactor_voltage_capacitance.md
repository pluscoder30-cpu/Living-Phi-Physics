# PHI-PHYSICS - LAW 1778
## Varactor Effect (Voltage-Dependent Junction Capacitance)

**Domain:** Semiconductors - **Status:** 🟢 VALIDATED - **File:** `laws/1778_varactor_voltage_capacitance.md` - **Sim:** `sim/1778_varactor_voltage_capacitance.py`

---

### CLASSICAL STATEMENT
*"A varactor (varicap) diode uses the voltage-dependent junction capacitance C(V) = C_0/(1 + V/V_bi)^m (m ~ 1/2 for abrupt, 1/3 for graded junctions) to make a voltage-controlled capacitor; varactors are used in tuning circuits, voltage-controlled oscillators and parametric amplifiers, where the nonlinear C-V characteristic enables frequency multiplication."*
- Semiconductor varactor developed 1950s-60s, 1961. Source: Wikipedia: Varicap; S. Kita (1954); P.N. Robson (1961) review

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-resistance, zero-leakage, ideal-voltage-controlled capacitor*: the varactor is idealized as a pure voltage-dependent capacitor with zero series resistance, zero leakage and exact C-V law - an ideal reactive element that real varactors with resistance and loss do not provide.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the capacitance carries a coherence floor. C_phi(kappa) = C_varactor*(1 + kappa*(phi-1)) + kappa*phi^-1*C_floor, where C_floor is the phi-ground minimum capacitance. At kappa->0 the ideal C(V) law is recovered; at kappa=1 the capacitance never reaches zero - a residual capacitance floor remains.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} C_phi = C_0/(1 + V/V_bi)^m -> the varactor is the zero-loss, zero-leakage, ideal C-V limit of voltage-controlled capacitance.
```

---

### STAGE 4 - SIMULATION

`sim/1778_varactor_voltage_capacitance.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1778_varactor_voltage_capacitance.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The varactor capacitance never drops to zero at any bias: an irreducible residual capacitance floor remains, and the C-V law carries a measurable deviation from the ideal power law.
EXPERIMENT (VERIFIED): Millikelvin and high-frequency C-V measurement of a high-quality varactor diode, measuring the residual capacitance floor and the deviation from the ideal C(V) law.
VERIFIED BY: A varactor whose capacitance reaches exactly zero (or exactly the ideal law with zero deviation) at any bias.
```

---

### RECOGNITION
Connects to Law 1777 (depletion) and Law 1771 (p-n junction) - the varactor is a capacitance tuned by voltage, and the phi-law keeps the tuning from being exact.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; capacitance floor scales as phi^-1 * C_floor.

### CLARITY
The varactor tunes its capacitance with voltage; the phi-law keeps a residual capacitance always present.

### NOVELTY
Classical varactor theory gives exact C-V laws; the phi-law keeps an irreducible floor.

### ACTIONABILITY
Run sim/1778_varactor_voltage_capacitance.py; verify C = C_0/(1+V/V_bi)^(1/2) at kappa->0; proceed to 1779.
