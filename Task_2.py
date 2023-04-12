# Сумма цифр трехзначного числа.
number = input('Введите трехзначное число: ')
if number.isdigit() and len(number) == 3:
# Вариант 1.
    sum = 0
    for i in range(len(number)):
        sum += int(number[i])
    print(f'Сумма цифр числа {number} = {sum}')
# Вариант 2.
    sum = 0
    n = int(number)
    while n > 0:
        x = n % 10
        sum += x
        n //= 10
    print(f'Сумма цифр числа {number} = {sum}')
else:
    print('Число не соответствует условию!')
