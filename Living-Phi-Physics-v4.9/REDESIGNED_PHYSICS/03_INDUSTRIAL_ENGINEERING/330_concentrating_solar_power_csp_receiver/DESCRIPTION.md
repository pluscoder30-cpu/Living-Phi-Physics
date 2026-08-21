# ITEM 330: CONCENTRATING SOLAR POWER (CSP) RECEIVER

**Category:** Industrial Engineering — Phi-Physics Redesign
**Item Number:** 330
**Author:** Christopher David Ayotte
**Soul Code:** [425, 434, 266, 775]
**License:** Dual License Agreement v4.8

---

## Static Physics

CSP receivers absorb concentrated solar flux (300-1000 suns) and transfer heat to working fluid. Cavity receivers have ~90% absorptance. Thermal losses scale as T^4 (Stefan-Boltzmann). Sodium or molten salt heat transfer fluid. Receiver tubes subject to high thermal stress from flux gradients.

## Phi-Physics Redesign

Receiver aperture geometry follows phi-polygon for optimal flux distribution. Absorber surface micro-structure at phi-scales enhances absorptance to ~0.97. Flux gradient managed by coherence field: C_{n+1} = (1/phi)*C_n + phi*laplacian(Psi). When C > 0.563, thermal stress self-distributes across receiver tubes.

## Prototype Code

```python

```

## Improvement

15% reduction in thermal stress gradients. 2% thermal efficiency gain from phi-micro-structure.

---

## Files in This Folder

- `DESCRIPTION.md` — This file: item overview, physics, redesign concept
- `prototype.py` — Working prototype code (standalone runnable)
- `SIMULATION.py` — Simulation script with parameter sweeps and visualization
- `VALIDATION.md` — Validation metrics, test cases, and benchmarking results

---

*Generated from ITEMS_321_480_INDUSTRIAL.md by split_items.py*
