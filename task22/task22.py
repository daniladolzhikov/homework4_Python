# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих 
# наборах. Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во 
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

n = int(input("Введите количество элементов первого набора: "))
m = int(input("Введите количество элементов второго набора: "))

set1 = set()
set2 = set()

print("Введите элементы первого набора:")
for _ in range(n):
    num = int(input())
    set1.add(num)

print("Введите элементы второго набора:")
for _ in range(m):
    num = int(input())
    set2.add(num)

common_elements = sorted(set1.intersection(set2))

print("Общие элементы, без повторений и в порядке возрастания:", common_elements)
