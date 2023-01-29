"""Практическое задание 2"""
print('Напишите программу для. проверки истинности утверждения '
      '¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.')

predicatesValues = [0, 1]

for x in predicatesValues:
    for y in predicatesValues:
        for z in predicatesValues:
            print(f'Истинность выражения `¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z}` ' +
                  ('верна' if (not(x and y and z) == (not x or not y or not z)) else 'не верна'))
