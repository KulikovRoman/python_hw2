# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2^k), 
# не превосходящие числа N.

a = int(input("Введите целое число "))
for i in range(0, a+1):
    if 2**i <= a:
        print(2**i)

#mЧерез while
# n = int(input("Введите число N: "))
# power = 1
# while power <= n:
#     print(power)
#     power *= 2