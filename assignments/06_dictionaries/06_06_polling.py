# Andre Pereira
# Chapter 6
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
}

coders_to_poll = ["phil", "josh", "sarah", "david", "jen", "hanna"]

for coder in coders_to_poll:
    if coder in favorite_languages.keys():
        print(f"Thank you for taking the poll, {coder.title()}!")
    else:
        print(f"Hi {coder.title()}, please take our favorite languages poll!")