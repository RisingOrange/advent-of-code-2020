import re


required_fields = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])


def num_valid_passports(raw):
    blocks = raw.split('\n\n')
    lines = [' '.join(block.split('\n')) for block in blocks]
    return len([line for line in lines if is_passport_valid(line)])


def is_passport_valid(line):
    d = dict(field.split(':') for field in line.split())
    return (
        (required_fields.issubset(set(d.keys()))) and
        (len(d['byr']) == 4 and 1920 <= int(d['byr']) <= 2002) and
        (len(d['iyr']) == 4 and 2010 <= int(d['iyr']) <= 2020) and
        (len(d['eyr']) == 4 and 2020 <= int(d['eyr']) <= 2030) and
        is_height_valid(d['hgt']) and
        (re.match(r'#[0-9a-f]{6}$', d['hcl'])) and
        d['ecl'] in 'amb blu brn gry grn hzl oth'.split() and
        re.match(r'\d{9}$', d['pid'])
    )


def is_height_valid(text):
    m = re.match('(\d+)(cm|in)', text)
    if not m:
        return False

    number_str, unit = m.groups()
    number = int(number_str)
    return (
        unit == 'cm' and (150 <= number <= 193) or
        unit == 'in' and (59 <= number <= 76)
    )


if __name__ == '__main__':
    with open('input.txt') as f:
        raw = f.read()

    print(num_valid_passports(raw))
