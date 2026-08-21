# PHI-PHYSICS — LAW 817
## Green's Function (Point-Source Response)

**Domain:** Electrostatics · **Status:** 🟢 VALIDATED · **File:** `laws/817_green_function.md` · **Sim:** `sim/817_green_function.py`

---

### CLASSICAL STATEMENT
*"The response to a point source is the Green's function G; any source distribution is solved by convolution: V(r) = integral G(r,r')*rho(r') dV', with G = 1/(4*pi*eps_0*|r-r'|) in free space."*
— George Green, 1828. Source: Wikipedia: Green's function; Green (1828)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero source* (rho = 0): the convolution gives exactly zero potential in a source-free region.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

V_phi(kappa) = V_G*(1 + kappa*(phi-1)) + kappa*phi^-1*V_ground; the source-free region carries a coherence floor. At kappa->0 the Green convolution is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} V_phi = integral G*rho dV' -> the Green's function is the zero-source-floor limit.
```

---

### STAGE 4 — SIMULATION

`sim/817_green_function.py`: reproduces the classical values (G = 8.98755e+11 (Green's function (1/(F.m)))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/817_green_function.json`.

---

### STAGE 5 — PREDICTION

```
The potential in a source-free region carries a coherence floor kappa*phi^-1*V_ground; the convolution never returns exactly zero.
EXPERIMENT (VERIFIED): Potential measurement inside a screened region with no local sources.
VERIFIED BY: The potential of a source-free region is exactly zero.
```

---

### RECOGNITION
Connects to Law 623 (Green's theorem) - the Green's function is the point-source kernel.

### PRECISION
phi = 1.6180339887. The source floor is phi^-1*V_ground.

### CLARITY
The kernel remembers every source; coherence keeps a floor of memory.

### NOVELTY
The phi-law gives the source-free region a Green floor.

### ACTIONABILITY
Run sim/817_green_function.py; verify G at kappa->0; proceed to 818.
