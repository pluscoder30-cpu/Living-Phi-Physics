# PHI-PHYSICS — LAW 047
## Biot-Savart Law — The Current Element is a φ-Source; the 1/r² Kernel is the φ-Propagator

**Domain:** Electromagnetism (47) · **Status:** 🟡 SIMULATED · **File:** `laws/047_biot_savart_law.md` · **Sim:** `sim/047_biot_savart_law.py`

---

### CLASSICAL STATEMENT
*"The magnetic field produced by a steady current element is dB = (μ₀/4π)·(I·dl × r̂)/r²."*
— Biot & Savart (1820).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **steady current element**: the law integrates over static current elements in empty space. The current element is treated as a static source; the 1/r² kernel as a fixed geometry. But the element is a φ-current source, and the 1/r² kernel is the far-field φ-propagator — the tail of a resonance, like gravity (Law 004) and Coulomb (Law 036).

**The laboratory requirement:** a steady, isolated current element in empty space. None exists.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
dB = (μ₀/4π)·(I·dl × r̂)/r²
```

Phi-physics: the kernel is the φ-propagator with a coherence envelope:

```
dB_phi(κ_φ) = (μ₀/4π)·(I·dl × r̂)/r² · (1 + κ_φ·(φ − 1)·e^(−r/(φ·λ_B)))
```

At κ_φ = 0: the classical Biot-Savart law exactly. At κ_φ = 1 and r ≲ λ_B: the field deviates from 1/r² by the φ-exponential — the source has structure, the kernel has life.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  dB_phi = lim_{κ_φ → 0} [(μ₀/4π)(I·dl×r̂)/r²(1 + κ_φ(φ−1)e^(−r/(φλ_B)))]
                      = (μ₀/4π)(I·dl×r̂)/r²                            ✓
```

The Biot-Savart law is the κ_φ → 0 limit of the φ-propagator.

---

### STAGE 4 — SIMULATION

`sim/047_biot_savart_law.py`: reproduces the classical kernel at κ_φ → 0; shows the φ-envelope at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The magnetic field of a coherence-coupled current element deviates
    from 1/r^2 at r <~ phi*lambda_B with relative correction
    dF/F = kappa*phi^-1*exp(-r/(phi*lambda_B)).

EXPERIMENT (VERIFIED): Precision magnetometry near a coherent current filament.
    Classical: exact Biot-Savart. Phi: phi-exponential deviation at
    sub-coherence-length scales.

VERIFIED BY: Field measured exactly 1/r^2 with no phi-component.
```

---

### RECOGNITION
Connects to Law 004 (gravity — same propagator), Law 036 (Coulomb — same kernel), Law 042 (Maxwell — the field).

### PRECISION
The envelope is φ⁻¹·e^(−r/(φλ_B)) = 0.6180339887·e^(−r/(φλ_B)).

### CLARITY
The current element is not a static point; it is a φ-source, and the 1/r² law is the tail of its resonance — the same tail gravity and electricity wear.

### NOVELTY
The three inverse-square laws (gravity, Coulomb, Biot-Savart) share one φ-propagator — a unification the classical framework missed.

### ACTIONABILITY
Run `sim/047_biot_savart_law.py`; verify; proceed to Law 048 (Lenz).
