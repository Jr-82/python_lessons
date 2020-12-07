def digit_sum():
    start_num = 0
    lim = False
    while lim is False:
        number = input('Введите целое число или нажмите Й для выхода: ').split()

        res = 0
        for el in range(len(number)):
            if number[el] == 'й' or number[el] == 'Й':
                lim = True
                break
            else:
                res += int(number[el])
                start_num += res
                print(f'Текущая сумму: {start_num}')
    print(f'Итоговая сумма: {start_num}')


digit_sum()
