# Andre Pereira
# Chapter 3
guests = ["Leonardo da Vinci", "Ada Lovelace", "Maya Angelou"]
print("Great news! I found a bigger dinner table, so more space is available.\n")
guests.insert(0, "Marie Curie")
guests.insert(2, "Socrates")
guests.append("Alan Turing")
for guest in guests:
    print(f"Dear {guest}, it would be an honor to have you join me for dinner tonight.")