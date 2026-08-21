#!/usr/bin/env python3
"""
Law 2950: Quantum Field Renormalization Flow
Simulates golden-ratio modified running of coupling constants
"""
import math

PHI = 1.618033988749895

def beta_qcd(alpha, n_f=6):
    """QCD beta function (one-loop)"""
    b0 = (33 - 2 * n_f) / (12 * math.pi)
    return -b0 * alpha**2

def running_coupling_standard(alpha_0, mu_0, mu, n_f=6):
    """Standard running coupling"""
    b0 = (33 - 2 * n_f) / (12 * math.pi)
    return alpha_0 / (1 + b0 * alpha_0 * math.log(mu / mu_0))

def running_coupling_phi(alpha_0, mu_0, mu, n_f=6):
    """Phi-modified running coupling"""
    dln_mu = 0.01
    alpha = alpha_0
    mu_current = mu_0
    while mu_current < mu:
        beta = beta_qcd(alpha, n_f)
        phi_factor = PHI**(-alpha / alpha_0)
        dalpha = beta * phi_factor * dln_mu
        alpha += dalpha
        mu_current *= math.exp(dln_mu)
    return alpha

def simulate_renormalization():
    print("=== Law 2950: Quantum Field Renormalization Flow ===")
    alpha_0 = 0.1179  # α_s(M_Z)
    M_Z = 91.2  # GeV
    mu_values = [M_Z, 100, 1000, 1e4, 1e6, 1e16]  # GeV
    
    print(f"α_s(M_Z) = {alpha_0}")
    print(f"\n{'μ (GeV)':>10} {'α_s std':>10} {'α_s phi':>10} {'Ratio':>10}")
    
    for mu in mu_values:
        alpha_std = running_coupling_standard(alpha_0, M_Z, mu)
        alpha_phi = running_coupling_phi(alpha_0, M_Z, mu)
        ratio = alpha_phi / alpha_std if alpha_std > 0 else 0
        print(f"{mu:>10.0e} {alpha_std:>10.5f} {alpha_phi:>10.5f} {ratio:>10.4f}")
    
    print(f"\nKey insight: phi-suppression slows coupling running at high energies")
    print(f"At GUT scale: ratio = {running_coupling_phi(alpha_0, M_Z, 1e16)/running_coupling_standard(alpha_0, M_Z, 1e16):.4f}")

if __name__ == "__main__":
    simulate_renormalization()
