"""Практическое задание 4"""
print('Напишите программу, которая по заданному номеру четверти, '
      'показывает диапазон возможных координат точек в этой четверти (x и y).')
while True:
    try:
        quarter = int(input('Введите номер четверти: '))
        if quarter < 1 or quarter > 4:
            raise ValueError
        forX = '>'
        forY = '>'
        if quarter == 2:
            forX = '<'
        elif quarter == 3:
            forX = '<'
            forY = '<'
        elif quarter == 4:
            forY = '<'
        print(f'Диапазон возможных координат: x {forX} 0, y {forY} 0')
        break
    except ValueError:
        print('Допустимые значения: от 1 до 4')
