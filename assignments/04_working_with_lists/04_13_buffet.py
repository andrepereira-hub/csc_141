# Andre Pereira
# Chapter 4
buffet_foods = ('pizza', 'pasta', 'salad', 'soup', 'breadsticks')

print("Original menu;")
for food in buffet_foods:
    print(f"-{food}")

#try to modify one of the items (causes error)
#buffet_foods[0] = "ice cream" (commented out to avoid error)

buffet_foods = ('pizza', 'pasta', 'salad', 'soup', 'breadsticks')

print("\nModified menu:")
for food in buffet_foods:
    print(f"-{food}")