# 1. 

my_string = "exemplary"
print(my_string[3:7])


# 2. More slices

my_string = "exemplary"
print(my_string[0:7:2])
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
print(my_list[6:2:-1])

# 3. Warning: using global variables within functions


def print_reversed(names: list):
    # using the global variable instead of the parameter by accident
    i = len(name_list) - 1
    while i >= 0:
        print(name_list[i])
        i -= 1


# here the global variable is assigned
name_list = ["Steve", "Jean", "Katherine", "Paul"]
print_reversed(name_list)
print()
print_reversed(["Huey", "Dewey", "Louie"])
# Sample output
# Paul
# Katherine
# Jean
# Steve

# Paul
# Katherine
# Jean
# Steve

# 4. Everything reversed


def everything_reversed(list):
    temp_list = []
    for i in list:
        temp_list.append(i[::-1])
    return temp_list[::-1]


my_list = ["Hi", "there", "example", "one more"]
new_list = everything_reversed(my_list)
print(new_list)

# Sample output
# ['erom eno', 'elpmaxe', 'ereht', 'iH']

# 5.Strings are immutable

my_list = [1, 2, 3]
my_list[0] = 10


my_string = "Hey"
my_string = my_string + "!"


# 6. More methods for lists and strings

my_string = "How much wood would a woodchuck chuck if a woodchuck could chuck wood"
print(my_string.count("ch"))

my_list = [1, 2, 3, 1, 4, 5, 1, 6]
print(my_list.count(1))
# Sample output
# 5
# 3



# 6. replace: 
my_string = "Hi there"
new_string = my_string.replace("Hi", "Hey")
print(new_string)
# Sample output
# Hey there


def no_vowels(text):
    new_text = text.replace('a' or 'e', '')

    return new_text


my_string = "this is an example"
print(no_vowels(my_string))


# 7. No shouting allowed isupper()

print("XYZ".isupper())

is_it_upper = "Abc".isupper()
print(is_it_upper)
# Sample output
# True
# False

# 8. No shouting allowed

def no_shouting(list):
    new_list = []
    for i in list:
        if not i.isupper():
            new_list.append(i)
    return new_list


my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER",
           "lower", "another lower", "Capitalized"]
pruned_list = no_shouting(my_list)
print(pruned_list)
# Sample output
# ['def', 'lower', 'another lower', 'Capitalized']


# 9. Developing a larger programming project

