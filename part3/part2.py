# 1. String operations

# Strings can be combined, or concatenated, with the + operator:

# begin = "ex"
# end = "ample"
# word = begin+end
# print(word)



# word = "banana"
# print(word*3)
# Sample output
# bananabananabanana

# 2. Using string operations together with a loop we can write a program which draws a pyramid:

from math import floor
n = 10 # number of layers in the pyramid
row = "*"

while n > 0:
    print(" " * n + row)
    row += "**"
    n -= 1

# This prints out the following:

#           *
#          ***
#         *****
#        *******
#       *********
#      ***********
#     *************
#    ***************
#   *****************
#  *******************



# 3. String multiplied


# An example of expected behaviour:

# Sample output
# Please type in a string: hiya
# Please type in an amount: 4
# hiyahiyahiyahiya

string = input('Please type in a string:')
amount = int(input('Please type in an amount:'))

print(f'{string *amount}')

# 4. The length and index of a string

# The function len returns the number of characters in a string, which is always an integer value. For example, len("hey") returns 3, because there are three characters in the string hey.

# The following program asks the user for a string and then prints it "underlined". The program prints a second line with as many - characters as is the length of the input:

# input_string = input("Please type in a string: ")
# print(input_string)
# print("-"*len(input_string))
# Sample output
# Please type in a string: Hi there!

# Hi there!
# ---------


# 5. The longer string

string_1 = input('Please type in string 1:')
string_2 = input('Please type in string 2:')

if len(string_1) > len(string_2):
    print(f'{string_1} is longer')
elif len(string_1) < len(string_2):
    print(f'{string_2} is longer')
else:
    print(f'The strings are equally long')

# 6. String index:

input_string = input("Please type in a string: ")
print(input_string[0])
print(input_string[1])
print(input_string[3])

# would print out this:

# Sample output
# Please type in a string: monkey
# m
# o
# k

# Since the first character in a string has the index 0, the last character has the index length - 1. The following program prints out the first and the last characters of a string:

# input_string = input("Please type in a string: ")
# print("First character: " + input_string[0])
# print("Last character: " + input_string[len(input_string) - 1])


# Sample output
# Please type in a string: testing
# First character: t
# Last character: g


# 7. IndexError: string index out of range

# If you tried the above examples for yourself, 
# you may already have come across the error message IndexError: string index out of range. This error appears if you try to access an index which is not present in the string.

input_string = input("Please type in a string: ")
print("The tenth character: " + input_string[9])

# Sample output
# Please type in a string: introduction to programming
# The tenth character: i


# 8. End to beginning

# Please write a program which asks the user for a string. The program then prints out the input string in reversed order, from end to beginning. Each character should be on a separate line.

# An example of expected behaviour:

# Sample output
# Please type in a string: hiya
# a
# y
# i
# h

string = input('Please type in a string:')[::-1]

for i in string:
    print(f'{i}')


# 9. Second and second to last characters

# Please write a program which asks the user for a string. The program then prints out a message based on whether the second character and the second to last character are the same or not . See the examples below.

# Sample output
# Please type in a string: python
# The second and the second to last characters are different

# Sample output
# Please type in a string: pascal
# The second and the second to last characters are a


string = input('Please type in a string:')
if string[1] == string[-2]:
    print(f'The second and the second to last characters are {string[1]}')
else:
    print(f'The second and the second to last characters are different')


# 10. A line of hashes

width = int(input('Width:'))

print(f"{'#' * width}")


# 11.A rectangle of hashes
width = int(input('Width:'))
height = int(input('Height:'))
start = 0
while start < height:
    print(f"{'#' * width }") 
    start +=1
# 11. Underlining

# Please write a program which asks the user for strings using a loop. The program prints out each string underlined as shown in the examples below. The execution ends when the user inputs an empty string - that is , just presses Enter at the prompt.

# Sample output
# Please type in a string: Hi there!

# Hi there!
# ---------
# Please type in a string: This is a test

# This is a test
# --------------
# Please type in a string: a

# a
# -
# Please type in a string:

string = input('Please type in a string:')
while len(string) != 0:
    print(f'{string}')
    print(f"{'-' * len(string)}")
    string = input('Please type in a string:')

# 12. Right-aligned


string = input('Please type in a string:')

print(f"{'*' * int(20 - len(string))}{string}")
# result:
# Sample output
# Please type in a string: alongerstring

# *******alongerstring
# Sample output
# Please type in a string: averyverylongstring

# *averyverylongstring

# 13. A framed word


string = input('Word:')
rest_len = floor(int(30 - len(string) - 2)/2)
print(f"{'*' * 30}")
print(f"{'*' + (' ' * rest_len )}{string} {(27 -rest_len - len(string)) * ' ' + '*'}")
print(f"{'*' * 30}")

# 14. Substrings and slices

input_string = "presumptious"

print(input_string[0:3])
print(input_string[4:10])

# if the beginning index is left out, it defaults to 0
print(input_string[:3])

# if the end index is left out, it defaults to the length of the string
print(input_string[4:])


# result: 
# pre
# umptio
# pre
# umptiou

string = input('Please type in string:')
end = 0
while end <= len(string):
    print(f'{string[0:end]}')
    end += 1


# 15. Substrings, part 2


string = input('Please type in string:')
start = int(len(string)) - 1
while start >= 0:
    print(f'{string[start:len(string)]}')
    start -= 1


# 16. Does it contain vowels

string = input('Please type in a string:')
vowel = ['a', 'e', 'o']

for i in vowel:
    if i in string:
        print(f'{i} found')
    else:
        print(f'{i} not found')


# 17. Find: 

input_string = "test"

print(input_string.find("t"))
print(input_string.find("x"))
print(input_string.find("es"))
print(input_string.find("ets"))

# The operator in returns a Boolean value, so it will only tell us if a substring exists in a string, but it will not be useful in finding out where exactly it is. Instead, the Python string method find can be used for this purpose. It takes the substring searched for as an argument, and returns either the first index where it is found, or -1 if the substring is not found within the string.

# 18. Find the first substring

word = input("Please type in a word: ")
char = input("Please type in a character: ")

start_index = word.find(char)
if start_index != -1 and start_index+2 < len(word):
    print(word[start_index:start_index+3])


# 19. Find all the substrings

# Please make an extended version of the previous program, which prints out all the substrings which are at least three characters long, and which begin with the character specified by the user. You may assume the input string is at least three characters long.

# Sample output
# Please type in a word: mammoth
# Please type in a character: m
# mam
# mmo
# mot


word = input("Please type in a word: ")
char = input("Please type in a character: ")

for i in range(len(word)):
    if word[i:i+1] == char:
        if len(word)-i >= 3:
            print(word[i:i+3])


# 20. The second occurrence


string = input("Please type in a string: ")
substring = input("Please type in a substring: ")

index = string.find(substring)
if index != -1:
    new_string = string[index + len(substring):len(string)]
    new_index = new_string.find(substring)
    if new_index != -1:
        print(
            f'The second occurrence of the substring is at index {new_index + index +len(substring)}.')

    else:
        print(f'The substring does not occur twice in the string.')
else:
    print(f'The substring does not occur twice in the string.')
