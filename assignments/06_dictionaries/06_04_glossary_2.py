# Andre Pereira
# Chapter 6
glossary = {
    "string": "A series of characters enclosed in quotes.",
    "comment": "A note in a program that Python ignores, used to explain code.",
    "list": "A collection of items in a particular order.",
    "loop": "Work through a collection of items, one by one.",
    "dictionary": "A collection of key-value pairs.",
    "variable": "A label that references a value stored in memory.",
    "integer": "A numerical value without a decimal point.",
    "float": "A numerical value with a decimal point.",
    "boolean": "An expression that evaluates to True or False.",
    "key": "The first part of a key-value pair in a dictionary.",
}

# Loop through the dictionary and print each word, meaning, and a blank line
for word, meaning in glossary.items():
    print(f"{word.title()}:{meaning}")