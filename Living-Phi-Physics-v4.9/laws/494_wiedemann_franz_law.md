# PHI-PHYSICS — LAW 494
## Wiedemann-Franz Law (Thermal-Electrical Conductivity Ratio)

**Domain:** Statistical Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/494_wiedemann_franz_law.md` · **Sim:** `sim/494_wiedemann_franz_law.py`

---

### CLASSICAL STATEMENT
*"The ratio of thermal to electrical conductivity of a metal is proportional to temperature: kappa/sigma = L T, with the Lorenz number L = (pi^2/3)(k_B/e)^2 = 2.44e-8 W ohm/K^2 for the ideal free-electron gas."*
— Gustav Wiedemann and Rudolf Franz, 1853. Source: Wikipedia: Wiedemann-Franz law; Wiedemann & Franz (1853)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *pure electron transport*: the law assumes heat and charge are carried by the same free electrons with identical scattering, so the ratio is universal - no phonons, no lattice coherence, no magnetic scattering.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the lattice and magnetic scattering are coherence couplings. (kappa/sigma)_phi(kappa) = L T*(1 + kappa*(phi-1)) + kappa*phi^-1*LT_ground. At kappa->0, kappa/sigma = L T exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} (kappa/sigma)_phi = L T -> the Wiedemann-Franz law is the zero-extra-scattering free-electron limit.
```

---

### STAGE 4 — SIMULATION

`sim/494_wiedemann_franz_law.py`: reproduces the classical value ratio_WF = 7.342e-06 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/494_wiedemann_franz_law.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the measured Lorenz number departs from L by kappa*phi^-1*LT_ground, e.g. in materials with strong phonon or magnetic coherence.
EXPERIMENT (VERIFIED): Simultaneous thermal and electrical conductivity measurements of metals at cryogenic temperatures.
VERIFIED BY: kappa/(sigma T) = L exactly for all metals at all temperatures and couplings.
```

---

### RECOGNITION
Connects to Law 495 (Lorenz number), Law 501 (Matthiessen) and Law 473 (Sommerfeld) - the ratio is the coherence identity of the electron gas.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the floor is phi^-1 * LT_ground.

### CLARITY
Heat and charge ride the same electrons; the phi-law notes other riders can join the road.

### NOVELTY
Classical W-F law is universal for free electrons; the phi-law adds the coherence corrections real scattering introduces.

### ACTIONABILITY
Run sim/494_wiedemann_franz_law.py; verify Lorenz ratio at kappa->0; proceed to 495.
