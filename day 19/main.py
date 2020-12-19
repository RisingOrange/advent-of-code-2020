import re


def to_regex(rules, idx=0):
    cur_rule = rules[idx]
    if '"' in cur_rule:
        return cur_rule.replace('"', '')

    options = [
        ''.join(to_regex(rules, rule_idx)
                for rule_idx in map(int, option.split()))
        for option in cur_rule.split(' | ')
    ]
    result = '(' + "|".join(options) + ')'
    return result


def valid(msg, rule_31_re, rule_42_re):
    # rule_0    8 11
    # a valid message consists of two parts, the part defined by rule 8
    # and the part defined by rule 11

    # rule 8    42 | 42 8
    # the string hast to start with rule_42, which is possibly repeated
    # candidates will contain the message from which a string matching rule_42 was removed n-times (n>1)
    candidates = []
    cur_msg = msg
    while re.match(rule_42_re, cur_msg):
        cur_msg = cur_msg[re.match(rule_42_re, cur_msg).end(0):]
        candidates.append(cur_msg)

    # rule 11   42 31 | 42 11 31
    # this part of the string has to have to be of the form ab or aabb or aaabbb, ...
    # with 'a' being a string matching rule_42 and 'b' being a string matching rule_31
    for candidate in candidates:
        ctr = 1
        while True:
            if not re.match((rule_42_re * ctr), candidate):
                break
            combined_re = (rule_42_re * ctr) + (rule_31_re * ctr) + '$'
            if re.match(combined_re, candidate):
                return True
            ctr += 1


if __name__ == '__main__':
    with open('input.txt') as f:
        raw = f.read()
    rules, messages = raw.split('\n\n')
    rules = [
        line.split(':', maxsplit=1)[1].strip()
        for line in sorted(rules.split('\n'), key=lambda s: int(s.split(': ', maxsplit=1)[0]))
    ]
    messages = messages.split('\n')

    pattern = to_regex(rules) + '$'
    part_1 = len([
        msg for msg in messages
        if re.match(pattern, msg)
    ])
    print(part_1)

    rules[8] = '42 | 42 8'
    rules[11] = '42 31 | 42 11 31'
    rule_31_re = to_regex(rules, 31)
    rule_42_re = to_regex(rules, 42)

    part_2 = len([
        msg for msg in messages
        if valid(msg, rule_31_re, rule_42_re)
    ])
    print(part_2)
