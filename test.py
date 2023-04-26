
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
