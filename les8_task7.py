#-------------------------------------------------------------------------------
# Name:        less8 Task7
# v: 3.8.27
# Created:     7.07.2020
#-------------------------------------------------------------------------------
''' Реализовать проект «Операции с комплексными числами». Создайте класс
«Комплексное число», реализуйте перегрузку методов сложения и умножения
комплексных чисел. Проверьте работу проекта, создав экземпляры класса
(комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата. '''

class Compl:
    def __init__(self, num, inum):
        self.num = num
        self.inum = inum

    def __add__(self, other):
        return Compl(self.num + other.num, self.inum+other.inum)

    def __mul__(self, other):
        #a+ib * c+id = (ac-bd)+i(ad+cb)
        return Compl(self.num * other.num - self.inum * other.inum, self.num * other.inum + self.inum * other.num)


if __name__ == '__main__':
    c1 = Compl(1, 2)
    c2 = Compl(3, 4)
    c3 = c1 + c2
    c4 = c1 * c2
    print (c3.num, c3.inum)
    print (c4.num, c4.inum)

