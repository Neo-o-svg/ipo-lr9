
def isCorrectRect(coords):
    leftCornerCoords, rightCornerCoords = coords
    x_left, y_left = leftCornerCoords
    x_right, y_right = rightCornerCoords


    if not isinstance(coords, list) or len(coords) != 2:
        return False

    elif not all(
        isinstance(coord_pair, tuple) and len(coord_pair) == 2
        for coord_pair in coords):

        return False

    elif not (
        isinstance(x_left, (int, float))
        and isinstance(y_left, (int, float))
        and isinstance(x_right, (int, float))
        and isinstance(y_right, (int, float))
        ):
        return False
        
    elif (
        (x_left > x_right)
        or (y_left > y_right)
        ):
        return False
        
    return True

