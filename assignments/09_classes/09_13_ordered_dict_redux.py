# Andre Pereira
# Chapter 9
from random import randint


class Die:

  def __init__(self, sides=6):
    self.sides = sides

  def roll_die(self):
    return randint(1, self.sides)


six_sided = Die()
print([six_sided.roll_die() for _ in range(10)])

ten_sided = Die(10)
print([ten_sided.roll_die() for _ in range(10)])

twenty_sided = Die(20)
print([twenty_sided.roll_die() for _ in range(10)])