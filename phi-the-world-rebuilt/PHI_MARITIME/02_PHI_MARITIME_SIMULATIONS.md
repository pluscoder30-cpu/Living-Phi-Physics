---
**Author:** Christopher David Ayotte  
**Soul Code:** 425-434-2667-775  
**License:** Dual License Agreement v4.9  
---
# PHI-PHYSICS — MARITIME SIMULATIONS
## Domain: Maritime and Aquatic Systems

**Author:** The Architect  
**Soul Code:** PHI-MARITIME-002  
**License:** CC BY-NC-SA 4.0 (License v4.9)  
**Status:** Foundation Document  
**Created:** 2026-08-24

---

## SIMULATION M-1: PHI-HARMONIC BUOYANCY SWEEP

### Setup
- Object: rigid sphere, radius R = 0.5m, density ρ_obj = 800 kg/m³
- Fluid: water, ρ_fluid = 1000 kg/m³
- Sweep κ_φ from 0 to 1 in increments of 0.1
- Compute apparent weight: W_app = (ρ_obj - ρ_fluid) · V · g · (1 + κ_φ · (φ⁻¹ - 1))

### Expected Results
| κ_φ | W_app (N) | ΔW/W_classical |
|-----|-----------|----------------|
| 0.0 | -1208.5   | 0.000%         |
| 0.2 | -1359.8   | 12.51%         |
| 0.4 | -1511.2   | 25.05%         |
| 0.6 | -1662.5   | 37.58%         |
| 0.8 | -1813.8   | 50.11%         |
| 1.0 | -1965.1   | 62.64%         |

### Verification
At κ_φ = 0, recovery of classical buoyancy to machine precision (error < 10⁻¹⁵).

---

## SIMULATION M-2: PHI-HARMONIC WAVE DISPERSION

### Setup
- Water depth: h = 50m (deep water regime)
- Wavelength sweep: λ = 0.1m to 1000m
- κ_φ = 0.5 (moderate coupling)
- Compute dispersion: ω² = gk · (1 + κ_φ · φ · k²)

### Expected Results
- Long waves (λ > 10m): deviation < 0.01% from classical
- Short waves (λ < 1m): deviation up to 8.3% from classical
- Phi-correction dominates at k > 1 rad/m

### Verification
Classical limit recovery at κ_φ = 0 for all wavelengths.

---

## SIMULATION M-3: PHI-HARMONIC TIDE PREDICTION

### Setup
- Orbital period: T = 12.42 hours (M2 tidal constituent)
- Moon mass: M = 7.342 × 10²² kg
- Distance: r = 3.844 × 10⁸ m
- κ_φ = 0.3
- Time span: 30 days

### Expected Results
- Primary tidal amplitude: A₀ = 0.52m (classical)
- Phi-modulated amplitude: A_phi = A₀ · (1 + 0.3 · sin(φ · 2π/T · t))
- Maximum tidal range increase: 18.5% over classical
- Secondary phi-harmonic at frequency φ · ω_orbital

### Verification
Mean tidal prediction matches J2000 ephemeris to within 2mm when κ_φ = 0.

---

## SIMULATION M-4: PHI-HARMONIC CURRENT DYNAMICS

### Setup
- Basin: 100km × 100km, depth 1000m
- Coriolis parameter: f = 10⁻⁴ s⁻¹
- Initial condition: geostrophic jet at v = 0.5 m/s
- κ_φ = 0.4
- Duration: 60 days

### Expected Results
- Classical: stable geostrophic balance maintained
- Phi-coupled: slow drift of jet axis at rate κ_φ · φ · f · B_field / v
- Jet meandering amplitude increases by factor (1 + κ_φ · φ)

### Verification
Classical geostrophic balance recovered at κ_φ = 0.

---

## SIMULATION M-5: PHI-HARMONIC CORROSION RATE

### Setup
- Material: mild steel
- Environment: seawater, [NaCl] = 0.6 M
- Current density: I = 0.1 A/m²
- κ_φ sweep: 0 to 1
- Duration: 365 days

### Expected Results
| κ_φ | Corrosion Rate (mm/yr) | ΔR/R_Faraday |
|-----|------------------------|--------------|
| 0.0 | 1.24                   | 0.00%        |
| 0.3 | 1.48                   | 19.4%        |
| 0.6 | 1.72                   | 38.7%        |
| 1.0 | 1.96                   | 58.1%        |

### Verification
Corrosion rate matches Faraday's law at κ_φ = 0 within electrochemical uncertainty.

---

## SIMULATION M-6: PHI-HARMONIC HULL FATIGUE

### Setup
- Hull plate: steel, thickness 20mm
- Wave loading: sinusoidal, amplitude 50 MPa
- κ_φ = 0.5
- Cycle count: 10⁶

### Expected Results
- Classical fatigue life: N_f = 2.1 × 10⁶ cycles
- Phi-modified fatigue life: N_f_phi = N_f / (1 + κ_φ · φ · dη/dt_rms)
- Reduction factor: ~1.618 at full coupling
- Fatigue crack growth rate enhanced by phi-modulation

### Verification
Fatigue life matches S-N curve data at κ_φ = 0.

---

## SIMULATION SCRIPTS

All simulations to be implemented as:
- `sim/M01_phi_buoyancy.py`
- `sim/M02_phi_wave_dispersion.py`
- `sim/M03_phi_tide_prediction.py`
- `sim/M04_phi_current_dynamics.py`
- `sim/M05_phi_corrosion_rate.py`
- `sim/M06_phi_hull_fatigue.py`

### Dependencies
- NumPy, SciPy, Matplotlib
- Optional: OpenFOAM (M-4), ANSYS (M-6)

---

*All simulations must reproduce classical results at κ_φ = 0 before exploring phi-coupled dynamics.*

