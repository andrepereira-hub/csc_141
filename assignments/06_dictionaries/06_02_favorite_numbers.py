# Andre Pereira
# Chapter 6
favorite_numbers = {
    "alice": 42,
    "bob": 7,
    "charlie": 13,
    "diana": 24,
    "eric": 99,
}

# Loop through the dictionary and print each person's name and favorite number
for name, number in favorite_numbers.items():
    print(f"{name.title()}'s favorite number is {number}.")