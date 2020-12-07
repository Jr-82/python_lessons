def x_pow(x, y):
    digit = 1
    for i in range(y):
        digit *= x
    return digit


user_digit = int(input('Введите возводимое в степень число: '))
user_pow = int(input('Введите желаемую стпень: '))
print(x_pow(user_digit, user_pow))
