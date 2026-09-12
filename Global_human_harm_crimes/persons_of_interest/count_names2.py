import re

# Read the list
with open('doj_305_list.txt', 'r') as f:
    content = f.read()

# Split into categories
categories = content.split('\n\n')

all_names = []

for category in categories:
    if category.strip():
        # Get category name (first line)
        lines = category.strip().split('\n')
        if len(lines) > 1:
            # Get names from second line
            names_str = lines[1]
            # Split by semicolon
            names = [name.strip() for name in names_str.split(';') if name.strip()]
            all_names.extend(names)

print(f"Total names before dedup: {len(all_names)}")

# Check for duplicates
from collections import Counter
name_counts = Counter(all_names)
duplicates = {name: count for name, count in name_counts.items() if count > 1}
if duplicates:
    print("\nDuplicates found:")
    for name, count in duplicates.items():
        print(f"  {name}: {count} times")

# Remove duplicates while preserving order
seen = set()
unique_names = []
for name in all_names:
    if name not in seen:
        seen.add(name)
        unique_names.append(name)

# Sort alphabetically by last name
def get_last_name(name):
    # Handle "Jr." and "III" suffixes
    name = re.sub(r'\s+(Jr\.|III|II|IV)$', '', name)
    # Get last name
    parts = name.split(',')
    if len(parts) >= 2:
        return parts[0].strip()
    return name

unique_names.sort(key=get_last_name)

print(f"\nTotal unique names: {len(unique_names)}")
print("\nPersons 251-305:")
for i, name in enumerate(unique_names[250:305], 251):
    print(f"{i}. {name}")

# Check which names from batch 5 are in the list
batch5_names = [
    "Reagan, Ronald", "Readler, Chad", "Recarey, Joseph", "Reiter, Michael",
    "Reno, Janet", "Reynolds, Tom", "Rice, Susan", "Richardson, Bill",
    "Rohrabach, Andrew", "Romney, Mitt", "Rosen, Jeffrey", "Rosenstein, Rod",
    "Ross, Diana", "Rossmiller, Alexander", "Roth, John", "Routch, Timothy",
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
for name in batch5_names:
    if name in unique_names:
        idx = unique_names.index(name) + 1
        print(f"  {name}: position {idx}")
    else:
        print(f"  {name}: NOT FOUND")