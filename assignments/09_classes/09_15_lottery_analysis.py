# Andre Pereira
# Chapter 9
from random import choice

possibilities = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "a", "b", "c", "d", "e")
my_ticket = [7, 2, "a", "e"]
pulls = 0
won = False

while not won:
  drawn = []
  while len(drawn) < 4:
    item = choice(possibilities)
    if item not in drawn:
      drawn.append(item)
  pulls += 1
  if set(drawn) == set(my_ticket):
    won = True

print(pulls)