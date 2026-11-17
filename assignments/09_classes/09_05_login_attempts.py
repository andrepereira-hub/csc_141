# Andre Pereira
# Chapter 9
class User:

  def __init__(self, first_name, last_name, username, email, location):
    self.first_name = first_name
    self.last_name = last_name
    self.username = username
    self.email = email
    self.location = location
    self.login_attempts = 0

  def describe_user(self):
    print(f"\nUser Profile: {self.first_name} {self.last_name}")

  def greet_user(self):
    print(f"Hello, {self.first_name}!")

  def increment_login_attempts(self):
    self.login_attempts += 1

  def reset_login_attempts(self):
    self.login_attempts = 0


user1 = User("Alice", "Smith", "asmith", "alice@example.com", "New York")
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(user1.login_attempts)

user1.reset_login_attempts()
print(user1.login_attempts)