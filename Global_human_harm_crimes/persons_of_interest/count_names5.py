import re

# Read the list
with open('doj_305_complete.txt', 'r') as f:
    content = f.read()

# Split by semicolon
names = [name.strip() for name in content.split(';') if name.strip()]

print(f"Total names: {len(names)}")

# Add missing names from batch 5
missing_names = [
    "Reno, Janet",
    "Rubensetin/Rubenstein, Howard",
    "Ruemmier, Kathy",
    "Schlaf, Martin",
    "Shapper, Gretchen"
]

# Check if these names are already in the list with different spellings
for missing in missing_names:
    found = False
    for name in names:
        if missing.split(',')[0] in name:
            print(f"Found similar: {missing} -> {name}")
            found = True
            break
    if not found:
        print(f"Not found: {missing}")
        names.append(missing)

print(f"\nTotal names after adding missing: {len(names)}")

# Sort alphabetically by last name
def get_last_name(name):
    # Handle "Jr." and "III" suffixes
    name = re.sub(r'\s+(Jr\.|III|II|IV)$', '', name)
    # Get last name
    parts = name.split(',')
    if len(parts) >= 2:
        return parts[0].strip()
    return name

names.sort(key=get_last_name)

print("\nPersons 251-305:")
for i, name in enumerate(names[250:305], 251):
    print(f"{i}. {name}")