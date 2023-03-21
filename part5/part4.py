# 1. Tuple is a data structure which is, in many ways, similar to a list.
# The most important differences between the two are:

# Tuples are enclosed in parentheses(), while lists are enclosed in square brackets[]
# Tuples are immutable, while the contents of a list may change
# The following bit of code creates a tuple containing the coordinates of a point:
point = (10, 20, 4)
print("x coordinate:", point[0])
print("y coordinate:", point[1])
print("y coordinate:", point[2])


#2. Create a tuple


def create_tuple(x: int, y: int, z: int) -> tuple:
    smallest = min(x, y, z)
    greatest = max(x, y, z)
    total = x + y + z
    return (smallest, greatest, total)


# 3. The oldest person:

# Please write a function named oldest_person(people: list), which takes a list of tuples as its argument. In each tuple, the first element is the name of a person, and the second element is their year of birth. The function should find the oldest person on the list and return their name.

# An example of the function in action:

p1 = ("Adam", 1977)
p2 = ("Ellen", 1985)
p3 = ("Mary", 1953)
p4 = ("Ernest", 1997)
people = [p1, p2, p3, p4]


def oldest_person(people: list) -> str:
    oldest = None
    for person in people:
        if oldest is None or person[1] < oldest[1]:
            oldest = person
    return oldest[0]

print(oldest_person(people))


# 4. Older people list: 
def older_people(people: list, year: int):
    oldest = []
    for person in people:
        if person[1] < year:
            oldest.append(person[0])
    return oldest


# 5. What is the purpose of a tuple?
# Tuples are ideal for when there is a set collection of values which are in some way connected. 
# For example, when there is a need to handle the x and y coordinates of a point, a tuple is a natural choice,
# because coordinates will always consist of two values:

# A list is a collection of consecutive items in a certain order. 
# The size of a list may also change. When we are storing the coordinates of a point, we want to store the x and y coordinates specifically, not an arbitrary list containing those values.

# Because tuples are immutable, unlike lists, they can be used as keys in a dictionary.
# The following bit of code creates a dictionary, where the keys are coordinate points:

points = {}
points[(3, 5)] = "monkey"
points[(5, 0)] = "banana"
points[(1, 2)] = "harpsichord"
print(points[(3, 5)])
# Sample output

# monkey


# 6. Tuples without parentheses


# The parentheses are not strictly necessary when defining tuples

numbers = (1, 2, 3)
numbers = 1, 2, 3


# This means we can also easily return multiple values using tuples. Let's have alook at he following example:

def minmax(my_list):
  return (min(my_list), max(my_list))


my_list = [33, 5, 21, 7, 88, 312, 5]

min_value, max_value = minmax(my_list)
print(f"The smallest item is {min_value} and the greatest item is {max_value}")


# 7. student database:
students = {}


def add_student(student_list, key):
    student_list[key] = []


def print_student(student_list, key):
    if key not in student_list:
        print(f'{key}: no such person in the database')
    else:
        print(f'{key}:')
        if len(student_list[key]) != 0:
            print('', f'{len(student_list[key])} completed courses:')
            sum = 0
            for i in student_list[key]:
                sum += i[1]
                print(' ', f'{i[0]} {i[1]}')
            print(
                '', f'average grade {float(round(sum/len(student_list[key]),1))}')
        else:
            print('', 'no completed courses ')


def add_course(student_list, key, data):
    course_exists = False
    for course in student_list[key]:
        if course[0] == data[0]:
            course_exists = True
            if data[1] != 0:
                course[1] = data[1]
            break
    if not course_exists and data[1] != 0:
        student_list[key].append([data[0], data[1]])


def summary(student_list):
    best_average = {'grade': 0, "name": ''}
    most_course = {'number': 0, 'name': ''}
    student = 0
    # average = 0
    for key, value in student_list.items():
        sum = 0
        for i in value:
            sum += i[1]
        temp = sum/len(value)
        if best_average['grade'] < temp:
            best_average['grade'] = temp
            best_average['name'] = key
    for key, value in student_list.items():
        student += 1
        if len(value) > most_course['number']:
            most_course['number'] = len(value)
            most_course['name'] = key
    print(f'students {student}')
    print(
        f'most courses completed {most_course["number"]} {most_course["name"]}')
    print(f'best average grade {best_average["grade"]} {best_average["name"]}')


students = {}
add_student(students, "Peter")
add_course(students, "Peter", ("Introduction to Programming", 3))
add_course(students, "Peter", ("Advanced Course in Programming", 2))
add_course(students, "Peter", ("Data Structures and Algorithms", 0))
add_course(students, "Peter", ("Introduction to Programming", 2))
print_student(students, "Peter")


# 8. 