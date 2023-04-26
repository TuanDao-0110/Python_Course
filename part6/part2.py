# Writing files
# After this section

# You will know how to create files with Python code
# You will be able to write text based data to a file
# You will know how to create a CSV file


# 1. create a new file: 
with open("new_file.txt", "w") as my_file:
    print('create new file')
# 1.1 NB: if the file already exists, all the contents will be overwritten. 
# It pays to be very careful when creating new files.
# With the file open you can write data to it. You can use the method write, which takes the string that is to be written as its argument.

with open("new_file.txt", "w") as my_file:
    my_file.write("Hello there!")


# 1.2 If you want line breaks in the file, you will have to add them by hand 
# - the write function doesn't work exactly like the more familiar print function, 
# though they are similar. So, the following program

with open("new_file.txt", "w") as my_file:
    my_file.write("Hello there!")
    my_file.write("This is the second line")
    my_file.write("This is the last line")

# Result is: 
# Sample data
# ==> Hello there!This is the second lineThis is the last line

# 1.3 Line breaks are achieved by adding new line characters \n to the argument strings:

with open("new_file.txt", "w") as my_file:
    my_file.write("Hello there!\n")
    my_file.write("This is the second line\n")
    my_file.write("This is the last line\n")

# Sample data:
# Hello there!
# This is the second line
# This is the last line

# 1.4 Inscription

# Please write a program which asks for the name of the user and then creates an "inscription" in a file specified by the user. Please see the example below.

# Sample output
# Whom should I sign this to: Ada
# Where shall I save it: inscribed.txt

# The contents of the file inscribed.txt would be

# Sample data
# Hi Ada, we hope you enjoy learning Python with us! Best, Mooc.fi Team

# NB: this exercise doesn't ask you to write any functions, so you should not place any code within an if __name__ == "__main__" block.

user_name = input('Whom should I sign this to:')
file_name = input('Where shall I save it:')

with open(file_name,'w') as new_file:
    new_file.write(f'Hi {user_name}, we hope you enjoy learning Python with us! Best, Mooc.fi Team')

# 1.5 Appending data to an existing file

# If you want to append data to the end of a file, instead of overwriting the entire file, you should open the file in append mode with the argument a.

# If the file doesn't yet exist, append mode works exatly like write mode.

# The following program opens the file new_file.txt and appends a couple of lines of text to the end:

with open("new_file.txt", "a") as my_file:
    my_file.write("This is the 4th line\n")
    my_file.write("And yet another line.\n")

# 1.6 Diary
# Please write a program which works as a simply diary. The diary entries should be saved in the file diary.txt.
# When the program is executed, it should first read any entries already in the file.

# NB: the automatic tests for this exercise will change the contents of the file. 
# If you want to keep its contents, first make a copy of the file under a different name.

# The program should work as follows:

# Sample output
# 1 - add an entry, 2 - read entries, 0 - quit
# Function: 1
# Diary entry: Today I ate porridge
# Diary saved

# 1 - add an entry, 2 - read entries, 0 - quit
# Function: 2
# Entries:
# Today I ate porridge
# 1 - add an entry, 2 - read entries, 0 - quit
# Function: 1
# Diary entry: I went to the sauna in the evening
# Diary saved

# 1 - add an entry, 2 - read entries, 0 - quit
# Function: 2
# Entries:
# Today I ate porridge
# I went to the sauna in the evening
# 1 - add an entry, 2 - read entries, 0 - quit
# Function: 0
# Bye now!

with open('diary.txt','a') as new_file:
    with open('diary.txt','r') as file:
        fn_number =1
        diary_entry = ''
        diary_list = []
        for i in(file.read().split('\n')):
            if i == '':
                continue
            diary_list.append(i)
        while (fn_number !=0):
            print('1 - add an entry, 2 - read entries, 0 - quit')
            fn_number =int(input('Function:'))
            if  fn_number ==1:
                diary_entry = input('Diary entry:')
                new_file.write(f'{diary_entry}\n')
                diary_list.append(diary_entry)
                print('Diary saved')
            if fn_number ==2 :
                print('Entries:')    
                for i in diary_list:
                    print(f'{i}')
            if ( fn_number ==0):
                print('Bye now!')

# 2. Writing CSV files

# 2.1 first way to write: 
with open("coders.csv", "w") as my_file:
    my_file.write("Eric;Windows;Pascal;10\n")
    my_file.write("Matt;Linux;PHP;2\n")
    my_file.write("Alan;Linux;Java;17\n")
    my_file.write("Emily;Mac;Cobol;9\n")
    
# 2.2 2nd way to write: 
with open("coders.csv", "w") as my_file:
    coders = []
    coders.append(["Eric", "Windows", "Pascal", 10])
    coders.append(["Matt", "Linux", "PHP", 2])
    coders.append(["Alan", "Linux", "Java", 17])
    coders.append(["Emily", "Mac", "Cobol", 9])
    for coder in coders:
        line = f"{coder[0]};{coder[1]};{coder[2]};{coder[3]}"
        my_file.write(line+"\n")
        
# 2.3 3rd wat to write: 

with open("coders.csv", "w") as my_file:
    coders = []
    coders.append(["Eric", "Windows", "Pascal", 10])
    coders.append(["Matt", "Linux", "PHP", 2])
    coders.append(["Alan", "Linux", "Java", 17])
    coders.append(["Emily", "Mac", "Cobol", 9])
    for coder in coders:
        line = ""
        for value in coder:
            line += f"{value};"
        line = line[:-1]
        my_file.write(line+"\n")

# 3 Clearing file contents and deleting files

# 3.1. Sometimes it is necessary to clear the contents of an existing file. 
# Opening the file in write mode and closing the file immediately will achieve just this:

with open("file_to_be_cleared.txt", "w") as my_file:
    pass

# 3.2 Now the with block only contains the command pass, which doesn't actually do anything. 
# Python does not allow empty blocks, so the command is necessary here.

# It is possible to also bypass the with block by using the following oneliner:
open('file_to_be_cleared.txt', 'w').close()

# 3.3 Deleting files:
import os
os.remove('unnecessary_file.txt')


# NB: this will not work when running the automatic tests on the course servers due to technical limitations in the testing environment. 
# If you are asked to clear the contents of a file, use the methods described above.

# 3.4 Filtering the contents of a file

def filter_solutions():
    incorrect_list =[]
    correct_list=[] 
    with open('./solution.csv','r')  as new_file:
        for i in new_file:
            parts =i.split(';')
            if parts[0] == '...jne...':
                continue
            name =parts[0]
            result =int(parts[2])
            number_1 =0
            number_2=0
            if '-' in parts[1]:
                numbers=parts[1].split('-')
                number_1 =float(numbers[0])
                number_2= float(numbers[1])
                if number_1 - number_2 == result:
                    # with open('./correct.csv','w') as correct_file:
                    correct_list.append(f'{name};{parts[1]};{result}\n')
                else:
                    # with open('./incorrect.csv','w') as incorrect_file:
                    incorrect_list.append(f'{name};{parts[1]};{result}\n')
            if '+' in parts[1]:
                numbers=parts[1].split('+')
                number_1 =float( numbers[0])
                number_2= float(numbers[1])
                if number_1 + number_2 == result:
                    # with open('./correct.csv','w') as correct_file:
                    correct_list.append(f'{name};{parts[1]};{result}\n')
                else:
                    # with open('./incorrect.csv','w') as incorrect_file:
                    incorrect_list.append(f'{name};{parts[1]};{result}\n')
    with open('./correct.csv','w') as correct_file:
        for i in correct_list:
            correct_file.write(i)
    with open('./incorrect.csv','w') as incorrect_file:
        for i in incorrect_list:
            incorrect_file.write(i)
    


# 4.1 Store personal data

# Please write a function named store_personal_data(person: tuple), which takes a tuple containing some identifying information as its argument.

# The tuple contains the following elements:

# Name (string)
# Age (integer)
# Height (float)
# This should be processed and written into the file people.csv. The file may already contain some data; the new entry goes to the end of the file. The data should be written in the format

# name;age;height

# Each entry should be on a separate line. If we call the function with the argument ("Paul Paulson", 37, 175.5), the function should write this line to the end of the file:

# Paul Paulson;37;175.5



student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")
exam_point1=input("Exercises points: ")
course_info = input('Course information:')
show_data = ['name','exec_nbr','exec_pts.','exm_pts.','tot_pts.','grade']
student = {}
course_name={}
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

def show_course ():
    with open('./part6/' +course_info,'r') as course_file:
        for i in course_file:
            line =i.split(':')
            course_name[line[0]] = line[1].strip()
def show_information():
    first_line = ''
    line =("{:30}{:10}{:10}{:10}{:10}{:10}\n".format(*show_data))
    list = []
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
        list.append(f"{full_name:<30}{total_exercise:<10}{award_point:<10}{point:<10}{total_score:<10}{grade:<10}\n")
    show_course()
    first_line = f"{course_name['name']}, {course_name['study credits']} credits"
    with open('./result.txt','w') as new_result : 
        new_result.write(first_line + '\n')
        new_result.write(int(len(first_line))*'=' + '\n')
        new_result.write(f'{line}')
        for i in list:
            new_result.write(f'{i}')
    with open('./result.csv','w') as new_result_csv : 
        new_result_csv.write(first_line + '\n')
        new_result_csv.write(int(len(first_line))*'=' + '\n')
        new_result_csv.write(f'{line}')
        for i in list:
            new_result_csv.write(f'{i}')
    print(f'Results written to files results.txt and results.csv')

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
