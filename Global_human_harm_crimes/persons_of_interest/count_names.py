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

print(f"Total unique names: {len(unique_names)}")
print("\nFirst 10 names:")
for i, name in enumerate(unique_names[:10], 1):
    print(f"{i}. {name}")

print("\nLast 10 names:")
for i, name in enumerate(unique_names[-10:], len(unique_names)-9):
    print(f"{i}. {name}")

print("\nPersons 251-305:")
for i, name in enumerate(unique_names[250:305], 251):
    print(f"{i}. {name}")