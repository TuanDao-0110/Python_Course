def largest():
    with open('numbers.txt', 'r') as f:
        numbers = [int(line.strip()) for line in f]
        
        return max(numbers)
