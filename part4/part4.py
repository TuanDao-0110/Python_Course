# 1. The for loop

# for <variable> in <collection>:
#     <block>

my_list = [3, 2, 4, 5, 2]

for item in my_list:
    print(item)

# Sample output
# 3
# 2
# 4
# 5
# 2


# 2. For loop in string: 
name = input("Please type in your name: ")

for character in name:
    print(character)

# 3. Star-studded

text = input('Pleast type in a string:')

for i in text:
    print(f'{i}')
    print(f'*')


# 4. The function range
# 4.1  from 0 to n-1
for i in range(5):
    print(i)
# Sample output
# 0
# 1
# 2
# 3
# 4

# 4.2 range(a,b) provides a range starting from a and ending at b-1
for i in range(3, 7):
    print(i)
# Sample output
# 3
# 4
# 5
# 6

# 4.3 The function call range(a, b, c) provides a range starting from a, ending at b-1, 
# and changing by c with every step:
for i in range(1, 9, 2):
    print(i)
# Sample output
# 1
# 3
# 5
# 7

# 4.4 Then the range will be in reversed orded. Notice the first two arguments are also flipped
for i in range(6, 2, -1):
    print(i)
# Sample output
# 6
# 5
# 4
# 3


# 5. From negative to positive

number = int(input('number:'))
for i in range(-number, number + 1):
    print(i)

# Sample output:
# Please type in a positive integer: 4
# -4
# -3
# -2
# -1
# 1
# 2
# 3
# 4


# 6. From a range to a list


numbers = list(range(2, 7))
print(numbers)


# 7. List of stars

def list_of_stars(list):
    for i in list:
        print('*' * i)


list_of_stars([3, 7, 1, 1, 2])

# Sample output:
# ***
# *******
# *
# *
# **


# 8. Anagrams 😜
def anagrams(text1, text2):
    for i in text1:
        return i in text2


# Some examples of how the function should work:

print(anagrams("tame", "meta"))  # True
print(anagrams("tame", "mate"))  # True
print(anagrams("tame", "team"))  # True
print(anagrams("tabby", "batty"))  # False
print(anagrams("python", "java"))  # False


# 9. Palindromes

def is_palindrome():
    text = input('text:')
    reverse = text[::-1]
    return text == reverse

# 10. The sum of positive numbers


def sum_of_positives(my_list):
    sum = 0
    for i in my_list:
        if i > 0:
            sum += i
    return sum

my_list = [1, -2, 3, -4, 5]
result = sum_of_positives(my_list)
print("The result is", result)

# Sample output
# The result is 9


def distinct_numbers(my_list):
    list = []
    for i in my_list:
        if i not in list:
            list.append(i)
    return sorted(list)


my_list = [3, 2, 2, 1, 3, 3, 1]
print(distinct_numbers(my_list))  # [1, 2, 3]


# 11. Finding the best or the worst item in a list


# best = initial_value  # The initial value depends on the situation
# for item in my_list:
#     if item is better than best:
#         best = item

# We now have the best one figured out!

