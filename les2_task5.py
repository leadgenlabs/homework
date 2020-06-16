#-------------------------------------------------------------------------------
# Name:        less2 Task5
# v: 3.8.2
# Created:     12.06.2020
#-------------------------------------------------------------------------------
''' Реализовать структуру «Рейтинг», представляющую собой не возрастающий
набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например,
my_list = [7, 5, 3, 3, 2].  '''

my_list = [7, 5, 3, 3, 2]

while True:
    elem = input('Введите элемент или "q" для окончания\n')
    if elem.isdigit():
        my_list.append(int(elem))
        my_list.sort(reverse=True)
        print (my_list)

    elif elem == 'q':
        break
