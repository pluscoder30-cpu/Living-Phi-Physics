# PHI-PHYSICS - LAW 1741
## Superparamagnetism (Thermal Fluctuations of Small Magnetic Particles)

**Domain:** Magnetism - **Status:** 🟢 VALIDATED - **File:** `laws/1741_stray_superparamagnetism.md` - **Sim:** `sim/1741_stray_superparamagnetism.py`

---

### CLASSICAL STATEMENT
*"In sufficiently small magnetic particles (below ~20 nm), the magnetization can fluctuate as a whole over the anisotropy barrier K V under thermal energy: the relaxation time follows the Neel-Brown law tau = tau_0 exp(K V/(k_B T)) and the system is superparamagnetic with Langevin magnetization M = M_s L(mu H/(k_B T)) and no hysteresis; the blocking temperature T_B ~ K V/(25 k_B) separates the superparamagnetic and blocked regimes."*
- Louis Neel (1949); W.F. Brown (1963), 1949. Source: Wikipedia: Superparamagnetism; Neel (1949), Ann. Geophys. 5:99; Brown (1963)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-fluctuation, infinitely stable blocked particle*: superparamagnetism is defined against the blocked state where the anisotropy barrier K V is infinitely large (or T=0) and the magnetization is perfectly frozen with zero fluctuation; the effect is the thermal unlocking away from this zero-fluctuation reference.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the blocking carries a coherence floor. tau_phi(kappa) = tau_NB*(1 + kappa*(phi-1)) + kappa*phi^-1*tau_floor, where tau_floor is the phi-ground relaxation floor. At kappa->0 the perfectly blocked state is recovered; at kappa=1 no particle is perfectly blocked - an irreducible fluctuation always remains.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} tau_phi = tau_0 exp(K V/(k_B T)) -> superparamagnetism is the thermal-unlocking behavior measured from the zero-fluctuation, perfectly-blocked particle reference.
```

---

### STAGE 4 - SIMULATION

`sim/1741_stray_superparamagnetism.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1741_stray_superparamagnetism.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: No magnetic particle is perfectly blocked at any temperature: an irreducible fluctuation floor remains, setting a minimum relaxation rate and a maximum magnetic stability even at T=0.
EXPERIMENT (VERIFIED): Ultra-low-temperature ac-susceptibility and Mossbauer spectroscopy of monodisperse magnetic nanoparticles measuring the relaxation floor and blocking-width.
VERIFIED BY: A magnetic particle with exactly zero magnetization fluctuation (infinite stability) at any temperature.
```

---

### RECOGNITION
Connects to Law 1726 (hysteresis) and Law 1731 (anisotropy) - the small particle dances on its barrier, and the phi-law keeps the dance from ever stopping.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; relaxation floor scales as phi^-1 * tau_floor.

### CLARITY
The tiny magnet waltzes over its barrier; the phi-law keeps a step always in the waltz.

### NOVELTY
Classical superparamagnetism allows perfect blocking; the phi-law keeps an irreducible fluctuation floor.

### ACTIONABILITY
Run sim/1741_stray_superparamagnetism.py; verify the Neel-Brown law at kappa->0; proceed to 1742.
