# Andre Pereira
# Chapter 7
sandwich_orders = [
    'tuna',
    'pastrami', 
    'turkey', 
    'pastrami', 
    'veggie', 
    'pastrami'
    'grilled cheese'
]
finished_sandwiches = []

print("sorry, we are out of pastrami today.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"I'm working on your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nAll of these sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich} sandwich")