import re
from functools import reduce


def ticket_scanning_error_rate(fields, tickets):
    result = 0
    for ticket in tickets:
        for value in ticket:
            if not is_value_valid_for_any_field(value, fields):
                result += value
    return result


def valid_tickets(fields, tickets):
    results = list()
    for ticket in tickets:
        if all(
            is_value_valid_for_any_field(value, fields)
            for value in ticket
        ):
            results.append(ticket)
    return results


def field_order(fields, tickets):
    valid_positions_for_field = valid_positions_for_field_dict(fields, tickets)
    field_name_for_pos = dict()
    for _ in range(len(fields)):
        for field, valid_positions in valid_positions_for_field.items():
            canidate_positions = set(valid_positions) - set(field_name_for_pos)
            if len(canidate_positions) == 1:
                (pos,) = canidate_positions
                field_name_for_pos[pos] = field

    assert len(field_name_for_pos) == len(
        fields), 'the shortcut used for computing the field_order is not applicable on the provided input'
    return [name for _, name in sorted(field_name_for_pos.items())]


def valid_positions_for_field_dict(fields, tickets):
    cache = dict()

    def is_field_position_valid(fields, field_name, position, tickets):
        args = (field_name, position)
        if args not in cache:
            cache[args] = all(
                is_value_valid_for_field(value, fields, field_name)
                for value in (ticket[position] for ticket in tickets)
            )
        return cache[args]

    result = dict()
    for field in fields:
        valid_positions_for_field = set([
            pos for pos in range(len(fields))
            if is_field_position_valid(fields, field, pos, valid_tickets(fields, tickets))
        ])
        result[field] = valid_positions_for_field
    return result


def is_value_valid_for_any_field(value, fields):
    return any(
        is_value_valid_for_field(value, fields, field)
        for field in fields
    )


def is_value_valid_for_field(value, fields, field_name):
    return any(
        a <= value <= b
        for a, b in fields[field_name]
    )


def parse_input(raw):
    fields, my_ticket, other_tickets = raw.split('\n\n')

    fields = fields.split('\n')
    fields_dict = dict()
    for line in fields:
        name, a, b, c, d = re.match(
            r'([\w ]+): (\d+)-(\d+) or (\d+)-(\d+)', line).groups()
        fields_dict[name] = ((int(a), int(b)), (int(c), int(d)))

    _, my_ticket = my_ticket.split('\n')
    my_ticket = [int(x) for x in my_ticket.split(',')]

    _, other_tickets = other_tickets.split('\n', maxsplit=1)
    other_tickets = [
        [int(x) for x in ticket_str.split(',')]
        for ticket_str in other_tickets.split('\n')
    ]
    return fields_dict, my_ticket, other_tickets


if __name__ == '__main__':
    with open('input.txt') as f:
        raw = f.read()

    fields, my_ticket, other_tickets = parse_input(raw)
    print(ticket_scanning_error_rate(fields, other_tickets))

    order = field_order(fields, valid_tickets(fields, other_tickets))
    departure_values = [
        value for field_name, value in zip(order, my_ticket) if field_name.startswith('departure')
    ]
    part2_result = reduce(lambda a, b: a*b, departure_values)
    print(part2_result)
