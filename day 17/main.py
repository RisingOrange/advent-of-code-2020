from itertools import product


def grid_to_positions(grid, num_dims):
    return set([
        tuple([x, y] + [0] * (num_dims-2))
        for y, row in enumerate(grid)
        for x, ch in enumerate(row)
        if ch == '#'
    ])


def adjacent_positions(pos):
    result = list(product(*[[k-1, k, k+1] for k in pos]))
    result.remove(pos)
    return result


def amount_neighbours(pos, positions):
    return len([pos for pos in adjacent_positions(pos) if pos in positions])


def num_active_cubes_after_boot(start_grid, num_dims):
    active_cube_positions = grid_to_positions(start_grid, num_dims)

    for _ in range(6):
        new_active_cube_positions = set()
        considered_positions = set() # inactive positions already considered for becoming active
        for cube_pos in active_cube_positions:
            if amount_neighbours(cube_pos, active_cube_positions) in (2, 3):
                new_active_cube_positions.add(cube_pos)
            for adjacient_pos in adjacent_positions(cube_pos):
                if adjacient_pos in active_cube_positions or adjacient_pos in considered_positions:
                    continue
                if amount_neighbours(adjacient_pos, active_cube_positions) == 3:
                    new_active_cube_positions.add(adjacient_pos)
                considered_positions.add(adjacient_pos)
        active_cube_positions = new_active_cube_positions
    return len(active_cube_positions)


if __name__ == '__main__':
    with open('input.txt') as f:
        raw = f.read()
    grid = [list(line) for line in raw.split('\n')]

    print(num_active_cubes_after_boot(grid, 3))
    print(num_active_cubes_after_boot(grid, 4))
