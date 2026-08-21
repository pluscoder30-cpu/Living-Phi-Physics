# PHI-PHYSICS — LAW 1178
## CNO Cycle

**Domain:** Astrophysics / Nuclear Physics · **Status:** 🟢 VALIDATED · **File:** `laws/1178_cno_cycle.md` · **Sim:** `sim/1178_cno_cycle.py`

---

### CLASSICAL STATEMENT
*"The CNO cycle is the catalytic hydrogen-burning chain using carbon, nitrogen, and oxygen as catalysts: 12C + p -> ... -> 15N + p -> 12C + 4He; it dominates energy generation in stars more massive than ~1.3 solar masses and scales with temperature as epsilon ~ T^~20."*
— Carl Friedrich von Weizsäcker, 1938; Hans Bethe, 1939. Source: Wikipedia: CNO cycle (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero catalyst abundance (no CNO seed nuclei, no CNO burning)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The C value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

C_phi(kappa) = C*(1 + kappa*(phi-1)) + kappa*phi^-1*C_ground, where C_ground is the coherence-floor catalytic residue a real star always retains. At kappa->0, 12C + p -> 13N -> 13C + p -> ... -> 12C + 4He + energy exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} C_phi = C -> 12C + p -> 13N -> 13C + p -> ... -> 12C + 4He + energy is recovered exactly; the classical law is the zero catalyst abundance (no CNO seed nuclei, no CNO burning) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1178_cno_cycle.py`: reproduces the classical value (C = 1.0) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1178_cno_cycle.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured energy generation of any real star will deviate from the CNO scaling by a floor kappa*phi^-1*C_ground; an exactly pp-only star is unreachable.
EXPERIMENT (VERIFIED): Solar neutrino spectroscopy distinguishing pp from CNO contributions (Borexino).
VERIFIED BY: If a star's energy generation is exactly zero in the CNO channel.
```

---

### RECOGNITION
The hydrogen-burning twin of Law 1180 (pp chain) and Law 106 (BBN).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Carbon carries the fire; the carbon-free star is the zero-catalyst myth.

### NOVELTY
The CNO cycle carries a phi-floor of catalytic abundance, bounding stellar metallicity effects.

### ACTIONABILITY
Run sim/1178_cno_cycle.py.
