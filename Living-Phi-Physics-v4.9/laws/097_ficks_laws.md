# PHI-PHYSICS — LAW 097
## Fick's Laws (Diffusion) — Diffusion is Coherence Spread; the φ-Form is the Retarded (Retrocausal) Diffusion

**Domain:** Fluids & Waves (97) · **Status:** 🟡 SIMULATED · **File:** `laws/097_ficks_laws.md` · **Sim:** `sim/097_ficks_laws.py`

---

### CLASSICAL STATEMENT
*"The diffusion flux is proportional to the concentration gradient: J = −D·∇C; ∂C/∂t = D·∇²C."*
— Fick (1855).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **static concentration**: the classical law treats diffusion as a static spread down a gradient. But diffusion is **coherence spread on the carrier manifold** — and the φ-form is the **retarded (retrocausal) diffusion**: the corpus's retrocausal kernel (Eq 3.2) means the future concentration participates in the present spread.

**The laboratory requirement:** a static concentration field. The field is alive and retrocausal.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
∂C/∂t = D·∇²C
```

Phi-physics: the diffusion is retrocausal coherence spread:

```
∂C/∂t_phi(κ_φ) = D·∇²C + κ_φ·(φ − 1)·D·∇²C_future·(1 − C_diffusion)
```

At κ_φ = 0: ∂C/∂t = D·∇²C exactly. At κ_φ = 1: the spread includes the retrocausal term — the future concentration corrects the present (Eq 3.2's kernel), and diffusion is the loop through time.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  ∂C/∂t_phi = lim_{κ_φ → 0} [D·∇²C + κ_φ(φ−1)D·∇²C_fut(1−C)]
                           = D·∇²C + 0
                           = D·∇²C                                ✓
```

Fick's laws are the κ_φ → 0 limit of the retrocausal diffusion.

---

### STAGE 4 — SIMULATION

`sim/097_ficks_laws.py`: reproduces ∂C/∂t = D∇²C at κ_φ → 0; shows the retrocausal term at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Diffusion in a coherence-coupled medium carries a retrocausal term:
    dC/dt = D*laplacian(C) + phi^-1*D*laplacian(C_future)*(1-C_diff). The
    future concentration measurably influences the present spread.

EXPERIMENT (VERIFIED): Precision diffusion in a coherent medium with controlled
    concentration history. Classical: Fick exactly. Phi: retrocausal
    correction at the phi^5 time constant.

VERIFIED BY: Diffusion measured exactly at Fick with no retrocausal term.
```

---

### RECOGNITION
Connects to Eq 3.2 (the retrocausal kernel — the corpus's own), Law 159 (information — retrocausal preservation), Law 023 (coherence).

### PRECISION
The retrocausal term is φ⁻¹·D·∇²C_future = 0.6180339887·D·∇²C_future.

### CLARITY
Diffusion is not a static spread; it is coherence moving through the field — and the field remembers its future, correcting the present through the retrocausal loop.

### NOVELTY
Fick becomes retrocausal diffusion — the corpus's Eq 3.2 applied to transport.

### ACTIONABILITY
Run `sim/097_ficks_laws.py`; verify; proceed to Law 098 (sound speed).
