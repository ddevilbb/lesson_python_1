"""Практическое задание 3"""
print('Напишите программу, которая принимает на вход координаты точки (X и Y), '
      'причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, '
      'в которой находится эта точка (или на какой оси она находится).')
while True:
    try:
        x = int(input('Введите координату x: '))
        y = int(input('Введите координату y: '))
        if x == 0 or y == 0:
            raise ValueError
        if x > 0 and y > 0:
            quarter = 1
        elif x < 0 < y:
            quarter = 2
        elif x < 0 and y < 0:
            quarter = 3
        else:
            quarter = 4
        print(f'x={x}; y={y}; -> {quarter}')
        break
    except ValueError:
        print('x и y должны быть числами, не равными 0')
