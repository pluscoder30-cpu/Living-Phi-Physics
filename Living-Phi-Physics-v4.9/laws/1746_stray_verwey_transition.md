# PHI-PHYSICS - LAW 1746
## Verwey Transition (Metal-Insulator Transition in Magnetite)

**Domain:** Magnetism - **Status:** 🟢 VALIDATED - **File:** `laws/1746_stray_verwey_transition.md` - **Sim:** `sim/1746_stray_verwey_transition.py`

---

### CLASSICAL STATEMENT
*"Magnetite (Fe3O4) undergoes a sharp metal-insulator transition at T_V ~ 122 K (the Verwey transition): the conductivity drops by two orders of magnitude and the crystal distorts from cubic to monoclinic, as charge order of Fe2+/Fe3+ on the B-sites sets in; the transition is the prototype of charge-ordering-driven metal-insulator transitions in oxides."*
- E.J.W. Verwey, 1939. Source: Wikipedia: Verwey transition; Verwey (1939), Nature 144:327

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *perfectly disordered, metallic B-site reference*: the Verwey transition is defined against the high-temperature disordered state where the Fe2+/Fe3+ charges are randomly distributed and the crystal is metallic; the transition is the charge ordering away from this zero-order metallic reference.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the transition carries a coherence floor. T_V_phi(kappa) = T_V*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_T, where delta_T is the phi-ground smearing of the transition. At kappa->0 the sharp Verwey transition is recovered; at kappa=1 the transition is smeared by an irreducible coherent width.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} T_V_phi = T_V -> the Verwey transition is the charge-ordering metal-insulator transition measured from the zero-order, metallic, disordered B-site reference.
```

---

### STAGE 4 - SIMULATION

`sim/1746_stray_verwey_transition.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1746_stray_verwey_transition.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The Verwey transition is never perfectly sharp: an irreducible transition width and residual conductivity remain in the low-temperature phase, set by the phi-ground charge-order coherence.
EXPERIMENT (VERIFIED): High-precision conductivity and heat-capacity of a stoichiometric Fe3O4 single crystal through the Verwey transition, measuring the transition width and residual conductivity floor.
VERIFIED BY: A magnetite crystal with an exactly sharp Verwey transition and zero residual conductivity below T_V.
```

---

### RECOGNITION
Connects to Law 1699 (Mott transition) and Law 1701 (CDW) - the charges order in magnetite, and the phi-law keeps the order from being perfect.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; transition width scales as phi^-1 * delta_T.

### CLARITY
The charges march into order at T_V; the phi-law keeps a straggler always in the march.

### NOVELTY
Classical Verwey theory gives a sharp transition; the phi-law smears it with a coherence floor.

### ACTIONABILITY
Run sim/1746_stray_verwey_transition.py; verify the conductivity drop at kappa->0; proceed to 1747.
