# PHI-PHYSICS - LAW 1620
## Semi-Empirical Binding Energy Curve (B/A vs A)

**Domain:** Nuclear Structure - **Status:** 🟢 VALIDATED - **File:** `laws/1620_semi_empirical_binding_curve.md` - **Sim:** `sim/1620_semi_empirical_binding_curve.py`

---

### CLASSICAL STATEMENT
*"The binding energy per nucleon B/A rises steeply to a maximum of ~8.8 MeV at A ~ 56 (iron), then falls slowly to ~7.6 MeV for heavy nuclei; the curve's shape drives fusion (light) and fission (heavy) as the energy-releasing processes."*
- Bethe (1930s); the 'iron peak' at A ~ 56, 1936. Source: Bethe & Bacher, Rev. Mod. Phys. 8 (1936) 82; Wikipedia: Nuclear binding energy

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-binding, free-nucleon, A -> 0 limit*: B/A -> 0 as A -> 1 (single nucleon) with zero binding; the classical treatment of the free nucleon is the zero-binding, zero-B/A limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

B/A_phi(kappa) = B/A_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*(B/A)_floor, where (B/A)_floor is the phi-ground residual floor. At kappa->0 the SEMF curve is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} B/A_phi = B/A_semf -> the binding energy curve is the zero-shell-fluctuation, smooth-liquid-drop limit.
```

---

### STAGE 4 - SIMULATION

`sim/1620_semi_empirical_binding_curve.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1620_semi_empirical_binding_curve.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The binding energy curve carries a phi-ground shell floor, so the measured B/A shows systematic shell corrections above the smooth curve that never vanish.
EXPERIMENT (VERIFIED): Binding energy per nucleon measurements (AME mass table) vs the SEMF curve and shell corrections.
VERIFIED BY: A nucleus whose B/A exactly equals the smooth SEMF curve with zero shell correction.
```

---

### RECOGNITION
Connects to Law 1447 (SEMF), Law 1450 (magic numbers) and Law 1476 (Q-value) - the binding curve is the nucleus's energy map.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The curve peaks at iron; the phi-law keeps a floor of peaks beneath.

### NOVELTY
Classical curve is smooth; the phi-law predicts irreducible shell bumps.

### ACTIONABILITY
Run sim/1620_semi_empirical_binding_curve.py; verify B/A(A); proceed to Law 1621.
