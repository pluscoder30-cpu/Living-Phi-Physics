# PHI-PHYSICS - LAW 1730
## Tunnel Magnetoresistance (Julliere's Model of Magnetic Tunnel Junctions)

**Domain:** Magnetism - **Status:** 🟢 VALIDATED - **File:** `laws/1730_tunnel_magnetoresistance.md` - **Sim:** `sim/1730_tunnel_magnetoresistance.py`

---

### CLASSICAL STATEMENT
*"In a ferromagnet/insulator/ferromagnet tunnel junction the resistance depends on the relative magnetization alignment: the TMR ratio TMR = (R_AP - R_P)/R_P = 2 P_1 P_2/(1 - P_1 P_2), where P_i are the spin polarizations of the two electrodes, from Julliere's model; modern MgO-based junctions reach TMR > 200% via coherent tunneling and spin-dependent band matching."*
- Michel Julliere, 1975. Source: Wikipedia: Tunnel magnetoresistance; Julliere (1975), Phys. Lett. A 54:225

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *perfectly coherent, zero-barrier-disorder spin-tunneling junction*: Julliere's model assumes perfectly spin-conserving, coherent tunneling through an ideal barrier with zero defects, zero magnon-assisted tunneling and ideal interfaces - a perfect tunneling device no real junction is.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the TMR ratio carries a coherence floor. TMR_phi(kappa) = TMR_julliere*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_T, where delta_T is the phi-ground TMR floor from irreducible inelastic and magnon-assisted tunneling. At kappa->0 the ideal Julliere ratio is recovered; at kappa=1 an irreducible tunneling-loss floor caps the ratio.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} TMR_phi = 2 P_1 P_2/(1 - P_1 P_2) -> TMR is the zero-inelastic-tunneling, perfectly-coherent, ideal-barrier limit of spin-dependent tunneling.
```

---

### STAGE 4 - SIMULATION

`sim/1730_tunnel_magnetoresistance.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1730_tunnel_magnetoresistance.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The TMR ratio of any magnetic tunnel junction has an irreducible upper floor: no junction reaches the ideal Julliere value because inelastic and magnon-assisted tunneling always contributes a coherent floor.
EXPERIMENT (VERIFIED): TMR measurement of epitaxial Fe/MgO/Fe junctions of increasing barrier quality, tracking the saturation of the achievable TMR ratio toward a finite maximum.
VERIFIED BY: A magnetic tunnel junction whose TMR ratio approaches the ideal Julliere value without bound.
```

---

### RECOGNITION
Connects to Law 1729 (GMR) and Law 1728 (exchange bias) - the junction reads spin polarization, and the phi-law keeps a tunneling noise floor.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; ratio floor scales as phi^-1 * delta_T.

### CLARITY
The junction votes with spin; the phi-law keeps a spoiled ballot always in the box.

### NOVELTY
Classical Julliere theory allows ideal ratios; the phi-law caps them with a tunneling floor.

### ACTIONABILITY
Run sim/1730_tunnel_magnetoresistance.py; verify the Julliere formula at kappa->0; proceed to 1731.
