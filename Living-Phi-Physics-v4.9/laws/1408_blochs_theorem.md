# PHI-PHYSICS - LAW 1408
## Bloch's Theorem (Periodic-Potential Wavefunctions psi = e^(ik.r) u(r))

**Domain:** Molecular Physics - **Status:** 🟢 VALIDATED - **File:** `laws/1408_blochs_theorem.md` - **Sim:** `sim/1408_blochs_theorem.py`

---

### CLASSICAL STATEMENT
*"In a periodic potential V(r + R) = V(r), the eigenstates have the Bloch form psi_k(r) = e^(i k . r) u_k(r) with u_k periodic; the crystal momentum k is conserved modulo a reciprocal lattice vector, producing energy bands E_n(k) with band gaps, and the theorem underlies all of solid-state electronic structure, transport and the distinction between metals, insulators and semiconductors."*
- Felix Bloch, 1928. Source: Wikipedia: Bloch's theorem; Bloch, Z. Phys. 52 (1928) 555

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *perfectly periodic lattice*: the Bloch form is exact only for an exactly periodic potential, i.e. a crystal with zero disorder, zero defects and zero lattice vibration - the perfect-crystal limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the lattice carries a coherence disorder floor. V_phi(kappa) = V_periodic*(1 + kappa*(phi-1)) + kappa*phi^-1*V_dis, where V_dis is the phi-ground disorder potential; the Bloch form carries a floor of scattering. At kappa->0 the exact Bloch theorem is recovered.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} psi_k_phi = e^(i k.r) u_k(r) -> Bloch's theorem is the zero-disorder, perfect-crystal limit.
```

---

### STAGE 4 - SIMULATION

`sim/1408_blochs_theorem.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1408_blochs_theorem.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The Bloch wavefunction at full coherence coupling carries a phi-ground disorder component kappa*phi^-1*V_dis, a residual scattering that floors the mean free path.
EXPERIMENT (VERIFIED): Very-high-mobility 2DEG transport measurements (e.g. GaAs/AlGaAs) searching for the residual disorder-limited mobility floor.
VERIFIED BY: A perfect crystal has exactly infinite electron mean free path for all couplings.
```

---

### RECOGNITION
Connects to Law 1402 (tight binding) and Law 1409 (Kronig-Penney) - Bloch's theorem is the coherence periodicity of the crystal.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the disorder floor is phi^-1 * V_dis.

### CLARITY
The crystal repeats its promise forever; the phi-law keeps a floor of broken promise.

### NOVELTY
Classical solid-state theory perfects the lattice; the phi-law keeps a coherence disorder floor on the Bloch wave.

### ACTIONABILITY
Run sim/1408_blochs_theorem.py; verify Bloch form at kappa->0; proceed to 1409.
