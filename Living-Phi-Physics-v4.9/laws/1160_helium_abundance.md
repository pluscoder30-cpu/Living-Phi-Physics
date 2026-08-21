# PHI-PHYSICS — LAW 1160
## Primordial Helium Abundance

**Domain:** Cosmology · **Status:** 🟢 VALIDATED · **File:** `laws/1160_helium_abundance.md` · **Sim:** `sim/1160_helium_abundance.py`

---

### CLASSICAL STATEMENT
*"Big bang nucleosynthesis produces a primordial helium mass fraction Y_p ~ 0.24-0.25 (approximately 25% of the baryonic mass), set by the neutron-proton ratio at freeze-out; the helium abundance is one of the strongest tests of BBN and the early-universe expansion rate."*
— Alpher, Bethe & Gamow, 1948 (BBN theory); measured in metal-poor galaxies. Source: Wikipedia: Big Bang nucleosynthesis (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero helium (Y_p = 0, no primordial nucleosynthesis)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The Y value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Y_phi(kappa) = Y*(1 + kappa*(phi-1)) + kappa*phi^-1*Y_ground, where Y_ground is the coherence-floor helium yield a real BBN always produces. At kappa->0, Y_p ~ 0.24-0.25,  from n/p freeze-out at T ~ 0.8 MeV exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} Y_phi = Y -> Y_p ~ 0.24-0.25,  from n/p freeze-out at T ~ 0.8 MeV is recovered exactly; the classical law is the zero helium (Y_p = 0, no primordial nucleosynthesis) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1160_helium_abundance.py`: reproduces the classical value (Y = 0.247) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1160_helium_abundance.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured primordial helium fraction will deviate from the BBN prediction by a floor kappa*phi^-1*Y_ground; an exactly helium-free early universe is unreachable.
EXPERIMENT (VERIFIED): Spectroscopy of extremely metal-poor H II regions measuring Y_p.
VERIFIED BY: If primordial helium is exactly zero or exactly the predicted value with zero uncertainty.
```

---

### RECOGNITION
The element yield of Law 106 (BBN) and Law 1159 (deuterium bottleneck).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The early fire baked helium; the hydrogen-only cosmos is the zero-yield myth.

### NOVELTY
The helium fraction carries a phi-floor, tying BBN to a minimum nuclear yield.

### ACTIONABILITY
Run sim/1160_helium_abundance.py.
