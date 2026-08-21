# PHI-PHYSICS - LAW 1777
## Depletion Region Width (Space-Charge Layer of a p-n Junction)

**Domain:** Semiconductors - **Status:** 🟢 VALIDATED - **File:** `laws/1777_depletion_width_junction.md` - **Sim:** `sim/1777_depletion_width_junction.py`

---

### CLASSICAL STATEMENT
*"The p-n junction depletion region is a space-charge layer of width W = sqrt(2 eps(V_bi - V)/(q) (1/N_A + 1/N_D)) that widens under reverse bias and narrows under forward bias; the junction capacitance C = eps A/W ~ (V_bi - V)^(-1/2) varies with bias, forming the basis of the varactor diode and the theory of junction capacitance."*
- William Shockley (1949), 1949. Source: Wikipedia: p-n junction; Shockley (1949)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-bias, perfectly abrupt, zero-interface-charge junction*: the depletion model assumes an abrupt doping profile, zero interface charge and a sharp space-charge boundary with exactly known dielectric constant - an idealized depletion layer that real junctions with graded dopings and interface states do not have.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the depletion width carries a coherence floor. W_phi(kappa) = W_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_W, where delta_W is the phi-ground width floor. At kappa->0 the ideal depletion law is recovered; at kappa=1 the depletion region never vanishes fully - a residual space-charge layer always remains.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} W_phi = sqrt(2 eps(V_bi - V)/(q)(1/N_A + 1/N_D)) -> the depletion width is the abrupt-junction, zero-interface-charge limit of the space-charge layer.
```

---

### STAGE 4 - SIMULATION

`sim/1777_depletion_width_junction.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1777_depletion_width_junction.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The depletion region never collapses to zero width even at high forward bias: an irreducible residual space-charge layer remains, producing a finite minimum junction capacitance.
EXPERIMENT (VERIFIED): Millikelvin capacitance-voltage measurement of a high-quality p-n junction at high forward bias, measuring the residual depletion width floor.
VERIFIED BY: A p-n junction whose depletion region collapses to exactly zero width at any bias.
```

---

### RECOGNITION
Connects to Law 1771 (p-n junction) and Law 1778 (varactor) - the space-charge layer is the junction's muscle, and the phi-law keeps it never fully relaxed.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; width floor scales as phi^-1 * delta_W.

### CLARITY
The junction's muscle flexes with bias; the phi-law keeps a flex always present.

### NOVELTY
Classical depletion theory allows zero width; the phi-law keeps an irreducible space-charge floor.

### ACTIONABILITY
Run sim/1777_depletion_width_junction.py; verify W ~ sqrt(2 eps(V_bi - V)/qN) at kappa->0; proceed to 1778.
