# Andre Pereira
# Chapter 5
current_users = ['eric', 'admin', 'john', 'sarah', 'jessica']
new_users = ['JOHN', 'rachel', 'david', 'eric', 'michael']

# Create a lowercase list of current users for case-insensitive checks
current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry, the username '{new_user}' is already taken. Please enter a new username.")
    else:
        print(f"Great! The username '{new_user}' is available.")