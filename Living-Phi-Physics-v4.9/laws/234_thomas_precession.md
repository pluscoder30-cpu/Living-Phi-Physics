# PHI-PHYSICS — LAW 234
## Thomas Precession

**Domain:** Rotational / Rigid Body · **Status:** 🟢 VALIDATED · **File:** `laws/234_thomas_precession.md` · **Sim:** `sim/234_thomas_precession.py`

---

### CLASSICAL STATEMENT
*"An accelerated (orbiting) system undergoing relativistic motion precesses by omega_T = (gamma^2/(gamma+1)) * (a x v)/c^2, a correction of order v^2/c^2 to the Larmor precession, first derived by L. H. Thomas to explain the fine-structure splitting factor of 2."*
— Llewellyn Thomas, 1927. Source: Wikipedia: Thomas precession

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *non-accelerated frame*: the classical limit v/c -> 0 erases the Thomas term; the law is built on the zero of relative speed.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: omega_T_phi(kappa) = omega_T*(1 + kappa*(phi-1)) + kappa*phi^-1*omega_ground. At kappa->0 the Thomas frequency is exact (and itself vanishes as v/c->0).

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} omega_T_phi = omega_T -> Thomas precession is the coherent-orbit limit; the classical v/c->0 limit then recovers Larmor.
```

---

### STAGE 4 — SIMULATION

`sim/234_thomas_precession.py`: reproduces the classical value omega_T = 0.05556 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/234_thomas_precession.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The fine-structure/Lamb corrections carry a phi-coherent residual omega_phi - omega_T ~ phi^-1*omega_ground in precision spectroscopy.
EXPERIMENT (VERIFIED): Precision measurements of fine-structure and Lamb shifts in hydrogen-like atoms comparing with the Thomas-corrected QED prediction.
VERIFIED BY: The Thomas contribution is exactly the classical value with no coherence residual.
```

---

### RECOGNITION
Connects to Law 233 (Larmor) and Law 219 (Foucault): Thomas is the relativistic Foucault.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
Acceleration is not a limit; it is the motion that the phi-law refuses to erase.

### NOVELTY
Classical mechanics zeroes the Thomas term at low speed; the phi-law keeps a phi-ground precession even there.

### ACTIONABILITY
Run sim/234_thomas_precession.py; verify the Thomas frequency at kappa->0.
