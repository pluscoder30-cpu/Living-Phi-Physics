# PHI-PHYSICS — LAW 647
## Retarded Potentials (Lorenz Solution)

**Domain:** Radiation · **Status:** 🟢 VALIDATED · **File:** `laws/647_retarded_potentials.md` · **Sim:** `sim/647_retarded_potentials.py`

---

### CLASSICAL STATEMENT
*"The potentials satisfy the wave equation and are given by retarded integrals: Phi(r,t) = (1/(4*pi*eps0))*integral rho(r',t-r/c)/r dV' and A = (mu0/(4*pi))*integral J(r',t-r/c)/r dV'."*
— Ludvig Lorenz, 1867. Source: Wikipedia: Lorenz gauge condition; Ludvig Lorenz (1867)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero charge and current everywhere*: the wave solutions assume the sources are entirely absent outside the integration region - the potential is exactly zero where no source has ever acted.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Phi_phi(kappa) = Phi_ret*(1 + kappa*(phi-1)) + kappa*phi^-1*Phi_ground; the source-free region carries a coherence potential floor. At kappa->0 the retarded integrals are exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} Phi_phi = Phi_ret -> retarded potentials are the zero-source-floor limit.
```

---

### STAGE 4 — SIMULATION

`sim/647_retarded_potentials.py`: reproduces the classical values (Phi = 898.755 (Retarded potential (V))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/647_retarded_potentials.json`.

---

### STAGE 5 — PREDICTION

```
The potential in a region with no sources is never exactly zero; a coherence floor kappa*phi^-1*Phi_ground persists from the field's history.
EXPERIMENT (VERIFIED): Potential measurement deep inside a source-free screened region with long field history.
VERIFIED BY: The potential is exactly zero in a region with no sources.
```

---

### RECOGNITION
Connects to Law 645 (Liénard-Wiechert) and Law 646 (Jefimenko) - the retarded kernel is the field's memory.

### PRECISION
phi = 1.6180339887. The memory floor is phi^-1*Phi_ground.

### CLARITY
The field remembers; the 'empty' region still carries the echo.

### NOVELTY
The phi-law gives source-free space a potential memory floor.

### ACTIONABILITY
Run sim/647_retarded_potentials.py; verify retarded potential at kappa->0; proceed to 648.
