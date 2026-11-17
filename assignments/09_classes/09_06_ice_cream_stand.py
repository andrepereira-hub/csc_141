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


class IceCreamStand(Restaurant):

  def __init__(self, restaurant_name, cuisine_type="Ice Cream"):
    super().__init__(restaurant_name, cuisine_type)
    self.flavors = ["Vanilla", "Chocolate", "Mint Chocolate Chip", "Strawberry"]

  def display_flavors(self):
    print("Available flavors:")
    for flavor in self.flavors:
      print(f"- {flavor}")


ice_cream_shop = IceCreamStand("Scoops & Smiles")
ice_cream_shop.describe_restaurant()
ice_cream_shop.display_flavors()