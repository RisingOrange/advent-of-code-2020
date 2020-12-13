from decimal import Decimal
from functools import reduce


def part_1(timestamp, intervals_string):
    intervals = [int(x) for x in intervals_string.split(',') if x != 'x']
    min_wait_time, interval = min(
        [(wait_time(timestamp, interval), interval) for interval in intervals])
    return min_wait_time * interval


def wait_time(time, interval):
    return (interval - (time % interval)) % interval


def part_2(intervals_string):
    wait_times_and_intervals = [
        (idx, int(interval))
        for (idx, interval) in enumerate(intervals_string.split(','))
        if interval != 'x'
    ]

    intervals = [interval for _, interval in wait_times_and_intervals]
    times_since_departure = [
        (interval - wait_time) % interval
        for (wait_time, interval) in wait_times_and_intervals
    ]
    return chinese_remainder(intervals, times_since_departure)


def chinese_remainder(modulos, vals):
    # solves system of equations of the form
    # x = vals[i] % modulos[i]
    # for x
    modulos = list(map(Decimal, modulos))
    vals = list(map(Decimal, vals))

    sum_ = 0
    prod = reduce(lambda a, b: a*b, modulos)
    for m_i, a_i in zip(modulos, vals):
        p = prod / m_i
        sum_ += a_i * mul_inv(p, m_i) * p
    return sum_ % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


if __name__ == '__main__':
    with open('input.txt') as f:
        raw = f.read()

    first_line, second_line = raw.split('\n')
    timestamp = int(first_line)

    print(part_1(timestamp, second_line))
    print(part_2(second_line))
