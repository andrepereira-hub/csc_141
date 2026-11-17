# Andre Pereira
# Chapter 9
from random import choice

possibilities = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "a", "b", "c", "d", "e")

winning_ticket = []
while len(winning_ticket) < 4:
  item = choice(possibilities)
  if item not in winning_ticket:
    winning_ticket.append(item)

print(winning_ticket)