# Numbers to Arrays and Vice Versa
# Based on: https://edabit.com/challenge/L9nvCobbYyGgKpWi8


def to_list(num_arg):
    """Converts a number to an integer list of its digits."""
    integer_lst = list()
    num_tmp = abs(num_arg)

    while num_tmp // 10 > 0:
        integer_lst.insert(0, num_tmp % 10)
        num_tmp = num_tmp // 10

    integer_lst.insert(0, num_tmp % 10)

    if num_arg < 0:
        integer_lst.insert(0, "-")

    return integer_lst


def to_number(integer_lst):
    if len(integer_lst) == 0:
        raise ValueError

    multiplier = 1
    num = 0

    for digit in reversed(integer_lst):
        if digit == "-":
            num *= -1
            continue

        num += digit * multiplier
        multiplier *= 10

    return num


print(to_list(-9658325))
print(to_list(456789))

print(to_number([1, 2, 3]))
print(to_number([4, 5, 6]))
print(to_number(["-", 1, 2, 3]))
