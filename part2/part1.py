# 1. statement:
# 1.1
# A statement is a part of the program which executes something. It often, but not always, refers to a single command.
# For example, print("Hi!") is a statement which prints out a line of text. Likewise, number = 2 is a statement which assigns a value to a variable.
name = input('insert name:')
if name == "Anna":
    print("Hi!")
    number = 2

# 1.2 Block
# A block is a group of consecutive statements that are at the same level in the structure of the program. For example, the block of a conditional statement contains those statements which are executed only if the condition is true.
age= 40
if age > 17:
    # beginning of the conditional block
    print("You are of age!")
    age = age + 1
    print("You are now one year older...")
    print(f'{age}')
    # end of the conditional block

print("This here belongs to another block")

# 1.3 Function

# A function is executed when it is called. That is, when the function (and its arguments, if any) is mentioned in the code. The following statement calls the print function with the argument "this is an argument":

print("this is an argument")
# Another function you've already used often is the input function, which asks the user for input. The argument of this function is the message that is shown to the user:
name = input("Please type in your name: ")


# 1.4 Data type
# Data type refers to the characteristics of any value present in the program. In the following bit of code the data type of the variable name is string or str, and the data type of the variable result is integer or int:


name = "Anna"
result = 100


# You can use the function type to find out the data type of any expression. An example of its use:


print(type("Anna"))
print(type(100))

# Expect Result: 
    # <class 'str'>
    # <class 'int'>

# 1.5 Syntax

# The syntax of Python specifies, among other things, 
# that the first line of an if statement should end in a colon character, and the block of the statement should be indented:

if name == "Anna":
    print("Hi!")

# 1.6 Debugging

# If the syntax of the program is correct but the program still doesn't function as intended, there is a bug in the program.

# Bugs manifest in different ways. Some bugs cause an error during execution. For example, the following program

x = 10
y = 0
result = x / y

print(f"{x} divided by {y} is {result}")
# Cause this error: 
# --> ZeroDivisionError: integer division or modulo by zero on line 3
# Reason:

# The problem here is mathematical in nature: division by zero is not allowed, 
# and this halts the execution of the program.

# 1.7 Fix the syntax: 

#   number = input("Please type in a number: ")
#   if number>100
#     print("The number was greater than one hundred")
#     number - 100
#     print("Now its value has decreased by one hundred)
#      print("Its value is now"+ number)
#  print(number + " must be my lucky number!")
#  print("Have a nice day!)

# Fix the program
number =int(input("Please type in a number: "))
if number>100:
    number =number- 100
    print("The number was greater than one hundred")
    print("Now its value has decreased by one hundred")
    print("Its value is now", int(number)) 
print(int(number) , " must be my lucky number!")
print("Have a nice day!")

# 1.8 Number of characters by using "len"
word = input('Please type in a word:')
length = len(word)
if length > 1:
    print(f'There are {length} letters in the world {word}')
print('Thank you!')

# 1.9 Typecasting using floor from math:
from math import floor

number = float(input('Please type in a number:'))
interger = floor(number)
decimal =float( number- interger)
print(f'Integer part: {interger}')
print(f'Decimal part: {decimal}')







