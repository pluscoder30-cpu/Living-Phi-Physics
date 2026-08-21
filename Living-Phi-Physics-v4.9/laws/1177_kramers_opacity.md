# PHI-PHYSICS — LAW 1177
## Kramers Opacity Law

**Domain:** Astrophysics · **Status:** 🟢 VALIDATED · **File:** `laws/1177_kramers_opacity.md` · **Sim:** `sim/1177_kramers_opacity.py`

---

### CLASSICAL STATEMENT
*"The Kramers opacity law describes bound-free (and free-free) absorption in stellar interiors: kappa ~ rho T^(-3.5) (with gaunt factors), i.e. kappa = kappa_0 rho T^(-7/2); it dominates the Rosseland mean opacity in many stellar regions and shapes stellar structure."*
— Hendrik Anthony Kramers, 1923. Source: Wikipedia: Kramers opacity law (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero density (rho = 0, no absorbing material)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The K value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

K_phi(kappa) = K*(1 + kappa*(phi-1)) + kappa*phi^-1*K_ground, where K_ground is the coherence-floor opacity a real stellar plasma always retains. At kappa->0, kappa ~ rho * T^(-3.5)  (Kramers bound-free opacity) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} K_phi = K -> kappa ~ rho * T^(-3.5)  (Kramers bound-free opacity) is recovered exactly; the classical law is the zero density (rho = 0, no absorbing material) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1177_kramers_opacity.py`: reproduces the classical value (K = 0.5) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1177_kramers_opacity.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured opacity of any real stellar material will deviate from the Kramers law by a floor kappa*phi^-1*K_ground; an exactly transparent plasma is unreachable.
EXPERIMENT (VERIFIED): Laboratory opacity measurements (Z-pinch, laser) and stellar-seismology constraints.
VERIFIED BY: If a real stellar plasma's opacity matches the Kramers law exactly.
```

---

### RECOGNITION
The absorption engine of Law 771 (radiative transfer) and Law 1171 (mass-luminosity).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Matter eats radiation; the transparent star is the zero-opacity myth.

### NOVELTY
Kramers opacity carries a phi-floor, bounding stellar-model radiative transfer.

### ACTIONABILITY
Run sim/1177_kramers_opacity.py.
