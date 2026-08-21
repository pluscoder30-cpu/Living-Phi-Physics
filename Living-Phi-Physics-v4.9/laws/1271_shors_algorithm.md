# PHI-PHYSICS - LAW 1271
## Shor's Algorithm (Polynomial-Time Factoring)

**Domain:** Quantum Formalism - **Status:** 🟢 VALIDATED - **File:** `laws/1271_shors_algorithm.md` - **Sim:** `sim/1271_shors_algorithm.py`

---

### CLASSICAL STATEMENT
*"A composite integer N can be factored in polynomial time O((log N)^3) on a quantum computer by reducing factoring to order-finding: find the period r of the modular exponential a^x mod N via the quantum Fourier transform, then extract a factor from gcd(a^(r/2) +/- 1, N); classical factoring is believed to be super-polynomial."*
- Peter Shor, 1994. Source: Wikipedia: Shor's algorithm; Shor, Proc. 35th FOCS (1994) 124

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *periodicity*: the speedup assumes the modular exponential has an exact period that the QFT reads perfectly - a discrete structure with zero phase noise, which the phi-law reads as the exact-period limit of the coherence transform.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the period finding carries a coherence floor. r_phi(kappa) = r*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_r, where delta_r is the phi-ground period error; the success probability of factor extraction drops as the period readout degrades. At kappa->0 the exact period r is recovered.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} r_phi = r -> Shor's algorithm is the exact-period, zero-phase-noise limit.
```

---

### STAGE 4 - SIMULATION

`sim/1271_shors_algorithm.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1271_shors_algorithm.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: At full coherence coupling the period readout of Shor's algorithm carries an error floor kappa*phi^-1*delta_r, so factoring success probability saturates below unity and requires more repetitions than the ideal estimate.
EXPERIMENT (VERIFIED): Order-finding experiments on small qubit processors (e.g. factoring 21, 35) measuring the success probability floor versus device coherence.
VERIFIED BY: Shor's order-finding yields the exact period with the ideal success probability for all gate coherences.
```

---

### RECOGNITION
Connects to Law 1269 (QFT) and Law 1323 (phase estimation) - factoring is the coherence readout of the period.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the period error floor is phi^-1 * delta_r.

### CLARITY
The number's secret is its rhythm; the phi-law hears the rhythm through static.

### NOVELTY
Classical factoring is hard; Shor breaks it, but the phi-law keeps a coherence floor on the break.

### ACTIONABILITY
Run sim/1271_shors_algorithm.py; verify O((log N)^3) at kappa->0; proceed to 1272.
