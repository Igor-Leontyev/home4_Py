# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, 
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику.
# Она растёт на круглой грядке, причём кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью,
# поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод,
# которое может собрать за один заход собирающий модуль, 
# находясь перед некоторым кустом заданной во входном файле грядки.

import random


def Task_22():
    n = int(input('введите количество элементов первого множества: '))
    m = int(input('введите количество элементов второго множества: '))
    
    list_first = list()
    list_second = list()
    
    for i in range(n):
        list_first.append(random.randint(1,21))
        
    for i in range(m):
        list_second.append(random.randint(1,21))
        
    print(f'первое множество {list_first}')
    print(f'второе множество {list_second}')
        
    set_first = set(list_first)
    set_second = set(list_second)
    
    set_result = (set_first).intersection( set_second)
    
    print(set_result)
    
    
# Task_22()


def Task_24():
    n = int(input('введите количество кустов: '))
    list_kust = list()
    
    for i in range(n):
        list_kust.append(random.randint(20,91))

    print(list_kust)
    max = 0
    list_index = list()
    
    
    for i in range(len(list_kust)-1):
        cur_max = list_kust[i - 1] + list_kust[i] + list_kust[i+1]
        if cur_max > max:
            list_index.clear()
            max = cur_max
            list_index.append(i-1)
            list_index.append(i)
            list_index.append(i+1)
    
    if list_kust[i - 2] + list_kust[i - 1] + list_kust[0] > max:
        max = list_kust[i - 2] + list_kust[i - 1] + list_kust[0]
           
            
    
    print(max)
    print(list_index)
    
Task_24()        
        
    