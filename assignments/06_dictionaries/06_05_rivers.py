# Andre Pereira
# Chapter 6
rivers = {
    "nile": "egypt",
    "amazon": "brazil",
    "yangtze": "china",
}

print("--- River Sentences ---")
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print("--- Rivers Included ---")
for river in rivers.keys():
    print(f"- {river.title()}")

# 3. Print the name of each country
print("--- Countries Included ---")
for country in rivers.values():
    print(f"- {country.title()}")