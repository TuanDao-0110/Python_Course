# 1. while: 
while True:
    number = int(input("Please type in a number, -1 to quit: "))

    if number == -1:
        break

    print(number ** 2)

print("Thanks and bye!")


# Program could look like this: 

# Please type in a number, -1 to quit: 2
# 4
# Please type in a number, -1 to quit: 4
# 16
# Please type in a number, -1 to quit: 10
# 100
# Please type in a number, -1 to quit: -1
# Thanks and bye!




# 2. Shall we continue?

# Let's create a program along the lines of the example above. This program should print out the message "hi" and then ask "Shall we continue?" until the user inputs "no". Then the program should print out "okay then" and finish. Please have a look at the example below.

# Sample output
# hi
# Shall we continue? yes
# hi
# Shall we continue? oui
# hi
# Shall we continue? jawohl
# hi
# Shall we continue? no
# okay then


while True:
    print('hi')
    ask = input("Shall we continue?")
    if ask == 'no':
        print(f'okay then')
        break



# Input validation: 
from math import sqrt

while True:
    num = int(input("Please type in a number: "))
    if num == 0:
        print("Exiting...")
        break
    elif num < 0:
        print("Invalid number")
    else:
        print(sqrt(num))


# Repeat password

# Please write a program which asks the user for a password. The program should then ask the user to type in the password again. If the user types in something else than the first password, the program should keep on asking until the user types the first password again correctly.

# Have a look at the expected behaviour below:

# Sample output
# Password: sekred
# Repeat password: secret
# They do not match!
# Repeat password: cantremember
# They do not match!
# Repeat password: sekred
# User account created!

while True: 
    pwd = input('Password')
    re_pwd = input('Repeat password:')
    if re_pwd == pwd:
        print('User account created!')
        break
    else:
        print('They do not match!')
        while True:
            re_pwd = input('Repeat password:')
            if re_pwd == pwd:
                print('User account created!')
                break   
            print('They do not match!')
    break
            


# 4.3 Loops and helper variables

attempts = 0

while True:
    code = input("Please type in your PIN: ")
    attempts += 1

    if code == "1234":
        success = True
        break

    if attempts == 3:
        success = False
        break

    # this is printed if the code was incorrect AND there have been less than three attempts
    print("Incorrect...try again")

if success:
    print("Correct PIN entered!")
else:
    print("Too many attempts...")


# 4.4 Debugging print statements in loops

attempts = 0

while True:
    code = input("Please type in your PIN: ")
    attempts += 1

    if attempts == 3:
        success = False
        break

    if code == "1234":
        success = True
        break

    print("Incorrect...try again")

if success:
    print("Correct PIN entered!")
else:
    print("Too many attempts...")

# Sample output
# Please type in your PIN: 0000
# Incorrect...try again
# Please type in your PIN: 9999
# Incorrect...try again
# Please type in your PIN: 1234
# Too many attempts...

# So, let's try and find the cause by adding some strategic debugging print statements inside the loop:
attempts = 0
while True:
    print("beginning of the while block:")
    code = input("Please type in your PIN: ")
    attempts += 1

    print("attempts:", attempts)
    print("condition1:", attempts == 3)
    if attempts == 3:
        success = False
        break

    print("code:", code)
    print("condition2:", code == "1234")
    if code == "1234":
        success = True
        break

    print("Incorrect...try again")


# 4.5 PIN and number of attempts

#  Please write a program which keeps asking the user for a PIN code until 
# they type in the correct one, which is 4321. The program should then print out the number of times the user tried different codes.

# Sample output
# PIN: 3245
# Wrong
# PIN: 1234
# Wrong
# PIN: 0000
# Wrong
# PIN: 4321
# Correct! It took you 4 attempts

# If the user gets it right on the first try, the program should print out something a bit different:

# Sample output
# PIN: 4321
# Correct! It only took you one single attempt!

# Write your solution here

attempt = 0 
while True:
    pin = int(input('Pin:'))
    attempt +=1
    if pin == 4321:
        if attempt >1 :
            print(f'Correct! It took you {attempt} attempts')
        else:   
            print(f'Correct! It only took you one single attempt!')
        break
    else:
        print(f'Wrong')

# 4.6 The next leap year

# Please write a program which asks the user for a year, and prints out the next leap year.

# Sample output
# Year: 2023
# The next leap year after 2023 is 2024

# If the user inputs a year which is a leap year (such as 2024), the program should print out the following leap year:

# Sample output
# Year: 2024
# The next leap year after 2024 is 2028


year  = int(input('Year:'))
add = 0
while True:
    add +=1
    # if int( year +add) % 4 == 0: 
    #     print(f'The next leap year after {year} is {int(year +add)}')
    #     break
 
    if (year+ add) % 4 == 0:
        if (year+ add) % 100 == 0:
            if (year+ add) % 400 == 0:
                print(f'The next leap year after {year} is {int(year +add)}')
                break
        else:
            # print((year+ add), "is a leap year")
            print(f'The next leap year after {year} is {int(year +add)}')
            break

# 4.7 Concatenating strings with the + operator
# Part 1
# Please write a program which keeps asking the user for words. If the user types in end, the program should print out the story the words formed, and finish.

# Sample output
# Please type in a word: Once
# Please type in a word: upon
# Please type in a word: a
# Please type in a word: time
# Please type in a word: there
# Please type in a word: was
# Please type in a word: a
# Please type in a word: girl
# Please type in a word: end
# Once upon a time there was a girl

# Part 2
# Change the program so that the loop ends also if the user types in the same word twice.

# Sample output
# Please type in a word: It
# Please type in a word: was
# Please type in a word: a
# Please type in a word: dark
# Please type in a word: and
# Please type in a word: stormy
# Please type in a word: night
# Please type in a word: night
# It was a dark and stormy night

# Part 1 and Part 2 solution:
words = []
while True:
    word = input("Please type in a word: ")
    if word == 'end':
        print(' '.join(words))
        break
    else:
        if len(words) >0:
            if words[-1] == word:
                print(' '.join(words))
                break
            else:
                words.append(word)
        else:
            words.append(word)
    
# 4.8 Working with numbers

# Please write a program which asks the user for integer numbers. The program should keep asking for numbers until the user types in zero.

# Sample output
# Please type in integer numbers. Type in 0 to finish.
# Number: 5
# Number: 22
# Number: 9
# Number: -2
# Number: 0

# Part 1: Count
# After reading in the numbers the program should print out how many numbers were typed in. The zero at the end should not be included in the count.

# You will need a new variable here to keep track of the numbers typed in.

# Sample output
# ... the program asks for numbers
# Numbers typed in 4

# Part 2: Sum
# The program should also print out the sum of all the numbers typed in. The zero at the end should not be included in the calculation.

# The program should now print out the following:

# Sample output
# ... the program asks for numbers
# Numbers typed in 4
# The sum of the numbers is 34

# Part 3: Mean
# The program should also print out the mean of the numbers. The zero at the end should not be included in the calculation. You may assume the user will always type in at least one valid non-zero number.

# Sample output
# ... the program asks for numbers
# Numbers typed in 4
# The sum of the numbers is 34
# The mean of the numbers is 8.5

# Part 4: Positives and negatives
# The program should also print out statistics on how many of the numbers were positive and how many were negative. The zero at the end should not be included in the calculation.

# Sample output
# ... the program asks for numbers
# Numbers typed in 4
# The sum of the numbers is 34
# The mean of the numbers is 8.5
# Positive numbers 3
# Negative numbers 1


count = 0
sum =0
positive = 0
negative =0
print('Please type in integer numbers. Type in 0 to finish.')
while True:
    number = int(input('Number:'))
    if  number ==0 : 
        print(f'Numbers typed in {count}\nThe sum of the numbers is {sum}\nThe mean of the numbers is {mean}\nPositive numbers {positive}\nNegative numbers {negative}')
        break
    count +=1
    sum +=number
    mean = float(sum/count)
    if number >0: 
        positive +=1
    else:
        negative+=1
    
