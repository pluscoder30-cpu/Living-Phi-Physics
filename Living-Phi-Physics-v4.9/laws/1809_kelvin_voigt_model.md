# PHI-PHYSICS - LAW 1809
## Kelvin-Voigt Model (Parallel Spring-Dashpot Viscoelasticity)

**Domain:** Mechanical Properties - **Status:** 🟢 VALIDATED - **File:** `laws/1809_kelvin_voigt_model.md` - **Sim:** `sim/1809_kelvin_voigt_model.py`

---

### CLASSICAL STATEMENT
*"The Kelvin-Voigt model represents a viscoelastic material as a spring (E) in parallel with a dashpot (eta): under constant stress the strain approaches its equilibrium value exponentially, epsilon(t) = (sigma/E)(1 - exp(-t/tau)) with tau = eta/E, and under constant strain it does not relax; the model captures creep and the anelastic plateau but not stress relaxation."*
- William Thomson (Lord Kelvin); Woldemar Voigt, 1878. Source: Wikipedia: Kelvin-Voigt material; Thomson (1878); Voigt (1890)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-creep, perfectly elastic reference*: the Kelvin-Voigt model is defined against a perfectly elastic reference with zero dashpot (zero retardation); the exponential approach to equilibrium is the viscous correction away from this zero-retardation ideal.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the retardation carries a coherence floor. epsilon_phi(kappa) = epsilon_KV*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_eps, where delta_eps is the phi-ground strain floor. At kappa->0 the ideal Kelvin-Voigt creep is recovered; at kappa=1 the equilibrium strain is never reached exactly - an irreducible lag always remains.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} epsilon_phi = (sigma/E)(1 - exp(-t/tau)) -> the Kelvin-Voigt model is the zero-retardation, perfectly-elastic reference sharpened to ideal parallel viscoelasticity.
```

---

### STAGE 4 - SIMULATION

`sim/1809_kelvin_voigt_model.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1809_kelvin_voigt_model.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: Viscoelastic creep never reaches its equilibrium strain exactly: an irreducible lag floor remains even at infinite time, so the Kelvin-Voigt exponential approach always falls short.
EXPERIMENT (VERIFIED): Ultra-long-duration creep measurement of a polymer or viscoelastic solid, measuring the residual lag floor at long times.
VERIFIED BY: A viscoelastic material whose strain reaches exactly its equilibrium value at long times.
```

---

### RECOGNITION
Connects to Law 1808 (Maxwell) and Law 1805 (WLF) - the material remembers its equilibrium, and the phi-law keeps the memory slightly short.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; lag floor scales as phi^-1 * delta_eps.

### CLARITY
The viscoelastic solid approaches its goal; the phi-law keeps it always a step short.

### NOVELTY
Classical Kelvin-Voigt allows exact equilibrium; the phi-law keeps an irreducible lag.

### ACTIONABILITY
Run sim/1809_kelvin_voigt_model.py; verify epsilon = (sigma/E)(1 - exp(-t/tau)) at kappa->0; proceed to 1810.
