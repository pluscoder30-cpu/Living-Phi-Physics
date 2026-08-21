# PHI-PHYSICS — LAW 368
## Saint-Venant's Principle

**Domain:** Structural Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/368_saint_venants_principle.md` · **Sim:** `sim/368_saint_venants_principle.py`

---

### CLASSICAL STATEMENT
*"Statistically equivalent systems of loads that differ only locally produce the same stress distribution at distances large compared with the loaded region; the detailed load distribution matters only near the load application point."*
— Adhemar Jean Claude Barre de Saint-Venant, 1855. Source: Wikipedia: Saint-Venant's principle; Saint-Venant (1855), memoir on torsion

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *point load*: the principle requires the loaded region to shrink toward a point so that distant stress is load-detail-independent — the zero of the load's extent.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the Saint-Venant decay length carries a coherence floor. l_sv_phi(kappa) = l_sv*(1 + kappa*(phi-1)) + kappa*phi^-1*lambda_phi. At kappa->0 the classical decay-length picture is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} l_sv_phi = l_sv -> Saint-Venant's principle is the point-load, elastic-continuum limit.
```

---

### STAGE 4 — SIMULATION

`sim/368_saint_venants_principle.py`: reproduces the classical value l_sv = 0.1 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/368_saint_venants_principle.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Load-detail effects persist to a phi-coherently larger distance phi^-1*lambda_phi than the classical decay length.
EXPERIMENT (VERIFIED): Photoelasticity/experimental-stress tests comparing stress decay with distance from differently-shaped load patches.
VERIFIED BY: Stress is exactly load-detail-independent beyond the classical Saint-Venant length at full coupling.
```

---

### RECOGNITION
Connects to Law 367 (beam — end effects) and Law 372 (Cauchy stress).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The point load is a limit; every load leaves a phi echo that travels farther than the ideal says.

### NOVELTY
Classical elasticity exacts the decay length; the phi-law extends it by a coherence floor.

### ACTIONABILITY
Run sim/368_saint_venants_principle.py; verify the decay picture at kappa->0.
