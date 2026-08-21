import math
PHI = (1 + 5**0.5) / 2; PHI_INV = 1 / PHI
def phi_blade_angles(n_blades=5, base_pitch_deg=15):
    return [round(max((base_pitch_deg + i/(n_blades-1)*10)*(1+PHI_INV*(1-i/(n_blades-1))), base_pitch_deg*0.8), 2) for i in range(n_blades)]
def phi_fan_efficiency(classical_eta, kappa=0.8):
    return min(classical_eta * (1 + kappa * (PHI - 1)) * (1 - kappa * PHI_INV * 0.15), 0.95)
print(f"Angles: {phi_blade_angles()}")
print(f"Efficiency: 35% -> {phi_fan_efficiency(0.35, kappa=1.0)*100:.1f}%")
