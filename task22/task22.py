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
