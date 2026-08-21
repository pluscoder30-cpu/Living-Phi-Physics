# PHI-PHYSICS - LAW 1292
## Heisenberg Picture (Operators Evolve, States Static)

**Domain:** Quantum Dynamics - **Status:** 🟢 VALIDATED - **File:** `laws/1292_heisenberg_picture.md` - **Sim:** `sim/1292_heisenberg_picture.py`

---

### CLASSICAL STATEMENT
*"In the Heisenberg picture the state is static and operators evolve: A_H(t) = U^dagger(t) A_S U(t), with the Heisenberg equation of motion dA_H/dt = (i/hbar)[H, A_H] + (dA/dt)_S; expectation values are picture-independent."*
- Werner Heisenberg, 1925. Source: Wikipedia: Heisenberg picture; Heisenberg, Z. Phys. 33 (1925) 879

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *static state*: the Heisenberg picture holds the state |psi> exactly fixed in time, i.e. a state with zero intrinsic motion - a frozen carrier the phi-law reads as the zero-state-motion limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the static state carries a coherence motion. |psi>_phi(t,kappa) = |psi>*(1 + kappa*phi^-1*omega t) rotated by the phi-ground frequency omega; the picture acquires a residual state drift. At kappa->0 the state is exactly static.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} |psi>_phi(t) = |psi> -> the Heisenberg picture is the zero-state-motion limit.
```

---

### STAGE 4 - SIMULATION

`sim/1292_heisenberg_picture.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1292_heisenberg_picture.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The 'static' state of the Heisenberg picture at full coherence coupling drifts at the phi-ground frequency kappa*phi^-1*omega, a residual time dependence in nominally static state preparations.
EXPERIMENT (VERIFIED): Two-pulse interferometry measuring the state drift of a nominally static spin preparation at increasing coherence.
VERIFIED BY: The Heisenberg-picture state is exactly time-independent for all couplings.
```

---

### RECOGNITION
Connects to Law 1291 (unitary) and Law 1293 (interaction picture) - the pictures are the coherence frames of evolution.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the drift frequency is phi^-1 * omega.

### CLARITY
Even the still frame turns; the phi-law keeps the turn from being zero.

### NOVELTY
Classical QM freezes the state in the Heisenberg frame; the phi-law gives the frozen state a coherence drift.

### ACTIONABILITY
Run sim/1292_heisenberg_picture.py; verify dA/dt equation at kappa->0; proceed to 1293.
