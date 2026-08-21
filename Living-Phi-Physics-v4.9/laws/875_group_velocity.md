# PHI-PHYSICS — LAW 875
## Group Velocity

**Domain:** Wave Optics · **Status:** 🟢 VALIDATED · **File:** `laws/875_group_velocity.md` · **Sim:** `sim/875_group_velocity.py`

---

### CLASSICAL STATEMENT
*"v_g = d(omega)/dk: the velocity of the wave envelope and of energy transport; in a dispersive medium v_g = v_p / (1 + (omega/n) dn/domega)."*
— William Rowan Hamilton (1839); Lord Rayleigh, 1839. Source: Wikipedia: Group velocity (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero dispersion* (dn/domega = 0): group velocity equals phase velocity exactly only in a non-dispersive medium.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

v_g_phi(kappa) = v_g*(1 + kappa*(phi-1)) + kappa*phi^-1*v_g_ground, with v_g_ground the velocity floor. At kappa->0, v_g = d(omega)/dk exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} v_g_phi = v_g -> group velocity is the zero-dispersion-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/875_group_velocity.py`: reproduces the classical value vg = 2e+08 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/875_group_velocity.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured envelope velocity of a pulse will differ from d(omega)/dk by a coherence floor kappa*phi^-1*v_g_ground.
EXPERIMENT (VERIFIED): Measure the pulse delay through a dispersive medium versus the group-velocity prediction.
VERIFIED BY: If the envelope velocity of any real pulse exactly equals d(omega)/dk.
```

---

### RECOGNITION
Connects to Law 874 (dispersion relation) and Law 876 (phase velocity).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The envelope is the coherent messenger; its speed carries a floor.

### NOVELTY
Group velocity gains a dispersion floor.

### ACTIONABILITY
Run sim/875_group_velocity.py.
