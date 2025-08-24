data = input('data: ')
lst = list(map(int, data.split(',')))

if lst[0] == 3 or lst[-1] == 3:
    print('True')
else:
    print('False')
