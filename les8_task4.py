#-------------------------------------------------------------------------------
# Name:        less8 Task4, 5, 6
# v: 3.8.27
# Created:     7.07.2020
#-------------------------------------------------------------------------------
''' Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий
склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом
классе определить параметры, общие для приведенных типов. В классах-наследниках
реализовать параметры, уникальные для каждого типа оргтехники. '''

class Stock:
    def __init__(self, place):
        self.place = place
        self.equip = {'Printer': 0, 'Scaner': 0, 'Xerox': 0}

    def add(self):
        equ = input('Введите название оборудования')
        q = input('Введите количество')
        if isdigit(q):
            temp = self.equip[equ] + int(q)
            self.equip[equ] = temp
        else:
            print('Количество должно быть числом')

        def move(self):
            equ = input('Введите название оборудования')
            q = input('Введите количество')
            if isdigit(q):
                temp = self.equip[equ] - int(q)
                self.equip[equ] = temp
            else:
                print('Количество должно быть числом')

class Equipment:
    def __init__(self, name):
        self.name = name

class Printer(Equipment):
    def __init__(self, net):
        self.net = net

class Scaner(Equipment):
    def __init__(self, color):
        self.color = color

class Xerox(Equipment):
    def __init__(self, speed):
        self.speed = speed