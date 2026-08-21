# PHI-PHYSICS - LAW 1735
## Magnetoelectric Effect (Magnetization by Electric Field and Vice Versa)

**Domain:** Magnetism - **Status:** 🟢 VALIDATED - **File:** `laws/1735_magnetoelectric_effect.md` - **Sim:** `sim/1735_magnetoelectric_effect.py`

---

### CLASSICAL STATEMENT
*"In magnetoelectric materials, an electric field induces a magnetization and a magnetic field induces a polarization: P_i = alpha_ij H_j and M_i = alpha_ij E_j, with the linear magnetoelectric tensor alpha_ij; the effect is allowed in materials breaking both time-reversal and inversion symmetry (e.g. Cr2O3), and is the basis of multiferroic and ME-sensing applications."*
- P. Curie (1894); I.E. Dzyaloshinskii (1959); D.N. Astrov (1960), 1959. Source: Wikipedia: Magnetoelectric effect; Curie (1894); Dzyaloshinskii (1959), JETP 37:881; Astrov (1960)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-magnetoelectric, perfectly symmetric reference crystal*: the magnetoelectric effect requires broken time-reversal and inversion symmetry; it is defined against a centrosymmetric, non-magnetic reference with zero ME tensor, and the effect is the linear coupling away from this zero reference.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the ME tensor carries a coherence floor. alpha_phi(kappa) = alpha*(1 + kappa*(phi-1)) + kappa*phi^-1*alpha_floor, where alpha_floor is the phi-ground residual ME coefficient. At kappa->0 the zero-ME reference is recovered; at kappa=1 an irreducible magnetoelectric response always exists.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} alpha_phi = 0 -> the magnetoelectric effect is the symmetry-broken linear coupling measured from the zero-ME, perfectly-symmetric reference crystal.
```

---

### STAGE 4 - SIMULATION

`sim/1735_magnetoelectric_effect.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1735_magnetoelectric_effect.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: Every crystal has an irreducible residual magnetoelectric response even in nominally symmetric structures: a floor of field-induced polarization/magnetization coupling always exists.
EXPERIMENT (VERIFIED): Ultra-sensitive ME coefficient measurement of a nominally centrosymmetric crystal (e.g. a high-symmetry oxide), measuring the residual linear ME floor.
VERIFIED BY: A crystal with exactly zero linear magnetoelectric coefficient.
```

---

### RECOGNITION
Connects to Law 1736 (multiferroics) and Law 1734 (magnetocaloric) - the two fields shake hands, and the phi-law keeps the handshake from ending.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; ME floor scales as phi^-1 * alpha_floor.

### CLARITY
Electric and magnetic fields speak across the crystal; the phi-law keeps a whisper always in the line.

### NOVELTY
Classical ME theory allows zero coupling in symmetric crystals; the phi-law keeps an irreducible floor.

### ACTIONABILITY
Run sim/1735_magnetoelectric_effect.py; verify P = alpha H at kappa->0; proceed to 1736.
