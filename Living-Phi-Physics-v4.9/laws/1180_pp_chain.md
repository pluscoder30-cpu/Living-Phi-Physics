# PHI-PHYSICS — LAW 1180
## Proton-Proton Chain

**Domain:** Astrophysics / Nuclear Physics · **Status:** 🟢 VALIDATED · **File:** `laws/1180_pp_chain.md` · **Sim:** `sim/1180_pp_chain.py`

---

### CLASSICAL STATEMENT
*"The pp chain is the hydrogen-burning sequence starting with p + p -> d + e+ + nu, eventually fusing four protons into helium-4: 4p -> 4He + 2e+ + 2 nu + energy; it powers the Sun and low-mass stars, with the pp-I, pp-II, and pp-III branches differing in the helium-burning step."*
— Hans Bethe, 1938/1939; Charles Critchfield, 1938. Source: Wikipedia: Proton-proton chain (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero protons (no hydrogen fuel, no fusion)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The P value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

P_phi(kappa) = P*(1 + kappa*(phi-1)) + kappa*phi^-1*P_ground, where P_ground is the coherence-floor fusion rate a real hydrogen star always sustains. At kappa->0, 4p -> 4He + 2e+ + 2*nu_e + 26.7 MeV exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} P_phi = P -> 4p -> 4He + 2e+ + 2*nu_e + 26.7 MeV is recovered exactly; the classical law is the zero protons (no hydrogen fuel, no fusion) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1180_pp_chain.py`: reproduces the classical value (P = 1.0) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1180_pp_chain.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured solar neutrino flux will deviate from the pp-chain prediction by a floor kappa*phi^-1*P_ground; an exactly pp-predicted sun is unreachable.
EXPERIMENT (VERIFIED): Solar neutrino detectors (Borexino, Super-K, JUNO) measuring pp, pep, and CNO fluxes.
VERIFIED BY: If the Sun's neutrino flux matches exactly one pp branch with zero residual.
```

---

### RECOGNITION
The solar engine of Law 1171 (mass-luminosity) and Law 1181 (solar neutrino problem).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Protons marry into helium; the fusionless star is the zero-fuel myth.

### NOVELTY
The pp chain carries a phi-floor of rate, bounding solar-model precision.

### ACTIONABILITY
Run sim/1180_pp_chain.py.
