from os import name

import matplotlib.pyplot as plt
import time

start = time.perf_counter()

INSIDE, LEFT, RIGHT, BOTTOM, TOP = 0, 1, 2, 4, 8


def region_code(x, y, x_min, y_min, x_max, y_max):
    code = INSIDE
    if x < x_min:
        code |= LEFT
    elif x > x_max:
        code |= RIGHT
    if y < y_min:
        code |= BOTTOM
    elif y > y_max:
        code |= TOP
    return code


def sutherland_cohen(x1, y1, x2, y2, x_min, y_min, x_max, y_max):
    code1 = region_code(x1, y1, x_min, y_min, x_max, y_max)
    code2 = region_code(x2, y2, x_min, y_min, x_max, y_max)
    while True:
        if code1 == 0 and code2 == 0:
            return x1, y1, x2, y2
        elif code1 & code2 != 0:
            return None
        else:
            if code1 != 0:
                code_out = code1
            else:
                code_out = code2
            if code_out & TOP:
                x, y = x1 + (x2 - x1) * (y_max - y1) / (y2 - y1), y_max
            elif code_out & BOTTOM:
                x, y = x1 + (x2 - x1) * (y_min - y1) / (y2 - y1), y_min
            elif code_out & RIGHT:
                x, y = x_max, y1 + (y2 - y1) * (x_max - x1) / (x2 - x1)
            elif code_out & LEFT:
                x, y = x_min, y1 + (y2 - y1) * (x_min - x1) / (x2 - x1)
            if code_out == code1:
                x1, y1, code1 = x, y, region_code(x, y, x_min, y_min, x_max, y_max)
            else:
                x2, y2, code2 = x, y, region_code(x, y, x_min, y_min, x_max, y_max)


def plot_lines(lines, x_min, y_min, x_max, y_max):
    fig, ax = plt.subplots()
    ax.plot([x_min, x_max, x_max, x_min, x_min], [y_min, y_min, y_max, y_max, y_min], 'k-', lw=2)
    for line in lines: x1, y1, x2, y2 = line; ax.plot([x1, x2], [y1, y2], 'r--')
    for line in lines:
        result = sutherland_cohen(*line, x_min, y_min, x_max, y_max)
        if result: x1, y1, x2, y2 = result; ax.plot([x1, x2], [y1, y2], 'g-', lw=2)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Sutherland-Cohen Clipping')
    plt.grid(True);
    plt.show()


if "__main__" != name:

    x_min, y_min, x_max, y_max = 50, 10, 150, 100
    lines = [(25, 80, 175, 80), (25, 25, 175, 120), (175, 20, 150, 140)]
    plot_lines(lines, x_min, y_min, x_max, y_max)
    finish = time.perf_counter()
    print('Время работы: ' + str(finish - start))