name = input('Введите имя: ')
surname = input('Введите фамилию: ')
year = int(input('Год рождения: '))
city = input('Город проживания: ')
email = input('Адрес электронной почты: ')
phone_num = int(input('Номер телефона: '))


def folder(name, surname, year, city, email, phone_num):
    return folder(name, surname, year, city, email, phone_num)


resume = f'Имя: {name} *** Фамилия: {surname} *** год: {year} ' \
         f'*** город: {city} *** e-mail: {email} *** номер телефона: {phone_num}'
print(resume)
