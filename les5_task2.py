#-------------------------------------------------------------------------------
# Name:        less5 Task2
# v: 3.8.2
# Created:     26.06.2020
#-------------------------------------------------------------------------------
''' Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке. '''


with open ('task2.txt', 'r') as file:
    strings = file.readlines()
    print(f'{len(strings)} strings of file')
    for idn, num in enumerate(strings):
        num = len(num.split(' '))
        print(f'{num} word(s) in {idn + 1} string')

