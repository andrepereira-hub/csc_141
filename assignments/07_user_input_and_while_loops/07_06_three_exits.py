# Andre Pereira
# Chapter 7
toppings = ""
print("Enter 'quit' to exit the program.")
while toppings != 'quit':
    toppings = input("What topping would you like on your pizza? ")
    if toppings != 'quit':
        toppings = input(f"Adding {toppings} to your pizza.")