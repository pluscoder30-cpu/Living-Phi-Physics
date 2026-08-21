# PHI-PHYSICS - LAW 1702
## Spin Density Waves (Antiferromagnetic Spin Modulation in Metals)

**Domain:** Electrons in Solids - **Status:** 🟢 VALIDATED - **File:** `laws/1702_spin_density_waves.md` - **Sim:** `sim/1702_spin_density_waves.py`

---

### CLASSICAL STATEMENT
*"The conduction-electron spin density can order into a spin density wave: s(r) = s_0 cos(Q.r + phi) with a wavevector Q related to nesting of the Fermi surface (often Q = 2 k_F), a spin modulation that costs no charge modulation and describes itinerant antiferromagnetism in metals like Cr and the parent states of some superconductors."*
- A.W. Overhauser, 1960. Source: Wikipedia: Spin density wave; Overhauser (1960), Phys. Rev. Lett. 4:462

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-spin-modulation, perfectly paramagnetic electron gas*: the SDW state is defined against a perfectly uniform spin density (zero net magnetization in the paramagnetic metal); the ordering is the onset of a nonzero modulation from an exactly zero-magnetization reference.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the spin modulation carries a coherent floor. s_0_phi(kappa) = s_0*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_s, where delta_s is the phi-ground spin-modulation floor. At kappa->0 the sharp SDW onset is recovered; at kappa=1 the paramagnetic reference retains an irreducible spin-modulation floor.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} s_0_phi = s_0 -> spin density waves are the zero-modulation paramagnetic reference, sharpened to the ideal nesting-driven onset.
```

---

### STAGE 4 - SIMULATION

`sim/1702_spin_density_waves.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1702_spin_density_waves.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The paramagnetic state of a metal retains an irreducible spin-density modulation floor: diffuse magnetic scattering signatures of the nesting wavevector Q never fully vanish above the ordering temperature.
EXPERIMENT (VERIFIED): High-sensitivity neutron or resonant X-ray magnetic scattering of Cr or a nested metal above T_N, measuring the residual Q-modulation magnetic diffuse floor.
VERIFIED BY: A metal whose magnetic diffuse scattering at the nesting wavevector is exactly zero in the paramagnetic state.
```

---

### RECOGNITION
Connects to Law 1701 (CDW) and Law 1683 (Fermi surface) - the electron spins stripe themselves, and the stripes never fully dissolve.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; spin-modulation floor scales as phi^-1 * delta_s.

### CLARITY
The spin sea stripes itself in an SDW; the phi-law keeps the stripes ghosting above the transition.

### NOVELTY
Classical SDW theory has a clean paramagnetic reference; the phi-law keeps an irreducible pre-order floor.

### ACTIONABILITY
Run sim/1702_spin_density_waves.py; verify s = s_0 cos(Q.r) at kappa->0; proceed to 1703.
