import matplotlib.pyplot as plt
import time

start = time.perf_counter()


def clip_line(x1, y1, x2, y2, xmin, ymin, xmax, ymax):
    if (x1 < xmin and x2 < xmin) or (x1 > xmax and x2 > xmax) or (y1 < ymin and y2 < ymin) or (y1 > ymax and y2 > ymax):
        return None

    clipped_points = [[x1, y1], [x2, y2]]

    for i in range(2):
        x, y = clipped_points[i]

        if x < xmin:
            y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
            x = xmin
        elif x > xmax:
            y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
            x = xmax

        if y < ymin:
            x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
            y = ymin
        elif y > ymax:
            x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)
            y = ymax

        clipped_points[i] = [x, y]

    if (clipped_points[0][0] < xmin and clipped_points[1][0] < xmin) or (
            clipped_points[0][0] > xmax and clipped_points[1][0] > xmax):
        return None

    return clipped_points[0][0], clipped_points[0][1], clipped_points[1][0], clipped_points[1][1]


def plot_clipped_lines(lines, xmin, ymin, xmax, ymax):
    fig, ax = plt.subplots()
    ax.plot([xmin, xmax, xmax, xmin, xmin], [ymin, ymin, ymax, ymax, ymin], 'k-', lw=2)

    for line in lines:
        x1, y1, x2, y2 = line
        ax.plot([x1, x2], [y1, y2], 'r--')

        clipped_line = clip_line(x1, y1, x2, y2, xmin, ymin, xmax, ymax)
        if clipped_line:
            cx1, cy1, cx2, cy2 = clipped_line
            ax.plot([cx1, cx2], [cy1, cy2], 'g-', lw=2)

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('CG/RK1')
    plt.grid(True)
    plt.show()


xmin, ymin, xmax, ymax = 50, 10, 150, 100
lines = [(25, 80, 175, 80), (25, 25, 175, 120), (175, 20, 150, 140)]

plot_clipped_lines(lines, xmin, ymin, xmax, ymax)
finish = time.perf_counter()
print('Время работы: ' + str(finish - start))