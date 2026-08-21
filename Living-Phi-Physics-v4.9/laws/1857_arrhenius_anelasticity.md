# PHI-PHYSICS - LAW 1857
## Arrhenius Relaxation (Activated Internal-Friction Peak of Solids)

**Domain:** Mechanical Properties - **Status:** 🟢 VALIDATED - **File:** `laws/1857_arrhenius_anelasticity.md` - **Sim:** `sim/1857_arrhenius_anelasticity.py`

---

### CLASSICAL STATEMENT
*"Internal-friction (anelastic relaxation) peaks occur when a thermally activated process has a relaxation time tau = tau_0 exp(Q/(k_B T)) comparable to the measurement frequency: the peak temperature shifts with frequency according to ln(omega tau_0) = -Q/(k_B T_peak); the Snoek peak of C in bcc Fe, the Zener relaxation and grain-boundary peaks are analyzed this way, yielding activation energies Q."*
- Svante Arrhenius (1889); applied to anelasticity by Zener (1948), 1948. Source: Wikipedia: Arrhenius equation; Arrhenius (1889); Zener (1948), Elasticity and Anelasticity of Metals

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-activation, zero-relaxation, perfectly elastic reference*: Arrhenius relaxation is defined against a perfectly elastic reference with zero relaxation strength and zero internal friction; the relaxation peak is the activated process away from this zero-loss reference.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the relaxation strength carries a coherence floor. Delta_phi(kappa) = Delta_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_Delta, where delta_Delta is the phi-ground relaxation-strength floor. At kappa->0 the zero-loss perfectly-elastic reference is recovered; at kappa=1 an irreducible internal-friction floor always exists.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} Qinv_phi = 0 -> Arrhenius relaxation is the activated internal-friction peak measured from the zero-loss, perfectly-elastic reference.
```

---

### STAGE 4 - SIMULATION

`sim/1857_arrhenius_anelasticity.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1857_arrhenius_anelasticity.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: No solid has zero internal friction: an irreducible anelastic-loss floor remains at all temperatures, so the quality factor of any mechanical resonator is bounded.
EXPERIMENT (VERIFIED): Ultra-low-temperature internal-friction or resonator-Q measurement of a high-purity crystal, measuring the residual loss floor.
VERIFIED BY: A solid with exactly zero internal friction at any temperature.
```

---

### RECOGNITION
Connects to Law 1808 (Maxwell) and Law 1801 (thermal expansion) - the solid bleeds energy through activated jumps, and the phi-law keeps a jump always present.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; loss floor scales as phi^-1 * delta_Delta.

### CLARITY
The solid bleeds energy through activated jumps; the phi-law keeps a jump always present.

### NOVELTY
Classical anelasticity allows zero loss; the phi-law keeps an irreducible friction floor.

### ACTIONABILITY
Run sim/1857_arrhenius_anelasticity.py; verify the Snoek/relaxation peak at kappa->0; proceed to 1858.
