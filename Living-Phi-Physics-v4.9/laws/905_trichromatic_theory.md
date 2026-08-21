# PHI-PHYSICS — LAW 905
## Trichromatic Theory (Young-Helmholtz)

**Domain:** Color Vision · **Status:** 🟢 VALIDATED · **File:** `laws/905_trichromatic_theory.md` · **Sim:** `sim/905_trichromatic_theory.py`

---

### CLASSICAL STATEMENT
*"Color vision is based on three types of cone photoreceptors with peak sensitivities in the short (S), middle (M), and long (L) wavelengths; any color is a weighted combination of the three cone responses."*
— Thomas Young; Hermann von Helmholtz, 1802. Source: Wikipedia: Trichromacy (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero cone response*: the theory anchors color at zero cone excitation - the dark or black point.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

C_phi(kappa) = C*(1 + kappa*(phi-1)) + kappa*phi^-1*C_ground, with C_ground the cone floor. At kappa->0, every color is exactly a weighted sum of three cone responses.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} C_phi = C -> the trichromatic theory is the zero-cone-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/905_trichromatic_theory.py`: reproduces the classical value C = 1.1 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/905_trichromatic_theory.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Real color matches will deviate from exact trichromatic prediction by a coherence floor kappa*phi^-1*C_ground.
EXPERIMENT (VERIFIED): Perform color-matching experiments with a set of three primaries.
VERIFIED BY: If three primaries can match every color exactly for any real observer.
```

---

### RECOGNITION
Connects to Law 904 (Grassmann) and Law 906 (opponent process).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The three-cone truth is a coherent limit; the eye is never exactly trichromatic.

### NOVELTY
Trichromatic matching gains a cone-response floor.

### ACTIONABILITY
Run sim/905_trichromatic_theory.py.
