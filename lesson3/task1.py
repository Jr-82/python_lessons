def div():
    try:
        user_dev = int(input("Введите делимое: "))
        user_diver = int(input("Введите делитель: "))
        res = user_dev / user_diver
    except ValueError:
        return 'Введите число'
    except ZeroDivisionError:
        return "Не верный делитель! По правилам деления, делить на ноль запрещено."
    return res


print(f'Результат  {div()}')
