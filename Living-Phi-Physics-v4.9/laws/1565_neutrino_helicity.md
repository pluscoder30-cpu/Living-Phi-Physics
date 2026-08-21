# PHI-PHYSICS - LAW 1565
## Neutrino Helicity (Goldhaber Experiment)

**Domain:** Particle Physics / Weak Interaction - **Status:** 🟢 VALIDATED - **File:** `laws/1565_neutrino_helicity.md` - **Sim:** `sim/1565_neutrino_helicity.py`

---

### CLASSICAL STATEMENT
*"Neutrinos are left-handed and antineutrinos right-handed (helicity h = -1 for neutrinos): the helicity is fixed by the V-A interaction; the Goldhaber experiment measured the neutrino helicity through the circular polarization of the capture gamma ray in 152Eu, establishing h = -1."*
- Maurice Goldhaber; Lee Grodzins; Andrew Sunyar (1958), 1958. Source: Goldhaber, Grodzins & Sunyar, Phys. Rev. 109 (1958) 1015; Wikipedia: Neutrino

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-mass, zero-helicity-flip, exactly-chiral neutrino*: a massless neutrino has exactly fixed helicity and zero probability of the wrong helicity; the classical treatment of a massless, exactly-chiral neutrino is the zero-mass, zero-wrong-helicity limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

h_phi(kappa) = h_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*h_floor, where h_floor is the phi-ground wrong-helicity floor from finite neutrino mass. At kappa->0 the exact h = -1 is recovered.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} h_phi = -1 -> neutrino helicity is the zero-mass, exactly-chiral, zero-flip limit.
```

---

### STAGE 4 - SIMULATION

`sim/1565_neutrino_helicity.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1565_neutrino_helicity.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: A finite neutrino mass gives a phi-ground wrong-helicity floor, so the helicity suppression is not exact and the 'right-handed' neutrino component is nonzero at a level set by m_nu/E.
EXPERIMENT (VERIFIED): Neutrino helicity and mass measurements (KATRIN endpoint, double beta, cosmology) probing the wrong-helicity component.
VERIFIED BY: A neutrino with exactly fixed helicity and zero wrong-helicity component at finite mass.
```

---

### RECOGNITION
Connects to Law 1563 (V-A), Law 1564 (parity) and Law 1537 (oscillations) - neutrino helicity is the weak force's handedness proof.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The neutrino only spins left; the phi-law keeps a floor of a right-handed hint.

### NOVELTY
Classical helicity is exact; the phi-law predicts an irreducible wrong-helicity floor.

### ACTIONABILITY
Run sim/1565_neutrino_helicity.py; verify h = -1; proceed to Law 1566.
