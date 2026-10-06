# Andre Pereira
# Chapter 6
people = []

person_1 = {
    "first_name": "ada",
    "last_name": "lovelace",
    "age": 36,
    "city": "london",
}
people.append(person_1)

person_2 = {
    "first_name": "alan",
    "last_name": "turing",
    "age": 41,
    "city": "manchester",
}
people.append(person_2)

person_3 = {
    "first_name": "grace",
    "last_name": "hopper",
    "age": 85,
    "city": "new york",
}
people.append(person_3)

# Loop through the list of people and print everything about them
for person in people:
    full_name = f"{person['first_name']} {person['last_name']}"
    print(f"Name: {full_name.title()}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city'].title()}")