# 1.Arithmetic operations

x = 3
y = 2

print(f"/ operator {x/y}")
print(f"// operator {x//y}")
# 2. Numbers as input

input_str = input("Which year were you born? ")
year = int(input_str)
print(f"Your age at the end of the year 2021: {2021 - year}" )
# for we can convert it straigth: 
year = int(input("Which year were you born? "))
current_year = int(input("Which yeart rigth now:"))
print(f"Your age at the end of the year {current_year}: {current_year - year}" )

# Similarly, a string can be converted into a floating point number with the function float. This programs asks the user for their height and weight, and uses these to calculate their BMI:

height = float(input("What is your height? "))
weight = float(input("What is your weight? "))

height = height / 100
bmi = weight / height ** 2

print(f"The BMI is {bmi}, height: {height}")

# 2.1 exercise: 
# require: 
# Please write a program which asks the user for a number. The program then prints out the number multiplied by five.

# The program should function as follows:

# Sample output
# Please type in a number: 3
# 3 times 5 is 15

# solution:

number = int(input("Please type in a number:"))
times = 5
multiple = times *number
print(f"{number} times {times} is {multiple}")

# 2.2 Name and age

# Please write a program which asks the user for their name and year of birth. The program then prints out a message as follows:

# Sample output
# What is your name? Frances Fictitious
# Which year were you born? 1990
# Hi Frances Fictitious, you will be 31 years old at the end of the year 2021

name = input('what is your name?')
year_born = int(input('which year were you born'))
current_year = 2021
age = current_year - year_born
print(f'Hi {name}, you will be {age} years old at the end of the year {current_year}')


# 3. Using variable
number1 = int(input("First number: "))
number2 = int(input("Second number: "))
number3 = int(input("Third number: "))

sum = number1 + number2 + number3
print(f"The sum of the numbers: {sum}")


# 3.1 Seconds in a day

# Please write a program which asks the user for a number of days. The program then prints out the number of seconds in the amount of days given.

# The program should function as follows:

# Sample output
# How many days? 1
# Seconds in that many days: 86400

# Another example:

# Sample output
# How many days? 7
# Seconds in that many days: 604800

days = int(input('How many days:'))
caculate_second = days * 24* 60**2
print(f'{days} day is {caculate_second} seconds')


# 3.2 Fix the code: Product


# This program asks the user for three numbers. The program then prints out their product, that is, the numbers multiplied by each other. There is, however, something wrong with the program - it doesn't work quite right, as you can see if you run it. Please fix it.

# An example of the expected execution of the program:

# Sample output
# Please type in the first number: 2
# Please type in the second number: 3
# Please type in the third number: 5
# The product is 30



# 3.3 Sum and product


# Please write a program which asks the user for two numbers. The program will then print out the sum and the product of the two numbers.

# The program should function as follows:

# Sample output
# Number 1: 3
# Number 2: 7
# The sum of the numbers: 10
# The product of the numbers: 21

number = int(input('Number 1:'))
sum = number
multiple = number
number = int(input('Number 2:'))
sum = number + sum
multiple = number * multiple

print(f'The sum of the numbers: {sum}\nTheProduct of the numbers: {multiple}')


# 3.4 Sum and mean

# Please write a program which asks the user for four numbers. The program then prints out the sum and the mean of the numbers.

# The program should function as follows:

# Sample output
# Number 1: 2
# Number 2: 1
# Number 3: 6
# Number 4: 7
# The sum of the numbers is 16 and the mean is 4.0

number = int(input('number 1:'))
sum = number
number = int(input('number 2:'))
sum = number +sum
number = int(input('number 3:'))
sum = number +sum
number = int(input('number 4:'))
sum = number + sum
mean = float(sum/4)
print(f'The sum of the numbers is {sum} and the mean is {mean}')


# 3.5 Food expenditure

# Please write a program which estimates a user's typical food expenditure.

# The program asks the user how many times a week they eat at the student cafeteria. Then it asks for the price of a typical student lunch, and for money spent on groceries during the week.

# Based on this information the program calculates the user's typical food expenditure both weekly and daily.

# The program should function as follows:

# Sample output
# How many times a week do you eat at the student cafeteria? 4
# The price of a typical student lunch? 2.5
# How much money do you spend on groceries in a week? 28.5

# Average food expenditure:
# Daily: 5.5 euros
# Weekly: 38.5 euros



times = int(input('How many times a week do you eat at the student cafeteria?'))
price = float(input('The price of a typical student lunch?'))
money_week = float(input('How much money do you spend on groceries in a week?'))
weekly = float((price * times + money_week))
daily = float(weekly/7)

print(f'Average food expenditure:\nDaily: {daily} euros\nWeekly: {weekly} euros')


# 3.6 Students in groups

# Please write a program which asks for the number of students on a course and the desired group size. The program will then print out the number of groups formed from the students on the course. If the division is not even, one of the groups may have fewer members than specified.

# If you can't get your code working as expected, it is absolutely okay to move on and come back to this exercise later. The topic of the next section is conditional statements. This exercise can also be solved using a conditional construction.

# Sample output
# How many students on the course? 8
# Desired group size? 4
# Number of groups formed: 2
num_students = int(input("How many students on the course? "))
group_size = int(input("Desired group size? "))

num_groups = num_students // group_size
if num_students % group_size != 0:
    num_groups += 1

print("Number of groups formed:", num_groups)


