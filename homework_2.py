"""Практическое задание 2"""
print('Напишите программу для. проверки истинности утверждения '
      '¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.')

predicatesValues = [0, 1]

flag = True

for x in predicatesValues:
    for y in predicatesValues:
        for z in predicatesValues:
            flag = (not(x and y and z) == (not x or not y or not z))
            if not flag:
                break
print('Истинность выражения `¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z` ' + ('верна' if flag else 'не верна'))
