import re

# Read the list
with open('doj_305_complete.txt', 'r') as f:
    content = f.read()

# Split by semicolon
names = [name.strip() for name in content.split(';') if name.strip()]

print(f"Total names: {len(names)}")

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

print("\nFirst 10 names:")
for i, name in enumerate(names[:10], 1):
    print(f"{i}. {name}")

print("\nLast 10 names:")
for i, name in enumerate(names[-10:], len(names)-9):
    print(f"{i}. {name}")

print("\nPersons 251-305:")
for i, name in enumerate(names[250:305], 251):
    print(f"{i}. {name}")

# Check which names from batch 5 are in the list
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
for name in batch5_names:
    if name in names:
        idx = names.index(name) + 1
        print(f"  {name}: position {idx}")
    else:
        print(f"  {name}: NOT FOUND")