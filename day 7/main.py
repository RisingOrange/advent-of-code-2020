
import re
from collections import defaultdict


def main(raw):
    children_dict = parse_rules(raw)
    print(len(precedessor_types('shiny gold', create_parents_dict(children_dict))))
    print(amount_descendants('shiny gold', children_dict))

def amount_descendants(target, children_dict):
    children = children_dict[target]
    amount_children = sum([amount for amount, _ in children])
    return amount_children + sum([amount * amount_descendants(child, children_dict) for amount, child in children])

def precedessor_types(target, parents_dict):
    parents = parents_dict[target]
    return set(parents).union(*[precedessor_types(parent, parents_dict) for parent in parents])

def create_parents_dict(children):
    result = defaultdict(list)
    for parent, children_types_and_amounts in children.items():
        for _, child in children_types_and_amounts:
            result[child].append(parent)
    return result

def parse_rules(text):
    result = defaultdict(list)
    for line in text.split('\n'):
        m = re.match(r'(?P<outer_bag>.+?) bags contain (?P<inner_bags_string>.+)\.', line)
        outer_bag = m['outer_bag']
        for inner_bag_string in m['inner_bags_string'].split(', '):
            inner_bag_string, _ = inner_bag_string.split(' bag')
            if not inner_bag_string.startswith('no other'):
                amount_str, name = inner_bag_string.split(' ', maxsplit=1)
                result[outer_bag].append((int(amount_str), name))
    return result


if __name__ == '__main__':
    with open('input.txt') as f:
        raw = f.read()

    main(raw)

