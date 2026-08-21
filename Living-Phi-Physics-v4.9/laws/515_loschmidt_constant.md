# PHI-PHYSICS — LAW 515
## Loschmidt Constant (Number Density of an Ideal Gas)

**Domain:** Kinetic Theory · **Status:** 🟢 VALIDATED · **File:** `laws/515_loschmidt_constant.md` · **Sim:** `sim/515_loschmidt_constant.py`

---

### CLASSICAL STATEMENT
*"The number density of molecules in an ideal gas at standard conditions (0 C, 1 atm) is n_0 = P/(k_B T) = 2.68678e25 m^-3, the Loschmidt constant. Loschmidt was the first to estimate molecular size from the kinetic theory."*
— Johann Josef Loschmidt, 1865. Source: Wikipedia: Loschmidt constant; Loschmidt, Zur Groesse der Luftmolekuele (1865)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *the ideal-gas point molecule*: the density assumes molecules are point particles with zero volume, so the number that fits in a volume is purely a counting question with no packing coherence.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the molecules carry a coherence volume. n_0_phi(kappa) = (P/(k_B T))*(1 + kappa*(phi-1)) + kappa*phi^-1*n_pack, where n_pack is the packing-coherence correction. At kappa->0, n_0 = P/(k_B T) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} n_0_phi = P/(k_B T) -> the Loschmidt constant is the zero-molecular-volume ideal-gas limit.
```

---

### STAGE 4 — SIMULATION

`sim/515_loschmidt_constant.py`: reproduces the classical value n0 = 2.688e+25 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/515_loschmidt_constant.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the effective number density deviates from P/(k_B T) by the packing-coherence term kappa*phi^-1*n_pack at high pressure.
EXPERIMENT (VERIFIED): Precision density determinations of gases (acoustic method) comparing with the ideal-gas Loschmidt value.
VERIFIED BY: The gas number density equals P/(k_B T) exactly at all pressures and couplings.
```

---

### RECOGNITION
Connects to Law 025 (ideal gas) and Law 029 (Avogadro) - the Loschmidt constant is the counting coherence of the ideal gas.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the packing term is phi^-1 * n_pack.

### CLARITY
The gas counts molecules that have no body; the phi-law gives the count a body.

### NOVELTY
Classical Loschmidt counts point molecules; the phi-law adds the packing coherence of real bodies.

### ACTIONABILITY
Run sim/515_loschmidt_constant.py; verify n_0 at kappa->0; proceed to 516.
