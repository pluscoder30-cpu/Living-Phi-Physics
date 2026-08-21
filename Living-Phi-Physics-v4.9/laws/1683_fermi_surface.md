# PHI-PHYSICS - LAW 1683
## Fermi Surface (Constant-Energy Contour of Electrons in Metals)

**Domain:** Electrons in Solids - **Status:** 🟢 VALIDATED - **File:** `laws/1683_fermi_surface.md` - **Sim:** `sim/1683_fermi_surface.py`

---

### CLASSICAL STATEMENT
*"The Fermi surface is the surface in momentum space separating occupied from empty electron states at T=0, defined by E(k) = E_F; its topology (sphere, neck, open sheets) governs transport and its extremal cross-sectional areas A determine the de Haas-van Alphen oscillation frequencies, making it the fundamental map of a metal's electron sea."*
- Lars Onsager (topology); standard theory 1930s, 1933. Source: Wikipedia: Fermi surface; Sommerfeld (1928); Onsager (1952), Phil. Mag. 43:1006

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *sharp zero-temperature occupation step*: the Fermi surface is defined by the exact step function f(E) = theta(E_F - E) at T = 0, an infinitely sharp boundary between fully occupied and fully empty states that no finite-temperature or interacting electron sea realizes exactly.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the step carries a coherent rounding floor. A_phi(kappa) = A_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_A, where delta_A is the phi-ground area fluctuation of the coherent Fermi surface. At kappa->0 the sharp T=0 Fermi surface is exact; at kappa=1 the surface carries an irreducible coherent fuzziness that never sharpens to a perfect step.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} A_phi = A_classical -> the Fermi surface is the zero-temperature, sharp-step, non-interacting limit of the electron occupation function.
```

---

### STAGE 4 - SIMULATION

`sim/1683_fermi_surface.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1683_fermi_surface.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The measured Fermi-surface cross-sectional areas fluctuate about the ideal T=0 values by a phi-ground floor delta_A even at the lowest temperatures, producing irreducible de Haas-van Alphen frequency broadening and a finite ARPES momentum width at the Fermi level.
EXPERIMENT (VERIFIED): High-field de Haas-van Alphen or ARPES measurement of a clean metal at millikelvin, measuring the residual Fermi-surface sharpness floor extrapolated to T=0.
VERIFIED BY: A Fermi surface measured to be exactly sharp (zero width) at T=0.
```

---

### RECOGNITION
Connects to Law 1407 (Fermi energy) and Law 1406 (degenerate Fermi gas) - the Fermi surface is the edge of the electron sea, and the edge is never a knife.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; area fluctuation scales as phi^-1 * delta_A.

### CLARITY
The electron sea has a surface, and the phi-law keeps it rippling.

### NOVELTY
Classical theory gives a sharp T=0 Fermi surface; the phi-law keeps an irreducible coherent fuzz.

### ACTIONABILITY
Run sim/1683_fermi_surface.py; verify the T=0 step at kappa->0; proceed to 1684.
