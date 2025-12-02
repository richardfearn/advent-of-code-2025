def part_1_answer(ranges):
    return sum_of_all_invalid_ids(ranges, is_invalid_part_1)


def part_2_answer(ranges):
    return sum_of_all_invalid_ids(ranges, is_invalid_part_2)


def sum_of_all_invalid_ids(ranges, check_fn):
    ranges = ranges.split(",")
    return sum(sum_of_invalid_ids(r, check_fn) for r in ranges)


def sum_of_invalid_ids(r, check_fn):
    first, last = r.split("-")
    first, last = int(first), int(last)
    return sum(n for n in range(first, last + 1) if check_fn(n))


def is_invalid_part_1(n):
    s = str(n)

    if (len(s) % 2) == 1:
        # odd number of digits - can't be some sequence of digits repeated twice
        return False

    mid = len(s) // 2
    return s[:mid] == s[mid:]


def is_invalid_part_2(n):
    s = str(n)
    s_len = len(s)

    # max sequence length is half the total number of digits (2 repetitions)
    max_seq_len = s_len // 2

    for seq_len in range(1, max_seq_len + 1):
        if (len(s) % seq_len) > 0:
            # number is not an exact multiple of seq_len digits
            continue

        sequence = s[:seq_len]
        num_repetitions = len(s) // seq_len
        if (num_repetitions >= 2) and ((sequence * num_repetitions) == s):
            return True

    return False
