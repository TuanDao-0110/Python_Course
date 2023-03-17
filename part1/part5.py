from math import sqrt

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

name = input('Please tell me your name:')
if name == 'Jerry':
    print('Next Please')
else: 
    portions = int(input('How many portions of soup?'))
    single_portion = 5.9
    sum = float(single_portion * portions)
    print(f'The Total Cost is {sum}')
    print('Next please')
# 3.4 Order of magnitude

# Please write a program which asks the user for an integer number. The program should then print out the magnitude of the number according to the following examples.

# Sample output
# Please type in a number: 950
# This number is smaller than 1000
# Thank you!

# Sample output
# Please type in a number: 59
# This number is smaller than 1000
# This number is smaller than 100
# Thank you!

# Sample output
# Please type in a number: 2
# This number is smaller than 1000
# This number is smaller than 100
# This number is smaller than 10
# Thank you!

# Sample output
# Please type in a number: 1123
# Thank you!

number = int(input('Please type in number:'))
if number<1000:
    print(f'This number is smaller than 1000')
if number < 100:
    print(f'This number is smaller than 100')
if number <10:
    print(f'This number is smaller than 10')
else:
    print
print('Thank you!')
# 3.5 Calculator: 

# Please write a program which asks the user for two numbers and an operation. If the operation is add, multiply or subtract, the program should calculate and print out the result of the operation with the given numbers. If the user types in anything else, the program should print out nothing.

# Some examples of expected behaviour:

# Sample output
# Number 1: 10
# Number 2: 17
# Operation: add

# 10 + 17 = 27

# Sample output
# Number 1: 4
# Number 2: 6
# Operation: multiply

# 4 * 6 = 24

# Sample output
# Number 1: 4
# Number 2: 6
# Operation: subtract

# 4 - 6 = -2

number_1 = int(input('Number 1:'))
number_2 = int(input('Number 2:'))
operation = input('Operation')

if operation == 'add':
    print(f'{number_1} + {number_2} = {number_1 + number_2}')
if operation == 'multiply':
    print(f'{number_1} * {number_2} = {number_1 * number_2}')
if operation == 'subtract':
    print(f'{number_1} - {number_2} = {number_1 - number_2}')

# 3.6 Temperatures


# Please write a program which asks the user for a temperature in degrees Fahrenheit, and then prints out the same in degrees Celsius. If the converted temperature falls below zero degrees Celsius, the program should also print out "Brr! It's cold in here!".

# The formula for converting degrees Fahrenheit to degrees Celsius can be found easily by any search engine of your choice.

# Two examples of expected behaviour:

# Sample output
# Please type in a temperature (F): 101
# 101 degrees Fahrenheit equals 38.333333333333336 degrees Celsius

# Please type in a temperature (F): 21
# 21 degrees Fahrenheit equals -6.111111111111111 degrees Celsius
# Brr! It's cold in here!

temperature = int(input('Please types in a tempertature (F):'))
celsius = float((temperature -32) * (5/9))
if celsius >= 0: 
    print(f'{temperature} degrees Fahrenheit equals {celsius} degrees Celsius')
if celsius <0:
    print(f"{temperature} degrees Fahrenheit equals {celsius} degrees Celsius")
    print("Brr! It's cold in here!")


# 3.6 Daily wages


# Please write a program which asks for the hourly wage, hours worked, and the day of the week. The program should then print out the daily wages, which equal hourly wage multiplied by hours worked, except on Sundays when the hourly wage is doubled.

# Sample output
# Hourly wage: 8.5
# Hours worked: 3
# Day of the week: Monday
# Daily wages: 25.5 euros

# Sample output
# Hourly wage: 12.5
# Hours worked: 10
# Day of the week: Sunday
# Daily wages: 250.0 euros

# Write your solution here

wage = float(input('Hourly wage:'))
work = int(input('Hours worked:'))
days = input('Day of the week:')
ratio = 1
sum = wage * work *ratio
if days =='Sunday':
    print(f'Daily wages: {sum *2} euros')
else:
    print(f'Daily wages: {sum} euros')

# 3.7 Loyalty bonus

# This program calculates the end of year bonus a customer receives on their loyalty card. The bonus is calculated with the following formula:

# If there are less than a hundred points on the card, the bonus is 10 %
# In any other case the bonus is 15 %
# The program should work like this:
# The program should work like this:

# Sample output
# How many points are on your card? 55
# Your bonus is 10 %
# You now have 60.5 points

# But there is a problem with the program, so with some inputs it doesn't work quite right:

# Sample output
# How many points are on your card? 95
# Your bonus is 10 %
# Your bonus is 15 %
# You now have 120.175 points

# Fix the program
points = int(input("How many points are on your card? "))
addpoint = points
if points < 100:
    addpoint *= 1.1
    print("Your bonus is 10 %")
if points >=100:
    addpoint *= 1.15
    print("Your bonus is 15 %")

print("You now have", points, "points")


# 3.8 What to wear tomorrow

# Please write a program which asks for tomorrow's weather forecast and then suggests weather-appropriate clothing.

# The suggestion should change if the temperature (measured in degrees Celsius) is over 20, 10 or 5 degrees, and also if there is rain on the radar.

# Some examples of expected behaviour:

# Sample output
# What is the weather forecast for tomorrow?
# Temperature: 21
# Will it rain (yes/no): no
# Wear jeans and a T-shirt

# Sample output
# What is the weather forecast for tomorrow?
# Temperature: 11
# Will it rain (yes/no): no
# Wear jeans and a T-shirt
# I recommend a jumper as well

# Sample output
# What is the weather forecast for tomorrow?
# Temperature: 7
# Will it rain (yes/no): no
# Wear jeans and a T-shirt
# I recommend a jumper as well
# Take a jacket with you

# Sample output
# What is the weather forecast for tomorrow?
# Temperature: 3
# Will it rain (yes/no): yes
# Wear jeans and a T-shirt
# I recommend a jumper as well
# Take a jacket with you
# Make it a warm coat, actually
# I think gloves are in order
# Don't forget your umbrella

print("What is the weather forecast for tomorrow?")
temperature = int(input("Temperature: "))
rain = input("Will it rain (yes/no): ")

if temperature > 20 and rain == "no":
    print("Wear shorts and a T-shirt")
elif temperature > 20 and rain == "yes":
    print("Wear shorts and a T-shirt with a raincoat")
elif 10 <= temperature <= 20 and rain == "no":
    print("Wear jeans and a T-shirt")
elif 10 <= temperature <= 20 and rain == "yes":
    print("Wear jeans and a T-shirt with a raincoat")
elif 5 <= temperature < 10 and rain == "no":
    print("Wear a sweater or a hoodie")
elif 5 <= temperature < 10 and rain == "yes":
    print("Wear a sweater or a hoodie with a raincoat")
elif temperature < 5 and rain == "no":
    print("Wear a jacket or a coat")
else:
    print("Wear a jacket or a coat with a raincoat")
    print("Also wear gloves and don't forget your umbrella!")

# 3.8 Solving a quadratic equation
# Sample output
# Value of a: 1
# Value of b: 2
# Value of c: -8

# The roots are 2.0 and -4.0



