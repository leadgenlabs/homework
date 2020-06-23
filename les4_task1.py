#-------------------------------------------------------------------------------
# Name:        less4 Task1
# v: 3.8.2
# Created:     23.06.2020
#-------------------------------------------------------------------------------
''' Реализовать скрипт, в котором должна быть предусмотрена функция расчета
заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах * ставка в час) + премия. Для выполнения расчета для
конкретных значений необходимо запускать скрипт с параметрами. '''

from sys import argv

def calc(w_h:int, w_r:float, w_b:float) -> float:
    """ payroll preparation
    :param w_h: work hours
    :param w_r: rate
    :param w_b: bonus
    :return: wage
    """
    return (int(w_h) * float(w_r) + float(w_b))


scr_name, work_hour, rate, bonus = argv
print(calc(work_hour, rate, bonus))