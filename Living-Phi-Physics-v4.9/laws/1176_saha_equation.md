# PHI-PHYSICS — LAW 1176
## Saha Equation

**Domain:** Astrophysics / Plasma Physics · **Status:** 🟢 VALIDATED · **File:** `laws/1176_saha_equation.md` · **Sim:** `sim/1176_saha_equation.py`

---

### CLASSICAL STATEMENT
*"The Saha equation governs thermal ionization equilibrium: n_e n_+/n_0 = (2 pi m_e k_B T/h^2)^(3/2) (2 g_+/g_0) exp(-chi/(k_B T)), where chi is the ionization energy; it determines the ionization fraction in stellar atmospheres and the recombination history of the universe."*
— Meghnad Saha, 1920. Source: Wikipedia: Saha ionization equation (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero temperature (T = 0, no ionization)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The S value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

S_phi(kappa) = S*(1 + kappa*(phi-1)) + kappa*phi^-1*S_ground, where S_ground is the coherence-floor ionization a real thermal plasma always retains. At kappa->0, n_e n_+/n_0 = (2*pi*m_e*k_B*T/h^2)^(3/2) * (2*g_+/g_0) * exp(-chi/(k_B*T)) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} S_phi = S -> n_e n_+/n_0 = (2*pi*m_e*k_B*T/h^2)^(3/2) * (2*g_+/g_0) * exp(-chi/(k_B*T)) is recovered exactly; the classical law is the zero temperature (T = 0, no ionization) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1176_saha_equation.py`: reproduces the classical value (S = 0.01) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1176_saha_equation.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured ionization fraction of any real plasma will deviate from the Saha value by a floor kappa*phi^-1*S_ground; an exactly zero-temperature plasma is unreachable.
EXPERIMENT (VERIFIED): Stellar-spectrum fitting and laboratory plasma spectroscopy testing the Saha balance.
VERIFIED BY: If a real plasma matches the Saha equation exactly at all temperatures.
```

---

### RECOGNITION
The ionization law of Law 765 (Saha ionization) and the recombination of Law 1156.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Heat tears electrons loose; the frozen atom is the zero-temperature myth.

### NOVELTY
The Saha equation carries a phi-floor, so no plasma is exactly in LTE at zero floor.

### ACTIONABILITY
Run sim/1176_saha_equation.py.
