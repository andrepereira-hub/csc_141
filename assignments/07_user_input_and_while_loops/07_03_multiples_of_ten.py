# Andre Pereira
# Chapter 7

while True:
    chosen_number = input('What is your chosen number?: ')
    yes_or_no = int(chosen_number) % 10
    if yes_or_no == 0:
        print (f'{chosen_number} is a multiple of 10.')
    else:
        print (f'{chosen_number} is not a multiple of 10.')