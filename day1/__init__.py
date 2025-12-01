def part_1_answer(lines):
    current_number = 50
    zero_count = 0
    for line in lines:
        direction = line[0]
        distance = int(line[1:])
        if direction == "L":
            distance = -distance
        current_number = (current_number + distance) % 100
        if current_number == 0:
            zero_count += 1
    return zero_count


def part_2_answer(lines):
    current_number = 50
    zero_count = 0

    for line in lines:

        prev_number = current_number

        direction = line[0]
        distance = int(line[1:])

        zero_count += (distance // 100)
        distance %= 100

        if distance > 0:

            if direction == "L":
                distance = -distance

            current_number = (current_number + distance) % 100

            if pointed_at_zero(direction, prev_number, current_number):
                zero_count += 1

    return zero_count


def pointed_at_zero(direction, prev_number, current_number):
    """Determines whether the dial pointed at zero during/after a rotation"""

    # Finished pointing at 0
    if current_number == 0:
        return True

    # Started pointing at zero - counted in previous iteration
    if prev_number == 0:
        return False

    # Pointed at 0 while rotating anticlockwise
    if (direction == "L") and (current_number > prev_number):
        return True

    # Pointed at 0 while rotating clockwise
    if (direction == "R") and (current_number < prev_number):
        return True

    return False
