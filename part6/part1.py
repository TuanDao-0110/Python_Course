# 1. Reading data from a file
with open("./part1.txt",'r') as new_file:
    contents = new_file.read()
    print(contents)


# with read() ==> each line will return '\n' as one line down. 
# 2. Going through the contents of a file


def largest():
    with open('./numbers.txt', 'r') as f:
        numbers = [int(line.strip()) for line in f]
        return max(numbers)
largest()
# <!-- List of query to open-->
# 'r': Open for reading(default)
# 'w': Open for writing, truncating(i.e. overwriting) the file first
# 'a': Open for writing, appending to the end of the file if it exists
# 'x': Open for exclusive creation, failing if the file already exists
# 'b': Binary mode(e.g. 'rb' to read a binary file)
# 't': Text mode(default)


# 2. reading CSV file:

text = "monkey,banana,harpsichord"
words = text.split(",")
for word in words:
    print(word)

with open('./fruits.csv','r') as new_file:
    for line in new_file:
        line = line.replace('\n','')
        parts= line.split(';')
        name= parts[0]
        grades = parts[1:]
        print('Name:',name)
        print('grades:',grades)
        
# 2.1 task: 
# The file fruits.csv contains names of fruits, and their prices, in the format specified in this example:

# banana;6.50
# apple;4.95
# orange;8.0
# ...etc...

def read_fruits():
    distionary={}
    with open('./fruits.csv','r') as new_file:
        for line in new_file:
            line = line.replace("\n",'')
            parts=line.split(';')
            name=parts[0]
            price=float( parts[1])
            distionary[name] = float(price)
    return distionary

# 2. Please write two functions, named matrix_sum and matrix_max. 
# Both go through the matrix in the file, and then return the sum of the elements or
# the element with the greatest value, as the names of the functions imply.

# Please also write the function row_sums, 
# which returns a list containing the sum of each row in the matrix.
# For example, calling row_sums when the matrix in the file is defined as

# 1,2,3
# 2,3,4
    

def sum_each_row(row):
    sum =0
    line= row.replace('\n','').split(',')
    for i in line:
        sum += int(i)
    return sum

def row_sums ():
    rows_sum =[]
    with open('./matrix.txt','r') as new_file:
        for line in new_file:
            rows_sum.append(sum_each_row(line))
    print(rows_sum)
    return rows_sum
    

def matrix_sum ():
    sum =0
    for i in row_sums(): 
        sum += i
    return sum

def matrix_max():
    list = []
    with open('./matrix.txt','r') as new_file:
        for line in new_file: 
            temp =line.replace('\n','').split(',')
            for i in temp:
                list.append(int(i))
    return max(list)

# 3. Reading the same file multiple times
with open("people.csv") as new_file:
    # print out the names
    for line in new_file:
        parts = line.split(";")
        print("Name:", parts[0])

    # find the oldest
    age_of_oldest = -1
    for line in new_file:
        parts = line.split(";")
        name = parts[0]
        age = int(parts[1])
        if age > age_of_oldest:
            age_of_oldest = age
            oldest = name
    print("the oldest is", oldest)

#3.1 Running this will result in a somewhat cryptic error message:

# Traceback (most recent call last):
    # print("the oldest is"; oldest)
# UnboundLocalError: local variable 'oldest' referenced before assignment
# The reason this happens is that the latter for loop is not executed at all,
# beacuse the file can only be processed once. Once the last line is read, 
# the file handle rests at the end of the file, and the data in the file can no longer be accessed.
with open("./people.csv") as new_file:
    # print out the names
    for line in new_file:
        parts = line.split(";")
        print("Name:", parts[0])
        
with open("./people.csv") as new_file:
    # find the oldest
    age_of_oldest = -1
    for line in new_file:
        parts = line.split(";")
        name = parts[0]
        age = int(parts[1])
        if age > age_of_oldest:
            age_of_oldest = age
            oldest = name
    print("the oldest is", oldest)

# 3.2 While the above code would work, it contains unnecessary repetition.
# It is usually best to read the file just once, and store its contents in an appropriate format for further processing:
people = []
# read the contents of the file and store it in a list
with open("./part6/people.csv") as new_file:
    for line in new_file:
        parts = line.split(";")
        people.append((parts[0], int(parts[1]), parts[2]))
print(people)
# print out the names
for person in people:
    print("Name:", person[0])

# find the oldest
age_of_oldest = -1
for person in people:
    name = person[0]
    age = person[1]
    if age > age_of_oldest:
        age_of_oldest = age
        oldest = name
print("the oldest is", oldest)

# 4.1 More CSV file processing
grades = {}
with open("grades.csv") as new_file:
    for line in new_file:
        line = line.replace("\n", "")
        parts = line.split(";")
        name = parts[0]
        grades[name] = []
        print(parts[1])
        for grade in parts[1:]:
            grades[name].append(int(grade))

print(grades)
# node: with grade[1:] --> run array from the place 1st 


#4.2 Now we can print out some statistics on each student based on the contents of the dictionary grades:

for name, grade_list in grades.items():
    best = max(grade_list)
    average = sum(grade_list) / len(grade_list)
    print(f"{name}: best grade {best}, average {average:.2f}")
    
# 4.3 Removing unnecessary lines, spaces and line breaks
last_names = []
with open("./part6/people1.csv") as new_file:
    for line in new_file:
        parts = line.split(";")
        # ignore the header line
        if parts[0] == "first":
            continue
        last_names.append(parts[1].strip())

print(last_names)

# without strip() --> answer will: [' Python\n', ' Java\n', ' Haskell']


# There are also the related string methods lstrip and rstrip. They remove only the leading or trailing unprintable characters, l for the left edge of the string and r for the right:

# >>> " teststring  ".rstrip()
# ' teststring'
# >>> " teststring  ".lstrip()
# 'teststring  '

# 4.4 Combining data from different files

names = {}

with open("./part6/employees.csv") as new_file:
    for line in new_file:
        parts = line.split(';')
        if parts[0] == "pic":
            continue
        names[parts[0]] = parts[1]

salaries = {}

with open("./part6/salaries.csv") as new_file:
    for line in new_file:
        parts = line.split(';')
        if parts[0] == "pic":
            continue
        salaries[parts[0]] = int(parts[1]) +int(parts[2])

print("incomes:")

for pic, name in names.items():
    if pic in salaries:
        salary = salaries[pic]
        print(f"{name:16} {salary} euros")
    else:
        print(f"{name:16} 0 euros")


# First the program produces the dictionaries names and salaries. 
# They have the following contents:

{
    '080488-123X': 'Pekka Mikkola',
    '290274-044S': 'Liisa Marttinen',
    '010479-007Z': 'Arto Vihavainen',
    '010499-345K': 'Leevi Hellas'
}

{
    '080488-123X': 3300,
    '290274-044S': 4350,
    '010479-007Z': 2500
}


# Course grading: 

student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")
exam_point1=input("Exercises points: ")
show_data = ['name','exec_nbr','exec_pts.','exm_pts.','tot_pts.','grade']
student = {}
with open('./part6/'+  student_info,'r') as new_file:
    for line in new_file:
        parts = line.split(';')
        if parts[0] =='id':
            continue
        student[parts[0]] = parts[1:]
exercises= {}
with open('./part6/'+  exercise_data,'r') as new_exercise:
    for line in new_exercise:
        parts = line.split(';')
        if parts[0] == 'id':
            continue
        exercises[parts[0]] = parts[1:]
points ={}
with open( './part6/'+ exam_point1,'r') as exam_points:
    for line in exam_points:
        parts = line.split(';')
        if parts[0] =='id':
            continue
        points[parts[0]] = parts[1:]
def sum_all_exercises(list_exercise ):
    total=0
    for i in list_exercise:
        total += int(i.strip())
    return total
def sum_all_award_point(total_exercise):
    award_point=0
    per_completed = round( (total_exercise/40 )* 100,1)
    award_point  =int( per_completed * 0.1)
    return award_point 
def sum_all_point(list_point):
    total = 0
    for i in list_point:
        total += int(i.strip())
    return total 
def show_information():
    print("{:30}{:10}{:10}{:10}{:10}{:10}".format(*show_data))
    for i  in student.items():
        id = i[0]
        full_name=''
        total_exercise=sum_all_exercises(exercises[id])
        award_point = sum_all_award_point(total_exercise)
        point= sum_all_point(points[id])
        total_score = award_point + point
        for j in i[1]:
            full_name += j.strip() +' '
        grade = check_grade(total_score)
        print(f"{full_name:<30}{total_exercise:<10}{award_point:<10}{point:<10}{total_score:<10}{grade:<10}")
def check_grade (total_score:int):
    if 0 <= total_score <=14:
        return 0
    if 15 <= total_score <=17:
        return 1
    if 18<= total_score <=20:
        return 2
    if 21<= total_score <= 23:
        return 3
    if 24<= total_score <= 27:
        return 4
    if 28<= total_score:
        return 5
show_information()



# 5.1 Spell checker


