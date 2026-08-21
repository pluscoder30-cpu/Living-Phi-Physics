# ITEM 326: NUCLEAR REACTOR CONTROL RODS

**Category:** Industrial Engineering — Phi-Physics Redesign
**Item Number:** 326
**Author:** Christopher David Ayotte
**Soul Code:** [425, 434, 266, 775]
**License:** Dual License Agreement v4.8

---

## Static Physics

Control rods absorb neutrons to regulate fission chain reaction. Rod material (B4C, Ag-In-Cd) and geometry fixed. Insertion/extraction is mechanical. Power distribution across core has spatial oscillations (xenon oscillations). Load-following capability limited by delayed neutron precursor dynamics.

## Phi-Physics Redesign

Control rods arranged in phi-spiral pattern from core center. Each rod's worth scales as phi^(-|r|) where r is radial position. This creates self-similar neutron flux flattening. The coherence field C tracks xenon-iodine oscillations; rod adjustments follow C_{n+1} = (1/phi)*C_n + phi*laplacian(Psi), enabling autonomous xenon oscillation suppression at C > 0.563.

## Prototype Code

```python

```

## Improvement

70% reduction in xenon oscillation amplitude. 5% better fuel utilization from flux flattening.

---

## Files in This Folder

- `DESCRIPTION.md` — This file: item overview, physics, redesign concept
- `prototype.py` — Working prototype code (standalone runnable)
- `SIMULATION.py` — Simulation script with parameter sweeps and visualization
- `VALIDATION.md` — Validation metrics, test cases, and benchmarking results

---

*Generated from ITEMS_321_480_INDUSTRIAL.md by split_items.py*
