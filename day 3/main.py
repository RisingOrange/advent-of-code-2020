
def main(raw):

    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    result = 1
    grid = raw.split('\n')
    for slope in slopes:
        result = result * trees_for_slope(grid, slope)
    return result


def trees_for_slope(grid, slope):
    result = 0
    dx, dy = slope
    x, y = 0, 0
    while y < len(grid):
        if grid[y][x] == '#':
            result += 1
        x = (x + dx) % len(grid[0])
        y += dy
    return result


if __name__ == '__main__':
    with open('input.txt') as f:
        raw = f.read()

    print(main(raw))
