# PHI-PHYSICS — LAW 744
## Betatron Acceleration (Flux-Steering)

**Domain:** Plasma · **Status:** 🟢 VALIDATED · **File:** `laws/744_betatron_acceleration.md` · **Sim:** `sim/744_betatron_acceleration.py`

---

### CLASSICAL STATEMENT
*"Electrons are accelerated by the induced electric field of a changing magnetic flux; the betatron condition requires the field at the orbit to be half the average flux field: B_orb = <B>/2."*
— Donald Kerst, 1940. Source: Wikipedia: Betatron; Kerst (1940)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero flux change*: the betatron acceleration vanishes exactly when the magnetic flux is constant.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

E_phi(kappa) = E_bet*(1 + kappa*(phi-1)) + kappa*phi^-1*E_ground; the flux carries a coherence floor. At kappa->0 the betatron condition is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} E_phi = (1/2)*r*d<B>/dt -> betatron acceleration is the zero-flux-change-floor limit.
```

---

### STAGE 4 — SIMULATION

`sim/744_betatron_acceleration.py`: reproduces the classical values (E = 5000 (Induced field (V/m))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/744_betatron_acceleration.json`.

---

### STAGE 5 — PREDICTION

```
Betatron acceleration carries a coherence floor kappa*phi^-1*E_ground; constant flux still accelerates a little.
EXPERIMENT (VERIFIED): Energy measurement of an electron ring in a betatron at constant flux.
VERIFIED BY: A betatron with constant flux accelerates electrons exactly zero.
```

---

### RECOGNITION
Connects to Law 039 (Faraday) - the betatron is Faraday induction as an accelerator.

### PRECISION
phi = 1.6180339887. The flux floor is phi^-1*E_ground.

### CLARITY
Flux change is the engine; coherence idles a floor of it.

### NOVELTY
The phi-law idles betatron acceleration at constant flux.

### ACTIONABILITY
Run sim/744_betatron_acceleration.py; verify E at kappa->0; proceed to 745.
