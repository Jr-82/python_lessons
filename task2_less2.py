user_el = int(input('Введите количество требуемых элементов: '))
empty_list = []
count = 0
element = 0

while count < user_el:
    empty_list.append(input('Введите элемент: '))
    count += 1
print(empty_list)

for place_el in range(int(len(empty_list)/2)):
    empty_list[element], empty_list[element + 1] = empty_list[element + 1], empty_list[element]
    element += 2
print(empty_list)
