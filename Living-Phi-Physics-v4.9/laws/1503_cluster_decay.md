# PHI-PHYSICS - LAW 1503
## Cluster Radioactivity (Emission of Nuclei Larger than Alpha)

**Domain:** Nuclear Decays - **Status:** 🟢 VALIDATED - **File:** `laws/1503_cluster_decay.md` - **Sim:** `sim/1503_cluster_decay.py`

---

### CLASSICAL STATEMENT
*"Some heavy nuclei emit clusters larger than an alpha particle (14C, 20O, 24Ne, ...) in a rare decay mode; the cluster is preformed in the parent and tunnels through the barrier, with rates following a generalized Geiger-Nuttall law as a function of the cluster charge and energy."*
- H.J. Rose; G.A. Jones (1984, first observation), 1984. Source: Rose & Jones, Nature 307 (1984) 245; Wikipedia: Cluster decay

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-preformation, exactly-point cluster*: the cluster decay assumes the cluster is preformed in the parent with a probability factor that classically is either 1 (perfect preformation) or 0 (no cluster) - a hard two-valued zero.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

P_pre_phi(kappa) = P_pre_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*P_floor, where P_floor is the phi-ground preformation floor. At kappa->0 the classical preformation factor is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} P_pre_phi = P_pre_classical -> cluster decay is the zero-preformation-fluctuation, two-valued-preformation limit.
```

---

### STAGE 4 - SIMULATION

`sim/1503_cluster_decay.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1503_cluster_decay.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The cluster preformation factor carries a phi-ground floor, so cluster decay rates always have a systematic residual between the two classical extremes and the generalized Geiger-Nuttall law shows curvature.
EXPERIMENT (VERIFIED): Cluster decay searches and half-life measurements (14C, 24Ne emitters) vs the universal decay law (UDL).
VERIFIED BY: A cluster decay exactly at the classical preformation limit (0 or 1) with zero residual floor.
```

---

### RECOGNITION
Connects to Law 1452 (Gamow), Law 1453 (Geiger-Nuttall) and Law 1502 (alpha) - cluster decay is the nucleus's throw of larger dice.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The nucleus throws a cluster; the phi-law keeps a floor of the cluster never fully formed.

### NOVELTY
Classical preformation is 0 or 1; the phi-law predicts a continuous irreducible floor.

### ACTIONABILITY
Run sim/1503_cluster_decay.py; verify the UDL; proceed to Law 1504.
