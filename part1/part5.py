# 1. 
# Thus far, every program we have written has been executed line by line in order.
# Instead of executing every line of code every single time a program is run, it is often useful to create sections of the program which are are only executed in certain situations.
# Example: 

age = int (input('How old are you? '))

if age > 20:
    print('age > 20')
    print('age <20')
print('age = 20')


# 2. Comparison operators

number = int(input("Please type in a number: "))

if number < 0:
    print("The number is negative.")

if number > 0:
    print("The number is positive.")

if number == 0:
    print("The number is zero.")

# 3. Exercise:

# 3.1 Orwell

# Please write a program which asks the user for an integer number. The program should print out "Orwell" if the number is exactly 1984, and otherwise do nothing.

# Sample output
# Please type in a number: 2020

# Sample output
# Please type in a number: 1984
# Orwel

number = int(input('Please type in a number:'))
if number == 1984:
    print('Orwell')

# 3.2 Absolute value

# Please write a program which asks the user for an integer number. If the number is less than zero, the program should print out the number multiplied by -1. Otherwise the program prints out the the number as is. Please have a look at the examples of expected behaviour below.

# Sample output
# Please type in a number: -7
# The absolute value of this number is 7

# Sample output
# Please type in a number: 1
# The absolute value of this number is 1

# Sample output
# Please type in a number: -99
# The absolute value of this number is 99
number = int(input('Please type in a number:'))
ratio = -1
if number < 0:
    print(f'The absolute value of this number is {ratio * number}')
print(f'The absolute value of this number is {number}')


# 3.3 Soup or no soup

# Please write a program which asks for the user's name. If the name is anything but "Jerry", the program then asks for the number of portions and prints out the total cost. The price of a single portion is 5.90.

# Two examples of the program's execution:

# Sample output
# Please tell me your name: Kramer
# How many portions of soup? 2
# The total cost is 11.8
# Next please!

# Sample output
# Please tell me your name: Jerry
# Next please!
