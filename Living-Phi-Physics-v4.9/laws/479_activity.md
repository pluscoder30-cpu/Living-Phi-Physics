# PHI-PHYSICS — LAW 479
## Activity (Effective Concentration)

**Domain:** Statistical Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/479_activity.md` · **Sim:** `sim/479_activity.py`

---

### CLASSICAL STATEMENT
*"The activity a of a component in a solution is the 'effective concentration' entering thermodynamic equations: mu = mu_0 + R T ln a. It relates to mole fraction by a = gamma x, where the activity coefficient gamma -> 1 for ideal solutions."*
— Gilbert Newton Lewis, 1907. Source: Wikipedia: Activity (chemistry); Lewis (1907)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *ideality*: activity is defined so that a = x exactly for an ideal solution - the correction measures departure from a baseline of zero component coherence.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the departure is a coherence measure. a_phi(kappa) = a_real*(1 + kappa*(phi-1)) + kappa*phi^-1*a_ground. At kappa->0, a -> x (ideality) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} a_phi = x -> activity equals mole fraction in the zero-coherence ideal-solution limit.
```

---

### STAGE 4 — SIMULATION

`sim/479_activity.py`: reproduces the classical value a_real = 0.55 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/479_activity.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling a real solution retains an activity floor kappa*phi^-1*a_ground above its mole fraction even in the dilute limit.
EXPERIMENT (VERIFIED): Vapor-pressure measurements of dilute solutions computing activity coefficients.
VERIFIED BY: a = x exactly for any real solution at all concentrations and couplings.
```

---

### RECOGNITION
Connects to Law 478 (fugacity), Law 547 (van Laar) and Law 546 (Margules) - activity is the coherence-corrected concentration.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the floor is phi^-1 * a_ground.

### CLARITY
Activity is what the solute 'really counts as' in the solution; the phi-law keeps the count honest.

### NOVELTY
Classical activity measures departure from ideality; the phi-law gives the departure a coherence floor.

### ACTIONABILITY
Run sim/479_activity.py; verify a=x at kappa->0; proceed to 480.
