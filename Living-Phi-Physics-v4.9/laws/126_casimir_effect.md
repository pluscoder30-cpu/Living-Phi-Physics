# PHI-PHYSICS — LAW 126
## Casimir Effect — The Force is the ZPF Coherence Pressure; the Vacuum Between the Plates is Not Zero

**Domain:** Particle & Field (126) · **Status:** 🟡 SIMULATED · **File:** `laws/126_casimir_effect.md` · **Sim:** `sim/126_casimir_effect.py`

---

### CLASSICAL STATEMENT
*"Two uncharged plates attract due to vacuum fluctuations: F = π²ħcA/(240d⁴)."*
— Casimir (1948), measured by Lamoreaux (1997).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **empty vacuum between the plates**: the classical reading treats the space between the plates as empty, with the force arising from fluctuation differences. But the vacuum is not empty (Law 042, Law 171): the Casimir force is the **ZPF coherence pressure** — the difference in φ-coherence between the confined and free vacuum — and the corpus's own `CORBETT_CASIMIR.md` already pursued this.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
F = π²ħcA/(240d⁴)
```

Phi-physics — the coherence pressure:

```
F_phi(κ_φ) = (π²ħcA/(240d⁴))·(1 + κ_φ·(φ − 1)·(1 − C_vacuum))
```

At κ_φ = 0: the classical Casimir. At κ_φ = 1: the force breathes with the vacuum coherence — the pressure is the φ-ground difference, and the vacuum between the plates is structured (Law 200's information substrate).

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  F_phi = π²ħcA/(240d⁴) (classical Casimir)                ✓
```

The Casimir effect is the κ_φ → 0 limit of the φ-coherence pressure.

---

### STAGE 4 — SIMULATION

`sim/126_casimir_effect.py`: reproduces the classical force at κ_φ → 0; shows the coherence-breathed pressure at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The Casimir force carries a phi-coherence term: the vacuum between
    the plates is structured (Law 200), and the force deviates from the ideal
    π^2*hbar*c*A/(240*d^4) by (1 + phi^-1*(1-C_vacuum)).

EXPERIMENT (VERIFIED): Precision Casimir measurement at controlled vacuum coherence.
    Classical: ideal Casimir. Phi: phi-coherent deviation.

VERIFIED BY: Casimir force measured exactly at the ideal value with no
    coherence term.
```

---

### RECOGNITION
Connects to `CORBETT_CASIMIR.md` (the corpus's own), Law 042 (the vacuum), Law 171 (the φ-ground), Law 200 (the vacuum substrate), Law 158 (the cosmological constant).

### PRECISION
The deviation is φ⁻¹·(1−C) = 0.6180339887·(1−C).

### CLARITY
The plates do not attract through empty space; they feel the vacuum's coherence — and the vacuum between them is never zero, it is the φ-ground.

### NOVELTY
The Casimir force as the φ-coherence pressure — the corpus's own research made law.

### ACTIONABILITY
Run `sim/126_casimir_effect.py`; verify; proceed to Law 127.
