# 1. Accessing items in a list
from math import floor
my_list = [7, 2, 3, 4, 5]

# 2.Add items to a list
array = []
for i in range(3):
    item = input(f'Item {i +1}:')
    array.append(item)

print(array)

# 2. Insert:

numbers = [1, 2, 3, 4, 5, 6]
numbers.insert(0, 10)
print(numbers)
numbers.insert(2, 20)
print(numbers)
# 3. Pop() vs remove()

my_list = [1, 2, 3, 4, 5, 6]

my_list.pop(2)
print(my_list)
my_list.pop(3)
print(my_list)


my_list = [1, 2, 1, 2]

my_list.remove(1)
print(my_list)
my_list.remove(1)
print(my_list)


# 4. conditon check:
my_list = [1, 3, 4]

if 1 in my_list:
    print("The list contains item 1")

if 2 in my_list:
    print("The list contains item 2")


# 5. Sort List:
my_list = [2, 5, 1, 2, 4]
my_list.sort()
print(my_list)


# so we use the function sorted instead. It returns a sorted list:
my_list = [2, 5, 1, 2, 4]
print(sorted(my_list))


# 7. Max, Min, Sum:

my_list = [5, 2, 3, 1, 4]

greatest = max(my_list)
smallest = min(my_list)
list_sum = sum(my_list)

print("Smallest:", smallest)
print("Greatest:", greatest)
print("Sum:", list_sum)


# 8. Methods vs functions

my_list = []

# method calls
my_list.append(3)
my_list.append(1)
my_list.append(7)
my_list.append(2)

# another method call
my_list.sort()

# 9. A list as an argument or a return value


def median(my_list: list):
    ordered = sorted(my_list)
    list_len = len(ordered)
    if list_len % 2 == 0:
        # if the list length is even
        middle_right = list_len // 2
        middle_left = middle_right - 1
        median_value = (ordered[middle_left] + ordered[middle_right]) / 2
    else:
        # if the list length is odd
        middle = list_len // 2
        median_value = ordered[middle]
    return median_value


# 10. The length of a list


def length(list):
    return len(list)


my_list = [1, 2, 3, 4, 5]
result = length(my_list)
print("The length is", result)

result = length([1, 1, 1, 1])
print("The length is", result)


# 11. Arithmetic mean:


def mean(list):
    return int(sum(list)/len(list))


my_list = [1, 2, 3, 4, 5]
result = mean(my_list)
print("mean value is", result)

# 12. The range of a list


def range_of_list(list):
    sort = sorted(list)
    length = len(sort) - 1
    return sort[length] - sort[0]


my_list = [1, 2, 3, 4, 5]
result = range_of_list(my_list)
print("The range of the list is", result)
