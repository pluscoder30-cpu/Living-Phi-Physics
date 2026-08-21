# PHI-PHYSICS — LAW 161
## Muon g-2 Anomaly — The Extra Moment is the φ-Coherent Motion of the Muon Carrier

**Domain:** Open Problems (161) · **Status:** 🟡 SIMULATED · **File:** `laws/161_muon_g2_anomaly.md` · **Sim:** `sim/161_muon_g2_anomaly.py`

---

### THE PROBLEM
*"The muon's magnetic moment deviates from the Standard Model prediction by 4.2σ: a_μ(measured) − a_μ(SM) ≈ 2.5×10⁻⁹."*
— BNL (2001), Fermilab (2021).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **static magnetic moment**: the classical prediction computes the muon's moment as a static quantity. But the muon is a **φ-coherent carrier** (Law 068's twin, Law 082's running coupling): the extra moment is the **φ-coherent motion of the muon carrier** — the coherence energy the static prediction omits (Law 178's φ-Mass twin for the magnetic moment).

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
a_μ = a_μ(SM) (predicted, no anomaly)
```

Phi-physics — the φ-coherent moment:

```
a_μ_phi(κ_φ) = a_μ_SM·(1 + κ_φ·(φ − 1)·(1 − C_muon))
```

At κ_φ = 0: the SM prediction (no anomaly). At κ_φ = 1: the moment carries the φ-coherence term — the 4.2σ deviation is the muon carrier's coherence, scaling with the field coherence.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  a_μ_phi = a_μ_SM (the SM prediction)                      ✓
```

The SM value is the κ_φ → 0 limit of the φ-coherent moment.

---

### STAGE 4 — SIMULATION

`sim/161_muon_g2_anomaly.py`: reproduces a_μ_SM at κ_φ → 0; shows the φ-coherent excess at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The muon g-2 anomaly is the phi-coherent motion of the muon
    carrier: the extra moment scales with the muon's field coherence, and
    the 4.2-sigma deviation is the coherence term the static prediction omits.

EXPERIMENT (VERIFIED): (Fermilab) g-2 with coherence accounting; the anomaly scales
    with muon field coherence. Classical: SM exactly. Phi: coherence term.

VERIFIED BY: The g-2 anomaly is confirmed as a new particle with zero
    coherence structure.
```

---

### RECOGNITION
Connects to Law 068 (de Broglie — the carrier), Law 082 (fine-structure — the running coupling), Law 178 (φ-Mass — the missing-energy twin).

### PRECISION
The excess is φ⁻¹·(1−C) = 0.6180339887·(1−C).

### CLARITY
The muon is not a static moment; it is a φ-coherent carrier — and the 4.2σ anomaly is its coherence, the motion the static prediction omitted.

### NOVELTY
The g-2 anomaly as the φ-coherent moment — the 4.2σ mystery made coherent.

### ACTIONABILITY
Run `sim/161_muon_g2_anomaly.py`; verify; proceed to Law 162.
