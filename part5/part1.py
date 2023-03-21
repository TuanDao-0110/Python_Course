# 1. Reminder: using global variables within functions

def print_reversed(names: list):
    # using the global variable instead of the parameter by accident
    i = len(name_list) - 1
    while i >= 0:
        print(name_list[i])
        i -= 1


# here the global variable is assigned
name_list = ["Steve", "Jean", "Katherine", "Paul"]
print_reversed(name_list)
print()
print_reversed(["Huey", "Dewey", "Louie"])
# Paul
# Katherine
# Jean
# Steve

# Paul
# Katherine
# Jean
# Steve


# 2. Warning: overwriting a parameter and returning too early

def number_in_list(numbers: list, number: int):
    for number in numbers:
        if number == number:
            return True
        else:
            return False


found = number_in_list([1, 2, 3, 4], 3)
print(found)  # prints out False


# 3. The longest string
# Please write a function named longest(strings: list), which takes a list of strings as its argument. The function finds and returns the longest string in the list. You may assume there is always a single longest string in the list.

# An example of expected behaviour:
def longest(list):
    longest_string = ''
    for i in list:
        if len(longest_string) < len(i):
            longest_string = i
    return longest_string

if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))
# Sample output
# howdydoody


# 4. Lists within lists

my_list = [[5, 2, 3], [4, 1], [2, 2, 5, 1]]
print(my_list)
print(my_list[1])
print(my_list[1][0])

# result:
# [[5, 2, 3], [4, 1], [2, 2, 5, 1]]
# [4, 1]
# 4


# 5. Accessing items in a matrix

# sum of row: 

def sum_of_row(my_matrix, row_no: int):
    # choose the desired row from within the matrix
    row = my_matrix[row_no]
    row_sum = 0
    for item in row:
        row_sum += item

    return row_sum


m = [[4, 2, 3, 2], [9, 1, 12, 11], [7, 8, 9, 5], [2, 9, 15, 1]]

my_sum = sum_of_row(m, 1)
print(my_sum)  # prints out 33 (which equals 9 + 1 + 12 + 11)

# sum of column:


def sum_of_column(my_matrix, column_no: int):
    # go through each row and select the item at the chosen position
    column_sum = 0
    for row in my_matrix:
        column_sum += row[column_no]

    return column_sum


m = [[4, 2, 3, 2], [9, 1, 12, 11], [7, 8, 9, 5], [2, 9, 15, 1]]

my_sum = sum_of_column(m, 2)
print(my_sum)  # prints out 39 (which equals 3 + 12 + 9 + 15)


# change value:

def change_value(my_matrix, row_no: int, column_no: int, new_value: int):
    # choose the desired row
    row = my_matrix[row_no]
    # select the correct item within the row
    row[column_no] = new_value


m = [[4, 2, 3, 2], [9, 1, 12, 11], [7, 8, 9, 5], [2, 9, 15, 1]]

print(m)
change_value(m, 2, 3, 1000)
print(m)


# upgrade +1 each value; 
m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in range(len(m)):  # using the number of rows in the matrix
    for j in range(len(m[i])):  # using the number of items on each row
        m[i][j] += 1

print(m)


# 6. Number of matching elements


# Please write a function named count_matching_elements(my_matrix: list, element: int), which takes a two-dimensional array of integers and a single integer value as its arguments. The function then counts how many elements within the matrix match the argument value.

# An example of how the function should work:
def count_matching_elements(m, element: int):
    count = 0
    for i in range(len(m)):  # using the number of rows in the matrix
        for j in range(len(m[i])):  # using the number of items on each row
            if m[i][j] == element:
                count += 1
    return count


# 7. A two-dimensional array as a data structure in a game
sudoku = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [0, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [0, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
]


def print_grid(sudoku):
    for row in sudoku:
        for square in row:
            if square > 0:
                print(f" {square}", end="")
            else:
                print(" _", end="")
        print()


print_grid(sudoku)


# The printout should look like this: :

#  9 _ _ _ 8 _ 3 _ _
#  _ _ _ 2 5 _ 7 _ _
#  _ 2 _ 3 _ _ _ _ 4
#  _ 9 4 _ _ _ _ _ _
#  _ _ _ 7 3 _ 5 6 _
#  7 _ 5 _ 6 _ 4 _ _
#  _ _ 7 8 _ 3 9 _ _
#  _ _ 1 _ _ _ _ _ 3
#  3 _ _ _ _ _ _ _ 2


# 7. Go


# In a game of Go two players take turns to place black and white stones on a game board. 
# The winner is the player who manages to encircle a bigger area on the board with their own game pieces.


# Please write a function named who_won(game_board: list), 
# which takes a two-dimensional array as its argument. 
# The array consists of integer values, which represent the following situations:

# 0: empty square
# 1: player 1 game piece
# 2: player 2 game piece
# The scoring rules of Go can be quite complex, but in this exercise it is enough to compare the number of pieces each player has on the game board. Also, the size of the game board is not limited.

# The function should return the value 1 if player 1 won, and the value 2 if player 2 won. 
# If both players have the same number of pieces on the board, the function should return the value 0.
def who_won(game_board: list) -> int:
    p1_score = 0
    p2_score = 0
    for row in game_board:
        for square in row:
            if square == 1:
                p1_score += 1
            elif square == 2:
                p2_score += 1
    if p1_score > p2_score:
        return 1
    elif p2_score > p1_score:
        return 2
    else:
        return 0


# 8. Sudoku: check row


# Please write a function named row_correct(sudoku: list, row_no: int), 
# which takes a two-dimensional array representing a sudoku grid, and an integer referring to a single row, as its arguments. Rows are indexed from 0.

# The function should return True or False, depending on whether the row is filled in correctly,
# that is, whether it contains each of the numbers 1 to 9 at most once.

# sudoku = [
#     [9, 0, 0, 0, 8, 0, 3, 0, 0],
#     [2, 0, 0, 2, 5, 0, 7, 0, 0],
#     [0, 2, 0, 3, 0, 0, 0, 0, 4],
#     [2, 9, 4, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 7, 3, 0, 5, 6, 0],
#     [7, 0, 5, 0, 6, 0, 4, 0, 0],
#     [0, 0, 7, 8, 0, 3, 9, 0, 0],
#     [0, 0, 1, 0, 0, 0, 0, 0, 3],
#     [3, 0, 0, 0, 0, 0, 0, 0, 2]
# ]

# print(row_correct(sudoku, 0))
# print(row_correct(sudoku, 1))

def row_correct(sudoku: list, row_no: int) -> bool:
    row = sudoku[row_no]
    nums = set()
    for num in row:
        if num != 0:
            if num in nums:
                return False
            nums.add(num)
    return True



def column_correct(list, col: int) -> bool:
    column_list = []
    nums = set()
    for row in list:
        column_list.append(row[col])
    for num in column_list:
            if num !=0:
                if num in nums:
                    return False
    return True


def block_correct (list, row_no: int, col_no : int) -> bool:
    block_list = []
    checkList = set()
    for i in range(3):
        # temp = []
        for j in range(3):
            block_list.append(list[row_no + i][col_no + j])
        # block_list.append(temp)
    for num in block_list:
        if num != 0:
            if num in checkList:
                return False
            checkList.add(num)
    return True


def sudoku_grid_correct(sudoku: list) -> bool:
    value = True
    block_coords = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3),
                    (3, 6), (6, 0), (6, 3), (6, 6)]
    while value:
        for i in range(9):
            value = row_correct(sudoku, i)
        for i in range(9):
            value = column_correct(sudoku, i)
        for (i, j) in block_coords:
            value = block_correct(sudoku, i, j)
        break
    return value
