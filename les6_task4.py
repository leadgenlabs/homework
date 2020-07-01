#-------------------------------------------------------------------------------
# Name:        less6 Task4
# v: 3.8.2
# Created:     30.06.2020
#-------------------------------------------------------------------------------
''' Реализуйте базовый класс Car. У данного класса должны быть следующие
атрибуты: speed, color, name, is_police (булево). А также методы: go, stop,
turn(direction), которые должны сообщать, что машина поехала, остановилась,
повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar,
WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен
показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и
40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ
к атрибутам, выведите результат. Выполните вызов методов и также покажите
результат. '''

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return(f'{self.name} rides')

    def stop(self):
        return(f'{self.name} is stopped')

    def turn(self, direction):
        return(f'{self.name} turn to {direction}')

    def show_speed(self):
        return(f"{self.name}'s speed is {self.speed}")

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return(f"{self.name}'s speed is {self.speed} Speed exceeded!!!")
        else:
            return(f"{self.name}'s speed is {self.speed}")
class SportCar(Car):
    pass
class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return(f"{self.name}'s speed is {self.speed} Speed exceeded!!!")
        else:
            return(f"{self.name}'s speed is {self.speed}")
class PoliceCar(Car):
    pass




if __name__ == '__main__':

    car1 = TownCar(10, 'red', 'Hammer', False)
    print(car1.name)
    print(car1.color)
    print(car1.speed)
    print(car1.is_police)
    print(car1.go())
    print(car1.stop())
    print(car1.turn('left'))
    print(car1.show_speed())

    car2 = PoliceCar(100, 'black', 'Kia', True)
    print(car2.name)
    print(car2.color)
    print(car2.speed)
    print(car2.is_police)
    print(car2.go())
    print(car2.stop())
    print(car2.turn('left'))
    print(car2.show_speed())

    car3 = WorkCar(80, 'green', 'Volvo', False)
    print(car3.name)
    print(car3.color)
    print(car3.speed)
    print(car3.is_police)
    print(car3.go())
    print(car3.stop())
    print(car3.turn('left'))
    print(car3.show_speed())

    car4 = SportCar(80, 'orange', 'Mustang', False)
    print(car4.name)
    print(car4.color)
    print(car4.speed)
    print(car4.is_police)
    print(car4.go())
    print(car4.stop())
    print(car4.turn('left'))
    print(car4.show_speed())


