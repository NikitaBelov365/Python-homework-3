""" Задача 18: Требуется найти в массиве A[1..N] самый близкий по
величине элемент к заданному числу X. Пользователь в первой строке
вводит натуральное число N – количество элементов в массиве. 
В последующих строках записаны N целых чисел Ai. Последняя строка
содержит число X """

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
    crutch = 0
    for i in range(len(list)):
        if list[i] == value:
            print(value)
            crutch = 1
    if crutch == 0:
        minDiff = 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        searchedValue = None
        for i in range(len(list)):
            if abs(value - list[i]) < minDiff:
                minDiff = abs(value - list[i])
                searchedValue = list[i]
        print(searchedValue)

Calculation(ListCreation())