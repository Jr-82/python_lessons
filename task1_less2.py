my_list = [True, 1, 1.2, ['hi', 2020], ('stroke', 'must be'), {'first', 'second'}, {'apple': 'яблоко'}]

for i in my_list:
    show = my_list.index(i)
    print(f'***{i} --- {type(i)}')
