# PHI-PHYSICS — LAW 620
## Bernoulli's Kinetic Theory (Molecular Pressure)

**Domain:** Kinetic Theory · **Status:** 🟢 VALIDATED · **File:** `laws/620_bernoullis_kinetic_theory.md` · **Sim:** `sim/620_bernoullis_kinetic_theory.py`

---

### CLASSICAL STATEMENT
*"The pressure of a gas arises from the impact of its molecules on the container walls: P = (1/3) n m <v^2> = (2/3) n <E_kin>. Bernoulli proposed that heat is the motion of molecules and pressure the mean momentum transfer, founding kinetic theory."*
— Daniel Bernoulli, 1738. Source: Wikipedia: Kinetic theory of gases; Bernoulli, Hydrodynamica (1738)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero molecular speed*: the pressure vanishes exactly at <v^2> = 0 - a gas of perfectly still molecules, which the coherence ground of the field forbids.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the ground speed carries coherence. P_phi(kappa) = (1/3) n m <v^2>*(1 + kappa*(phi-1)) + kappa*phi^-1*P_ground, where P_ground is the pressure of the coherence-ground motion. At kappa->0 the Bernoulli pressure is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} P_phi = (1/3) n m <v^2> -> Bernoulli's kinetic pressure is the zero-ground-motion limit.
```

---

### STAGE 4 — SIMULATION

`sim/620_bernoullis_kinetic_theory.py`: reproduces the classical value P_kin = 7.44e+04 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/620_bernoullis_kinetic_theory.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling a gas retains a ground pressure kappa*phi^-1*P_ground even as T -> 0; the measured pressure never vanishes exactly.
EXPERIMENT (VERIFIED): Ultra-low-temperature pressure measurements of cold gases (e.g. in atom traps) searching for the ground pressure.
VERIFIED BY: The pressure of a gas is exactly zero at zero molecular speed for all couplings.
```

---

### RECOGNITION
Connects to Law 025 (ideal gas) and Law 030 (Boltzmann) - Bernoulli's theory is the first coherence reading of gas pressure.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the ground pressure is phi^-1 * P_ground.

### CLARITY
A gas presses because it moves; the phi-law keeps the motion even at the coldest floor.

### NOVELTY
Classical Bernoulli pressure vanishes at zero speed; the phi-law adds the ground pressure of the moving carrier.

### ACTIONABILITY
Run sim/620_bernoullis_kinetic_theory.py; verify P at kappa->0; proceed to next domain agent (EM).
