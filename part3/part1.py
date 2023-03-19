# 1. Loops with conditions: 
# while <condition>:
    # <block>

# In the following loop we have the condition number < 10. The block within the loop is executed only if the variable number is less than 10.

# number = int(input("Please type in a number: "))

# while number < 10:
#     print(number)
#     number += 1

# print("Execution finished.")

# 2. Countdown


print("Are you ready?")
number = int(input("Please type in a number: "))
while number > 0: 
    print(f'{number}')
    number -=1
print('Now!')


# 3. Writing conditions

number = int(input("Please type in a number: "))

while number != 10:
    print(number)
    number += 2

# 4. Numbers

# Write your solution here

limit_number = int(input('Upper limit:'))
start = 1
while start < limit_number:
    print(f'{start}')
    start +=1
    
# 5. Debugging tips

# Imagine you are writing some slightly more complicated program, 
# such as the one in the next exercise, Powers of two. 
# The first efforts could look like this:


# limit = int(input("Upper limit:"))
# number = 1
# while number == limit:
   # more code

# 6.Powers of base 

limit = int(input('Upper limit:'))
base = int(input('Base:'))
start = 1
while start<= limit :
    print(f'{start}')
    start = start *base

# 7. The sum of consecutive numbers, version 1

limit = int(input('Limit:'))
sum = 0 
start = 1

while sum < limit: 
    sum +=start
    start +=1

print(f'{sum}')

# 8. Building strings

words = "pride"
words = words + ", prejudice"
words = words + " and python"

print(words)


# 9. The sum of consecutive numbers, version 2

# Please write a new version of the program in the previous exercise. 
# In addition to the result it should also print out the calculation performed:

# Sample output
# Limit: 2
# The consecutive sum: 1 + 2 = 3

limit = int(input('Limit: '))
start = 1
sum = 0
words = '1'
while sum  < limit:
    sum += start
    start += 1
    if(sum < limit):
        words += f' + {start}'
print(f'The consecutive sum: {words} = {sum}')









