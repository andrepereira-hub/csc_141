# Andre Pereira
# Chapter 6
cities = {
    "tokyo": {
        "country": "japan",
        "population": "14 million",
        "fact": "It is the most populous metropolitan area in the world.",
        "major_landmark": "Tokyo Tower",
    },
    "paris": {
        "country": "france",
        "population": "2.1 million",
        "fact": "It is famously known as the City of Light.",
        "major_landmark": "Eiffel Tower",
    },
    "cairo": {
        "country": "egypt",
        "population": "10 million",
        "fact": "It is home to the Giza Pyramids.",
        "major_landmark": "Great Pyramid of Giza",
    },
}

print("WORLD CITIES PROFILE")

for city_name, info in cities.items():
    print(f" {city_name.upper()}")
    print(f"• Country:       {info['country'].title()}")
    print(f"• Population:    {info['population']}")
    print(f"• Landmark:      {info['major_landmark']}")
    print(f"• Fun Fact:      {info['fact']}")
    print("-" * 30)