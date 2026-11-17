# Andre Pereira
# Chapter 9
class Restaurant:

  def __init__(self, restaurant_name, cuisine_type):
    self.restaurant_name = restaurant_name
    self.cuisine_type = cuisine_type

  def describe_restaurant(self):
    print(
        f"{self.restaurant_name} serves wonderful {self.cuisine_type} cuisine."
    )

  def open_restaurant(self):
    print(f"{self.restaurant_name} is now open!")


r1 = Restaurant("Pasta Palace", "Italian")
r2 = Restaurant("Taco Time", "Mexican")
r3 = Restaurant("Sakura", "Japanese")

r1.describe_restaurant()
r2.describe_restaurant()
r3.describe_restaurant()