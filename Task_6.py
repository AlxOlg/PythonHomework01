# Счастливый билет.
number = input('Введите шестизначный номер: ')
if number.isdigit() and len(number) == 6:
    sumLeft = 0
    sumRight = 0
    for i in range(int(len(number) / 2)):
        sumLeft += int(number[i])
        sumRight += int(number[i + int(len(number) / 2)])
    if sumLeft == sumRight:
        print('Билет счастливый!')
    else:
        print('Не повезло.')
else:
    print('Число не соответствует условию!')
