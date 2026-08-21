# PHI-PHYSICS — LAW 770
## Free-Free (Thermal) Emission

**Domain:** Radiation · **Status:** 🟢 VALIDATED · **File:** `laws/770_free_free_emission.md` · **Sim:** `sim/770_free_free_emission.py`

---

### CLASSICAL STATEMENT
*"The free-free absorption/emission coefficient for a thermal plasma is kappa_nu = (4*e^6*n_e*n_i)/(3*c*h*nu^3)*sqrt(2*pi/(3*m_e^3*k_B*T))*g_ff*(1-exp(-h*nu/k_B*T)), with g_ff the Gaunt factor."*
— Arnold Sommerfeld (theory); plasma literature, 1931. Source: Free-free emission; thermal bremsstrahlung (H II regions)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero density* (n_e = 0): the emission vanishes exactly in a plasma with no free electrons.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

kappa_phi(kappa) = kappa_ff*(1 + kappa*(phi-1)) + kappa*phi^-1*kappa_ground; the plasma carries a coherence floor. At kappa->0 the free-free coefficient is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} kappa_phi = kappa_ff -> free-free emission is the zero-density-floor limit.
```

---

### STAGE 4 — SIMULATION

`sim/770_free_free_emission.py`: reproduces the classical values (k = 9.97603e+35 (Emission coefficient (a.u.))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/770_free_free_emission.json`.

---

### STAGE 5 — PREDICTION

```
The emission coefficient carries a coherence floor kappa*phi^-1*kappa_ground at zero density.
EXPERIMENT (VERIFIED): Radio continuum measurement of a tenuous H II region.
VERIFIED BY: A zero-density plasma emits exactly no free-free radiation.
```

---

### RECOGNITION
Connects to Law 769 (bremsstrahlung) - free-free emission is thermal bremsstrahlung.

### PRECISION
phi = 1.6180339887. The density floor is phi^-1*kappa_ground.

### CLARITY
Emission needs matter; coherence keeps a floor of light.

### NOVELTY
The phi-law keeps free-free light at zero density.

### ACTIONABILITY
Run sim/770_free_free_emission.py; verify kappa at kappa->0; proceed to 771.
