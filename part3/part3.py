# 1.The break vs continues command:
sum = 0

while True:
    number = int(input("Please type in a number, -1 to exit: "))
    if number == -1:
        break
    if number >= 10:
        continue
    sum += number

print(f"The sum is {sum}")



# 2. Nested Loops: 

while True:
    number = int(input("Please type in a number: "))
    if number == -1:
        break
    while number > 0:
        print(number)
        number -= 1

while True:
    number = int(input("Please type in a number: "))
    if number == -1:
        break
    while True:
        if number <= 0:
            break
        print(number)
        number -= 1

number = int(input("Please type in a number: "))
while number > 0:
    i = 0
    while i < number:
        print(f"{i} ", end="")
        i += 1
    print()
    number -= 1


# 3.More helper variables with loops


# We've already used helper variables, which increase or decrease with every iteration of a loop, many times before, so the following program should look quite familiar in structure. The program prints out all even numbers above zero until it reaches a limit set by the user:

# limit = int(input("Please type in a number: "))
# i = 0
# while i < limit:
#     print(i)
#     i += 2


# 4.Multiplication


number = int(input('Please type in a number:'))

for i in range(1, number + 1):
    for j in range(1, number + 1):
        sum = i * j
        print(f'{i} x {j} = {sum}')

# 5. First letters of words
sentence = input('Please type in a sentence:')
list = sentence.split(' ')

for i in list:
    print(f'{i[0]}')


# 6. Factorial
# Please write a program which asks the user to type in an integer number. If the user types in a number equal to or below 0, the execution ends. Otherwise the program prints out the factorial of the number.

# The factorial of a number involves multiplying the number by all the positive integers smaller than itself. In other words, it is the product of all positive integers less than or equal to the number. For example, the factorial of 5 is 1 * 2 * 3 * 4 * 5 = 120.

# Some examples of expected behaviour:

# Sample output
# Please type in a number: 3
# The factorial of the number 3 is 6
# Please type in a number: 4
# The factorial of the number 4 is 24
# Please type in a number: -1
# Thanks and bye!

number = int(input("Please type in a number:"))
sum = 1
while number > 0:
    for i in range(number + 1):
        if i > 0:
            sum *= i
    print(f'The factorial of the number {number} is {sum}')
    number = int(input("Please type in a number:"))
    sum = 1
if number <= 0:
    print(f'Thanks and bye!')

# 7. Flip the pairs

# Please write a program which asks the user to type in a number.
# The program then prints out all the positive integer values from 1 up to the number. 
# However, the order of the numbers is changed so that each pair or numbers is flipped. 
# That is, 2 comes before 1, 4 before 3 and so forth. See the examples below for details.


num = int(input("Please type in a number: "))

# create a list of integers from 1 to num
integers = list(range(1, num+1))
# loop through the list by pairs and swap their positions
for i in range(0, len(integers)-1, 2):
    integers[i], integers[i+1] = integers[i+1], integers[i]

# print the modified list of integers
for integer in integers:
    print(integer)

# 8. Taking turns


num = int(input("Please type in a number: "))

# initialize start and end values
start = 1
end = num

# loop until start and end cross over
while start <= end:
    # print the start value
    print(start)
    # if start and end are the same, break out of the loop
    if start == end:
        break
    # otherwise, print the end value and decrement it
    print(end)
    end -= 1
    # increment the start value
    start += 1


# 