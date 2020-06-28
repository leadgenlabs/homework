#-------------------------------------------------------------------------------
# Name:        less5 Task3
# v: 3.8.2
# Created:     26.06.2020
#-------------------------------------------------------------------------------
''' Создать текстовый файл (не программно), построчно записать фамилии
сотрудников и величину их окладов. Определить, кто из сотрудников имеет
оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет
средней величины дохода сотрудников. '''

def file_to_dic(fname:str) -> dict:
    """ returns dictionary from file
    :param fname: name of file
    :return: returns dictionary
    """
    with open(fname, 'r') as file:
        strings = file.read().split('\n')
        return {el.split(' ')[0]:el.split(' ')[1] for el in strings}


if __name__ == '__main__':
    temp = 0
    df = file_to_dic('task3.txt')
    for key, value in df.items():
        if int(value) < 20000:
            print(key)
        temp += int(value)
    print(f'Average salary {temp /len(df)}')
