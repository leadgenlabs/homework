#-------------------------------------------------------------------------------
# Name:        less5 Task4
# v: 3.8.2
# Created:     26.06.2020
#-------------------------------------------------------------------------------
''' Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую
построчно данные. При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл. '''

def transl(sourse: str) -> str:
    """ returns
    :param sourse: sourse string
    :return: translated string
    """
    tr_dic = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
    temp = sourse.split(' — ')
    return '{0} — {1}'.format(tr_dic[temp[0]],temp[1])

with open ('task4.txt', 'r') as file:
    strings = file.readlines()

out = map(transl, strings)

with open ('task4_1.txt', 'w') as file:
    file.write(''.join(out))