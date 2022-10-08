a, b = input(), input()
if a == b and (a == 'красный' or a == 'желтый' or a == 'синий'):
    print(a)
elif a == 'красный' and b == 'синий':
    print('фиолетовый')
elif a == 'красный' and b == 'желтый':
    print('оранжевый')
elif a == 'синий' and b == 'желтый':
    print('зеленый')
elif a == 'синий' and b == 'красный':
    print('фиолетовый')
elif a == 'желтый' and b == 'красный':
    print('оранжевый')
elif a == 'желтый' and b == 'синий':
    print('зеленый')
else:
    print("ошибка цвета")
