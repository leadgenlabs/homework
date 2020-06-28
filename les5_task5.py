#-------------------------------------------------------------------------------
# Name:        less5 Task5
# v: 3.8.2
# Created:     26.06.2020
#-------------------------------------------------------------------------------
''' Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле
выводить ее на экран. '''

import random

num = 20 #number of elements
with open ('task5.txt', 'w') as file:
    string = [str(random.randint(0, 200)) for idn in range(num)]
    file.write(' '.join(string))

with open ('task5.txt', 'r') as file:
    strings = file.read()
    print(sum(map(int, strings.split(' '))))

