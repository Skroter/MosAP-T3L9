﻿list1 = set(input("Введите первый список: ").split())
list2 = set(input("Введите второй список: ").split())
print("Наименьшее колличество чисел в списках:", len(list1&list2))

# print("Наименьшее колличество чисел в списках:", len(set(input("Введите первый список: ").split()) & set(input("Введите второй список: ").split()))) # тоже работает, но читается труднее