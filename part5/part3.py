# 1. Using a dictionary

# The following example shows you how the dictionary data structure works.
# Here is a simple dictionary from Finnish to English:
my_dictionary = {}

my_dictionary["apina"] = "monkey"
my_dictionary["banaani"] = "banana"
my_dictionary["cembalo"] = "harpsichord"

print(len(my_dictionary))
print(my_dictionary)
print(my_dictionary["apina"])


# 2. What can be stored in a dictionary?
# The data type is called dictionary, but it does not have to contain only strings. For example, in the following dictionary the keys are strings, but the values are integers:

results = {}
results["Mary"] = 4
results["Alice"] = 5
results["Larry"] = 2
# Here the keys are integers and the values are lists:

lists = {}
lists[5] = [1, 2, 3]
lists[42] = [5, 4, 5, 4, 5]
lists[100] = [5, 2, 3]


# 3. How keys and values work
# Each key can appear only once in the dictionary. If you add an entry using a key that already exists in the dictionary, the original value mapped to that key is replaced with the new value:

my_dictionary["suuri"] = "big"
my_dictionary["suuri"] = "large"
print(my_dictionary["suuri"])

# 4. Times ten


def times_ten(start_index: int, end_index: int):
    list = {}
    for i in range(start_index, end_index + 1):
        list[i] = i * 10
    return list


d = times_ten(3, 6)
print(d)


# 5. Factorials
def factorials(n: int) -> dict:
    factorials_dict = {}
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
        factorials_dict[i] = factorial
    return factorials_dict


k = factorials(5)
print(k[1])
print(k[3])
print(k[5])


# 6. Traversing a dictionary


my_dictionary = {}

my_dictionary["apina"] = "monkey"
my_dictionary["banaani"] = "banana"
my_dictionary["cembalo"] = "harpsichord"

for key in my_dictionary:
    print("key:", key)
    print("value:", my_dictionary[key])

# or we can write:


for key, value in my_dictionary.items():
    print("key:", key)
    print("value:", value)

# 7. Some more advanced ways to use dictionaries


word_list = [
    "banana", "milk", "beer", "cheese", "sourmilk", "juice", "sausage",
    "tomato", "cucumber", "butter", "margarine", "cheese", "sausage",
    "beer", "sourmilk", "sourmilk", "butter", "beer", "chocolate"
]


def counts(my_list):
    words = {}
    for word in my_list:
        # if the word is not yet in the dictionary, initialize the value to zero
        if word not in words:
            words[word] = 0
        # increment the value
        words[word] += 1
    return words


# call the function
print(counts(word_list))


# What if we wanted to categorize the words based on the initial letter in each word? One way to accomplish this would be to use dictionaries:


def categorize_by_initial(my_list):
    groups = {}
    for word in my_list:
        initial = word[0]
        # initialize a new list when the letter is first encountered
        if initial not in groups:
            groups[initial] = []
        # add the word to the appropriate list
        groups[initial].append(word)
    return groups


groups = categorize_by_initial(word_list)

for key, value in groups.items():
    print(f"words beginning with {key}:")
    for word in value:
        print(word)


# 8. phonebook:

phone_book = {}

while True:
    command = input("command (1 search, 2 add, 3 quit): ")
    if command == "1":
        name = input("name: ")
        if name in phone_book:
            numbers = phone_book[name]
            for number in numbers:
                print(number)
        else:
            print("no number")
    elif command == "2":
        name = input("name: ")
        number = input("number: ")
        if name in phone_book:
            phone_book[name].append(number)
        else:
            phone_book[name] = [number]
        print("ok!")
    elif command == "3":
        print("quitting...")
        break


# 9. Removing keys and values from a dictionary vs "del" vs "pop"


#9.1 There are two ways to accomplish this. The first is the command del:

staff = {"Alan": "lecturer", "Emily": "professor", "David": "lecturer"}
del staff["David"]
print(staff)
# Sample output
# {'Alan': 'lecturer', 'Emily': 'professor'}


# If you try to use the del command to delete a key which doesn't exist in the dictionary, there will be an error:
# So, before deleting a key you should check if it is present in the dictionary:
staff = {"Alan": "lecturer", "Emily": "professor", "David": "lecturer"}
if "Paul" in staff:
    del staff["Paul"]
    print("Deleted")
else:
    print("This person is not a staff member")


# 9.2 As you can see above, pop also returns the value from the deleted entry.
staff = {"Alan": "lecturer", "Emily": "professor", "David": "lecturer"}
deleted = staff.pop("Paul", None)
if deleted == None:
    print("This person is not a staff member")
else:
    print(deleted, "deleted")
# Sample output
# This person is not a staff member


# 9.3 NB: if you need to delete the contents of the entire dictionary, and try to do it with a for loop, like so

staff = {"Alan": "lecturer", "Emily": "professor", "David": "lecturer"}
for key in staff:
  del staff[key]
# you will receive an error message:

# Sample output
# RuntimeError: dictionary changed size during iteration

# 9.4 delete all:
staff.clear()


# 10. Invert a dictionary


s = {1: "first", 2: "second", 3: "third", 4: "fourth"}


def invert(dictionary: dict):
    new_dict = {}
    for key, value in dictionary.items():
        new_dict[value] = key
    dictionary.clear()
    dictionary.update(new_dict)


print(s)


# 11. Number spelled out: 

def dict_of_numbers():
    # Define a list of numbers spelled out in words
    spellings = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen",
        "twenty", "twenty-one", "twenty-two", "twenty-three", "twenty-four", "twenty-five", "twenty-six", "twenty-seven", "twenty-eight", "twenty-nine",
        "thirty", "thirty-one", "thirty-two", "thirty-three", "thirty-four", "thirty-five", "thirty-six", "thirty-seven", "thirty-eight", "thirty-nine",
        "forty", "forty-one", "forty-two", "forty-three", "forty-four", "forty-five", "forty-six", "forty-seven", "forty-eight", "forty-nine",
        "fifty", "fifty-one", "fifty-two", "fifty-three", "fifty-four", "fifty-five", "fifty-six", "fifty-seven", "fifty-eight", "fifty-nine",
        "sixty", "sixty-one", "sixty-two", "sixty-three", "sixty-four", "sixty-five", "sixty-six", "sixty-seven", "sixty-eight", "sixty-nine",
        "seventy", "seventy-one", "seventy-two", "seventy-three", "seventy-four", "seventy-five", "seventy-six", "seventy-seven", "seventy-eight", "seventy-nine",
        "eighty", "eighty-one", "eighty-two", "eighty-three", "eighty-four", "eighty-five", "eighty-six", "eighty-seven", "eighty-eight", "eighty-nine",
        "ninety", "ninety-one", "ninety-two", "ninety-three", "ninety-four", "ninety-five", "ninety-six", "ninety-seven", "ninety-eight", "ninety-nine"
    ]
    # Create a dictionary with the numbers as keys and the corresponding spellings as values
    numbers = {i: spellings[i] for i in range(len(spellings))}
    return numbers


# 12. Using dictionaries for structured data


# 13. Find movies

database = [{"name": "Gone with the Python", "director": "Victor Pything", "year": 2017, "runtime": 116},
            {"name": "Pythons on a Plane", "director": "Renny Pytholin",
                "year": 2001, "runtime": 94},
            {"name": "Dawn of the Dead Programmers", "director": "M. Night Python", "year": 2011, "runtime": 101}]


def find_movies(database, search_term):
    """
    Return a list of movies whose title includes the given search term.
    """
    matching_movies = []
    for movie in database:
        if search_term.lower() in movie['name'].lower():
            matching_movies.append(movie)
    return matching_movies

my_movies = find_movies(database, "python")
print(my_movies)
