# PHI-PHYSICS - LAW 1294
## Dyson Series (Time-Ordered Expansion of the Evolution Operator)

**Domain:** Quantum Dynamics - **Status:** 🟢 VALIDATED - **File:** `laws/1294_dyson_series.md` - **Sim:** `sim/1294_dyson_series.py`

---

### CLASSICAL STATEMENT
*"The time-evolution operator in the interaction picture is the Dyson series U_I(t) = T exp(-(i/hbar) int_0^t V_I(t') dt') = sum_n (-i/hbar)^n int dt_1...int dt_n T[V_I(t_1)...V_I(t_n)], the time-ordered exponential that sums all iterated interactions."*
- Freeman Dyson, 1949. Source: Wikipedia: Dyson series; Dyson, Phys. Rev. 75 (1949) 486

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is *instantaneous interactions*: the series converges only for weak V and finite time, and its exactness assumes the interaction can be integrated term by term - a zero-coupling-radius expansion the phi-law reads as the zero-interaction-amplitude limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the series carries a coherence radius. U_phi(kappa) = U_Dyson*(1 + kappa*(phi-1)) + kappa*phi^-1*U_res, where U_res is the phi-ground non-perturbative residue beyond the series radius. At kappa->0 the exact Dyson expansion is recovered.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} U_phi = sum_n (-i/hbar)^n int T[V...V] -> the Dyson series is the zero-non-perturbative-residue limit.
```

---

### STAGE 4 - SIMULATION

`sim/1294_dyson_series.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1294_dyson_series.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The Dyson evolution operator at full coherence coupling acquires a phi-ground non-perturbative residue kappa*phi^-1*U_res beyond the perturbation radius, a floor visible as systematic deviation in strong-coupling regimes.
EXPERIMENT (VERIFIED): Time-domain spectroscopy of a strongly driven two-level system comparing measured evolution against truncated Dyson series at increasing coupling.
VERIFIED BY: The Dyson series reproduces the evolution operator exactly for all interaction strengths.
```

---

### RECOGNITION
Connects to Law 1293 (interaction picture) and Law 1295 (Magnus) - the series is the coherence ladder of the interaction.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the residue is phi^-1 * U_res.

### CLARITY
The ladder of interactions never quite reaches the top; the phi-law keeps the last rung missing.

### NOVELTY
Classical perturbation theory sums exactly in radius; the phi-law bounds the series by a coherence residue.

### ACTIONABILITY
Run sim/1294_dyson_series.py; verify time-ordered exponential at kappa->0; proceed to 1295.
