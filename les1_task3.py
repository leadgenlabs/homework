#-------------------------------------------------------------------------------
# Name:        less1 Task3
# v: 3.8.2
# Created:     12.06.2020
# Copyright:   (c)
#-------------------------------------------------------------------------------
''' Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369 '''

user_num = input('Your number?  ')
str_num = int(user_num) + int(user_num*2) + int(user_num*3)
print(str_num)
