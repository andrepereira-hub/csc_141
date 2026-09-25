# Andre Pereira
# Chapter 3
guests = [
    "Marie Curie",
    "Leonardo da Vinci",
    "Socrates",
    "Ada Lovelace",
    "Maya Angelou",
    "Alan Turing",
]

print(
    "Unfortunately, the new dinner table won't arrive in time, so I can only invite two people for dinner.\n"
)

uninvited_guest = guests.pop()
print(
    f"Dear {uninvited_guest}, I'm so sorry, but I can no longer invite you to dinner."
)

uninvited_guest = guests.pop()
print(
    f"Dear {uninvited_guest}, I'm so sorry, but I can no longer invite you to dinner."
)

uninvited_guest = guests.pop()
print(
    f"Dear {uninvited_guest}, I'm so sorry, but I can no longer invite you to dinner."
)

uninvited_guest = guests.pop()
print(
    f"Dear {uninvited_guest}, I'm so sorry, but I can no longer invite you to dinner.\n"
)

for guest in guests:
    print(
        f"Dear {guest}, you are still invited to dinner! I look forward to seeing you."
    )

del guests[0]
del guests[0]
print("\nFinal guest list:", guests)