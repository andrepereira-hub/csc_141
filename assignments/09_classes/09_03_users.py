# Andre Pereira
# Chapter 9
class User:

  def __init__(self, first_name, last_name, username, email, location):
    self.first_name = first_name
    self.last_name = last_name
    self.username = username
    self.email = email
    self.location = location

  def describe_user(self):
    print(f"\nUser Profile: {self.first_name} {self.last_name}")
    print(f"  Username: {self.username}")
    print(f"  Email: {self.email}")
    print(f"  Location: {self.location}")

  def greet_user(self):
    print(f"Hello, {self.first_name}! Welcome back.")


user1 = User("Alice", "Smith", "asmith", "alice@example.com", "New York")
user2 = User("Bob", "Jones", "bjones", "bob@example.com", "Seattle")

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()