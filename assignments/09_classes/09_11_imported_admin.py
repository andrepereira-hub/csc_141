# Andre Pereira
# Chapter 9
# admin_module.py
class User:

  def __init__(self, first_name, last_name, username, email, location):
    self.first_name = first_name
    self.last_name = last_name
    self.username = username
    self.email = email
    self.location = location


class Privileges:

  def __init__(self):
    self.privileges = ["can add post", "can delete post"]

  def show_privileges(self):
    for p in self.privileges:
      print(f"- {p}")


class Admin(User):

  def __init__(self, first_name, last_name, username, email, location):
    super().__init__(first_name, last_name, username, email, location)
    self.privileges = Privileges()


# my_admin.py
from admin_module import Admin

admin = Admin("John", "Doe", "jdoe", "john@example.com", "NYC")
admin.privileges.show_privileges()