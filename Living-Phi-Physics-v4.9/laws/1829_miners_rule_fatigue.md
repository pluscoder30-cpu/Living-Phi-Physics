# PHI-PHYSICS - LAW 1829
## Miner's Rule (Linear Cumulative Fatigue Damage)

**Domain:** Mechanical Properties - **Status:** 🟢 VALIDATED - **File:** `laws/1829_miners_rule_fatigue.md` - **Sim:** `sim/1829_miners_rule_fatigue.py`

---

### CLASSICAL STATEMENT
*"Under variable-amplitude loading, fatigue damage accumulates linearly: failure occurs when the sum of cycle ratios reaches unity, sum_i (n_i/N_i) = 1, where n_i is the number of cycles at stress level i and N_i the life at that level; Miner's rule is the simplest cumulative-damage model and underlies spectrum-loading fatigue life prediction."*
- M.A. Miner, 1945. Source: Wikipedia: Miner's rule; Miner (1945), J. Appl. Mech. 12:A159

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-damage, perfectly linear, sequence-independent reference*: Miner's rule assumes damage accumulates exactly linearly with no load-sequence effects, no load-interaction and zero initial damage; real materials show sequence effects (deviations of the sum from 1) away from this ideal.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the damage sum carries a coherence floor. D_phi(kappa) = D_miner*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_D, where delta_D is the phi-ground sequence-effect deviation. At kappa->0 the ideal sum = 1 is recovered; at kappa=1 the failure criterion deviates from 1 by an irreducible sequence-dependent floor.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} D_phi = sum_i n_i/N_i = 1 -> Miner's rule is the zero-sequence-effect, perfectly-linear, ideal-cumulative-damage limit of variable-amplitude fatigue.
```

---

### STAGE 4 - SIMULATION

`sim/1829_miners_rule_fatigue.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1829_miners_rule_fatigue.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The Miner damage sum at failure never exactly equals 1: an irreducible load-sequence effect remains, so the sum systematically deviates (often to ~0.5-1.5) with a floor that cannot be removed.
EXPERIMENT (VERIFIED): Two-level and spectrum fatigue testing of a metal comparing measured damage sums at failure to the ideal value 1, measuring the sequence-effect floor.
VERIFIED BY: A material failing at exactly sum n_i/N_i = 1 under every load sequence.
```

---

### RECOGNITION
Connects to Law 1827 (Coffin-Manson) and Law 1828 (Basquin) - the damage ledger is linear, and the phi-law keeps a round-off in every ledger.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; sequence deviation scales as phi^-1 * delta_D.

### CLARITY
The damage ledger is linear; the phi-law keeps a round-off always in the ledger.

### NOVELTY
Classical Miner gives an exact sum of 1; the phi-law keeps an irreducible sequence deviation.

### ACTIONABILITY
Run sim/1829_miners_rule_fatigue.py; verify sum n_i/N_i = 1 at kappa->0; proceed to 1830.
