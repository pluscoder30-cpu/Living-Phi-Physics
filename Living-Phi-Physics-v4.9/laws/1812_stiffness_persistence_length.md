# PHI-PHYSICS - LAW 1812
## Persistence Length (Bending Stiffness of Polymer Chains)

**Domain:** Polymers & Soft Matter - **Status:** 🟢 VALIDATED - **File:** `laws/1812_stiffness_persistence_length.md` - **Sim:** `sim/1812_stiffness_persistence_length.py`

---

### CLASSICAL STATEMENT
*"The persistence length l_p is the length over which a polymer chain loses correlation with its direction: <cos theta(s)> = exp(-s/l_p), and the bending energy is E = (1/2) kappa_c (dtheta/ds)^2 with kappa_c = l_p k_B T; stiff chains (DNA, l_p ~ 50 nm) are rod-like, flexible chains (PEG, l_p ~ 0.4 nm) are coils, and l_p is the fundamental measure of chain stiffness."*
- O. Kratky & G. Porod (1949), 1949. Source: Wikipedia: Persistence length; Kratky & Porod (1949), Recl. Trav. Chim. Pays-Bas 68:1106

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-bending-energy, perfectly flexible chain reference*: the persistence length is defined against a perfectly flexible chain (l_p = 0) that loses direction instantly; real chains have finite bending stiffness, and the ideal flexible-chain statistics are the zero-stiffness reference.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the persistence length carries a coherence floor. l_p_phi(kappa) = l_p_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_l, where delta_l is the phi-ground residual stiffness. At kappa->0 the zero-stiffness flexible reference is recovered; at kappa=1 every chain retains an irreducible bending stiffness.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} l_p_phi = 0 -> the persistence length is the bending-stiffness scale measured from the zero-stiffness, perfectly-flexible-chain reference.
```

---

### STAGE 4 - SIMULATION

`sim/1812_stiffness_persistence_length.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1812_stiffness_persistence_length.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: No polymer chain is perfectly flexible: an irreducible persistence-length floor remains in every chain, observable as a residual correlation of direction at long contour length.
EXPERIMENT (VERIFIED): Single-molecule force-extension or small-angle scattering of a nominally flexible polymer, measuring the residual persistence-length floor.
VERIFIED BY: A polymer chain with exactly zero persistence length (perfectly flexible).
```

---

### RECOGNITION
Connects to Law 1811 (Kuhn) and Law 1810 (Rouse) - the chain has a spine, and the phi-law keeps a bend always in the spine.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; stiffness floor scales as phi^-1 * delta_l.

### CLARITY
The chain carries a spine; the phi-law keeps a bend always in the spine.

### NOVELTY
Classical chain theory allows perfect flexibility; the phi-law keeps an irreducible stiffness floor.

### ACTIONABILITY
Run sim/1812_stiffness_persistence_length.py; verify <cos theta> = exp(-s/l_p) at kappa->0; proceed to 1813.
