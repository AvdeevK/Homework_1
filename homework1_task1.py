# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
# https://drive.google.com/file/d/1E4sOxnTcbwJPO5unJb7sJf-DM4Tc39dZ/view?usp=sharing

a = int(input('Ведите целое положительное трехзначное число: '))
p = 1
s = 0
b = a % 10
c = (a % 100) // 10
d = a // 100

p = b * c * d
s = b + c + d

print(f'Произведение чисел {p = }, сумма чисел {s = }')
