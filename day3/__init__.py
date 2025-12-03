def part_1_answer(lines):
    return sum(largest_joltage_2(bank) for bank in lines)


def largest_joltage_2(bank):
    joltages = [int(n) for n in bank]

    # For the first battery, find the largest joltage, excluding the last
    # battery (because there needs to be a second battery after the first)
    first = max(joltages[:-1])
    first_pos = joltages.index(first)

    # For the second battery, find the largest joltage after the first
    second = max(joltages[first_pos + 1:])

    return first * 10 + second


def part_2_answer(lines):
    return sum(largest_joltage_12(bank) for bank in lines)


def largest_joltage_12(bank):
    joltages = [int(n) for n in bank]
    bank_size = len(bank)

    largest_joltage = 0
    last_battery_used = -1

    for i in range(12):
        batteries_needed = 12 - i
        batteries_to_keep = batteries_needed - 1

        start = last_battery_used + 1
        end = bank_size - batteries_to_keep
        max_num = max(joltages[start:end])

        largest_joltage = (largest_joltage * 10) + max_num

        last_battery_used = joltages.index(max_num, start)

    return largest_joltage
