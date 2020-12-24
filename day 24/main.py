from collections import Counter
from copy import copy

directions = {
    'e':   (1, 0),
    'se':  (0, 1),
    'sw':  (-1, +1),
    'w':   (-1, 0),
    'nw':  (0, -1),
    'ne':  (1, -1)
}


def part_2(black_tile_positions):
    new_black_tile_positions = set(black_tile_positions[:])
    for _ in range(100):
        for pos in black_tile_positions:
            tile_num_neighbours = num_neighbours(pos, black_tile_positions)
            if tile_num_neighbours == 0 or tile_num_neighbours > 2:
                new_black_tile_positions.remove(pos)

            for adj_pos in adjacient_positions(pos):
                if adj_pos not in black_tile_positions and num_neighbours(adj_pos, black_tile_positions) == 2:
                    new_black_tile_positions.add(adj_pos)
        black_tile_positions = copy(new_black_tile_positions)

    return len(black_tile_positions)


def num_neighbours(pos, black_tile_positions):
    return len([
        adj_pos
        for adj_pos in adjacient_positions(pos)
        if adj_pos in black_tile_positions
    ])


def adjacient_positions(pos):
    q, r = pos
    return [
        (q+dq, r+dr)
        for (dq, dr) in directions.values()
    ]


def parse(line):
    q, r = (0, 0)
    while line:
        name, (dq, dr) = next(
            (name, vec)
            for name, vec in directions.items()
            if line.startswith(name)
        )
        q += dq
        r += dr
        line = line[len(name):]
    return (q, r)


if __name__ == '__main__':
    with open('input.txt') as f:
        raw = f.read()
    lines = raw.split('\n')
    positions = [parse(line) for line in lines]

    cnts = Counter(positions)
    black_tile_positions = [x for x, cnt in cnts.items() if cnt % 2 == 1]
    print(len(black_tile_positions))

    print(part_2(black_tile_positions))
