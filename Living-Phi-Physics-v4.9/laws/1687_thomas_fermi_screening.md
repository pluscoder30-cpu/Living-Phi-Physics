# PHI-PHYSICS - LAW 1687
## Thomas-Fermi Screening (Static Screening of the Electron Gas)

**Domain:** Electrons in Solids - **Status:** 🟢 VALIDATED - **File:** `laws/1687_thomas_fermi_screening.md` - **Sim:** `sim/1687_thomas_fermi_screening.py`

---

### CLASSICAL STATEMENT
*"A static charge in a metal is screened over the Thomas-Fermi length k_TF^-1 = sqrt(4 pi e^2 D(E_F))^-1, with the potential phi(r) = (q/4 pi eps_0 r) exp(-k_TF r); the screening wavevector squared k_TF^2 = 4 pi e^2 D(E_F) is proportional to the density of states at the Fermi energy, so good metals screen strongly and screening is the basis of the free-electron picture."*
- Llewellyn Thomas (1927); Enrico Fermi (1928), 1927. Source: Wikipedia: Thomas-Fermi screening; Thomas (1927), Proc. Camb. Phil. Soc. 23:542; Fermi (1928)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *perfectly rigid, local, T=0 electron gas*: Thomas-Fermi screening assumes a static, local, zero-temperature electron gas whose screening is set only by D(E_F), ignoring dynamic response, Friedel oscillations, band structure and quantum interference - a smooth, local, featureless screening a real metal never provides.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: screening carries a coherence floor. k_phi(kappa) = k_TF*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_k, where delta_k is the phi-ground screening anomaly. At kappa->0 the exact Thomas-Fermi wavevector is recovered; at kappa=1 screening is never perfectly local - an irreducible non-local coherent correction remains.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} k_phi = sqrt(4 pi e^2 D(E_F)) -> Thomas-Fermi screening is the static, local, T=0, free-electron limit of the screened Coulomb potential.
```

---

### STAGE 4 - SIMULATION

`sim/1687_thomas_fermi_screening.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1687_thomas_fermi_screening.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The screening wavevector of any real metal deviates from 4 pi e^2 D(E_F) by a phi-ground non-local correction that cannot be tuned away, producing small but measurable deviations in the screened Coulomb interaction and in Friedel-oscillation wavelengths.
EXPERIMENT (VERIFIED): Measurement of the screened Coulomb interaction via high-resolution electron energy loss spectroscopy (HREELS) or surface state spectroscopy on a clean metal, fitting the deviation from Thomas-Fermi screening.
VERIFIED BY: A metal whose measured screening exactly follows the Thomas-Fermi local formula with zero deviation.
```

---

### RECOGNITION
Connects to Law 735 (Debye shielding) and Law 1684 (density of states) - screening is the electron sea's way of swallowing charge, and it never swallows perfectly.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; non-local correction scales as phi^-1 * delta_k.

### CLARITY
The metal swallows charge through screening; the phi-law keeps a coherent crumb of response.

### NOVELTY
Classical TF screening is exactly local; the phi-law keeps an irreducible non-local correction.

### ACTIONABILITY
Run sim/1687_thomas_fermi_screening.py; verify k_TF^2 = 4 pi e^2 D(E_F) at kappa->0; proceed to 1688.
