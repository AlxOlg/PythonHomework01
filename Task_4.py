# Петя, Катя и Сережа... S = П + К + С, С = П, К = 2(П + С).
S = int(input('Введите общее количество: '))
# Решение системы уравнений: K = 4П, П = S/6.
# Здесь не плохо было бы проверить делимость S на 6, ответ мог бы быть целым.
Pet = S / 6
Kat = Pet * 4
Ser = Pet
print(f'Петя = {Pet}')
print(f'Катя = {Kat}')
print(f'Серёжа = {Ser}')