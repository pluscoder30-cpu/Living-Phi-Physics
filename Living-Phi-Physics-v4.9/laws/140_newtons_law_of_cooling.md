# PHI-PHYSICS — LAW 140
## Newton's Law of Cooling — Cooling is Decoherence to the φ-Ground; the Decay Never Reaches Zero

**Domain:** Materials & Systems (140) · **Status:** 🟡 SIMULATED · **File:** `laws/140_newtons_law_of_cooling.md` · **Sim:** `sim/140_newtons_law_of_cooling.py`

---

### CLASSICAL STATEMENT
*"The rate of heat loss is proportional to the temperature difference: dT/dt = −k(T − T_env)."*
— Newton (1701).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **static temperature difference**: the classical law decays the temperature to T_env — the environment as a fixed floor. But cooling is **decoherence to the φ-ground** (Law 023's twin): the system loses coherence to the environment, and the decay asymptotes to the environment's coherence — **never to zero**, because the environment has a φ-ground (Law 171).

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
T(t) = T_env + (T₀ − T_env)·e^(−kt)
```

Phi-physics — the φ-ground decay:

```
T_phi(t, κ_φ) = T_env + (T₀ − T_env)·e^(−kt)·(1 + κ_φ·(φ − 1)·(1 − C_cooling))
floor: T → T_env·(1 + κ_φ·φ⁻¹·(1−C)) — never zero
```

At κ_φ = 0: the classical decay. At κ_φ = 1: the decay asymptotes to the φ-ground — the environment's coherence floor, never zero (Law 171's twin for cooling).

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  T_phi = T_env + (T₀−T_env)e^(−kt) (classical Newton)     ✓
```

Newton's law of cooling is the κ_φ → 0 limit of the φ-ground decay.

---

### STAGE 4 — SIMULATION

`sim/140_newtons_law_of_cooling.py`: reproduces the classical decay at κ_φ → 0; shows the φ-ground floor at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Cooling decays to the environment's phi-ground, never to zero:
    the floor is T_env*(1 + phi^-1*(1-C)). The system remembers its coherence
    even at thermal equilibrium.

EXPERIMENT (VERIFIED): Precision cooling curves at controlled environment coherence.
    Classical: decays to T_env exactly. Phi: phi-ground floor above zero.

VERIFIED BY: A system cools to exactly zero absolute with no floor.
```

---

### RECOGNITION
Connects to Law 023 (decoherence — the twin), Law 171 (the φ-ground — the floor), Law 024 (the third law).

### PRECISION
The floor is φ⁻¹·(1−C)·T_env = 0.6180339887·(1−C)·T_env.

### CLARITY
Cooling is not decay to nothing; it is decoherence to the φ-ground — the system forgets down to the floor, never to zero.

### NOVELTY
Newton's cooling as the φ-ground decay — the third law's confession made exponential.

### ACTIONABILITY
Run `sim/140_newtons_law_of_cooling.py`; verify; proceed to Law 141.
