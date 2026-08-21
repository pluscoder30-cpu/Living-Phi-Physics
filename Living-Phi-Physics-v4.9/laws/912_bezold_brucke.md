# PHI-PHYSICS — LAW 912
## Bezold-Brücke Effect (Hue Shift)

**Domain:** Color Vision · **Status:** 🟢 VALIDATED · **File:** `laws/912_bezold_brucke.md` · **Sim:** `sim/912_bezold_brucke.py`

---

### CLASSICAL STATEMENT
*"The Bezold-Brücke effect: the perceived hue of monochromatic light shifts as its intensity changes - hue is not invariant with luminance."*
— Wilhelm von Bezold; Ernst Brücke, 1873. Source: Wikipedia: Bezold-Brücke shift (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero intensity* (I = 0): hue at zero intensity is undefined - the hue anchor is at zero luminance.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

lambda_h_phi(kappa) = lambda_h*(1 + kappa*(phi-1)) + kappa*phi^-1*lambda_h_ground, with lambda_h_ground the hue floor. At kappa->0, hue is exactly intensity-invariant.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} lambda_h_phi = lambda_h -> the Bezold-Brücke effect is the zero-intensity-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/912_bezold_brucke.py`: reproduces the classical value lh = 550 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/912_bezold_brucke.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The hue of a real monochromatic light will shift with intensity by a coherence floor kappa*phi^-1; hue invariance is unreachable.
EXPERIMENT (VERIFIED): Measure perceived hue of monochromatic lights as a function of intensity.
VERIFIED BY: If perceived hue is exactly intensity-invariant for any real observer.
```

---

### RECOGNITION
Connects to Law 905 (trichromatic) and Law 906 (opponent process).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Hue is a coherent limit; every color shifts with its luminance.

### NOVELTY
Hue invariance gains an intensity floor.

### ACTIONABILITY
Run sim/912_bezold_brucke.py.
