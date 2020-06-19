#-------------------------------------------------------------------------------
# Name:        less3 Task1
# v: 3.8.2
# Created:     19.06.2020
#-------------------------------------------------------------------------------
''' Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов. '''

def my_func(f_n: float, s_n: float, t_n: float) -> float:
    """ takes three positional arguments, and returns the sum of the largest two arguments
    :param f_n: first number
    :param s_n: second number
    :param t_n: third number
    :return: sum of the largest two arguments
    """
    return (sum([f_n, s_n, t_n]) - min([f_n, s_n, t_n]) )

print (my_func(3, 10, 8))
