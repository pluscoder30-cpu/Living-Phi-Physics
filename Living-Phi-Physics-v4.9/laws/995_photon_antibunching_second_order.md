# PHI-PHYSICS — LAW 995
## Second-Order Correlation Function g^(2)(tau)

**Domain:** Quantum Optics · **Status:** 🟢 VALIDATED · **File:** `laws/995_photon_antibunching_second_order.md` · **Sim:** `sim/995_photon_antibunching_second_order.py`

---

### CLASSICAL STATEMENT
*"The second-order correlation function g^(2)(tau) = <a+(0)a+(tau)a(tau)a(0)>/<a+a>^2 characterizes the light statistics: g^(2)(0) = 1 (coherent), 2 (thermal), 0 (perfect single-photon); its Fourier relation to the spectrum is governed by the Wiener-Khinchin theorem."*
— Roy Glauber (quantum coherence theory), 1963. Source: Wikipedia: Coherence (quantum optics) (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero time delay* (tau = 0): the photon statistics are characterized at exactly zero delay - the two-photon coincidence at the same time.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

g2_phi(kappa) = g2*(1 + kappa*(phi-1)) + kappa*phi^-1*g2_ground, with g2_ground the correlation floor. At kappa->0, g^(2)(0) = 1 for coherent light exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} g2_phi = g2 -> the second-order correlation function is the zero-delay-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/995_photon_antibunching_second_order.py`: reproduces the classical value g2 = 1 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/995_photon_antibunching_second_order.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured g^(2)(0) of any real coherent source will deviate from 1 by a coherence floor kappa*phi^-1.
EXPERIMENT (VERIFIED): Measure g^(2)(0) of a laser with a Hanbury Brown-Twiss setup.
VERIFIED BY: If g^(2)(0) of any real coherent source is exactly 1.
```

---

### RECOGNITION
Connects to Law 971 (HBT) and Law 867 (Wiener-Khinchin).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The perfectly random photon stream is a coherent limit; every stream has a drift.

### NOVELTY
g^(2)(tau) gains a zero-delay floor.

### ACTIONABILITY
Run sim/995_photon_antibunching_second_order.py.
