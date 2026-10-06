# Andre Pereira
# Chapter 6
pet_1 = {"kind": "dog", "owner": "sarah"}
pet_2 = {"kind": "cat", "owner": "john"}
pet_3 = {"kind": "parrot", "owner": "elena"}
pet_4 = {"kind": "turtle", "owner": "michael"}

pets = [pet_1, pet_2, pet_3, pet_4]

for pet in pets:
    print(f"Animal: {pet['kind'].title()}")
    print(f"Owner: {pet['owner'].title()}")