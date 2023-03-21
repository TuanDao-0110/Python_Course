# 1. The function id can be used to find out the exact location the variable points to:

a = [1, 2, 3]
print(id(a))
b = "This is a reference, too"
print(id(b))
# Sample output
# 4538357072
# 4537788912


# The reference, or the ID of the variable, is an integer,
# which can be thought of as the address in computer memory where the value of the variable is stored.
# If you execute the above code on your own computer, the result will likely be different,
# as your variables will point to different locations - the references will be different.


# 2. immutable:
# Many of the builtin types in Python, such as str, are immutable. This means the value of the object, or any part of it, cannot change. 
# The value can be replaced with a new value:
b = "This is a reference, too"
print(id(b))
b = 'new string'
print(id(b))

# result:
# 4345992560
# 4345845808

# 3. mutable:
a = [1, 2, 3]
print(id(a))
a[0] = 10
print(id(a))

# result:

# 4337457920
# 4337457920


# 4. Multiple references to the same list
list1 = [1, 2, 3, 4]
list2 = list1

list1[0] = 10
list2[1] = 20

print(list1)
print(list2)


# result:

# [10, 20, 3, 4]
# [10, 20, 3, 4]


# 5. Copying a list --> as separate copy of a list:

my_list = [1, 2, 3, 3, 5]

new_list = []
for item in my_list:
    new_list.append(item)

new_list[0] = 10
new_list.append(6)
print("the original:", my_list)
print("the copy:", new_list)
# Sample output
# my_list[1, 2, 3, 3, 5]
# new_list[10, 2, 3, 3, 5, 6]


# An easier way to copy a list is the bracket operator []

my_list = [1, 2, 3, 4]
new_list = my_list[:]

my_list[0] = 10
new_list[1] = 20

print(my_list)
print(new_list)
# Sample output
# [10, 2, 3, 4]
# [1, 20, 3, 4]


# 6. Using lists as parameters in functions


def add_item(my_list: list):
    new_item = 10
    my_list.append(new_item)


a_list = [1, 2, 3]
print(a_list)
add_item(a_list)
print(a_list)
# Sample output

# [1, 2, 3]
# [1, 2, 3, 10]


# Another way to implement this functionality would be to create a new list within the function, and return that:

def add_item(my_list: list) -> list:
    new_item = 10
    my_list_copy = my_list[:]
    my_list_copy.append(new_item)
    return my_list_copy


numbers = [1, 2, 3]
numbers2 = add_item(numbers)

print("original list:", numbers)
print("new list:", numbers2)
# Sample output
# original list: [1, 2, 3]
# new list: [1, 2, 3, 10]


# 7. Editing a list given as an argument
# This function wont work: when attempt to change variable out function:
def augment_all(my_list: list):
    new_list = []
    for item in my_list:
        new_list.append(item + 10)
    my_list = new_list


numbers = [1, 2, 3]
print("in the beginning:", numbers)
augment_all(numbers)
print("after the function is executed:", numbers)

# One way to fix this is to copy all the items from the new list to the old list, one by one:


def augment_all(my_list: list):
    new_list = []
    for item in my_list:
        new_list.append(item + 10)

    # copy items from the new list into the old list
    for i in range(len(my_list)):
        my_list[i] = new_list[i]

# or 


def augment_all(my_list: list):
    new_list = []
    for item in my_list:
        new_list.append(item + 10)

    my_list[:] = new_list

# Actually, there is no need to create a new list within the function at all. We can just assign the new values directly into the original list:


def augment_all(my_list: list):
    for i in range(len(my_list)):
        my_list[i] += 10

# 8. Items multiplied by two


def print_sudoku(sudoku):
    for i in range(len(sudoku)):
        for j in range(len(sudoku[i])):
            if sudoku[i][j] == 0:
                print("_", end=" ")
            else:
                print(sudoku[i][j], end=" ")
            if (j + 1) % 3 == 0 and j < 8:
                print("", end=" ")
        print()
        if (i + 1) % 3 == 0 and i < 8:
            print(" " * 11)


def add_number(sudoku, row_no: int, col_no: int, number: int):
    sudoku[row_no][col_no] = number

# 9. Sudoku: add number to a copy of the grid

def copy_and_add(sudoku, row_no, col_no, number):
    # create a new copy of the input grid using list comprehension
    copy_grid = [[sudoku[row][col] for col in range(9)] for row in range(9)]
    # modify the value at the specified row and column in the new copy
    copy_grid[row_no][col_no] = number
    return copy_grid


# 10. Tic-Tac-Toe
game_board = [["", "", ""], ["", "", ""], ["", "", ""]]

def play_turn(game_board: list, x: int, y: int, piece: str):
    if x < 3 and y < 3 and y >= 0 and x >= 0:
        if game_board[y][x] == '':
            game_board[y][x] = piece
            return True
        return False
    return False


print(play_turn(game_board, 2, 0, "X"))

print(game_board)

# 11. Transpose a matrix


def transpose(matrix: list) -> list:
    n = len(matrix)
    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix


# Side effects of functions
# Let's take a look at a function which is supposed to find the second smallest item in a list:


def second_smallest(my_list: list) -> int:
    # in an ordered list, the second smallest item is at index 1
    my_list.sort()
    return my_list[1]


numbers = [1, 4, 2, 5, 3, 6, 4, 7]
print(second_smallest(numbers))
print(numbers)
# Sample output

# 2
# [1, 2, 3, 4, 4, 5, 6, 7]
# The function does find the second smallest item reliably, but it additionally sorts the list in place, changing the order of the items. If the order is significant elsewhere in the program, calling the function could cause errors. Unintentional modifications to an object accessed through a reference is called a side effect of a function.

# We can avoid the side effect by making a small change to the function:


def second_smallest(my_list: list) -> int:
    list_copy = sorted(my_list)
    return list_copy[1]


numbers = [1, 4, 2, 5, 3, 6, 4, 7]
print(second_smallest(numbers))
print(numbers)
# Sample output
# 2
# [1, 4, 2, 5, 3, 6, 4, 7]

# The function sorted returns a new, sorted copy of the list, so looking for the second smallest item no longer messes with the order of the original list.
