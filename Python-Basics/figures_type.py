import math
type_figure = input()

if type_figure == 'square':
    square_side = float(input())
    square_area = square_side * square_side
    print(f"{square_area:.3f}")
elif type_figure == 'rectangle':
    rectangle_width = float(input())
    rectangle_lenght = float(input())
    rectangle_area = rectangle_lenght * rectangle_width
    print(f"{rectangle_area:.3f}")
elif type_figure == 'circle':
    circle_radius = float(input())
    circle_area = math.pi * circle_radius * circle_radius
    print(f"{circle_area:.3f}")
elif type_figure == 'triangle':
    triangle_side = float(input())
    triangle_height = float(input())
    triangle_area = (triangle_height * triangle_side) / 2
    print(f"{triangle_area:.3f}")



