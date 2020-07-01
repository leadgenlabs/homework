#-------------------------------------------------------------------------------
# Name:        less6 Task1
# v: 3.8.2
# Created:     30.06.2020
#-------------------------------------------------------------------------------
''' Создать класс TrafficLight (светофор) и определить у него один атрибут color
(цвет) и метод running (запуск). Атрибут реализовать как приватный. В рамках
метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго
(желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. Переключение
 режимами должно осуществляться только в указанном порядке (красный, желтый,
 зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении
выводить соответствующее сообщение и завершать скрипт. '''

import colorama
from time import sleep

colorama.init() #for win10
#print(colorama.Fore.GREEN + 'Green')


class TrafficLight:
    def __init__(self, color):
        self.__color = color

    def running(self):
        if self.__color == 'red':
            print(colorama.Fore.RED + self.__color)
            sleep(7)
            self.__color = 'yellow'
            print(colorama.Fore.YELLOW + self.__color)
            sleep(2)
            self.__color = 'grin'
            print(colorama.Fore.GREEN + self.__color)
            sleep(7)
        else:
            print('Script interrupted')

if __name__ == '__main__':
    traf = TrafficLight('red')
    traf.running()

