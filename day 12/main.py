

def part_1(lines):
    directions = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
    ship_pos = (0, 0)
    facing_direction = directions['E']
    for line in lines:
        cmd, arg = line[0], int(line[1:])
        if cmd == 'F':
            ship_pos = move(ship_pos, facing_direction, arg)
        if cmd in directions:
            ship_pos = move(ship_pos, directions[cmd], arg)
        elif cmd in 'RL':
            if cmd == 'R':
                facing_direction = rotate_90(facing_direction, int(arg/90))
            else:
                facing_direction = rotate_90(facing_direction, int(360-arg/90))
    return manhattan_distance(ship_pos, (0, 0))


def part_2(lines):
    directions = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
    ship_pos = (0, 0)
    wp_pos = (10, 1)
    for line in lines:
        cmd, arg = line[0], int(line[1:])
        if cmd == 'F':
            ship_pos = move(ship_pos, wp_pos, arg)
        elif cmd in directions:
            wp_pos = move(wp_pos, directions[cmd], arg)
        elif cmd in 'RL':
            if cmd == 'R':
                wp_pos = rotate_90(wp_pos, int(arg/90))
            else:
                wp_pos = rotate_90(wp_pos, int(360-arg/90))
    return manhattan_distance(ship_pos, (0, 0))


def move(pos, direction, times):
    rx, ry = pos
    dx, dy = direction
    rx += dx * times
    ry += dy * times
    return rx, ry


def rotate_90(pos, times):
    rx, ry = pos
    for _ in range(times):
        rx, ry = ry, -rx
    return rx, ry


def manhattan_distance(a, b):
    ax, ay = a
    bx, by = b
    return abs(bx-ax) + abs(by-ay)


if __name__ == '__main__':
    with open('input.txt') as f:
        raw = f.read()
    lines = raw.split('\n')

    print(part_1(lines))
    print(part_2(lines))
