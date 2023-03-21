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
    most_course = {'number':0,'name':''}
    student=0
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
        student +=1
        if len(value) > most_course['number']:
            most_course['number'] = len(value)
            most_course['name'] = key
    print(f'students {student}')
    print(f'most courses completed {most_course["number"]} {most_course["name"]}')
    print(f'best average grade {best_average["grade"]} {best_average["name"]}')

students = {}
add_student(students, "Peter")
add_course(students, "Peter", ("Introduction to Programming", 3))
add_course(students, "Peter", ("Advanced Course in Programming", 2))
add_course(students, "Peter", ("Data Structures and Algorithms", 0))
add_course(students, "Peter", ("Introduction to Programming", 2))
print_student(students, "Peter")
