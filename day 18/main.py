

def evaluate(expr):
    a, rest = split_next_expr_part(expr)
    if rest == '':
        if ' ' not in expr:
            return int(expr)
        else:
            return evaluate(a)

    operator, rest = split_next_expr_part(rest)

    if operator == '*':
        return evaluate(a) * evaluate(rest)
    elif operator == '+':
        b, rest = split_next_expr_part(rest)
        return evaluate(f'{evaluate(a) + evaluate(b)} {rest}')
    else:
        raise RuntimeError()


def split_next_expr_part(expr):
    if expr[0] == '(':
        i = 1
        depth = 1
        while(depth != 0):
            cur = expr[i]
            if cur == '(':
                depth += 1
            elif cur == ')':
                depth -= 1
            i += 1
        return expr[1:i-1], expr[i:]
    else:
        result = expr.split(maxsplit=1)
        if len(result) == 1:
            result.append('')
        return result


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        raw = f.read()
    lines = raw.split('\n')

    part_2_result = sum(evaluate(line) for line in lines)
    print(part_2_result)
