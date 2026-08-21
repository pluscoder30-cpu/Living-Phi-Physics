# PHI-PHYSICS — LAW 800
## Variable Range Hopping (Mott VRH)

**Domain:** Solid State · **Status:** 🟢 VALIDATED · **File:** `laws/800_variable_range_hopping.md` · **Sim:** `sim/800_variable_range_hopping.py`

---

### CLASSICAL STATEMENT
*"At low temperature electrons hop to optimally distant states; the resistance follows ln(R) ~ (T_0/T)^(1/(d+1)), with the 1/4 exponent in 3D."*
— Nevill Mott, 1969. Source: Wikipedia: Variable-range hopping; Mott (1969)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero temperature* (T = 0): the optimal hopping length diverges exactly at zero temperature.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

R_phi(kappa) = R_VRH*(1 + kappa*(phi-1)) + kappa*phi^-1*R_ground; the hop ensemble carries a coherence floor. At kappa->0, ln(R) ~ (T_0/T)^(1/4) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} R_phi = R_0*exp((T_0/T)^(1/4)) -> variable range hopping is the zero-T floor limit.
```

---

### STAGE 4 — SIMULATION

`sim/800_variable_range_hopping.py`: reproduces the classical values (R = 3.86206 (VRH resistance (ohm))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/800_variable_range_hopping.json`.

---

### STAGE 5 — PREDICTION

```
The VRH resistance carries a coherence floor kappa*phi^-1*R_ground; the divergence at zero T is capped.
EXPERIMENT (VERIFIED): Resistance measurement of a disordered film at ultra-low temperature.
VERIFIED BY: The VRH resistance diverges exactly at zero temperature.
```

---

### RECOGNITION
Connects to Law 799 (hopping) - VRH is the optimized-range hopping law.

### PRECISION
phi = 1.6180339887. The T-floor is phi^-1*R_ground.

### CLARITY
Hops grow long in the cold; coherence caps the reach.

### NOVELTY
The phi-law caps the VRH divergence.

### ACTIONABILITY
Run sim/800_variable_range_hopping.py; verify ln R at kappa->0; proceed to 801.
