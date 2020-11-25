user_try = input('Введите одно или несколько слов: ')
empty_list = []
digit = 1

for i in range(user_try.count(' ') + 1):
    empty_list = user_try.split()
    if len(str(user_try)) <= 10:
        print(f'{digit} {empty_list [i]}')
        digit += 1
    else:
        print(f'{digit} {empty_list [i] [0:10]}')
#       print(f'{digit} {empty_list [i] [:10]}')   # проверить, есть ли разница
        digit += 1
