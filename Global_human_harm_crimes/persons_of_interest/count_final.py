import re

# Read the list
with open('final_305_list.txt', 'r') as f:
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
missing = []
for name in batch5_names:
    if name not in names:
        missing.append(name)
        print(f"  {name}: NOT FOUND")

if missing:
    print(f"\nMissing {len(missing)} names from batch 5")
else:
    print("\nAll batch 5 names found in list")