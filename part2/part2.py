# 2.1 The if-else construction as a whole forms a single conditional statement.

number = int(input("Please type in a number: "))

if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

# 2.2 Age of maturity

age = int(input('How old are you?'))

if age < 18:
    print('You are not of age!')
else:
    print('You are of age!')

# 2.3 Alternative branches using the elif statement

goals_home = int(input("Home goals scored: "))
goals_away = int(input("Away goals scored: "))

if goals_home > goals_away:
    print("The home team won!")
elif goals_away > goals_home:
    print("The away team won!")
else:
    print("It's a tie!")

# 2.4 The elder


print('Person 1:')
name = input('Name:')
age = int(input("age"))

print('Person 2:')
name_2= input('Name')
age_2 = int(input('Age'))


if age_2 < age :
    print(f'The elder is {name}')
elif age_2 > age:
    print(f'The elder is {name_2}')
else:
    print(f'{name} and {name_2} are the same age')

# 2.5 Alphabetically last

word_1 = input('Please type in 1st word:')
word_2 = input('Please type in 2nd word:')
if word_1.capitalize()> word_2.capitalize():
    print(f'{word_1} comes alphabetically last')
elif word_1.capitalize()< word_2.capitalize():
    print(f'{word_2} comes alphabetically last')
else:
    print(f'You gave the same word twice.')


