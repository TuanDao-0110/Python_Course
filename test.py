from math import floor

number = float(input('Please type in a number:'))
interger = floor(number)
decimal =float( number- interger)
print(f'Integer part: {interger}')
print(f'Decimal part: {decimal}')
