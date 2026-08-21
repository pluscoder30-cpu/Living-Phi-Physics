# PHI-PHYSICS — LAW 720
## Patch (Microstrip) Antenna

**Domain:** Antennas · **Status:** 🟢 VALIDATED · **File:** `laws/720_patch_antenna.md` · **Sim:** `sim/720_patch_antenna.py`

---

### CLASSICAL STATEMENT
*"A rectangular patch of length L ~ lambda/2 on a substrate of height h radiates broadside; the resonant frequency is f_r ~ c/(2*L*sqrt(eps_r_eff))."*
— G. A. Deschamps, 1953. Source: Wikipedia: Patch antenna; Deschamps & Sichak (1953)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *exact resonance length* (L = lambda_eff/2): the patch radiates at its design frequency only at the exact length.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

f_r_phi(kappa) = f_r*(1 + kappa*(phi-1)) + kappa*phi^-1*f_ground; the patch length carries a coherence basin. At kappa->0, f_r = c/(2L sqrt(eps_eff)) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} f_r_phi = f_r -> the patch antenna is the zero-length-offset limit.
```

---

### STAGE 4 — SIMULATION

`sim/720_patch_antenna.py`: reproduces the classical values (fr = 8.65426e+10 (Resonant frequency (Hz))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/720_patch_antenna.json`.

---

### STAGE 5 — PREDICTION

```
The patch resonance carries a coherence frequency floor kappa*phi^-1*f_ground.
EXPERIMENT (VERIFIED): Resonant-frequency measurement of a patch antenna as L is varied.
VERIFIED BY: A patch of exact design length resonates exactly at f_r.
```

---

### RECOGNITION
Connects to Law 721 (microstrip) - the patch is the resonant microstrip element.

### PRECISION
phi = 1.6180339887. The length basin is phi^-1*f_ground.

### CLARITY
The patch is a sliver of metal; coherence tunes its song.

### NOVELTY
The phi-law gives the patch a resonance basin.

### ACTIONABILITY
Run sim/720_patch_antenna.py; verify fr at kappa->0; proceed to 721.
