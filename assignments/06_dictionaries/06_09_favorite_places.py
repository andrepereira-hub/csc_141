# Andre Pereira
# Chapter 6
favorite_places = {
    "eric": ["tokyo", "kyoto", "osaka"],
    "jen": ["paris", "rome"],
    "sarah": ["yosemite"],
}

for name, places in favorite_places.items():
    print(f"{name.title()}'s favorite places are:")
    for place in places:
        print(f"- {place.title()}")