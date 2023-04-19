# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть
# Input:
# 5 -> 1 0 1 1 0
# Output:
# 2

# Орел = 0
# Решко = 1

import random

# Формирование списка данных 
count_coin = int(input("Введите общее кол-во монет: "))
temps = []
for i in range(count_coin):
    n = random.randint(0, 1)
    temps.append(n)
print(temps)

# Вычисление суммы решек
# sum_coin = 0
# count = 0   # счетчик
# for n in temps:
#     if count < count_coin and n > 0:
#         sum_coin += 1
# print(sum_coin)
sum_coin = sum(temps)

# Вычисление минимального кол-ва перевертываний
min_count_flip = 0
if count_coin - sum_coin < sum_coin:
    min_count_flip = count_coin - sum_coin
else:
    min_count_flip = sum_coin
print(f"Минимальное количество монет, которые нужно перевернуть > {min_count_flip}")