# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.
# Input:
# 4 4 -> 2 2
# 5 6 -> 2 3

a = int(input("Введите первое число подсказку (результата суммы) "))
b = int(input("Введите второе число подсказку (результата произведения) "))
if 0 < a and b < 1000:
    for i in range(1, (a//2) + 1):
        if (i * (a-i)) == b:
            print(i, a-i)
else:
    print("Введите числа от 0 до 1000")