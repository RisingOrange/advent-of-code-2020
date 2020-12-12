

def main(raw):
    lines = raw.split('\n')
    
    for i in range(len(lines)):
        cmd, arg = lines[i].split()
        if cmd == 'acc':
            continue
        
        modified_lines = lines[:]
        if cmd == 'nop':
            modified_lines[i] = 'jmp ' + arg
        elif cmd == 'jmp':
            modified_lines[i] = 'nop ' + arg

        code_result = acc_at_end(modified_lines)
        if code_result is not None:
            return code_result

def acc_at_end(lines):
    result = 0
    visited_line_indeces = set()
    cur_line_idx = 0
    while cur_line_idx < len(lines):
        if cur_line_idx in visited_line_indeces:
            return None
        visited_line_indeces.add(cur_line_idx)  

        cmd, arg = lines[cur_line_idx].split()
        if cmd == 'acc':
            result += int(arg)
            cur_line_idx += 1
        elif cmd == 'jmp':
            cur_line_idx += int(arg)
        elif cmd == 'nop':
            cur_line_idx += 1
    return result


if __name__ == '__main__':
    with open('input.txt') as f:
        raw = f.read()

    print(main(raw))

