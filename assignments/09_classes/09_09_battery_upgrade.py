# Andre Pereira
# Chapter 9
class Car:

  def __init__(self, manufacturer, model, year):
    self.manufacturer = manufacturer
    self.model = model
    self.year = year


class Battery:

  def __init__(self, battery_size=40):
    self.battery_size = battery_size

  def get_range(self):
    if self.battery_size == 40:
      return 150
    elif self.battery_size == 65:
      return 225

  def upgrade_battery(self):
    if self.battery_size != 65:
      self.battery_size = 65


class ElectricCar(Car):

  def __init__(self, manufacturer, model, year):
    super().__init__(manufacturer, model, year)
    self.battery = Battery()


my_leaf = ElectricCar("nissan", "leaf", 2024)
print(my_leaf.battery.get_range())
my_leaf.battery.upgrade_battery()
print(my_leaf.battery.get_range())