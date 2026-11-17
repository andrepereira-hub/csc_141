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
    print(f"\nUser: {self.first_name} {self.last_name} ({self.username})")

  def greet_user(self):
    print(f"Hello, {self.first_name}!")


class Privileges:

  def __init__(self):
    self.privileges = ["can add post", "can delete post", "can ban user"]

  def show_privileges(self):
    print("Administrator Privileges:")
    for privilege in self.privileges:
      print(f"- {privilege}")


class Admin(User):

  def __init__(self, first_name, last_name, username, email, location):
    super().__init__(first_name, last_name, username, email, location)
    self.privileges = Privileges()


admin_user = Admin("Sarah", "Connor", "sconnor", "sarah@skynet.com", "LA")
admin_user.describe_user()
admin_user.privileges.show_privileges()