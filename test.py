

def sum_each_row(row):
    sum =0
    line= row.replace('\n','').split(',')
    for i in line:
        sum += int(i)
    return sum

def row_sums ():
    rows_sum =[]
    with open('./part6/matrix.txt','r') as new_file:
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
    with open('./part6/matrix.txt','r') as new_file:
        for line in new_file: 
            temp =line.replace('\n','').split(',')
            for i in temp:
                list.append(int(i))
    return max(list)
        
print(matrix_sum())
print(matrix_max())            
        
    
