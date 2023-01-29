"""Практическое задание 1"""
print('Программа, которая принимает на вход цифру, '
      'обозначающую день недели, и проверяет, является ли этот день выходным.')
while True:
    try:
        dayNumber = int(input('Введите номер дня недели(1-7): '))
        if dayNumber < 1 or dayNumber > 7:
            raise ValueError
        print(f'{dayNumber} -> '+('да' if dayNumber in (6, 7) else 'нет'))
        break
    except ValueError:
        print('Допустимые значения: 1 до 7')
