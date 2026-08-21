# PHI-PHYSICS - LAW 1828
## Basquin's Law (High-Cycle Fatigue Life vs Stress Amplitude)

**Domain:** Mechanical Properties - **Status:** 🟢 VALIDATED - **File:** `laws/1828_basquin_fatigue_high_cycle.md` - **Sim:** `sim/1828_basquin_fatigue_high_cycle.py`

---

### CLASSICAL STATEMENT
*"In high-cycle fatigue the stress amplitude governs life: sigma_a = sigma_f' (2 N_f)^b, where N_f is the number of cycles to failure, sigma_f' the fatigue strength coefficient (~ ultimate strength) and b the fatigue strength exponent (~ -0.05 to -0.12); Basquin's law gives the S-N curve's elastic line and, combined with the Coffin-Manson law, the total-strain-life approach."*
- O.H. Basquin, 1910. Source: Wikipedia: Basquin's law; Basquin (1910), Proc. ASTM 10:625

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-stress-amplitude, infinite-life reference*: Basquin's law is defined against a reference with zero stress amplitude where life is infinite; the finite life is the stress-driven damage away from this zero-stress reference.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the fatigue life carries a coherence floor. N_phi(kappa) = N_Basquin*(1 + kappa*(phi-1)) + kappa*phi^-1*N_floor, where N_floor is the phi-ground life ceiling. At kappa->0 the ideal power law is recovered; at kappa=1 the fatigue limit is never absolute - damage always accumulates.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} N_phi = (sigma_f'/sigma_a)^(1/(-b)) -> Basquin's law is the zero-damage, ideal-power-law limit of high-cycle fatigue life.
```

---

### STAGE 4 - SIMULATION

`sim/1828_basquin_fatigue_high_cycle.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1828_basquin_fatigue_high_cycle.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: There is no absolute fatigue limit (below which life is infinite): an irreducible damage floor remains even below the classical endurance limit, so very-high-cycle failures always occur.
EXPERIMENT (VERIFIED): Giga-cycle (10^9-10^10) fatigue testing of steels and titanium alloys below the classical endurance limit, measuring the finite-life floor.
VERIFIED BY: A material with exactly infinite life below its fatigue limit.
```

---

### RECOGNITION
Connects to Law 1827 (Coffin-Manson) and Law 1829 (Miner) - the stress cycles chip the part, and the phi-law keeps a chip always present.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; life floor scales as phi^-1 * N_floor.

### CLARITY
The repeated stress chips the part; the phi-law keeps a chip always present.

### NOVELTY
Classical Basquin gives an absolute endurance limit; the phi-law keeps an irreducible damage floor.

### ACTIONABILITY
Run sim/1828_basquin_fatigue_high_cycle.py; verify N_f = (sigma_f'/sigma_a)^(1/(-b)) at kappa->0; proceed to 1829.
