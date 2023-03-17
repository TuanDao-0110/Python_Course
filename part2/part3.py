# 1. Logical oprators: 


# 1.1 You can combine conditions with the logical operators and and or.

#  Example:
number = int(input("Please type in a number: "))
if number >= 5 and number <= 8:
    print("The number is between 5 and 8")

# or: 

number = int(input("Please type in a number: "))
if number >= 5 or number <= 8:
    print("The number is between 5 and 8")

# 1.2 if not: 

number = int(input("Please type in a number: "))
if not (number >= 5 and number <= 8):
    print("The number is not within the range of 5 to 8")

# 1.3 Combining and chaining conditions
n1 = int(input("Number 1: "))
n2 = int(input("Number 2: "))
n3 = int(input("Number 3: "))
n4 = int(input("Number 4: "))

if n1 > n2 and n1 > n3 and n1 > n4:
    greatest = n1
elif n2 > n3 and n2 > n4:
    greatest = n2
elif n3 > n4:
    greatest = n3
else:
    greatest = n4

print(f" {greatest} is the greatest of the numbers.")

# 1.4 Age check

age = int(input("What is your age?"))
if age>=5:
    print(f"Ok, you're {age} years old")
elif age<5 and age>=0:
    print(f"I suspect you can't write quite yet...")
else:
    print('That must eb a mistake')


# 1.5 Nephews

name = input('Please type in your name:')
if name == 'Morty' or name =='Ferdie': 
    print(f"I think you might be one of Mickey Mouse's nephews.")
elif name =='Huey' or name== 'Dewey' or name=='Louie':
    print(f"I think you might be one of Donald Duck's nephews.")
else:
    print(f"You're not a nephew of any character I know of.")

# 1.6 Grades and points
# The table below outlines the grade boundaries on a certain university course. Please write a program which asks for the amount of points received and then prints out the grade attained according to the table.

# points	grade
# < 0	impossible!
# 0-49	fail
# 50-59	1
# 60-69	2
# 70-79	3
# 80-89	4
# 90-100	5
# > 100	impossible!
points = float(input("Enter the points received: "))

if points < 0 or points > 100:
    print("impossible!")
elif points >= 90:
    print("Grade: 5")
elif points >= 80:
    print("Grade: 4")
elif points >= 70:
    print("Grade: 3")
elif points >= 60:
    print("Grade: 2")
elif points >= 50:
    print("Grade: 1")
else:
    print("Grade: fail")



# 1.7 FizzBuzz


number = int(input('Number:'))
if number % 3 == 0 and number % 5 ==0:
    print('FizzBuzz')
elif number % 5 ==0:
    print('Buzz')
elif number % 3 ==0 :
    print('Fizz')

# 1.8 nested conditionals: 

number = int(input("Please type in a number: "))

if number > 0:
    if number % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")
else:
    print("The number is negative or zero")


# 1.9 Leap year
# Generally, any year that is divisible by four is a leap year. 
# However, if the year is additionally divisible by 100, 
# it is a leap year only if it also divisible by 400.

# Please write a program which asks the user for a year, 
# and then prints out whether that year is a leap year or not.

# Some examples:

# Sample output
# Please type in a year: 2011
# That year is not a leap year.

# Sample output
# Please type in a year: 2020
# That year is a leap year.

# Sample output
# Please type in a year: 1800
# That year is not a leap year.

year = int(input("Enter a year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year, "is a leap year")
        else:
            print(year, "is not a leap year")
    else:
        print(year, "is a leap year")
else:
    print(year, "is not a leap year")



# 1.8 Alphabetically in the middle

letter1 = input("1st letter: ")
letter2 = input("2nd letter: ")
letter3 = input("3rd letter: ")

letters = [letter1, letter2, letter3]  # Store the letters in a list
letters.sort()  # Sort the letters in alphabetical order

print("The letter in the middle is", letters[1])  # Print the middle letter (index 1)

# 1.9 Gift tax calculator

# Some say paying taxes makes Finns happy, so let's see if the secret of happiness lies in one of the taxes set out in Finnish tax code.

# According to the Finnish Tax Administration, a gift is a transfer of property to another person against no compensation or payment. If the total value of the gifts you receive from the same donor in the course of 3 years is €5,000 or more, you must pay gift tax.

# When the gift is received from a close relative or a family member, the amount of tax to be paid is determined by the following table, which is also available on this website:

# Value of gift	Tax at the lower limit	Tax rate for the exceeding part (%)
# 5 000 — 25 000	100	8
# 25 000 — 55 000	1 700	10
# 55 000 — 200 000	4 700	12
# 200 000 — 1 000 000	22 100	15
# 1 000 000 —	142 100	17
# So, for a gift of 6 000 euros the recipient pays a tax of 180 euros (100 + (6 000 - 5 000) * 0.08). Similarly, for a gift of 75 000 euros the recipient pays a tax of 7 100 euros (4 700 + (75 000 - 55 000) * 0.12).

# Please write a program which calculates the correct amount of tax for a gift from a close relative. Have a look at the examples below to see what is expected. Notice the lack of thousands separators in the input values - you may assume there will be no spaces or other thousands separators in the numbers in the input, as we haven't yet covered dealing with these.

# Write your solution here

value = int(input("Value of the gift: "))  # Get the value of the gift from the user

if value < 5000:
    tax = 0  # No tax for gifts under 5000 euros
    print(f'No tax!')
else:
    if value < 25000:
        tax = 100 + (value - 5000) * 0.08
    elif value < 55000:
        tax = 1700 + (value - 25000) * 0.1
    elif value < 200000:
        tax = 4700 + (value - 55000) * 0.12
    elif value < 1000000:
        tax = 22100 + (value - 200000) * 0.15
    else:
        tax = 142100 + (value - 1000000) * 0.17
    print(f'Amount of tax: {float(tax)} euros, when input is {float(value)}')
    # print(f'when input is {float(value)}')