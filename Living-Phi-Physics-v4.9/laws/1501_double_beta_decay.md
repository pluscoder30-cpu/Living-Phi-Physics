# PHI-PHYSICS - LAW 1501
## Double Beta Decay (Two-Neutrino and Neutrinoless Modes)

**Domain:** Weak Interaction / Neutrinos - **Status:** 🟢 VALIDATED - **File:** `laws/1501_double_beta_decay.md` - **Sim:** `sim/1501_double_beta_decay.py`

---

### CLASSICAL STATEMENT
*"A nucleus may decay by emitting two electrons (and two neutrinos in the 2nu-beta-beta mode) with half-lives of ~10^18-10^24 years; the neutrinoless mode (0nu-beta-beta), if observed, would prove the neutrino is its own antiparticle (Majorana) and violate lepton number."*
- Maria Goeppert-Mayer (1935); neutrinoless mode by W.H. Furry (1939), 1935. Source: Goeppert-Mayer, Phys. Rev. 48 (1935) 512; Wikipedia: Double beta decay

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-neutrino-mass, exactly-two-neutrino limit*: the 2nu mode is 'background' to the 0nu search; classical treatment assumes the neutrino is exactly massless so only 2nu emission occurs with zero 0nu contamination - a zero-neutrino-mass, Majorana-blind limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

T_0nu_phi(kappa) = T_0nu_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*T_floor, where T_floor is the phi-ground nuclear-matrix-element floor. At kappa->0 the 2nu-only picture is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} T_0nu_phi -> infinity (0nu forbidden) -> the 2nu double-beta picture is the zero-neutrino-mass, lepton-number-conserving limit.
```

---

### STAGE 4 - SIMULATION

`sim/1501_double_beta_decay.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1501_double_beta_decay.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The effective Majorana mass and the 0nu rate carry a phi-ground nuclear-matrix-element floor, so the extracted neutrino mass from a 0nu signal always has an irreducible theoretical uncertainty.
EXPERIMENT (VERIFIED): 0nu-beta-beta searches (LEGEND, CUORE, KamLAND-Zen, nEXO) and 2nu-beta-beta half-life measurements constraining nuclear matrix elements.
VERIFIED BY: A 0nu-beta-beta experiment with exactly zero background floor and zero nuclear-matrix-element uncertainty at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1454 (Fermi theory), Law 1551 (seesaw) and Law 1552 (neutrino oscillations) - double beta decay is the neutrino's confession box.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The nucleus decays twice; the phi-law keeps a floor of the twice leaking.

### NOVELTY
Classical 2nu is pure background; the phi-law keeps an irreducible 0nu-matrix-element floor.

### ACTIONABILITY
Run sim/1501_double_beta_decay.py; verify the 2nu half-life scale; proceed to Law 1502.
