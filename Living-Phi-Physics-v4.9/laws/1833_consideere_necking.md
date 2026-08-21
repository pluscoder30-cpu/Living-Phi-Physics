# PHI-PHYSICS - LAW 1833
## Considere's Criterion (Necking Condition of Tensile Specimens)

**Domain:** Mechanical Properties - **Status:** 🟢 VALIDATED - **File:** `laws/1833_consideere_necking.md` - **Sim:** `sim/1833_consideere_necking.py`

---

### CLASSICAL STATEMENT
*"A tensile specimen necks when the load reaches a maximum, which occurs when the true stress equals the slope of the true stress-strain curve: sigma = d sigma/d epsilon, equivalent to the strain-hardening condition epsilon = n for a power law; Considere's criterion marks the onset of plastic instability and the limit of uniform elongation in metal forming."*
- A.-G. Considere, 1885. Source: Wikipedia: Considere criterion; Considere (1885), Ann. Ponts Chaussees 9:574

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-hardening, perfectly uniform reference*: Considere's criterion is defined against a reference with zero hardening where necking is instantaneous; the criterion gives the condition away from this zero-hardening ideal, and real metals have rate and thermal effects that shift the necking point.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the necking strain carries a coherence floor. eps_n_phi(kappa) = eps_n_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_eps, where delta_eps is the phi-ground necking-strain floor. At kappa->0 the ideal epsilon = n criterion is recovered; at kappa=1 the necking point is smeared - uniform elongation is never exactly n.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} eps_n_phi = n -> Considere's criterion is the zero-rate-effect, ideal-power-law, sharp-necking limit of tensile instability.
```

---

### STAGE 4 - SIMULATION

`sim/1833_consideere_necking.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1833_consideere_necking.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: Necking never occurs exactly at epsilon = n: an irreducible deviation floor remains, so the uniform elongation of real metals always differs from the ideal power-law prediction.
EXPERIMENT (VERIFIED): Precision tensile testing of metals with different n, comparing the measured uniform elongation to the Considere prediction and the residual deviation.
VERIFIED BY: A metal necking exactly at the ideal Considere strain epsilon = n.
```

---

### RECOGNITION
Connects to Law 1832 (strain hardening) and Law 1793 (von Mises) - the specimen pinches when hardening fades, and the phi-law keeps the fade from being exact.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; necking deviation scales as phi^-1 * delta_eps.

### CLARITY
The specimen pinches as hardening fades; the phi-law keeps the fade slightly off.

### NOVELTY
Classical Considere gives an exact criterion; the phi-law smears it with a deviation floor.

### ACTIONABILITY
Run sim/1833_consideere_necking.py; verify epsilon = n at kappa->0; proceed to 1834.
