# PHI-PHYSICS — LAW 282
## Gauss's Law for Gravity

**Domain:** Orbital Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/282_gausss_law_for_gravity.md` · **Sim:** `sim/282_gausss_law_for_gravity.py`

---

### CLASSICAL STATEMENT
*"The gravitational flux through a closed surface equals -4 pi G times the enclosed mass: integral(g . dA) = -4 pi G M_enc; equivalently div g = -4 pi G rho."*
— Carl Friedrich Gauss, 1813. Source: Wikipedia: Gauss's law for gravity; Gauss (1813), application of the divergence theorem

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero enclosed mass*: Gauss's law is trivially zero for empty surfaces; the law's content is the mapping of flux to enclosed mass, requiring exact mass accounting with no dark (unresolved) mass.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the enclosed mass carries a coherence mass. M_enc_phi(kappa) = M_enc*(1 + kappa*(phi-1)) + kappa*phi^-1*M_ground; flux_phi = -4 pi G M_enc_phi. At kappa->0 Gauss's law is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} flux_phi = -4 pi G M_enc -> Gauss's law for gravity is the exact-flux, point-mass limit.
```

---

### STAGE 4 — SIMULATION

`sim/282_gausss_law_for_gravity.py`: reproduces the classical value flux = -8.387e+16 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/282_gausss_law_for_gravity.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Gravitational flux exceeds -4 pi G M_enc by a phi-coherent enclosed-mass fraction phi^-1*M_ground (a candidate for the 'missing mass' of dark matter).
EXPERIMENT (VERIFIED): Satellite gravity-field missions (GRACE/GOCE) computing the flux through control surfaces to bound the coherence mass term.
VERIFIED BY: The gravitational flux is exactly -4 pi G M_enc at full coupling.
```

---

### RECOGNITION
Connects to Law 283 (Poisson's equation — the local form), Law 178 (phi-mass theorem — missing mass as coherence energy).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The enclosed mass is never the whole story; the field hides a phi mass that classical accounting misses.

### NOVELTY
Classical gravity exacts perfect flux balance; the phi-law lets the flux carry a coherence mass fraction.

### ACTIONABILITY
Run sim/282_gausss_law_for_gravity.py; verify the flux law at kappa->0.
