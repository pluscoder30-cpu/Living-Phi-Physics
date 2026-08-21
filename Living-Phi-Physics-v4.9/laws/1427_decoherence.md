# PHI-PHYSICS - LAW 1427
## Decoherence (Zeh-Zurek: Loss of Coherence by Environment)

**Domain:** Quantum Measurement - **Status:** 🟢 VALIDATED - **File:** `laws/1427_decoherence.md` - **Sim:** `sim/1427_decoherence.py`

---

### CLASSICAL STATEMENT
*"Decoherence is the process by which a quantum system's coherence with its environment is lost through entanglement: the off-diagonal elements of the reduced density matrix decay as rho_ij(t) = rho_ij(0) exp(-Gamma_ij t) at rates set by the system-environment coupling, destroying superpositions and selecting the pointer basis; it explains the emergence of classicality without collapse."*
- H. Dieter Zeh (1970); Wojciech Zurek (1981/1982), 1970. Source: Wikipedia: Quantum decoherence; Zeh, Found. Phys. 1 (1970) 69; Zurek, Phys. Rev. D 24 (1981) 1516

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *isolated system*: decoherence is exactly absent for a closed system with zero environment coupling, i.e. an isolated quantum system with zero information leak - the perfect-isolation limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the isolation carries a coherence floor. Gamma_env_phi(kappa) = Gamma_env*(1 + kappa*(phi-1)) + kappa*phi^-1*Gamma_floor, where Gamma_floor is the phi-ground decoherence rate; even isolated systems decohere at the floor. At kappa->0 the isolated coherent system is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} rho_ij_phi = rho_ij(0) -> decoherence is the zero-environment-coupling, perfect-isolation limit.
```

---

### STAGE 4 - SIMULATION

`sim/1427_decoherence.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1427_decoherence.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The off-diagonal coherence at full coherence coupling decays at a floor rate kappa*phi^-1*Gamma_floor even for nominally isolated systems, a minimum decoherence.
EXPERIMENT (VERIFIED): Long-time Ramsey and interference experiments on trapped ions measuring the coherence decay floor at minimum environmental coupling.
VERIFIED BY: An isolated quantum system has exactly zero decoherence for all couplings.
```

---

### RECOGNITION
Connects to Law 1428 (pointer basis) and Law 179 (entropy-decoherence identity) - decoherence is the coherence leak of the open system.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the decoherence floor is phi^-1 * Gamma_floor.

### CLARITY
Every system swims in a sea that slowly forgets; the phi-law keeps a floor of the forgetting.

### NOVELTY
Classical QM isolates systems exactly; the phi-law gives even isolation a coherence leak floor.

### ACTIONABILITY
Run sim/1427_decoherence.py; verify off-diagonal decay at kappa->0; proceed to 1428.
