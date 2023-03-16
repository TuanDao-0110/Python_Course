# 1. Changing the value of a variable

word = input("Please type in a word: ")
print(word)

word = input("And another word: ")
print(word)

word = "third"
print(word)

# 2. Integers

age = 24
print(age)
# 2.1 wrong number
number = "100"
print(number / 2)
# 3.Combining values when printing

result = 10 * 25
# the following line produces an error
print("The result is " + result)
# The program does not print out anything, but instead throws an error:
# fix it 
print('The result is' + str(result))
# or
print('The result is',result)


# 4. Printing with f-strings

result = 10 * 25
print(f'the result is {result}')
name = "Mark"
age = 37
city = "Palo Alto"
print(f"Hi {name}, you are {age} years old. You live in {city}.")


# 5. float point number

number1 = 2.5
number2 = -1.25
number3 = 3.62

mean = (number1 + number2 + number3) / 3
print(f'Mean: {mean}')

# 6. Fix the code: Print a single line
print("Hi ", end="")
print("there!")
# expect: Hi there!
# more example:
print('5',end='')
print(" + ", end='')
print(8,end='')
print(" - ",end='')
print(4,end='')
print(" = ",end='')
print(5 + 8 - 4)


