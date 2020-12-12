from copy import deepcopy


def apply_rules_until_stable(grid, cell_transform):
    while True:
        grid, stable = apply_rules_to_every_cell(grid, cell_transform)

        if stable:
            break

    return sum([
        row.count('#')
        for row in grid
    ])


def apply_rules_to_every_cell(grid, cell_transform):
    result = deepcopy(grid)
    stable = True
    for y, row in enumerate(grid):
        for x in range(len(row)):
            new_cell_value = cell_transform(x, y, grid)
            if new_cell_value != grid[y][x]:
                result[y][x] = new_cell_value
                stable = False
    return result, stable


def cell_transform_1(x, y, grid):
    ch = grid[y][x]
    # If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
    if ch == 'L' and num_adjacient_occupied_seats(x, y, grid) == 0:
        return '#'
    # If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
    elif ch == '#' and num_adjacient_occupied_seats(x, y, grid) >= 4:
        return 'L'
    return ch


def num_adjacient_occupied_seats(x, y, grid):
    result = 0
    for cur_x in (x-1, x, x+1):
        for cur_y in (y-1, y, y+1):
            if ((cur_x == x and cur_y == y) or
                    not is_pos_on_grid(cur_x, cur_y, grid)):
                continue
            if grid[cur_y][cur_x] == '#':
                result += 1
    return result


def cell_transform_2(x, y, grid):
    ch = grid[y][x]
    # If a seat is empty (L) and there are no seats visible from it, the seat becomes occupied.
    if ch == 'L' and num_visible_seats(x, y, grid) == 0:
        return '#'
    # If a seat is occupied (#) and five or more seats are visible form it, the seat becomes empty.
    elif ch == '#' and num_visible_seats(x, y, grid) >= 5:
        return 'L'
    return ch


def num_visible_seats(x, y, grid):
    directions = [
        (dx, dy)
        for dy in (-1, 0, +1)
        for dx in (-1, 0, +1)
        if not (dx == 0 and dy == 0)
    ]
    result = 0
    for dx, dy in directions:
        cur_x, cur_y = x, y
        while True:
            cur_x += dx
            cur_y += dy
            if not is_pos_on_grid(cur_x, cur_y, grid):
                break
            ch = grid[cur_y][cur_x]
            if ch == 'L':
                break
            if ch == '#':
                result += 1
                break
    return result


def is_pos_on_grid(x, y, grid):
    return (
        0 <= x < len(grid[0]) and
        0 <= y < len(grid)
    )


def grid_to_string(grid):
    return '\n'.join((''.join(row) for row in grid))


def to_grid(raw):
    return [list(row) for row in raw.split('\n')]


if __name__ == '__main__':
    with open('input.txt') as f:
        raw = f.read()

    print(apply_rules_until_stable(to_grid(raw), cell_transform_2))
