"""Практическое задание 5"""
print('Напишите программу, которая принимает на вход координаты двух точек'
      ' и находит расстояние между ними в 2D пространстве.')
while True:
    try:
        xA, yA = (int(i) for i in input(
            'Введите через запятую координаты точки A (x,  y): '
        ).split(','))
        xB, yB = (int(i) for i in input(
            'Введите через запятую координаты точки B (x,  y): '
        ).split(','))
        distance = ((xB - xA) ** 2 + (yB - yA) ** 2) ** 0.5
        print(f'A {xA, yA}; B {xB, yB}; -> {round(distance, 2)}')
        break
    except ValueError:
        print('Неверный ввод')
