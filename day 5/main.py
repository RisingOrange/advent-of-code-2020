

def main(raw):
   all_seats = set([
       seat_id((row, col))
       for row in range(128)
       for col in range(8)
   ])

   seen_seats = set([
       seat_id(seat_pos(seat_str))
       for seat_str in raw.split('\n')
   ])

   unseen_seats = all_seats - seen_seats
   for seat in unseen_seats:
       if set([(seat-1), (seat+1)]) <= seen_seats:
           return seat

def seat_id(seat_pos):
    row, col = seat_pos
    return row * 8 + col

def seat_pos(seat_str):
    row_str, col_str = seat_str[:-3], seat_str[-3:]
    row = int(row_str.translate({'F' : '0', 'B' : '1'}), 2)
    col = int(col_str.replace('L', '0').replace('R', '1'), 2)
    return (row, col)


if __name__ == '__main__':
    with open('input.txt') as f:
        raw = f.read()

    print(main(raw))

