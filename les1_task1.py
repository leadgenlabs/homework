#-------------------------------------------------------------------------------
# Name:        less1 Task1
# v: 3.8.2
# Created:     12.06.2020
# Copyright:   (c)
#-------------------------------------------------------------------------------
''' Поработайте с переменными, создайте несколько, выведите на экран,
запросите у пользователя несколько чисел и строк и сохраните в
переменные, выведите на экран. '''

bot_name = 'ChatBot'
chat_num = 34567732289
pwd = 'qwerty'

welcom = "Hello! I'm {}.".format(bot_name)
ch_n = "My chat number {}.".format(str(chat_num))
print (welcom, ch_n)

user_log = input('Your login?')
user_age = input('Your age?')
user_pwd = input('Your password?')

if (user_pwd == pwd):
    year_birth = 2020 - int(user_age)
    print ('Welcom {}, Your year of birth {}'.format(user_log, year_birth))
else:
    print ('Access is denied')
