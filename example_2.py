a = int(input())
if a < 0 or a > 36:
    print('ошибка ввода')
elif a == 0:
    print('зеленый')
elif a <= 10 and a % 2 == 1 or 10 < a <= 18 and a % 2 == 0 or 18 < a <= 28 and a % 2 == 1 or 28 < a <= 36 and a % 2 == 0:
    print('красный')
else:
    print("черный")
