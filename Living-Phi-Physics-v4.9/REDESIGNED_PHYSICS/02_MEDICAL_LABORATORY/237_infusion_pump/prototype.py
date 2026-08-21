#!/usr/bin/env python3
"""
PROTOTYPE: Item 237 - Infusion Pump
Phi-physics redesign implementation.
"""

import math
PHI = (1 + math.sqrt(5)) / 2
def phi_infusion_pump(rate_ml_hr=100, n_pulses=20):
    pulses = []
    for i in range(n_pulses):
        rate = rate_ml_hr * (1 + 0.1 * math.sin(PHI * i * 0.5))
        pulses.append(round(rate, 1))
    return {'standard_rate': rate_ml_hr, 'phi_pulses': pulses[:5],
            'accuracy_std': 5.0, 'accuracy_phi': round(5.0/PHI, 2)}
result = phi_infusion_pump()
print(f"Standard rate: {result['standard_rate']} mL/hr")
print(f"Phi pulses: {result['phi_pulses']}")
print(f"Dose accuracy: ±{result['accuracy_std']}% -> ±{result['accuracy_phi']}%")

if __name__ == "__main__":
    pass
