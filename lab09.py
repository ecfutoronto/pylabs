import json

with open('countries1.json', encoding="utf-8") as data_file:
    countries = json.load(data_file)

print(f"Read {len(countries)} countries from the JSON file.")

# Question 1
letters_table = {}
for country in countries:
    countryName = country["Name"]
    for char in countryName:
        # Do not double count upper case and lower case
        char = char.lower()
        # Ignore anything that is not an alphabetical character
        if char >= 'a' and char <= 'z':
            letters_table[char] = letters_table.get(char, 0) + 1
    
print("\nHere are the occurrences for each alphabetical character:")
for char in sorted(letters_table.keys(), key=(lambda x: letters_table[x]), reverse = True):
    print(f"{char} occurs {letters_table[char]} times.")

# Question 2
countries_area = {}

for country in countries:
    population = int(country["Population"].split(" ")[0])
    area = int(country["Area"].split(" ")[0])
    countryName = country["Name"]
    countries_area[countryName] = countries_area.get(countryName, 0) + area
      
print("\nHere are the areas of countries around the world:")
for country in sorted(countries_area.keys(), key=(lambda x: countries_area[x]), reverse = True)[:20]:
    print(f"{country} has an area of {countries_area[country]} kilometers squared.")

# Question 3
countries_density = {}

for country in countries:
    population = int(country["Population"].split(" ")[0])
    area = int(country["Area"].split(" ")[0])
    if area == 0:
        area = 1
    countryName = country["Name"]
    countries_density[countryName] = countries_density.get(countryName, 0) + int(population/area)
      
print("\nHere are the areas of countries around the world:")
for country in sorted(countries_density.keys(), key=(lambda x: countries_density[x]), reverse = True)[:20]:
    print(f"{country} has a population density of {countries_density[country]} per kilometers squared.")

# Question 4

with open('mountains1.json', encoding="utf-8") as data_file:
    mountains = json.load(data_file)

print(f"\nRead {len(mountains)} mountains from the JSON file.")
print("JSON data file generated from Wolfram Mathematica.")

mic = {}
tallest = {}
smallest = ('Molehill', 0)

for mountain in mountains:
    if mountain['ClimbingDifficulty'] == 'Walk Up':
        for country in mountain['Countries']:
            mic[country] = mic.get(country, []) + [mountain['Name']]
            t = tallest.get(country, smallest)
            try:
                e = int(mountain['Elevation'].split(' ')[0])
            except ValueError:
                e = 0
            if e > t[1]:
                tallest[country] = (mountain['Name'], e)
    else: 
        continue

print("\nHere are top twenty countries sorted by their tallest mountains:")

countries = sorted(countries, key = (lambda x: tallest.get(x['Name'], smallest)[1]), reverse = True)
for i in range(20):
    c = countries[i]['Name']
    t = tallest[c]
    print(f'{i+1:2}. {c} with {t[0]}, elevation {t[1]} m.')