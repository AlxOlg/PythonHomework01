# Шоколадка m * n долек. Отломить k долек? ОДИН разлом по прямой!
print('Размер шоколадки в дольках:')
n = int(input('n = '))
m = int(input('m = '))
k = int(input('Количество долек = '))
if k < m * n and (k % n == 0 or k % m == 0):
    print('Да')
else:
    print('Нет')
