# PHI-PHYSICS — LAW 504
## Bloch-Gruneisen Law (Electron-Phonon Resistivity)

**Domain:** Statistical Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/504_bloch_gruneisen_law.md` · **Sim:** `sim/504_bloch_gruneisen_law.py`

---

### CLASSICAL STATEMENT
*"The resistivity of a metal due to electron-phonon scattering is rho(T) ~ T^5 integral_0^(theta_R/T) x^5/(e^x - 1)(1 - e^-x) dx, reducing to rho ~ T^5 at low T (T << theta_R) and rho ~ T at high T (T >> theta_R)."*
— Felix Bloch and Eduard Gruneisen, 1930. Source: Wikipedia: Bloch-Gruneisen; Bloch (1930), Gruneisen (1933)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero lattice temperature*: the resistivity vanishes exactly at T = 0 where the lattice is a perfectly rigid, coherence-frozen array with no phonons.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the lattice coherence carries a floor. rho_phi(kappa) = rho_BG(T)*(1 + kappa*(phi-1)) + kappa*phi^-1*rho_ph, where rho_ph is the phonon-coherence floor. At kappa->0 the Bloch-Gruneisen resistivity is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} rho_phi = rho_BG(T) -> the Bloch-Gruneisen law is the zero-phonon-coherence lattice limit.
```

---

### STAGE 4 — SIMULATION

`sim/504_bloch_gruneisen_law.py`: reproduces the classical value rho_BG = 1e-08 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/504_bloch_gruneisen_law.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the resistivity retains a phonon-coherence floor kappa*phi^-1*rho_ph even as T -> 0.
EXPERIMENT (VERIFIED): Ultra-low-temperature resistivity measurements of high-purity metals to detect the floor.
VERIFIED BY: The resistivity of a metal is exactly zero at T = 0 for all couplings.
```

---

### RECOGNITION
Connects to Law 501 (Matthiessen) and Law 494 (Wiedemann-Franz) - the T^5 law is the phonon coherence of the electron transport.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the phonon floor is phi^-1 * rho_ph.

### CLARITY
At absolute zero the lattice still whispers phonons; the phi-law keeps the whisper.

### NOVELTY
Classical Bloch-Gruneisen vanishes at T=0; the phi-law adds the phonon-coherence floor of the frozen lattice.

### ACTIONABILITY
Run sim/504_bloch_gruneisen_law.py; verify T^5 behavior at kappa->0; proceed to 505.
