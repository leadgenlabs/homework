#-------------------------------------------------------------------------------
# Name:        less1 Task2
# v: 3.8.2
# Created:     12.06.2020
# Copyright:   (c)
#-------------------------------------------------------------------------------
''' Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды
и выведите в формате чч:мм:сс.
Используйте форматирование строк. '''

time = input('Input time')
time = int(time)
time_h = time // 3600 # hours
time_m = (time//60) % 60 # minutes
time_s = time % 60 # sec
if time_m < 10 :
    time_m = '0{}'.format(time_m)
if time_h < 10 :
    time_h = '0{}'.format(time_h)
if time_s < 10 :
    time_s = '0{}'.format(time_s)


print ('{}:{}:{}'.format(time_h, time_m, time_s))