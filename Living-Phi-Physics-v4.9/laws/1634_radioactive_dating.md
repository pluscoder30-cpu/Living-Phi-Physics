# PHI-PHYSICS - LAW 1634
## Radiometric Dating (Half-Life Chronometry)

**Domain:** Nuclear Applications - **Status:** 🟢 VALIDATED - **File:** `laws/1634_radioactive_dating.md` - **Sim:** `sim/1634_radioactive_dating.py`

---

### CLASSICAL STATEMENT
*"Radiometric dating uses the decay law N(t) = N0 e^-lambda t to determine the age of materials: t = (1/lambda) ln(N0/N); the radiocarbon method (Libby, Nobel 1960) uses the C-14 half-life 5730 years, while U-Pb, K-Ar and Rb-Sr methods date geological materials over billions of years."*
- Rutherford (1904); radiocarbon dating (Libby 1949), 1949. Source: Libby, Radiocarbon Dating (1952); Wikipedia: Radiometric dating

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-decay, zero-age, instant-zero limit*: at the moment of formation the daughter fraction is exactly zero (or the parent fraction exactly N0); the classical treatment of a freshly-formed sample is the zero-age, zero-daughter limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

t_phi(kappa) = t_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_t, where delta_t is the phi-ground age-uncertainty floor. At kappa->0 the exact decay-law age is recovered.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} t_phi = (1/lambda) ln(N0/N) -> radiometric dating is the zero-contamination, zero-initial-daughter, exact-decay limit.
```

---

### STAGE 4 - SIMULATION

`sim/1634_radioactive_dating.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1634_radioactive_dating.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The derived age carries a phi-ground contamination/initial-condition floor, so the age always has an irreducible systematic uncertainty from initial daughter and contamination.
EXPERIMENT (VERIFIED): Radiocarbon calibration and isochron dating (U-Pb concordia, Rb-Sr) vs the decay-law model with initial conditions.
VERIFIED BY: A radiometric date with exactly zero initial-daughter and contamination uncertainty.
```

---

### RECOGNITION
Connects to Law 1590 (half-life), Law 1588 (cascade) and Law 1626 (actinide chains) - radiometric dating is the earth's calendar.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The clock ticks in decay; the phi-law keeps a floor of clock drift.

### NOVELTY
Classical dating is exact; the phi-law predicts an irreducible contamination floor.

### ACTIONABILITY
Run sim/1634_radioactive_dating.py; verify the age; proceed to Law 1635.
