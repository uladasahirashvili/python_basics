first_string = input('Enter your 1st string: ')
second_string = input('Enter your 2nd string: ')

if len(first_string) != len(second_string):
    print('Strings must be the same length for a cyclic shift.')
elif second_string in first_string * 2:
    shift_counter = (first_string * 2).find(second_string)
    print(f'The first string is obtained from the second one by a shift of {shift_counter}.')
else:
    print('The first string cannot be obtained from the second one using a cyclic shift.')



