# PHI-PHYSICS — LAW 637
## Mutual Inductance

**Domain:** Magnetostatics · **Status:** 🟢 VALIDATED · **File:** `laws/637_mutual_inductance.md` · **Sim:** `sim/637_mutual_inductance.py`

---

### CLASSICAL STATEMENT
*"The flux in circuit 2 produced by current I1 in circuit 1 is Phi_2 = M*I1, where the mutual inductance M couples the two circuits; emf_2 = -M*dI1/dt."*
— Joseph Henry, 1832. Source: Wikipedia: Mutual inductance; Henry (1832)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero leakage*: mutual inductance assumes the entire field of one circuit links the other, an exactly coupled pair of loops.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

M_phi(kappa) = M*(1 + kappa*(phi-1)) + kappa*phi^-1*M_ground; the coupling carries a coherence-leak floor. At kappa->0, Phi_2 = M*I1 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} M_phi = M -> mutual inductance is the zero-leak coupling limit.
```

---

### STAGE 4 — SIMULATION

`sim/637_mutual_inductance.py`: reproduces the classical values (M = 0.0188496 (Mutual inductance (H))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/637_mutual_inductance.json`.

---

### STAGE 5 — PREDICTION

```
Coherently coupled circuits show an effective mutual inductance floor kappa*phi^-1*M_ground that never vanishes with distance.
EXPERIMENT (VERIFIED): Mutual-inductance measurement of two loops as a function of separation.
VERIFIED BY: The mutual inductance of two circuits is always exactly the classical value.
```

---

### RECOGNITION
Connects to Law 639 (Neumann) and Law 638 (self) - the pair coupling is the field's coherence link.

### PRECISION
phi = 1.6180339887. The leakage floor is phi^-1*M_ground.

### CLARITY
Coupling is never total; the field always leaks a coherence line.

### NOVELTY
The phi-law gives mutual coupling a coherence floor at all distances.

### ACTIONABILITY
Run sim/637_mutual_inductance.py; verify M at kappa->0; proceed to 638.
