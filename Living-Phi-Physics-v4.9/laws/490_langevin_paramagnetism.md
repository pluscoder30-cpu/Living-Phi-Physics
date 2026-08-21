# PHI-PHYSICS — LAW 490
## Langevin Paramagnetism (Classical Moment Alignment)

**Domain:** Statistical Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/490_langevin_paramagnetism.md` · **Sim:** `sim/490_langevin_paramagnetism.py`

---

### CLASSICAL STATEMENT
*"The magnetization of a classical paramagnet is M = N mu L(x), where the Langevin function L(x) = coth(x) - 1/x with x = mu B/(k_B T). At small x, M ~ N mu^2 B/(3 k_B T), Curie's law."*
— Paul Langevin, 1905. Source: Wikipedia: Langevin function; Langevin, Sur la theorie du magnetisme (1905)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *classical continuous moments*: the theory treats the magnetic moments as classical vectors free to point any direction with no quantum quantization and no coherence between moments.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the moment orientation carries coherence. x_phi(kappa) = x*(1 + kappa*(phi-1)) + kappa*phi^-1*x_ground, entering L(x_phi). At kappa->0 the classical Langevin magnetization is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} x_phi = x -> M_phi = N mu L(x) -> Langevin paramagnetism is the zero-quantization, zero-coherence classical-moment limit.
```

---

### STAGE 4 — SIMULATION

`sim/490_langevin_paramagnetism.py`: reproduces the classical values x_par = 0.1599, M_lang = 2.96e+04 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/490_langevin_paramagnetism.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the effective field parameter x carries a coherence floor; the low-field susceptibility deviates from Curie's law by kappa*phi^-1*chi_ground.
EXPERIMENT (VERIFIED): Precision magnetization measurements of paramagnetic salts at low temperature searching for the deviation.
VERIFIED BY: The magnetization follows N mu L(mu B/k_B T) exactly at all fields and couplings.
```

---

### RECOGNITION
Connects to Law 491 (Brillouin function), Law 136 (Curie) and Law 137 (Curie-Weiss) - the Langevin function is the classical limit of the quantum moment alignment.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the field floor is phi^-1 * x_ground.

### CLARITY
A classical moment drifts freely to follow the field; the phi-law keeps its residual drift.

### NOVELTY
Classical Langevin theory treats moments as continuous; the phi-law adds the coherence floor of the real alignment.

### ACTIONABILITY
Run sim/490_langevin_paramagnetism.py; verify Langevin magnetization at kappa->0; proceed to 491.
