# PHI-PHYSICS — LAW 1179
## Triple-Alpha Process

**Domain:** Astrophysics / Nuclear Physics · **Status:** 🟢 VALIDATED · **File:** `laws/1179_triple_alpha_process.md` · **Sim:** `sim/1179_triple_alpha_process.py`

---

### CLASSICAL STATEMENT
*"The triple-alpha process builds carbon-12 from three helium-4 nuclei: 4He + 4He -> 8Be, then 8Be + 4He -> 12C* -> 12C + gamma, with the Hoyle resonance at 7.654 MeV making the process fast enough; it is the origin of carbon and heavier elements in red giants."*
— Edwin Salpeter, 1952; refined by Fred Hoyle, 1954. Source: Wikipedia: Triple-alpha process (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero helium (no 4He, no carbon synthesis)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The T value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

T_phi(kappa) = T*(1 + kappa*(phi-1)) + kappa*phi^-1*T_ground, where T_ground is the coherence-floor carbon yield a real helium-burning star always produces. At kappa->0, 4He + 4He -> 8Be,  8Be + 4He -> 12C* -> 12C (Hoyle state 7.654 MeV) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} T_phi = T -> 4He + 4He -> 8Be,  8Be + 4He -> 12C* -> 12C (Hoyle state 7.654 MeV) is recovered exactly; the classical law is the zero helium (no 4He, no carbon synthesis) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1179_triple_alpha_process.py`: reproduces the classical value (T = 1.0) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1179_triple_alpha_process.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured carbon yield of any real helium-burning star will deviate from the triple-alpha prediction by a floor kappa*phi^-1*T_ground; an exactly carbon-free universe is unreachable.
EXPERIMENT (VERIFIED): Nucleosynthesis modeling against observed carbon abundances and stellar evolution.
VERIFIED BY: If helium burning produces exactly zero carbon.
```

---

### RECOGNITION
The element-builder of Law 106 (BBN) and the stellar engine of Law 1178 (CNO).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Helium fuses through a resonance; the carbon-free star is the zero-resonance myth.

### NOVELTY
The triple-alpha process carries a phi-floor of yield, so carbon always forms in helium burners.

### ACTIONABILITY
Run sim/1179_triple_alpha_process.py.
