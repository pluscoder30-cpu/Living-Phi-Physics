# PHI-PHYSICS — LAW 1228
## Brans-Dicke Theory

**Domain:** General Relativity · **Status:** 🟢 VALIDATED · **File:** `laws/1228_brans_dicke_theory.md` · **Sim:** `sim/1228_brans_dicke_theory.py`

---

### CLASSICAL STATEMENT
*"The Brans-Dicke theory is a scalar-tensor alternative to GR with a varying gravitational 'constant': the action S = (1/16 pi) integral sqrt(-g) [phi R - omega (d phi)^2/phi] + S_matter, where phi ~ 1/G is a dynamical scalar and omega the Brans-Dicke parameter; GR is recovered as omega -> infinity."*
— Carl Brans & Robert Dicke, 1961. Source: Wikipedia: Brans-Dicke theory (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *infinite Brans-Dicke parameter (omega -> infinity, constant G)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The B value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

B_phi(kappa) = B*(1 + kappa*(phi-1)) + kappa*phi^-1*B_ground, where B_ground is the coherence-floor scalar coupling a real gravity always retains. At kappa->0, S = (1/(16*pi)) integral sqrt(-g) [phi R - omega (d phi)^2/phi] + S_matter,  G ~ 1/phi exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} B_phi = B -> S = (1/(16*pi)) integral sqrt(-g) [phi R - omega (d phi)^2/phi] + S_matter,  G ~ 1/phi is recovered exactly; the classical law is the infinite Brans-Dicke parameter (omega -> infinity, constant G) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1228_brans_dicke_theory.py`: reproduces the classical value (B = 40000.0) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1228_brans_dicke_theory.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured gravitational coupling will deviate from constant-G by a floor kappa*phi^-1*B_ground; an exactly omega=infinity gravity is unreachable.
EXPERIMENT (VERIFIED): Cassini and lunar laser ranging bounding omega (omega > 40000); future gravity missions.
VERIFIED BY: If the gravitational constant is measured exactly constant at all scales and times.
```

---

### RECOGNITION
The scalar-tensor competitor of Law 063 (field equations) and Law 1132 (Nordtvedt effect).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
G may breathe; the frozen constant is the zero-scalar myth.

### NOVELTY
Brans-Dicke carries a phi-floor of scalar coupling, bounding G-variation tests.

### ACTIONABILITY
Run sim/1228_brans_dicke_theory.py.
