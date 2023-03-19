string = input("Please type in a string: ")
substring = input("Please type in a substring: ")

index = string.find(substring)
if index != -1: 
    new_string = string[index + len(substring):len(string)]
    new_index = new_string.find(substring)
    if new_index != -1:
        print(f'The second occurrence of the substring is at index {new_index + index +len(substring)}.')

    else:
        print(f'The substring does not occur twice in the string.')
else:
    print(f'The substring does not occur twice in the string.')
