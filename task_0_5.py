def area_of_triangle(side1, side2, side3):
    perimeter = side1 + side2 + side3
    smp = 1 / 2 * perimeter
    area = (smp * (smp - side1) * (smp - side2) * (smp - side3)) ** 0.5
    return area


print(area_of_triangle(6, 5, 5))
