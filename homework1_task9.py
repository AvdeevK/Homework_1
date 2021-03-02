# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
# https://drive.google.com/file/d/1E4sOxnTcbwJPO5unJb7sJf-DM4Tc39dZ/view?usp=sharing

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))

if a > b:
    if a > c:
        if b > c:
            print(f'Среднее число {b}')
        else:
            print(f'Среднее число {c}')
    else:
        print(f'Среднее число {a}')
elif (b > c):
    if (a > c):
        print(f'Среднее число {a}')
    else:
        print(f'Среднее число {c}')
else:
    print(f'Среднее число {b}')


