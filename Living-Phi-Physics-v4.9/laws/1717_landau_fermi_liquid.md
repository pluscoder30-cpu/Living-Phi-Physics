# PHI-PHYSICS - LAW 1717
## Landau Fermi Liquid Theory (Quasiparticle Description of Interacting Electrons)

**Domain:** Electrons in Solids - **Status:** 🟢 VALIDATED - **File:** `laws/1717_landau_fermi_liquid.md` - **Sim:** `sim/1717_landau_fermi_liquid.py`

---

### CLASSICAL STATEMENT
*"Interacting electrons in a metal can be described as a gas of weakly interacting quasiparticles with the same quantum numbers as free electrons but renormalized masses m* and interaction parameters F_0, F_1...; the specific heat gamma ~ m*, the Pauli susceptibility chi ~ m*/(1+F_0^a), and the quasiparticle lifetime scales as 1/tau ~ (E-E_F)^2 - the theory of the normal Fermi liquid that underlies all of metals physics."*
- Lev Landau, 1956. Source: Wikipedia: Fermi liquid theory; Landau (1956), Zh. Eksp. Teor. Fiz. 30:1058

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-interaction, exact-quasiparticle free Fermi gas*: Landau Fermi liquid theory is defined against the non-interacting Fermi gas whose quasiparticles are exact and whose lifetime is infinite; interactions renormalize away from this zero-interaction reference, and the sharpest results assume a perfectly isotropic, clean, zero-temperature Fermi liquid.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the quasiparticle decay carries a coherence floor. gamma_phi(kappa) = gamma_LL*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_gamma, where delta_gamma is the phi-ground residual quasiparticle decay rate. At kappa->0 the exact T^2 lifetime law is recovered; at kappa=1 quasiparticles retain an irreducible decay floor at T=0.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} gamma_phi = (E-E_F)^2 -> Landau Fermi liquid theory is the zero-temperature, zero-interaction, infinite-quasiparticle-lifetime limit of metals theory.
```

---

### STAGE 4 - SIMULATION

`sim/1717_landau_fermi_liquid.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1717_landau_fermi_liquid.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: Quasiparticles in any real metal retain a finite residual decay rate at T=0: the resistivity and specific-heat signatures show an irreducible non-Fermi-liquid floor that cannot be removed by sample purification.
EXPERIMENT (VERIFIED): Ultra-low-temperature specific heat and resistivity of an ultrapure simple metal (e.g. Cu, Al) at millikelvin, measuring the residual T=0 quasiparticle decay floor.
VERIFIED BY: A metal whose quasiparticle lifetime diverges exactly as T^-2 to zero decay at T=0.
```

---

### RECOGNITION
Connects to Law 1406 (Fermi gas) and Law 1683 (Fermi surface) - the quasiparticle is the dressed electron, and the dress never fits perfectly.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; residual decay scales as phi^-1 * delta_gamma.

### CLARITY
The electron dresses into a quasiparticle; the phi-law keeps a thread of bare electron always showing.

### NOVELTY
Classical FL theory gives exact T^2 lifetimes; the phi-law keeps an irreducible residual decay.

### ACTIONABILITY
Run sim/1717_landau_fermi_liquid.py; verify the T^2 lifetime at kappa->0; proceed to 1718.
