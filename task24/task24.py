# # Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой 
# # грядке, причем кусты высажены только по окружности. Таким образом, у каждого куста есть 
# # ровно два соседних. Всего на грядке растет N кустов. i ягод. Эти кусты обладают разной 
# # урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте 
# # выросло aВ этом фермерском хозяйстве внедрена система автоматического сбора черники.
# # Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# # Собирающий модуль за один заход, находясь непосредственно перед некоторым
# # кустом, собирает ягоды с этого куста и с двух соседних с ним.
# # Напишите программу для нахождения максимального числа ягод, которое может
# # собрать за один заход собирающий модуль, находясь перед некоторым кустом
# # заданной во входном файле грядки.

N = int(input("Введите количество кустов: "))  

berries = []  
for i in range(N):
    berry_count = int(input(f"Введите количество ягод на кусте {i+1}: "))
    berries.append(berry_count)

def max_berry_harvest(N, berries):
    s = [0] * N  
    for i in range(N):
        s[i] = berries[i] + berries[(i + 1) % N] + berries[(i - 1) % N]  
    
    max_harvest = max(s)  
    return max_harvest

result = max_berry_harvest(N, berries)

print("Максимальное кол-во за один заход:", result)

