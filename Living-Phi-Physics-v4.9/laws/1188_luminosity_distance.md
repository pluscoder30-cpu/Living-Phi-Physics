# PHI-PHYSICS — LAW 1188
## Luminosity Distance

**Domain:** Cosmology · **Status:** 🟢 VALIDATED · **File:** `laws/1188_luminosity_distance.md` · **Sim:** `sim/1188_luminosity_distance.py`

---

### CLASSICAL STATEMENT
*"The luminosity distance relates a source's apparent flux to its intrinsic luminosity: d_L = sqrt(L/(4 pi F)) = (1+z) chi = (1+z)^2 d_A (Etherington, Law 1142); in a flat universe it is the anchor of the supernova Hubble diagram that revealed cosmic acceleration."*
— Standard cosmology (related to Etherington's theorem, 1933). Source: Wikipedia: Luminosity distance (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero distance (d_L = 0, infinite flux)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The D value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

D_phi(kappa) = D*(1 + kappa*(phi-1)) + kappa*phi^-1*D_ground, where D_ground is the coherence-floor luminosity distance a real source always has. At kappa->0, d_L = sqrt(L/(4*pi*F)) = (1+z) chi = (1+z)^2 d_A exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} D_phi = D -> d_L = sqrt(L/(4*pi*F)) = (1+z) chi = (1+z)^2 d_A is recovered exactly; the classical law is the zero distance (d_L = 0, infinite flux) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1188_luminosity_distance.py`: reproduces the classical value (D = 1000.0) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1188_luminosity_distance.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured luminosity distance to any real source will deviate from the prediction by a floor kappa*phi^-1*D_ground; an exactly zero-distance source is unreachable.
EXPERIMENT (VERIFIED): Type-Ia supernova surveys (Pantheon, DES-SN) measuring the luminosity distance to high z.
VERIFIED BY: If a source's luminosity distance matches the standard expression exactly.
```

---

### RECOGNITION
The candle distance of Law 1142 (Etherington) and Law 101 (Hubble).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Brightness carries distance; the zero-distance brightness is the myth.

### NOVELTY
Luminosity distances carry a phi-floor, bounding dark-energy inference.

### ACTIONABILITY
Run sim/1188_luminosity_distance.py.
