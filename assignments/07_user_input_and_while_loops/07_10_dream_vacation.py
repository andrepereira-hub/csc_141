# Andre Pereira
# Chapter 7
place_prompt = "\nIf you could visit one place in the world, where would you go? "
continue_prompt = "\nwhould you like to let someone else respond? (yes/no) "

destinations = []

repeat = "yes"
while repeat.lower() == "yes":
    place = input(place_prompt)
    destinations.append(place)
    repeat = input(continue_prompt)

print("\n--- Dream Vacation Poll Results ---")
for destination in destinations:
    print(f"- {destination}")  