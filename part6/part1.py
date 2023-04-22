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

    
      
        
    
