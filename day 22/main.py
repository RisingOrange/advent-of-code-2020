

def normal_combat(cards_a, cards_b):
    while cards_a and cards_b:
        cur_card_a, *cards_a = cards_a
        cur_card_b, *cards_b = cards_b
        if cur_card_a > cur_card_b:
            cards_a += [cur_card_a, cur_card_b]
        else:
            cards_b += [cur_card_b, cur_card_a]
    return cards_a if cards_a else cards_b


def recursive_combat(cards_a, cards_b):
    if not cards_a:
        return (False, cards_a + cards_b)

    if not cards_b:
        return (True, cards_a + cards_b)

    seen_card_configs = set()
    while cards_a and cards_b:
        if (tuple(cards_a), tuple(cards_b)) in seen_card_configs:
            return (True, cards_a + cards_b)

        seen_card_configs.add((tuple(cards_a), tuple(cards_b)))

        a_won = None
        cur_card_a, *cards_a = cards_a
        cur_card_b, *cards_b = cards_b
        if cur_card_a > len(cards_a) or cur_card_b > len(cards_b):
            a_won = cur_card_a > cur_card_b
        else:
            a_won, _ = recursive_combat(
                cards_a[:cur_card_a],
                cards_b[:cur_card_b]
            )
        if a_won:
            cards_a += [cur_card_a, cur_card_b]
        else:
            cards_b += [cur_card_b, cur_card_a]

    if cards_a:
        return (True, cards_a)
    else:
        return (False, cards_b)


def score(cards):
    return sum([
        i * card
        for i, card in enumerate(reversed(cards), 1)
    ])


if __name__ == '__main__':
    with open('input.txt') as f:
        raw = f.read()

    cards_a, cards_b = raw.split('\n\n')
    cards_a = list(map(int, cards_a.split('\n')[1:]))
    cards_b = list(map(int, cards_b.split('\n')[1:]))

    part_1_result = score(normal_combat(cards_a, cards_b))
    print(part_1_result)

    _, cards = recursive_combat(cards_a, cards_b)
    part_2_result = score(cards)
    print(part_2_result)
