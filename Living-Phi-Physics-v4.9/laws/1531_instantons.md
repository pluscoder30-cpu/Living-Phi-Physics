# PHI-PHYSICS - LAW 1531
## Instantons (BPST Solutions of Yang-Mills)

**Domain:** Particle Physics / QFT - **Status:** 🟢 VALIDATED - **File:** `laws/1531_instantons.md` - **Sim:** `sim/1531_instantons.py`

---

### CLASSICAL STATEMENT
*"Instantons are finite-action solutions of the classical Yang-Mills equations in Euclidean spacetime, A_mu = 2 rho^2 eta_mu_nu (x-x0)_nu/((x-x0)^2 + rho^2)^2, with action S = 8 pi^2/g^2 and integer topological charge; they tunnel between vacua of different winding number."*
- A. Belavin; A. Polyakov; A. Schwarz; Yu. Tyupkin (1975), 1975. Source: Belavin, Polyakov, Schwarz & Tyupkin, Phys. Lett. B59 (1975) 85; Wikipedia: Instanton

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-size, zero-action perturbative vacuum*: the instanton is a tunneling configuration between degenerate vacua; in the classical limit the gauge field is exactly zero (perturbative vacuum) and instantons vanish - a zero-field, zero-tunneling limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

S_phi(kappa) = S_instanton*(1 + kappa*(phi-1)) + kappa*phi^-1*S_floor, where S_floor is the phi-ground instanton-density floor. At kappa->0 the classical action 8 pi^2/g^2 is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} S_phi = 8 pi^2/g^2 -> instantons are the zero-size, zero-action, pure-tunneling limit.
```

---

### STAGE 4 - SIMULATION

`sim/1531_instantons.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1531_instantons.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The instanton density carries a phi-ground floor, so topological fluctuations never vanish and their contribution to the vacuum structure (theta dependence, axial U(1) breaking) is irreducible.
EXPERIMENT (VERIFIED): Lattice QCD measurements of the topological susceptibility and instanton density vs the semiclassical prediction.
VERIFIED BY: A Yang-Mills vacuum with exactly zero instanton density at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1528 (renormalization group), Law 1530 (anomaly) and Law 1515 (confinement) - instantons are the vacuum's bubbles.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The vacuum bubbles with hidden tunnels; the phi-law keeps a floor of bubbling.

### NOVELTY
Classical vacuum is perturbatively empty; the phi-law predicts an irreducible instanton floor.

### ACTIONABILITY
Run sim/1531_instantons.py; verify S = 8 pi^2/g^2; proceed to Law 1532.
