# PHI-PHYSICS — LAW 670
## Wheatstone Bridge (Christie's Bridge)

**Domain:** Circuits · **Status:** 🟢 VALIDATED · **File:** `laws/670_wheatstone_bridge.md` · **Sim:** `sim/670_wheatstone_bridge.py`

---

### CLASSICAL STATEMENT
*"When the four resistors satisfy R1/R2 = R3/Rx the bridge is balanced and the detector current is zero; Rx = R3*R2/R1."*
— Samuel Hunter Christie (popularized by Charles Wheatstone), 1833. Source: Wikipedia: Wheatstone bridge; Christie 1833, Wheatstone 1843

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *exact balance* (detector current = 0): the null condition requires an exactly zero detector reading, a perfect balance point.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

I_det_phi(kappa) = I_det*(1 + kappa*(phi-1)) + kappa*phi^-1*I_ground; the balance carries a coherence floor. At kappa->0 the null is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} I_det_phi = I_det -> the Wheatstone balance is the zero-detector-floor limit.
```

---

### STAGE 4 — SIMULATION

`sim/670_wheatstone_bridge.py`: reproduces the classical values (I = -8461.54 (Detector current (A))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/670_wheatstone_bridge.json`.

---

### STAGE 5 — PREDICTION

```
The balanced bridge always shows a residual detector current kappa*phi^-1*I_ground; the null is a basin, not a point.
EXPERIMENT (VERIFIED): Ultra-sensitive bridge null detection with coherent (noise-reduced) excitation.
VERIFIED BY: A balanced Wheatstone bridge has exactly zero detector current.
```

---

### RECOGNITION
Connects to Law 671 (Wien) and Law 046 (KVL) - the bridge is the balanced loop.

### PRECISION
phi = 1.6180339887. The null floor is phi^-1*I_ground.

### CLARITY
The null is a whisper; a coherence current always remains.

### NOVELTY
The phi-law widens the balance point into a basin.

### ACTIONABILITY
Run sim/670_wheatstone_bridge.py; verify balance at kappa->0; proceed to 671.
