"""
16_LADDER_INVARIANT_PROOF.py
Verifies: 528 x phi^n x phi^(9-n) = 528 x phi^9 = 40,134.946 for all n = 0..9
Author: Christopher David Ayotte
"""

from decimal import Decimal, getcontext
import sys
import io

# Force UTF-8 output on Windows
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Set precision to 50 decimal places
getcontext().prec = 50

# Golden ratio to 50 digits
PHI = Decimal(1 + 5**0.5) / 2

# Known value of 528 x phi^9 to compare against
KNOWN_VALUE = Decimal('40134.946')

print("=" * 72)
print("LADDER INVARIANT PROOF")
print("528 x phi^n x phi^(9-n) = 528 x phi^9 for all n = 0, 1, ..., 9")
print("=" * 72)

# Step 1: Compute 528 x phi^9 to maximum precision
phi_9 = PHI ** 9
target = 528 * phi_9

print(f"\nGolden ratio phi = {PHI}")
print(f"phi^9 = {phi_9}")
print(f"528 x phi^9 = {target}")
print(f"Known value = {KNOWN_VALUE}")
print(f"Difference = {abs(target - KNOWN_VALUE)}")

# Step 2: Verify for every n from 0 to 9
print(f"\n{'n':>3} | {'phi^n x phi^(9-n)':>20} | {'528 x product':>20} | {'Delta from target':>15} | {'Match':>6}")
print("-" * 72)

all_match = True
for n in range(10):
    phi_n = PHI ** n
    phi_9_minus_n = PHI ** (9 - n)
    product = phi_n * phi_9_minus_n
    full = 528 * product
    delta = abs(full - target)
    match = delta < Decimal('0.001')

    print(
        f"{n:>3} | {product:>20.10f} | {full:>20.10f} | {delta:>15.12f} | {'PASS' if match else 'FAIL':>6}"
    )

    if not match:
        all_match = False

# Step 3: Show exponent arithmetic invariance
print(f"\n{'-' * 72}")
print("EXPONENT ARITHMETIC PROOF:")
print(f"  For every n: phi^n x phi^(9-n) = phi^(n + 9 - n) = phi^9 = {phi_9}")
print(f"  Therefore: 528 x phi^n x phi^(9-n) = 528 x phi^9 = {target}")
print(f"  The product is INDEPENDENT of n.")

# Step 4: Verify against known value to 10 decimal places
print(f"\n{'-' * 72}")
print(f"KNOWN VALUE COMPARISON:")
print(f"  Computed : {target}")
print(f"  Known    : {KNOWN_VALUE}")
print(f"  Delta    : {abs(target - KNOWN_VALUE)}")
print(f"  Match to 10 decimal places: {abs(target - KNOWN_VALUE) < Decimal('0.0000000001')}")

# Step 5: Final verdict
print(f"\n{'=' * 72}")
if all_match:
    print("LADDER INVARIANT VERIFIED: 528 x phi^n x phi^(9-n) = 528 x phi^9 for all n in {0,...,9}")
else:
    print("FAILURE: Invariant broken for some n")
print(f"{'=' * 72}")
