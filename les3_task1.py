#-------------------------------------------------------------------------------
# Name:        less3 Task1
# v: 3.8.2
# Created:     19.06.2020
#-------------------------------------------------------------------------------
''' Реализовать функцию, принимающую два числа (позиционные аргументы) и
выполняющую их деление. Числа запрашивать у пользователя, предусмотреть
обработку ситуации деления на ноль. '''

def division (first_num: float, sec_num: float) -> float:
    """ dividing two numbers by checking by dividing by 0
    :param first_num: first number
    :param sec_num: second number
    :return: division result
    """
    return (first_num / sec_num)


f_num = input('First number\n')
s_num = input('Second number\n')


if s_num == '0':
    print ('Dividing by 0')
elif f_num.isdigit() & s_num.isdigit():
    print (division(float(f_num), float(s_num)))
else:
    print ('Invalid values')



