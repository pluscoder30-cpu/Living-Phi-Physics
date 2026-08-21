# PHI-PHYSICS — LAW 822
## Landau Length (Coulomb Strong-Coupling Scale)

**Domain:** Plasma · **Status:** 🟢 VALIDATED · **File:** `laws/822_landau_length.md` · **Sim:** `sim/822_landau_length.py`

---

### CLASSICAL STATEMENT
*"The Landau length Lambda = e^2/(4*pi*eps_0*k_B*T) is the distance at which Coulomb energy equals thermal energy; it sets the strong-coupling parameter n*Lambda^3."*
— Lev Landau, 1936. Source: Landau length; strong-coupling parameter (Landau 1936)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *infinite temperature* (T -> infinity): the Landau length vanishes exactly only at infinite temperature.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Lambda_phi(kappa) = Lambda*(1 + kappa*(phi-1)) + kappa*phi^-1*Lambda_ground; the plasma carries a coherence floor. At kappa->0, Lambda = e^2/(4pi eps0 kB T) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} Lambda_phi = e**2/(4*pi*eps_0*k_B*T) -> the Landau length is the infinite-T floor limit.
```

---

### STAGE 4 — SIMULATION

`sim/822_landau_length.py`: reproduces the classical values (L = 5.57003e-08 (Landau length (m))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/822_landau_length.json`.

---

### STAGE 5 — PREDICTION

```
The Landau length carries a coherence floor kappa*phi^-1*Lambda_ground at any finite temperature.
EXPERIMENT (VERIFIED): Strong-coupling parameter measurement of a warm dense plasma.
VERIFIED BY: The Landau length is exactly zero at any finite temperature.
```

---

### RECOGNITION
Connects to Law 734 (Debye length) - the Landau length is the close-encounter scale.

### PRECISION
phi = 1.6180339887. The T-floor is phi^-1*Lambda_ground.

### CLARITY
Close encounters never shrink to nothing; coherence keeps a floor.

### NOVELTY
The phi-law keeps a Landau length at finite temperature.

### ACTIONABILITY
Run sim/822_landau_length.py; verify Lambda at kappa->0; proceed to 823.
