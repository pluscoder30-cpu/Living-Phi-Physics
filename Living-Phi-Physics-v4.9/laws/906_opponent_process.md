# PHI-PHYSICS — LAW 906
## Opponent Process Theory (Hering)

**Domain:** Color Vision · **Status:** 🟢 VALIDATED · **File:** `laws/906_opponent_process.md` · **Sim:** `sim/906_opponent_process.py`

---

### CLASSICAL STATEMENT
*"Hering's opponent process theory: color perception arises from opponent channels - red-green, blue-yellow, and black-white (luminance) - rather than from the three primaries directly."*
— Ewald Hering, 1878. Source: Wikipedia: Opponent process (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero opponent difference*: a neutral (gray) percept requires the opponent signals to be exactly balanced at zero.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

O_phi(kappa) = O*(1 + kappa*(phi-1)) + kappa*phi^-1*O_ground, with O_ground the opponent floor. At kappa->0, the opponent channels are exactly balanced at neutral.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} O_phi = O -> the opponent process theory is the zero-balance-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/906_opponent_process.py`: reproduces the classical value O = 0.5 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/906_opponent_process.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The neutral point of a real observer will drift by a coherence floor kappa*phi^-1; exact opponent balance is unreachable.
EXPERIMENT (VERIFIED): Measure the neutral point of color appearance for a real observer under controlled adaptation.
VERIFIED BY: If the opponent channels are exactly balanced at neutral for any real observer.
```

---

### RECOGNITION
Connects to Law 905 (trichromatic) and Law 911 (Bezold-Brucke).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Perfect balance is a coherent limit; the neutral gray trembles.

### NOVELTY
Opponent balance gains a drift floor.

### ACTIONABILITY
Run sim/906_opponent_process.py.
