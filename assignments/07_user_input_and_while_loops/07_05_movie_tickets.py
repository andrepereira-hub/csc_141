# Andre Pereira
# Chapter 7

tickets = True
while tickets:
    age_of_person = input('How old are you?: ')
    if age_of_person == 'quit':
        tickets = False
    elif int(age_of_person) < 3:
        print('Your ticket is free.')
    elif int(age_of_person) >= 3 and int(age_of_person) <= 12:
        print('Your ticket is $10.')
    else:
        print('Your ticket is $15.')