name = input('Please tell me your name:')
if name == 'Jerry':
    print('Next Please')
else: 
    portions = int(input('How many portions of soup?'))
    single_portion = 5.9
    sum = float(single_portion * portions)
    print(f'The Total Cost is {sum}')
    print('Next Please')