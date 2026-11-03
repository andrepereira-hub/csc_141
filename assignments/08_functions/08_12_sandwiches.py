# Andre Pereira
# Chapter 8
def make_sandwich(*items):
    print("Making a sandwich with the following items:")
    for item in items:
        print(f"- {item}")

make_sandwich("cheese", "ham")
make_sandwich("turkey", "lettuce", "tomato")
make_sandwich("peanut butter", "jelly")