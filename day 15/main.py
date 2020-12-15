

def nth_number(starting_numbers, n):
    said_on_turn = dict()

    for turn, num in enumerate(starting_numbers[:-1]):
        said_on_turn[num] = turn

    prev = numbers[-1]
    for turn in range(len(starting_numbers), n):
        if prev not in said_on_turn:
            cur = 0
        else:
            cur = (turn-1) - said_on_turn[prev] 
        said_on_turn[prev] = turn - 1
        prev = cur
    return prev

if __name__ == '__main__':
    with open('input.txt') as f:
        raw = f.read()

    numbers = [int(x) for x in raw.split(',')]
    print(nth_number(numbers, 2020))
    print(nth_number(numbers, 30000000))

