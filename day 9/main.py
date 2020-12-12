

def part_1(nums):
    n_previous_nums = nums[:25]
    for x in nums[25:]:
        if not any([x != y and x - y in n_previous_nums for y in n_previous_nums]):
            return x
        n_previous_nums.pop(0)
        n_previous_nums.append(x)


def part_2(nums):
    target = 144381670

    start_idx, end_idx = 0, 1
    cur_sum = nums[0]
    while True:
        while cur_sum < target:
            cur_sum += nums[end_idx]
            end_idx += 1

        while cur_sum > target:
            cur_sum -= nums[start_idx]
            start_idx += 1

        if cur_sum == target:
            range_ = nums[start_idx:end_idx]
            return min(range_) + max(range_)


if __name__ == '__main__':
    with open('input.txt') as f:
        raw = f.read()

    nums = list(map(int, raw.split('\n')))
    print(part_1(nums))
    print(part_2(nums))
