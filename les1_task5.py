#-------------------------------------------------------------------------------
# Name:        less1 Task5
# v: 3.8.2
# Created:     12.06.2020
# Copyright:   (c)
#-------------------------------------------------------------------------------
''' Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение. Если фирма отработала с прибылью,
вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль
фирмы в расчете на одного сотрудника. '''

revenue = input('Your revenue?  ')
costs = input('Your costs?  ')
revenue = float(revenue)
costs = float(costs)


if (revenue <= costs):
    print ('Sorry, the company is unprofitable')
else:
    profit = (revenue - costs)/revenue
    print ('Profit is {}'.format(profit))
    employ = input('Number of employees?  ')
    employ = int(employ)
    print ('Profit is {} per employee'.format((revenue - costs)/employ))


