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


# Please write a program which asks the user to type in some text. 
# Your program should then perform a spell check, and print out feedback to the user,
# so that all misspelled words have stars around them. 
# Please see the two examples below:

# Sample output
# Write text: We use ptython to make a spell checker

# We use *ptython* to make a spell checker
# Sample output
# Write text: This is acually a good and usefull program

# This is *acually* good and *usefull* program
# The case of the letters should be irrelevant to the functioning of your program.

# The exercise template includes the file wordlist.txt, 
# which contains all the words the spell checker should accept as correct.

# NB: this exercise doesn't ask you to write any functions,
# so you should not place any code within an if __name__ == "__main__" block.

# NB2 If Visual Studio can't find the file and you have checked that there are no spelling errors,
# take a look at these instructions


def check_letter (letter):
    value = False
    with open('./part6/wordlist.txt','r') as new_file:
        for line in new_file:
            parts = line.strip()
            if parts.capitalize() == letter.capitalize():
                value = True
    return value


def spell_checker ():
    text = input('Write text:').rstrip('\n')
    list = text.split(' ')
    for word in list:
        if check_letter(word)==True:
            print(word, end=" ")
        else:
            print(f"*{word}*", end=" ")


spell_checker()



# 6.1 Receip search:
# NB: Some exercises have multiple parts, and you can receive points for the different parts separately.
# You can submit a partially completed exercise by choosing 'Submit Solution' from the menu next to the button for executing tests .

# This exercise is about creating a program which allows the user to search for recipes based on their names, 
# preparation times, or ingredients used.
# The program should read the recipes from a file submitted by the user.

# Each recipe consists of three or more lines. The first line has the name of the recipe,
# the second line contains an integer number representing the preparation time in minutes, 
# and the remaining line or lines contain the ingredients used, one on each line.
# The recipe ends with an empty line,
# with the exception of the final recipe in the file which just ends with the end of the file. 
# So, there can be more than one recipe in a single file, like in the example below.

# Pancakes
# 15
# milk
# eggs
# flour
# sugar
# salt
# butter

# Meatballs
# 45
# mince
# eggs
# breadcrumbs

# Tofu rolls
# 30
# tofu
# rice
# water
# carrot
# cucumber
# avocado
# wasabi

# Cake pops
# 60
# milk
# bicarbonate
# eggs
# salt
# sugar
# cardamom
# butter
def render_recipes (filename:str):
    recipes={}
    temp_list =[]
    with open('./part6/'+filename) as new_file:
        for data in new_file:
            line = data.strip()
            temp_list.append(line)
    for i in temp_list:
        if i == '':
            continue  
        if len(i)>0:
            if i[0].isupper():
                temp=i
                recipes[temp]=[]
            else:
                recipes[temp].append(i)
    return recipes
                
def search_by_name (filename:str,word:str):
    recipes=render_recipes(filename)
    list = []
    for i in recipes.items():
        if word.upper() in i[0].upper():
            list.append(i[0])
    return list

def search_by_time(filename:str,prep_time:int):
    smallest =prep_time
    time =0
    cake_name=''
    recipes=render_recipes(filename)
    list=[]
    for recipe in recipes.items():
        if int(recipe[1][0]) < prep_time:
            # temp = prep_time - int(recipe[1][0])
            time = recipe[1][0]
            cake_name = recipe[0]
            # if temp < smallest :
                # smallest = temp
            list.append(f'{cake_name}, preparation time {time} min')
    return list

found_recipes = search_by_time("recipes1.txt", 35)

for recipe in found_recipes:
    print(recipe)

def search_by_ingredient(filename:str,ingredient: str):
    time = ''
    recipe_name=''
    recipes=render_recipes(filename)
    list =[]
    for i in recipes.items():
        if ingredient in i[1]:
            time = i[1][0]
            recipe_name = i[0]
            list.append(f'{recipe_name}, preparation time {time} min')
    return list

# 7.1 City bikes

# NB: Some exercises have multiple parts, and you can receive points for the different parts separately. 
# You can submit a partially completed exercise by choosing 'Submit Solution' from the menu next to the button for executing tests .

# In this exercise we will write some functions for working on a file containing location data from the stations for city bikes in Helsinki.

# Each file will follow this format:

# Longitude;Latitude;FID;name;total_slot;operative;id
# 24.950292890004903;60.155444793742276;1;Kaivopuisto;30;Yes;001
# 24.956347471358754;60.160959093887129;2;Laivasillankatu;12;Yes;002
# 24.944927399779715;60.158189199971673;3;Kapteeninpuistikko;16;Yes;003
# Each station has a single line in the file. The line contains the coordinates, name, and other identifying information for the station.


# Distance between stations
# First, write a function named get_station_data(filename: str). This function should read the names 
# and locations of all the stations in the file, and return them in a dictionary with the following format:

# Sample output
# {
#   "Kaivopuisto: (24.950292890004903, 60.155444793742276),
#   "Laivasillankatu: (24.956347471358754, 60.160959093887129),
#   "Kapteeninpuistikko: (24.944927399779715, 60.158189199971673)
# }
# Dictionary keys are the names of the stations, and the value attached is a tuple containing the location coordinates of the station.
# The first element in the tuple is the Longitude field, and the second is the Latitude field.

# Next, write a function named distance(stations: dict, station1: str, station2: str),
# which returns the distance between the two stations given as arguments.

# The distance is calculated using the Pythagorean theorem. 
# The multiplication factors below are approximate values for converting latitudes and longitudes to distances in kilometres in the Helsinki region.

# # we will need the function sqrt from the math module 
# import math

# x_km = (longitude1 - longitude2) * 55.26
# y_km = (latitude1 - latitude2) * 111.2
# distance_km = math.sqrt(x_km**2 + y_km**2)
# Some examples of the function in action:

# stations = get_station_data('stations1.csv')
# d = distance(stations, "Designmuseo", "Hietalahdentori")
# print(d)
# d = distance(stations, "Viiskulma", "Kaivopuisto")
# print(d)
# Sample output
# 0.9032737292463177
# 0.7753594392019532

# NB: If Visual Studio can't find the file and you have checked that there are no spelling errors, take a look at these instructions.



import math

def get_station_data(filename: str) : 
    data ={}
    with open( './part6/'+filename) as new_file:
        for i in new_file:
            line = i.strip()
            if 'id' in line:
                continue
            parts = line.split(';')
            data[parts[3]] = (float(parts[0]),float(parts[1]))
    return data


def distance(stations: dict, station1: str,station2:str):
    longitude1 =float(stations[station1][0])
    longitude2= float(stations[station2][0])
    latitude1= float(stations[station1][1])
    latitude2=float(stations[station2][1])
    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)
    return distance_km



def greatest_distance(stations: dict):
    greatest=0
    station_1=''
    station_2=''
    for i in stations:
        for j in stations:
            if i != j: 
                temp = distance(stations,i,j)
                if greatest < temp:
                    greatest =temp
                    station_1= i
                    station_2=j
    return(station_1, station_2, greatest)
                



