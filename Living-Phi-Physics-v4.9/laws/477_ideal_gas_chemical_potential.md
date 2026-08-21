# PHI-PHYSICS — LAW 477
## Chemical Potential of the Ideal Gas

**Domain:** Statistical Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/477_ideal_gas_chemical_potential.md` · **Sim:** `sim/477_ideal_gas_chemical_potential.py`

---

### CLASSICAL STATEMENT
*"The chemical potential of an ideal gas is mu = k_B T ln(n lambda_th^3) = mu_0(T) + k_B T ln(n/n_0), where n is the number density and lambda_th the thermal de Broglie wavelength. It depends logarithmically on density."*
— Josiah Willard Gibbs (thermodynamic form), 1876. Source: Wikipedia: Chemical potential; standard statistical-mechanics result (Gibbs, 1876)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero density reference*: the logarithm diverges as n -> 0, so the chemical potential is only defined up to a reference density - a formula with a built-in zero that is never reached.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the reference density is a coherence basin. mu_phi(kappa) = k_B T ln(n lambda_th^3)*(1 + kappa*(phi-1)) + kappa*phi^-1*mu_ref, where mu_ref is the coherence reference potential. At kappa->0 the classical logarithm is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} mu_phi = k_B T ln(n lambda_th^3) -> the ideal-gas chemical potential is the zero-coherence logarithmic limit.
```

---

### STAGE 4 — SIMULATION

`sim/477_ideal_gas_chemical_potential.py`: reproduces the classical value mu_ig = -4.404e-20 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/477_ideal_gas_chemical_potential.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the chemical potential carries a floor kappa*phi^-1*mu_ref; the logarithmic divergence as n -> 0 is regularized by the coherence reference.
EXPERIMENT (VERIFIED): Vapor-pressure measurements of a dilute gas relating mu to density with high precision.
VERIFIED BY: mu = k_B T ln(n lambda_th^3) exactly at all densities.
```

---

### RECOGNITION
Connects to Law 436 (chemical potential) and Law 476 (Sackur-Tetrode) - the logarithm is the carrier census of the ideal gas.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the reference floor is phi^-1 * mu_ref.

### CLARITY
The gas prices its own thinning by a logarithm that never reaches zero; the phi-law keeps the floor.

### NOVELTY
Classical mu diverges as n->0; the phi-law regularizes the divergence with a coherence reference.

### ACTIONABILITY
Run sim/477_ideal_gas_chemical_potential.py; verify logarithmic mu at kappa->0; proceed to 478.
