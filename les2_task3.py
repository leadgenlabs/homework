#-------------------------------------------------------------------------------
# Name:        less2 Task3
# v: 3.8.2
# Created:     12.06.2020
#-------------------------------------------------------------------------------
'''Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому
времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict. '''

while True:
    month = input('Введите месяц\n')
    if month.isdigit():
        month = int(month)
        if month > 12:
            print('В году 12 месяцев!')
            continue
        break

# with list
seasons_list = ['зима', 'весна', 'лето', 'осень', 'зима']
print ('На календаре', seasons_list[month // 3])


# with dict
seasons_dic = {1:'зима', 2:'зима', 3:'весна', 4:'весна', 5:'весна', 6:'лето',
    7:'лето', 8:'лето', 9:'осень', 10:'осень', 11:'осень', 12:'зима'}
print ('На календаре', seasons_dic[month])
