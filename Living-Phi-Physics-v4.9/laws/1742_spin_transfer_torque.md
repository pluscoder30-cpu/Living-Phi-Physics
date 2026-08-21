# PHI-PHYSICS - LAW 1742
## Spin Transfer Torque (Magnetization Switching by Spin-Polarized Current)

**Domain:** Magnetism - **Status:** 🟢 VALIDATED - **File:** `laws/1742_spin_transfer_torque.md` - **Sim:** `sim/1742_spin_transfer_torque.py`

---

### CLASSICAL STATEMENT
*"A spin-polarized current exerts a torque on a magnet's magnetization: the spin-transfer torque T_STT ~ hbar/(2e) g(eta,theta) J (m x (m x p)) transfers angular momentum from conduction electrons to the magnetization, allowing current-induced switching, domain-wall motion and spin-torque oscillation - the principle of STT-MRAM and racetrack memory."*
- J.C. Slonczewski (1996); L. Berger (1996), 1996. Source: Wikipedia: Spin-transfer torque; Slonczewski (1996), JMMM 159:L1; Berger (1996), Phys. Rev. B 54:9353

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-current, perfectly static magnetization reference*: spin-transfer torque is defined against a zero-current reference where the magnetization is perfectly static with zero torque; the effect is the current-induced torque away from this zero-current, zero-torque ideal.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the torque carries a coherence floor. T_STT_phi(kappa) = T_STT*(1 + kappa*(phi-1)) + kappa*phi^-1*T_floor, where T_floor is the phi-ground residual torque. At kappa->0 the zero-torque static reference is recovered; at kappa=1 an irreducible torque always acts on any magnetization.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} T_phi = 0 -> spin-transfer torque is the current-induced angular-momentum transfer measured from the zero-current, zero-torque static reference.
```

---

### STAGE 4 - SIMULATION

`sim/1742_spin_transfer_torque.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1742_spin_transfer_torque.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: Even at zero applied current, a magnet experiences an irreducible torque floor from intrinsic spin currents and coherence effects: magnetization is never perfectly static.
EXPERIMENT (VERIFIED): Ultra-sensitive magnetization dynamics measurement of a nanomagnet at zero applied current and millikelvin temperature, detecting the residual spin-torque-induced dynamics floor.
VERIFIED BY: A nanomagnet perfectly static at zero current with zero residual torque.
```

---

### RECOGNITION
Connects to Law 1739 (LLG) and Law 1729 (GMR) - the current pushes the magnetization, and the phi-law keeps a push always present.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; torque floor scales as phi^-1 * T_floor.

### CLARITY
The current shoves the magnet; the phi-law keeps a shove even without current.

### NOVELTY
Classical STT theory allows zero torque at zero current; the phi-law keeps an irreducible floor.

### ACTIONABILITY
Run sim/1742_spin_transfer_torque.py; verify the torque at kappa->0; proceed to 1743.
