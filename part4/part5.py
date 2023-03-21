# 1. f-strings

name = "Erkki"
age = 39
print(f"Hi {name} your age is {age} years")


number = 1/3
print(f"The number is {number:.2f}")
# The number is 0.33


names = ["Steve", "Jean", "Katherine", "Paul"]
for name in names:
  print(f"{name:15} centre {name:>15}")


# Steve           centre           Steve
# Jean            centre            Jean
# Katherine       centre       Katherine
# Paul            centre            Paul


name = "Larry"
age = 48
city = "Palo Alto"
greeting = f"Hi {name}, you are {age} years of age"
print(greeting + f", and you live in {city}")


# Hi Larry, you are 48 years of age, and you live in Palo Alto


# 2. Integers to strings


def formatted(list):
    new_list = []
    for i in list:
        new_list.append('{}'.format(round(i, 2)))
    return new_list


my_list = [1.234, 0.3333, 0.11111, 3.446]
new_list = formatted(my_list)
print(new_list)

# Sample output
# ['1.23', '0.33', '0.11', '3.45']

# 3. 