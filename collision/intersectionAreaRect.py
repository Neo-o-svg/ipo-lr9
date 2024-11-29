from .isCorrectRect import isCorrectRect


class ValueError(Exception):
    pass


def intersectionAreaRect(list_1, list_2):

    firstRectangleCoords, secondRectangleCoords = list_1, list_2

    if not isCorrectRect(firstRectangleCoords):
        raise ValueError("1й прямоугольник некорректный")

    elif not isCorrectRect(secondRectangleCoords):
        raise ValueError("2й прямоугольник некорректный")

    else:

        (x1_left, y1_left), (x1_right, y1_right) = firstRectangleCoords
        (x2_left, y2_left), (x2_right, y2_right) = secondRectangleCoords

        if (
            (x1_left > x2_right)
            or (y1_left > y2_right)
            or (x1_right < x2_left)
            or (y1_right < y2_left)
        ):
            return "Площадь равна 0"

        xCross_left = max(x1_left, x2_left)
        yCross_bottom = max(y1_left, y2_left)
        xCross_right = min(x1_right, x2_right)
        yCross_top = min(y1_right, y2_right)

        crossWidth = xCross_right - xCross_left
        crossHeight = yCross_top - yCross_bottom

        square = crossWidth * crossHeight

        return f"Площадь равна {square}"


