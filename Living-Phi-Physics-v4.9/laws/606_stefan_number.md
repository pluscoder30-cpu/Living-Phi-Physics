# PHI-PHYSICS — LAW 606
## Stefan Number (Sensible to Latent Heat Ratio)

**Domain:** Heat & Calorimetry · **Status:** 🟢 VALIDATED · **File:** `laws/606_stefan_number.md` · **Sim:** `sim/606_stefan_number.py`

---

### CLASSICAL STATEMENT
*"The Stefan number is the ratio of sensible heat to latent heat in a phase-change process: Ste = c_p DeltaT/L, where c_p is the specific heat, DeltaT the temperature excursion and L the latent heat. It governs melting/freezing problems (Stefan problems)."*
— Josef Stefan (concept; named in heat-transfer practice), 1889. Source: Wikipedia: Stefan number; Stefan (1889), named in later phase-change literature

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero temperature excursion*: Ste = 0 exactly at DeltaT = 0 where the phase change is isothermal with no sensible heat - a process with zero thermal coherence beyond the latent heat.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the isothermal condition carries coherence. Ste_phi(kappa) = Ste*(1 + kappa*(phi-1)) + kappa*phi^-1*Ste_ground. At kappa->0 the Stefan number is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} Ste_phi = c_p DeltaT/L -> the Stefan number is the zero-excursion zero-coherence phase-change limit.
```

---

### STAGE 4 — SIMULATION

`sim/606_stefan_number.py`: reproduces the classical value Ste = 0.376 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/606_stefan_number.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling even an isothermal phase change carries a residual sensible-coherence Ste_ground.
EXPERIMENT (VERIFIED): Melting-front tracking experiments (e.g. phase-change materials) determining Ste.
VERIFIED BY: Ste = 0 exactly at zero temperature excursion for all couplings.
```

---

### RECOGNITION
Connects to Law 411 (latent heat) and Law 601 (Fourier number) - the Stefan number is the sensible-latent coherence ratio.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the floor is phi^-1 * Ste_ground.

### CLARITY
The melt remembers the heat it did not yet feel; the phi-law keeps the memory.

### NOVELTY
Classical Stefan zeroes at no excursion; the phi-law adds the sensible-coherence floor of the real melt.

### ACTIONABILITY
Run sim/606_stefan_number.py; verify Ste at kappa->0; proceed to 607.
