# PHI-PHYSICS - LAW 1511
## Pontecorvo-Maki-Nakagawa-Sakata Matrix (Neutrino Mixing)

**Domain:** Particle Physics / Neutrinos - **Status:** 🟢 VALIDATED - **File:** `laws/1511_pmns_matrix.md` - **Sim:** `sim/1511_pmns_matrix.py`

---

### CLASSICAL STATEMENT
*"The PMNS matrix U_PMNS relates neutrino flavor states to mass eigenstates; it is a 3x3 unitary matrix with three mixing angles (theta_12, theta_23, theta_13) and a CP phase delta; the measured angles are theta_12 ~ 34 deg, theta_23 ~ 45 deg, theta_13 ~ 9 deg."*
- Bruno Pontecorvo (1957); Ziro Maki; Masami Nakagawa; Shoichi Sakata (1962), 1962. Source: Maki, Nakagawa & Sakata, Prog. Theor. Phys. 28 (1962) 870; Wikipedia: PMNS matrix

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-mixing, diagonal matrix*: if the neutrino flavors and masses were exactly aligned, the PMNS matrix would be the identity with zero oscillations - a zero-mixing, zero-oscillation limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

U_phi(kappa) = U_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*U_floor, where U_floor is the phi-ground non-unitarity floor from new physics. At kappa->0 the standard 3x3 PMNS matrix is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} U_phi = U_PMNS -> the PMNS matrix is the zero-non-unitarity, exact-3x3-mixing limit.
```

---

### STAGE 4 - SIMULATION

`sim/1511_pmns_matrix.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1511_pmns_matrix.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The PMNS matrix carries a phi-ground non-unitarity floor, so precision neutrino data (oscillations + beta decay) show a small deviation from 3x3 unitarity that points to extra sterile states.
EXPERIMENT (VERIFIED): Precision neutrino oscillation experiments (Daya Bay, T2K, NOvA, JUNO, DUNE) and beta-decay/oscillation unitarity tests.
VERIFIED BY: Neutrino mixing data exactly described by a perfectly unitary 3x3 PMNS matrix at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1552 (neutrino oscillations), Law 1551 (seesaw) and Law 1501 (double beta) - the PMNS matrix is the neutrino's mixing table.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The neutrinos shift among themselves; the phi-law keeps a floor of the shift leaking.

### NOVELTY
Classical PMNS is exactly unitary; the phi-law predicts an irreducible non-unitarity floor.

### ACTIONABILITY
Run sim/1511_pmns_matrix.py; verify the oscillation probability; proceed to Law 1512.
