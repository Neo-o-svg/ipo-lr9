
from collision import *

print(isCorrectRect([(-3.4, 1), (9.2, 10)]))
print(isCorrectRect([(-7, 9), (3, 6)]))


print(isCollisionRect([(-3.4, 1), (9.2, 10)], [(-7.4, 0), (13.2, 12)]))

print(isCollisionRect([(1, 1), (2, 2)], [(3, 0), (13, 1)]))

print(isCollisionRect([(1, 1), (2, 2)], [(3, 17),(13, 1)]))


print(intersectionAreaRect([(-3, 1), (9, 10)], [(-7, 0), (13, 12)]))

print(intersectionAreaRect([(1, 1), (2, 2)], [(3, 0), (13, 1)]))

print(intersectionAreaRect([(1, 1), (2, 2)], [(3, 17), (13, 1)]))


rectangles = [
    [(-3, 1), (9, 10)],
    [(-7, 0), (13, 12)],
    [(0, 0), (5, 5)],
    [(2, 2), (7, 7)]
]

result = intersectionAreaMultiRect(rectangles)
print(f"Уникальная площадь пересечения: {result}")


incorrect_rectangles = [
    [(-3, 1), (9, 10)],
    [(3, 17), (13, 1)]
]
print(intersectionAreaMultiRect(incorrect_rectangles))
