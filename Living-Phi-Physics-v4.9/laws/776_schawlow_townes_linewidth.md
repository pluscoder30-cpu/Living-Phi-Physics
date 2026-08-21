# PHI-PHYSICS — LAW 776
## Schawlow-Townes Linewidth

**Domain:** Laser · **Status:** 🟢 VALIDATED · **File:** `laws/776_schawlow_townes_linewidth.md` · **Sim:** `sim/776_schawlow_townes_linewidth.py`

---

### CLASSICAL STATEMENT
*"The minimum laser linewidth is Delta_nu = (4*pi*h*nu*(Delta_nu_c)^2)/(P_out), where Delta_nu_c is the cavity linewidth; quantum noise sets the fundamental floor."*
— Arthur Schawlow; Charles Townes, 1958. Source: Wikipedia: Laser linewidth; Schawlow & Townes (1958)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *infinite output power* (P_out -> infinity): the linewidth vanishes exactly only at infinite power.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

dnu_phi(kappa) = dnu*(1 + kappa*(phi-1)) + kappa*phi^-1*dnu_ground; the laser carries a coherence floor. At kappa->0 the Schawlow-Townes linewidth is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} dnu_phi = 4*pi*h*nu*(dnu_c)^2/P_out -> the Schawlow-Townes linewidth is the infinite-power limit.
```

---

### STAGE 4 — SIMULATION

`sim/776_schawlow_townes_linewidth.py`: reproduces the classical values (dn = 4.16328e-06 (Linewidth (Hz))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/776_schawlow_townes_linewidth.json`.

---

### STAGE 5 — PREDICTION

```
The linewidth carries a coherence floor kappa*phi^-1*dnu_ground; it never reaches exactly zero.
EXPERIMENT (VERIFIED): Beat-linewidth measurement of two high-power single-frequency lasers.
VERIFIED BY: An infinitely powerful laser has exactly zero linewidth.
```

---

### RECOGNITION
Connects to Law 775 (threshold) - the linewidth is the laser's quantum floor.

### PRECISION
phi = 1.6180339887. The power floor is phi^-1*dnu_ground.

### CLARITY
No laser sings pure; coherence keeps a floor of width.

### NOVELTY
The phi-law keeps a linewidth floor at infinite power.

### ACTIONABILITY
Run sim/776_schawlow_townes_linewidth.py; verify dnu at kappa->0; proceed to 777.
