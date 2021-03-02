# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
#https://drive.google.com/file/d/1E4sOxnTcbwJPO5unJb7sJf-DM4Tc39dZ/view?usp=sharing

a = int(input('Введите номер буквы латинского алфавита: '))
a = chr(a + 96)
print(f'Буква, соответствующая данному номеру - {a}')
