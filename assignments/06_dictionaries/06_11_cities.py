# Andre Pereira
# Chapter 6
cities = {
    "tokyo": {
        "country": "japan",
        "population": "14 million",
        "fact": "It is the most populous metropolitan area in the world.",
    },
    "paris": {
        "country": "france",
        "population": "2.1 million",
        "fact": "It is famously known as the City of Light.",
    },
    "cairo": {
        "country": "egypt",
        "population": "10 million",
        "fact": "It is home to the last remaining of the Seven Wonders of the Ancient World.",
    },
}

for city_name, city_info in cities.items():
    print(f"City: {city_name.title()}")
    print(f"Country: {city_info['country'].title()}")
    print(f"Population: {city_info['population']}")
    print(f"Fact: {city_info['fact']}")