# Andre Pereira
# Chapter 6
glossary = {
    "string": "A series of characters enclosed in quotes.",
    "comment": "A note in a program that Python ignores, used to explain code.",
    "list": "A collection of items in a particular order.",
    "loop": "Work through a collection of items, one by one.",
    "dictionary": "A collection of key-value pairs.",
}

# Print each word and its meaning with a blank line between them
word = "string"
print(f"{word.title()}:\n\t{glossary[word]}\n")

word = "comment"
print(f"{word.title()}:\n\t{glossary[word]}\n")

word = "list"
print(f"{word.title()}:\n\t{glossary[word]}\n")

word = "loop"
print(f"{word.title()}:\n\t{glossary[word]}\n")

word = "dictionary"
print(f"{word.title()}:\n\t{glossary[word]}\n")