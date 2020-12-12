from collections import Counter
from functools import lru_cache


def task_1(values):
    differences = [
        b - a
        for a, b in zip(values, values[1:])
    ]
    difference_counts = Counter(differences)
    return difference_counts[1] * difference_counts[3]


@lru_cache(50)
def valid_chains_amount(values):
    if len(values) == 1:
        return 1

    cur = values[0]
    return sum([
        valid_chains_amount(values[values.index(cur + diff):])
        for diff in (1, 2, 3)
        if (cur + diff) in values
    ])


if __name__ == '__main__':
    with open('input.txt') as f:
        raw = f.read()

    values = list(map(int, raw.split('\n')))
    values = sorted(values)
    last_adapter_value = values[-1] + 3
    values = tuple([0] + values + [last_adapter_value])

    print(task_1(values))
    print(valid_chains_amount(values))
