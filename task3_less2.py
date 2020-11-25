list_season = ['Зима', 'Весна', 'Лето', 'Осень']
list_month = ['Декабрь', 'Январь', 'Февраль']
diction_season = {1: 'Зима', 2: 'Весна', 3: 'Лето', 4: 'Осень'}
user_num = int(input('Введите номер месяца: '))

if user_num == 12:
    print(f'{list_season[0]} --> {list_month[0]}')
    print(f'{diction_season.get(1)} *** {list_month[0]}')
elif user_num == 1:
    print(f'{list_season[0]} --> {list_month[1]}')
    print(f'{diction_season.get(1)} *** {list_month[1]}')
elif user_num == 2:
    print(f'{list_season[0]} --> {list_month[2]}')
    print(f'{diction_season.get(1)} *** {list_month[2]}')
elif 3 <= user_num <= 5:
    print(list_season[1])
    print(diction_season.get(2))
elif 6 <= user_num <= 8:
    print(list_season[2])
    print(diction_season.get(3))
elif 9 <= user_num <= 11:
    print(list_season[3])
    print(diction_season.get(4))
else:
    print('Двенадцати месяцев достаточно!')
