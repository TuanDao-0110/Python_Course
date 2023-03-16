# 1. 
# Thus far, every program we have written has been executed line by line in order.
# Instead of executing every line of code every single time a program is run, it is often useful to create sections of the program which are are only executed in certain situations.
# Example: 

age = int (input('How old are you? '))

if age > 20:
    print('age > 20')
    print('age <20')
print('age = 20')
