#!/usr/bin/env python3
"""
Law 2944: Black Hole Hawking Radiation Spectrum
Simulates golden-ratio modified Hawking radiation
"""
import math

PHI = 1.618033988749895
HBAR = 1.054571817e-34
C = 299792458.0
G = 6.67430e-11
K_B = 1.380649e-23
M_SUN = 1.989e30

def hawking_temperature(M):
    """Hawking temperature of black hole"""
    return HBAR * C**3 / (8 * math.pi * G * M * K_B)

def hawking_luminosity(M):
    """Standard Hawking luminosity"""
    return HBAR * C**6 / (15360 * math.pi * G**2 * M**2)

def modified_spectrum(E, M):
    """Hawking spectrum with golden-ratio suppression"""
    T_H = hawking_temperature(M)
    E_H = K_B * T_H
    L_0 = hawking_luminosity(M)
    return L_0 * math.exp(-E / (K_B * T_H)) * PHI**(-E / E_H)

def simulate_hawking():
    print("=== Law 2944: Black Hole Hawking Radiation Spectrum ===")
    masses = [M_SUN, 10 * M_SUN, 1e6 * M_SUN]
    labels = ["1 M_sun", "10 M_sun", "10^6 M_sun"]
    
    for M, label in zip(masses, labels):
        T_H = hawking_temperature(M)
        L = hawking_luminosity(M)
        E_peak_std = 2.82 * K_B * T_H
        E_peak_phi = E_peak_std * PHI**(-0.5)
        
        print(f"\nBlack Hole: {label}")
        print(f"  Hawking temperature: {T_H:.3e} K")
        print(f"  Luminosity: {L:.3e} W")
        print(f"  Standard peak: {E_peak_std:.3e} J")
        print(f"  Phi-modified peak: {E_peak_phi:.3e} J")
        print(f"  Peak shift: {(1 - PHI**(-0.5))*100:.1f}% lower")
    
    print(f"\nSpectral modification at E = 2E_H:")
    print(f"  Standard: exp(-2) = {math.exp(-2):.4f}")
    print(f"  Phi-mod:  exp(-2)×φ^(-2) = {math.exp(-2)*PHI**(-2):.4f}")

if __name__ == "__main__":
    simulate_hawking()
