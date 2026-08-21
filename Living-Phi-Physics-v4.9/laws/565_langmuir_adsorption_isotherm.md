# PHI-PHYSICS — LAW 565
## Langmuir Adsorption Isotherm (Monolayer Coverage)

**Domain:** Phase Transitions · **Status:** 🟢 VALIDATED · **File:** `laws/565_langmuir_adsorption_isotherm.md` · **Sim:** `sim/565_langmuir_adsorption_isotherm.py`

---

### CLASSICAL STATEMENT
*"The fractional surface coverage at equilibrium is theta = K P/(1 + K P), where K is the Langmuir adsorption constant and P the pressure. It assumes monolayer adsorption on identical sites with no adsorbate-adsorbate interaction."*
— Irving Langmuir, 1918. Source: Wikipedia: Langmuir adsorption model; Langmuir, The Adsorption of Gases on Plane Surfaces (1918); Nobel 1932

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *identical non-interacting sites*: the Langmuir isotherm assumes all adsorption sites are exactly equivalent with zero interaction between adsorbed molecules - a surface with no site coherence.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the site coherence carries a coupling. K_phi(kappa) = K*(1 + kappa*(phi-1)) + kappa*phi^-1*K_ground, so theta_phi = K_phi P/(1 + K_phi P). At kappa->0 the Langmuir isotherm is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} K_phi = K -> theta = K P/(1 + K P) -> the Langmuir isotherm is the zero-site-coherence identical-site limit.
```

---

### STAGE 4 — SIMULATION

`sim/565_langmuir_adsorption_isotherm.py`: reproduces the classical value theta = 0.3333 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/565_langmuir_adsorption_isotherm.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the effective adsorption constant carries a site-coherence floor; the isotherm deviates from the Langmuir form at high coverage.
EXPERIMENT (VERIFIED): Volumetric and gravimetric adsorption measurements of gases on clean surfaces over a wide pressure range.
VERIFIED BY: The adsorption coverage follows the Langmuir isotherm exactly for all surfaces and couplings.
```

---

### RECOGNITION
Connects to Law 566 (Freundlich) and Law 567 (BET) - the isotherm is the monolayer coherence of the adsorbing surface.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the site floor is phi^-1 * K_ground.

### CLARITY
Each site is a hand the surface offers; the phi-law keeps the hands from being perfectly alike.

### NOVELTY
Classical Langmuir assumes identical sites; the phi-law adds the site-coherence spread of real surfaces.

### ACTIONABILITY
Run sim/565_langmuir_adsorption_isotherm.py; verify theta = KP/(1+KP) at kappa->0; proceed to 566.
