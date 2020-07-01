#-------------------------------------------------------------------------------
# Name:        less6 Task3
# v: 3.8.2
# Created:     3023.06.2020
#-------------------------------------------------------------------------------
''' Реализовать базовый класс Worker (работник), в котором определить
атрибуты: name, surname, position (должность), income (доход). Последний
атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс
Position (должность) на базе класса Worker. В классе Position реализовать
методы получения полного имени сотрудника (get_full_name) и дохода с учетом
премии (get_total_income). Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения
атрибутов, вызвать методы экземпляров). '''

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

class Position(Worker):
    def get_full_name(self):
        return(f'{self.surname} {self.name}')

    def get_total_income(self):
        return(self._income['wage'] + self._income['bonus'])


if __name__ == '__main__':
    worker1 = Position('Kim', 'Li', 'manager', 32000, 2000)
    print(worker1.name)
    print(worker1.surname)
    print(worker1.position)
    print(worker1._income)
    print(worker1.get_full_name())
    print(worker1.get_total_income())