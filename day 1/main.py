from itertools import combinations

with open('input.txt') as f:
    raw = f.read()

nums = [int(line) for line in raw.split('\n')]

for (x, y, z) in combinations(nums, 3):
    if x + y + z == 2020:
        print(x * y * z)