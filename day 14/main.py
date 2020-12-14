import re
from itertools import product


def execute_lines(lines, write_function):
    memory = dict()
    mask = None
    for line in lines:
        if line.startswith('mask'):
            _, mask = line.split('= ')
        else:
            address, value = map(int, re.match(
                r'mem\[(\d+)\] = (\d+)', line).groups())
            write_function(memory, address, value, mask)
    return sum(memory.values())


def mask_written_value(memory, address, value, mask):
    value_bits = list(bin(value)[2:].zfill(len(mask)))
    for i, mask_bit in enumerate(mask):
        if mask_bit == '0':
            value_bits[i] = '0'
        elif mask_bit == '1':
            value_bits[i] = '1'
    masked_value = int(''.join(value_bits), 2)
    memory[address] = masked_value


def mask_address(memory, address, value, mask):
    address_bits = list(bin(address)[2:].zfill(len(mask)))
    for i, mask_bit in enumerate(mask):
        if mask_bit == '1':
            address_bits[i] = '1'
        if mask_bit == 'X':
            address_bits[i] = 'X'

    for option in product('01', repeat=address_bits.count('X')):
        option_list = list(option)
        concrete_address_bits = address_bits[:]
        for i, bit in enumerate(concrete_address_bits):
            if bit == 'X':
                concrete_address_bits[i] = option_list.pop()
        concrete_address = int(''.join(concrete_address_bits), 2)
        memory[concrete_address] = value


if __name__ == '__main__':
    with open('input.txt') as f:
        raw = f.read()

    lines = raw.split('\n')
    print(execute_lines(lines, mask_written_value))
    print(execute_lines(lines, mask_address))
