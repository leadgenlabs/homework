#-------------------------------------------------------------------------------
# Name:        less8 Task2
# v: 3.8.27
# Created:     7.07.2020
#-------------------------------------------------------------------------------
''' Создайте собственный класс-исключение, обрабатывающий ситуацию деления на
нуль. Проверьте его работу на данных, вводимых пользователем. При вводе
пользователем нуля в качестве делителя программа должна корректно обработать
эту ситуацию и не завершиться с ошибкой. '''

class DivZerError(Exception):
    def __init__(self, txt):
        self.txt = txt


if __name__ == '__main__':
    first = input("First number: ")
    second = input("Second number: ")
    try:
        if int(second) == 0:
            raise DivZerError("Division by zero!")
    except DivZerError as err:
        print(err)
    else: print (int(first) / int(second))
