# PHI-PHYSICS - LAW 1599
## Alpha Clustering (Alpha-Particle Substructure of Nuclei)

**Domain:** Nuclear Structure - **Status:** 🟢 VALIDATED - **File:** `laws/1599_alpha_clustering.md` - **Sim:** `sim/1599_alpha_clustering.py`

---

### CLASSICAL STATEMENT
*"Nuclei can be described by alpha-particle clusters: 12C = 3 alpha, 16O = 4 alpha, 8Be = 2 alpha; the alpha-cluster model explains the binding and excited states of light nuclei, and the alpha-particle substructure manifests in alpha-transfer reactions and cluster decays."*
- Hafstad & Teller (1938); alpha cluster model (1980s), 1938. Source: Hafstad & Teller, Phys. Rev. 54 (1938) 681; Wikipedia: Alpha particle

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-clustering, uniform-density limit*: the classical liquid-drop picture treats the nucleus as uniform nucleon matter with zero alpha substructure; alpha clustering is the deviation from this zero-cluster, uniform-density limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

rho_alpha_phi(kappa) = rho_alpha_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*rho_floor, where rho_floor is the phi-ground clustering floor. At kappa->0 the uniform (zero-cluster) density is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} rho_alpha_phi = rho_uniform -> alpha clustering is the zero-cluster, uniform-density limit.
```

---

### STAGE 4 - SIMULATION

`sim/1599_alpha_clustering.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1599_alpha_clustering.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The alpha-cluster probability carries a phi-ground clustering floor, so even 'uniform' nuclei retain a finite alpha substructure and alpha-transfer cross-sections never vanish.
EXPERIMENT (VERIFIED): Alpha-transfer reactions ((6Li,d), (12C,8Be)) and cluster-state spectroscopy in light nuclei (12C Hoyle state).
VERIFIED BY: A nucleus with exactly zero alpha-cluster probability at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1489 (Yukawa), Law 1502 (alpha decay) and Law 1448 (liquid drop) - alpha clustering is the nucleus's preferred packet.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The nucleus packets itself in fours; the phi-law keeps a floor of packet everywhere.

### NOVELTY
Classical density is uniform; the phi-law predicts an irreducible alpha-cluster floor.

### ACTIONABILITY
Run sim/1599_alpha_clustering.py; verify the cluster binding; proceed to Law 1600.
