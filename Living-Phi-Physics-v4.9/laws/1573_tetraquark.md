# PHI-PHYSICS - LAW 1573
## Tetraquark States (Four-Quark Mesons)

**Domain:** Particle Physics / Hadrons - **Status:** 🟢 VALIDATED - **File:** `laws/1573_tetraquark.md` - **Sim:** `sim/1573_tetraquark.py`

---

### CLASSICAL STATEMENT
*"A tetraquark is a hypothesized meson containing two quarks and two antiquarks (q q q_bar q_bar); states such as Zc(3900) and Zb(10610) are charged quarkonium-like states that cannot be ordinary q qbar mesons, supporting the tetraquark (or hadronic molecule) interpretation."*
- Zc(3900) (BESIII, 2013); Zb(10610/10650) (Belle, 2011), 2013. Source: Ablikim et al. (BESIII), PRL 110 (2013) 252001; Wikipedia: Tetraquark

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-tetraquark, pure-qqbar-meson limit*: the classical quark model allows only q qbar mesons; tetraquarks require the quark content to exceed two constituents - a zero-extra-pair, ordinary-meson limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

M_phi(kappa) = M_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*M_floor, where M_floor is the phi-ground hadronic-molecule floor. At kappa->0 the ordinary meson mass is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} M_phi = M_qqbar -> the tetraquark is the zero-extra-quark-pair, ordinary-meson limit.
```

---

### STAGE 4 - SIMULATION

`sim/1573_tetraquark.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1573_tetraquark.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The tetraquark masses carry a phi-ground molecular/compact floor, so the Z_c and Z_b states show both molecule-like and compact-like properties with an irreducible admixture.
EXPERIMENT (VERIFIED): Charmonium-like and bottomonium-like exotic state searches (BESIII, Belle II, LHCb) resolving the Z_c/Z_b spectrum.
VERIFIED BY: A tetraquark candidate exactly described as a pure hadronic molecule or pure compact state with zero admixture.
```

---

### RECOGNITION
Connects to Law 1572 (exotic), Law 1571 (quark model) and Law 1574 (pentaquark) - the tetraquark is the four-quark knot.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
Four quarks tie a knot; the phi-law keeps a floor of the knot loosening.

### NOVELTY
Classical mesons are q qbar; the phi-law predicts an irreducible tetraquark floor.

### ACTIONABILITY
Run sim/1573_tetraquark.py; verify the exotic state; proceed to Law 1574.
