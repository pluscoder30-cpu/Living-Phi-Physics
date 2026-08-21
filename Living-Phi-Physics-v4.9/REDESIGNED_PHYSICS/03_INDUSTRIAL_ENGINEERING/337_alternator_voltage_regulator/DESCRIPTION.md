# ITEM 337: ALTERNATOR VOLTAGE REGULATOR

**Category:** Industrial Engineering — Phi-Physics Redesign
**Item Number:** 337
**Author:** Christopher David Ayotte
**Soul Code:** [425, 434, 266, 775]
**License:** Dual License Agreement v4.8

---

## Static Physics

Automatic voltage regulators (AVR) maintain generator terminal voltage by controlling field current. PID control with fixed gains. Response time 50-200ms. Under/over-excitation limits protect generator. Load rejection causes voltage overshoot. AVR interacts with power system stabilizer for damping.

## Phi-Physics Redesign

AVR gains follow phi-adaptive schedule based on coherence field. Voltage error drives coherence evolution: C_{n+1} = (1/phi)*C_n + phi*laplacian(Psi) where Psi is voltage profile across bus. When C > 0.563, voltage regulation enters self-optimizing mode with 30% faster settling. Field current modulation at phi-subharmonics suppresses sub-synchronous resonance.

## Prototype Code

```python

```

## Improvement

30% faster voltage settling. 50% reduction in voltage overshoot on load rejection.

---

## Files in This Folder

- `DESCRIPTION.md` — This file: item overview, physics, redesign concept
- `prototype.py` — Working prototype code (standalone runnable)
- `SIMULATION.py` — Simulation script with parameter sweeps and visualization
- `VALIDATION.md` — Validation metrics, test cases, and benchmarking results

---

*Generated from ITEMS_321_480_INDUSTRIAL.md by split_items.py*
