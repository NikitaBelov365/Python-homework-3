""" Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X """

import random

def ListCreation():
    listLength = int(input("Input length of array: "))
    newList = []
    for i in range(listLength):
        newList.append(random.randint(1, 10))
    print(*newList)
    return newList

def Calculation(list):
    value = int(input("Input desired value: "))
    counter = 0
    for i in range(len(list)):
        if list[i] == value:
            counter += 1
    print(counter)

Calculation(ListCreation())