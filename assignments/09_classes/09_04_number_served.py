# Andre Pereira
# Chapter 9
class Restaurant:

  def __init__(self, restaurant_name, cuisine_type):
    self.restaurant_name = restaurant_name
    self.cuisine_type = cuisine_type
    self.number_served = 0

  def describe_restaurant(self):
    print(
        f"{self.restaurant_name} serves wonderful {self.cuisine_type} cuisine."
    )

  def open_restaurant(self):
    print(f"{self.restaurant_name} is now open!")

  def set_number_served(self, number):
    self.number_served = number

  def increment_number_served(self, count):
    self.number_served += count


restaurant = Restaurant("Bistro Bella", "French")
print(restaurant.number_served)

restaurant.number_served = 15
print(restaurant.number_served)

restaurant.set_number_served(50)
print(restaurant.number_served)

restaurant.increment_number_served(120)
print(restaurant.number_served)