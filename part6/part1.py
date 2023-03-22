# 1. Reading data from a file
with open("./part1.txt") as new_file:
    contents = new_file.read()
    print(contents)

# 2. Going through the contents of a file


def largest():
    with open('numbers.txt', 'r') as f:
        numbers = [int(line.strip()) for line in f]
        return max(numbers)
