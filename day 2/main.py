
def main(raw):
    result = len([
        x for x in
        raw.split('\n')
        if is_password_valid(*x.split(': '))
    ])
    return result

def is_password_valid(rule, password):
    indeces_str, letter = rule.split()
    index_1, index_2 = map(lambda x: int(x)-1, indeces_str.split('-'))
    return len([idx for idx in [index_1, index_2] if idx < len(password) and password[idx] == letter]) == 1


if __name__ == '__main__':
    with open('input.txt') as f:
        raw = f.read()

    print(main(raw))