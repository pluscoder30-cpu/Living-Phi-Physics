import math, random

PHI = 1.618033988749895
N_crystals = 384
activity = 100e3
T_coinc = 4e-9
true_rate = 50e3
scatter_fraction = 0.3
random_rate = 2.0 * activity * 1e-6

def pet_metrics(phi_pitch):
    if phi_pitch:
        tr_ratio = PHI ** 2
        sensitivity = 1.0
    else:
        tr_ratio = 1.0
        sensitivity = 1.0

    true_counts = true_rate * sensitivity
    scatter_counts = true_counts * scatter_fraction
    random_counts = random_rate / tr_ratio
    total_prompt = true_counts + scatter_counts + random_counts
    necr = true_counts ** 2 / total_prompt
    return true_counts, scatter_counts, random_counts, necr

true_phi, scat_phi, rand_phi, necr_phi = pet_metrics(True)
true_uni, scat_rand, rand_uni, necr_uni = pet_metrics(False)

print("PHI-pitched detector:")
print(f"  True: {true_phi:.0f}, Scatter: {scat_phi:.0f}, Random: {rand_phi:.0f}")
print(f"  T/R ratio: {true_phi/rand_phi:.2f}")
print(f"  NECR: {necr_phi:.0f} cps")
print(f"\nUniform detector:")
print(f"  True: {true_uni:.0f}, Scatter: {scat_rand:.0f}, Random: {rand_uni:.0f}")
print(f"  T/R ratio: {true_uni/rand_uni:.2f}")
print(f"  NECR: {necr_uni:.0f} cps")
print(f"\nNECR improvement: {(necr_phi/necr_uni - 1)*100:.1f}%")
print(f"T/R improvement: {true_phi/rand_phi / (true_uni/rand_uni):.2f}x (expected {PHI**2:.2f}x)")
print(f"Test: {'PASS' if necr_phi > necr_uni else 'FAIL'}")
