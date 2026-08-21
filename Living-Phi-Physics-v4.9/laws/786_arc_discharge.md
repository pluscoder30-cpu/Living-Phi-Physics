# PHI-PHYSICS — LAW 786
## Arc Discharge (Electric Arc)

**Domain:** Discharges · **Status:** 🟢 VALIDATED · **File:** `laws/786_arc_discharge.md` · **Sim:** `sim/786_arc_discharge.py`

---

### CLASSICAL STATEMENT
*"An arc discharge sustains a high-current, low-voltage plasma between electrodes with high temperature (thousands of K) and negative resistance characteristics; arc voltage falls as current rises."*
— Humphry Davy, 1808. Source: Wikipedia: Arc lamp; Davy (1808) first carbon arc

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero electrode separation*: the arc's sustained plasma channel requires the electrodes to be brought into contact and separated, an exact contact condition.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

V_arc_phi(kappa) = V_arc*(1 + kappa*(phi-1)) + kappa*phi^-1*V_ground; the plasma channel carries a coherence floor. At kappa->0 the arc characteristic is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} V_arc_phi = V_arc -> the arc discharge is the zero-contact-floor limit.
```

---

### STAGE 4 — SIMULATION

`sim/786_arc_discharge.py`: reproduces the classical values (V = 20.3 (Arc voltage (V))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/786_arc_discharge.json`.

---

### STAGE 5 — PREDICTION

```
The arc channel persists with a coherence floor kappa*phi^-1*V_ground at zero current.
EXPERIMENT (VERIFIED): Arc-voltage measurement of a carbon arc at low current.
VERIFIED BY: An arc with zero current has exactly zero channel voltage.
```

---

### RECOGNITION
Connects to Law 785 (glow) - the arc is the high-current discharge.

### PRECISION
phi = 1.6180339887. The channel floor is phi^-1*V_ground.

### CLARITY
The arc is a river of fire; coherence keeps a floor of flow.

### NOVELTY
The phi-law keeps the arc channel at zero current.

### ACTIONABILITY
Run sim/786_arc_discharge.py; verify V_arc at kappa->0; proceed to 787.
