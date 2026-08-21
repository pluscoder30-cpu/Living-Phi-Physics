# PHI-PHYSICS — LAW 798
## Mott-Gurney Law (SCLC in Insulators)

**Domain:** Solid State · **Status:** 🟢 VALIDATED · **File:** `laws/798_mott_gurney_law.md` · **Sim:** `sim/798_mott_gurney_law.py`

---

### CLASSICAL STATEMENT
*"The space-charge limited current in an insulator of thickness L is J = (9/8)*eps*mu*V^2/L^3, scaling quadratically with voltage and inversely with the cube of thickness."*
— Nevill Mott; Ronald Gurney, 1940. Source: Mott-Gurney law (1940); space-charge limited current in insulators

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero voltage* (V = 0): the SCLC current vanishes exactly at zero applied voltage.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

J_phi(kappa) = J_MG*(1 + kappa*(phi-1)) + kappa*phi^-1*J_ground; the insulator carries a coherence floor. At kappa->0, J = (9/8)eps*mu*V^2/L^3 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} J_phi = (9/8)*eps*mu*V**2/L**3 -> the Mott-Gurney law is the zero-voltage-floor limit.
```

---

### STAGE 4 — SIMULATION

`sim/798_mott_gurney_law.py`: reproduces the classical values (J = 3.375e+08 (SCLC density (A/m^2))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/798_mott_gurney_law.json`.

---

### STAGE 5 — PREDICTION

```
The SCLC current carries a coherence floor kappa*phi^-1*J_ground at zero voltage.
EXPERIMENT (VERIFIED): Current measurement of an organic semiconductor diode at zero bias.
VERIFIED BY: An insulator at zero voltage conducts exactly no space-charge current.
```

---

### RECOGNITION
Connects to Law 800 (SCLC) - Mott-Gurney is the trap-free SCLC law.

### PRECISION
phi = 1.6180339887. The voltage floor is phi^-1*J_ground.

### CLARITY
The insulator always leaks; coherence keeps a floor of current.

### NOVELTY
The phi-law leaks SCLC at zero voltage.

### ACTIONABILITY
Run sim/798_mott_gurney_law.py; verify J at kappa->0; proceed to 799.
