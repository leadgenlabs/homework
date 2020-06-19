#-------------------------------------------------------------------------------
# Name:        less3 Task1
# v: 3.8.2
# Created:     19.06.2020
#-------------------------------------------------------------------------------
''' Реализовать функцию, принимающую несколько параметров, описывающих данные
пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой. '''

def user_info (name: str, sec_name: str, y_b: str, sity: str, mail: str, phone: str) -> str:
    """ displays user data
    :param name: first name
    :param sec_name: second name
    :param y_b: year of birth
    :param sity: sity
    :param mail: e-mail
    :param phone: telephone number
    :return: users data string
    """
    return (f'{name} {sec_name} {y_b} {sity} {mail} {phone}')

n = 'Max'
sn = 'Li'
y = '2006'
s = 'Seoul'
m = 'manage@gmail.com'
p = '+8223182116'

print (user_info(name = n, sec_name = sn, y_b = y, sity = s, mail = m, phone = p))