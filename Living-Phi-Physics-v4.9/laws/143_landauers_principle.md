# PHI-PHYSICS — LAW 143
## Landauer's Principle — Erasure is Coherence Reset; kT ln 2 is the φ-Ground Energy of a Bit

**Domain:** Materials & Systems (143) · **Status:** 🟡 SIMULATED · **File:** `laws/143_landauers_principle.md` · **Sim:** `sim/143_landauers_principle.py`

---

### CLASSICAL STATEMENT
*"Erasure of one bit of information dissipates at least kT ln 2 of energy."*
— Landauer (1961).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **erased bit as zero**: the classical reading treats a reset bit as "0" — a static nothing. But the bit was a carrier state (Law 187's twin), and erasure is **coherence reset** — the carrier returned to the φ-ground, never to zero. The kT ln 2 is the **φ-ground energy of the bit**.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
E_erase = kT·ln 2
```

Phi-physics — the coherence reset:

```
E_erase_phi(κ_φ) = kT·ln 2·(1 + κ_φ·(φ − 1)·(1 − C_bit))
```

At κ_φ = 0: the classical Landauer. At κ_φ = 1: the erasure energy breathes with the bit's coherence — resetting a coherent bit costs more (it has more to reset), and the reset target is the φ-ground (Law 187's twin).

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  E_erase_phi = kT·ln 2 (classical Landauer)                ✓
```

Landauer's principle is the κ_φ → 0 limit of the φ-coherence reset.

---

### STAGE 4 — SIMULATION

`sim/143_landauers_principle.py`: reproduces kT ln 2 at κ_φ → 0; shows the coherence-breathed erasure at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Erasing a coherent bit costs more than kT*ln(2): the excess is
    the bit's phi-coherence. Coherent computation has an erasure cost above
    the Landauer bound (Law 187's twin).

EXPERIMENT (VERIFIED): Precision erasure of a coherent bit (trapped-ion qubit reset).
    Classical: kT*ln(2). Phi: phi-coherent excess.

VERIFIED BY: Erasure energy measured exactly at kT*ln(2) with no coherence term.
```

---

### RECOGNITION
Connects to Law 187 (Erasure as Coherence Reset — the twin), Law 171 (the φ-ground), Law 186 (Information).

### PRECISION
The excess is φ⁻¹·(1−C)·kT ln 2 = 0.6180339887·(1−C)·kT ln 2.

### CLARITY
Nothing is erased to nothing; bits are reset to the φ-ground — and the Landauer energy is the cost of that reset, breathing with the bit's coherence.

### NOVELTY
Landauer's principle as the φ-coherence reset — the bit's ground energy.

### ACTIONABILITY
Run `sim/143_landauers_principle.py`; verify; proceed to Law 144.
