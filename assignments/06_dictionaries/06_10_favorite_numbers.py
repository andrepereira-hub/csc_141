# Andre Pereira
# Chapter 6
favorite_numbers = {
    "alice": [42, 7],
    "bob": [13, 21, 99],
    "charlie": [8],
    "diana": [3, 11, 24],
    "eric": [50, 100],
}

for name, numbers in favorite_numbers.items():
    print(f"{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"{number}")