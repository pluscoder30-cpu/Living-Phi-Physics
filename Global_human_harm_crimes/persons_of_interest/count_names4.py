import re

# Read the list
with open('doj_305_complete.txt', 'r') as f:
    content = f.read()

# Split by semicolon
names = [name.strip() for name in content.split(';') if name.strip()]

print(f"Total names: {len(names)}")

# Check for duplicates
from collections import Counter
name_counts = Counter(names)
duplicates = {name: count for name, count in name_counts.items() if count > 1}
if duplicates:
    print("\nDuplicates found:")
    for name, count in duplicates.items():
        print(f"  {name}: {count} times")

# Check for names that might be missing
# From batch 5, we know these names should be in the list
batch5_names = [
    "Reagan, Ronald", "Readler, Chad", "Recarey, Joseph", "Reiter, Michael",
    "Reno, Janet", "Reynolds, Tom", "Rice, Susan", "Richardson, Bill",
    "Rohrabach, Andrew", "Romney, Mitt", "Rosen, Jeffrey", "Rosenstein, Rod",
    "Ross, Diana", "Rossmiller, Alexander", "Roth, John", "Routh, Timothy",
    "Rowan, Marc", "Rove, Karl", "Rubenstein, Howard", "Rubio, Marco",
    "Ruemmler, Kathryn", "Ryan, Paul", "Salinger, Pierre", "Sasse, Ben",
    "Scanlon, Mary Gay", "Scarola, John", "Schenberg, Janis", "Schlaff, Martin",
    "Schiff, Adam", "Schwarzman, Stephen", "Schumer, Amy", "Schumer, Chuck",
    "Scott, Tim", "Sekulow, Jay", "Senatore, Adrienne", "Sessions, Jeff",
    "Shamir, Yitzhak", "Shapiro, Ben", "Shappert, Gretchen", "Shea, Timothy",
    "Siad, Daniel", "Soros, Alex", "Soros, George", "Spacey, Kevin",
    "Spitzer, Eliot", "Springsteen, Bruce", "Stabenow, Debbie", "Staley, Jes"
]

print("\nChecking batch 5 names in list:")
missing = []
for name in batch5_names:
    if name not in names:
        missing.append(name)
        print(f"  {name}: NOT FOUND")

if missing:
    print(f"\nMissing {len(missing)} names from batch 5")
else:
    print("\nAll batch 5 names found in list")