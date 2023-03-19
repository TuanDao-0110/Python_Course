# 1. The parameters and arguments of a function

# A function can take one or more arguments. When the function is called, the arguments are assigned to variables, which are defined in the function definition. These variables are called parameters, and they are listed inside the parentheses after the function name.

# In the following code the function greet has one parameter defined, while the function sum has two.


def greet(name):
    print("Hello there,", name)


def sum(a, b):
    print("The sum of the arguments is", a + b)


greet("Emily")
sum(2, 3)
# Sample output
# Hello there, Emily
# The sum of the arguments is 5

# 2. A triangle

def triangle (times):
    for i in range(times):
        print('*' * i)


triangle(6)

# 3. A shape


def shape(times1, text1, times2, text2):
    for i in range(times1 + 1):
        print(text1 * i)
    for j in range(times2):
        print(text2 * (times1))


shape(5, "X", 3, "*")

# 4. A spruce:


def spruce(time):
    count = -1
    print('a spruce!')
    for i in range(0, time):
        count += 2
        print(' ' * (time - i + 1), '*' * (count))
    print(' ' * (time + 1), '*')


spruce(5)
#     *
#    ***
#   *****
#  *******
# *********
#     *
spruce(2)

#   *
#  ***
# *****
#   *


# 5. The return value of a function

# 6.The return statement
def my_sum(a, b):
    return a + b


result = my_sum(2, 3)

print("Sum:", result)


# 7. Using return values from functions

def my_sum(a, b):
    return a + b


result = my_sum(4, 6)
print("The sum is", result)
# Sample output
# The sum is 10


# 8. The difference between return and print

def max1(a, b):
    if a > b:
        return a
    else:
        return b


def max2(a, b):
    if a > b:
        print(a)
    else:
        print(b)


result = max1(3, 5)
print(result)

max2(7, 2)

# Sample output
# 5
# 7


# 9.The greatest number
def greatest_number(n1,n2,n3):
   return max(n1,n2,n3)


print(greatest_number(3, 4, 1)) # 4
print(greatest_number(99, -4, 7))  # 99
print(greatest_number(0, 0, 0))  # 0


# 10.Same characters

def same_chars(string, index1, index2):
   # Check if either of the indexes falls outside the scope of the string
    if index1 < 0 or index2 < 0 or index1 >= len(string) or index2 >= len(string):
        return False

    # Check if the two characters are the same
    if string[index1] == string[index2]:
        return True
    else:
        return False
